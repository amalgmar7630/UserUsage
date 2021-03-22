# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # OS to be installed in the VM
  config.vm.box = "ubuntu/focal64"
  config.vm.box_version = "20210106.0.0"

  # run vagrant with 3GB RAM and 3 cpus
  config.vm.provider "virtualbox" do |v|
    v.memory = 3072
    v.cpus = 3
  end

  # You can go to localhost:8000 to access the project
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  # a script that will be run after creating the VM to install the project
  # install ubuntu packages
  config.vm.provision :shell, path: "dev/install_ubuntu_packages.sh"
  # Setup Python Environment
  config.vm.provision :shell, path: "dev/create_dev_env.sh"
  # setup postgres and create a db
  config.vm.provision :shell, path: "dev/setup_db.sh"

  # setup redis docker container
  # config.vm.provision :host_shell do |host_shell|
  #  host_shell.inline = 'chmod u+x dev/setup_redis_docker.sh && bash dev/setup_redis_docker.sh'
  # end
  # setup postgres docker container, create a db and import dump
  # config.vm.provision :host_shell do |host_shell|
  #  host_shell.inline = 'chmod u+x dev/setup_db_docker.sh && bash dev/setup_db_docker.sh'
  # end
  # insert initial data for the project
  config.vm.provision :shell, path: "dev/insert_initial_data.sh"
  # from the guest, the host is accessible at 10.0.2.2
  config.vm.provision "shell", privileged: false, inline: <<-MSG
    GREEN='\033[1;36m'
    NC='\033[0m' # No Color
    echo -e "${GREEN}Dev Environment with demo data is ready to use!${NC}"
    echo -e "${GREEN}A user 'admin' with password 'adminpass' and email 'admin@example.com' is available${NC}"
  MSG
end
