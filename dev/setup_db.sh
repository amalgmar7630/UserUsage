#!/bin/sh -e
# This script is based on https://github.com/jackdb/pg-app-dev-vm
APP_DB_USER=postgres1
APP_DB_PASS=postgres1
APP_DB_NAME=planetly
PG_VERSION=11

###########################################################
# Changes below this line are probably not necessary
###########################################################
print_db_usage () {
  GREEN='\033[1;36m'
  NC='\033[0m' # No Color
  echo "${GREEN}Your PostgreSQL database has been setup and can be accessed on your local machine on the forwarded port (default: 15432)${NC}"
  echo "${GREEN}  Host: localhost${NC}"
  echo "${GREEN}  Port: 15432${NC}"
  echo "${GREEN}  Database: $APP_DB_NAME${NC}"
  echo "${GREEN}  Username: $APP_DB_USER${NC}"
  echo "${GREEN}  Password: $APP_DB_PASS${NC}"
  echo ""
  echo "${GREEN}Admin access to postgres user via VM:${NC}"
  echo "${GREEN}  vagrant ssh${NC}"
  echo "${GREEN}  sudo su - postgres${NC}"
  echo ""
  echo "${GREEN}psql access to app database user via VM:${NC}"
  echo "${GREEN}  vagrant ssh${NC}"
  echo "${GREEN}  sudo su - postgres${NC}"
  echo "${GREEN}  PGUSER=$APP_DB_USER PGPASSWORD=$APP_DB_PASS psql -h localhost $APP_DB_NAME${NC}"
  echo ""
  echo "${GREEN}Env variable for application development:${NC}"
  echo "${GREEN}  DATABASE_URL=postgresql://$APP_DB_USER:$APP_DB_PASS@localhost:15432/$APP_DB_NAME${NC}"
  echo ""
  echo "${GREEN}Local command to access the database via psql:${NC}"
  echo "${GREEN}  PGUSER=$APP_DB_USER PGPASSWORD=$APP_DB_PASS psql -h localhost -p 15432 $APP_DB_NAME${NC}"
}

export DEBIAN_FRONTEND=noninteractive

PROVISIONED_ON=/etc/vm_provision_on_timestamp
if [ -f "$PROVISIONED_ON" ]
then
  echo "VM was already provisioned at: $(cat $PROVISIONED_ON)"
  echo "To run system updates manually login via 'vagrant ssh' and run 'apt-get update && apt-get upgrade'"
  echo ""
  print_db_usage
  exit
fi

PG_REPO_APT_SOURCE=/etc/apt/sources.list.d/postgresql.list
if [ ! -f "$PG_REPO_APT_SOURCE" ]
then
  # Add PGDG repo key:
  wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O- | apt-key add -

  # Add PG apt repo:
  echo "deb [arch=amd64] http://apt.postgresql.org/pub/repos/apt/ focal-pgdg main" | sudo tee "$PG_REPO_APT_SOURCE"

fi

# Update package list and upgrade all packages
apt-get update

apt install -y "postgresql-$PG_VERSION" "postgresql-$PG_VERSION-postgis-2.5"

PG_CONF="/etc/postgresql/$PG_VERSION/main/postgresql.conf"
PG_HBA="/etc/postgresql/$PG_VERSION/main/pg_hba.conf"
PG_DIR="/var/lib/postgresql/$PG_VERSION/main"

# Edit postgresql.conf to change listen address to '*':
sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '*'/" "$PG_CONF"

# Append to pg_hba.conf to add password auth:
echo "host    all             all             all                     md5" >> "$PG_HBA"

# Explicitly set default client_encoding
echo "client_encoding = utf8" >> "$PG_CONF"

# Restart so that all new config is loaded:
service postgresql restart

cat << EOF | su - postgres -c psql
-- Create the database user:
CREATE USER $APP_DB_USER WITH PASSWORD '$APP_DB_PASS';
ALTER USER $APP_DB_USER CREATEDB;
ALTER USER $APP_DB_USER WITH SUPERUSER;

-- Create the database:
CREATE DATABASE $APP_DB_NAME WITH OWNER=$APP_DB_USER
                                  LC_COLLATE='en_US.utf8'
                                  LC_CTYPE='en_US.utf8'
                                  ENCODING='UTF8'
                                  TEMPLATE=template0;
EOF

# Tag the provision time:
date > "$PROVISIONED_ON"

echo "Successfully created PostgreSQL dev virtual machine."
echo ""
print_db_usage
