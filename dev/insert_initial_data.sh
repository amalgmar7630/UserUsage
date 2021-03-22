#!/usr/bin/env bash
PROJECT_ROOT="/vagrant"
VM_HOME="/home/vagrant"
VIRTUAL_ENV_PATH="${VM_HOME}/venv"

# activate the virtual env
source ${VIRTUAL_ENV_PATH}/bin/activate

# migrate the db
python ${PROJECT_ROOT}/manage.py migrate

# create a dev user
python ${PROJECT_ROOT}/manage.py shell -c "from users.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')"

# insert metadata and tasks and project templates into db
PROVISIONED_ON=/etc/vm_provision_on_timestamp
if [ -f "$PROVISIONED_ON" ]; then
  echo "VM was already provisioned at: $(cat $PROVISIONED_ON)"
  echo "To run system updates manually login via 'vagrant ssh' and run 'apt-get update && apt-get upgrade'"
  echo ""
  exit
fi

