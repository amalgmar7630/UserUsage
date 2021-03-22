#!/usr/bin/env bash

PROJECT_ROOT="/vagrant"
VM_HOME="/home/vagrant"
VIRTUAL_ENV_PATH="${VM_HOME}/venv"


# create virtual environment and  project requirements
pip3 install virtualenv
export VIRTUALENV_ALWAYS_COPY=1
INSTALL_VIRTUALENV="virtualenv ${VIRTUAL_ENV_PATH} --python=/usr/bin/python3.8"
UPDATE_PIP="${VIRTUAL_ENV_PATH}/bin/python -m pip install --upgrade pip"
INSTALL_REQUIREMENT="${VIRTUAL_ENV_PATH}/bin/pip install -r ${PROJECT_ROOT}/requirements.txt"
su - vagrant -c "${INSTALL_VIRTUALENV} && ${UPDATE_PIP} && ${INSTALL_REQUIREMENT}"

# redirect user to project root when he ssh into the VM
echo "cd ${PROJECT_ROOT}" >>${VM_HOME}/.bashrc

# create aliases for the mostly used commands
# we need to run the server with 0.0.0.0:8000
echo "alias runserver=\"python manage.py runserver 0.0.0.0:8000\"" >>${VM_HOME}/.bashrc
echo "alias migrate=\"python manage.py migrate\"" >>${VM_HOME}/.bashrc
echo "alias makemigrations=\"python manage.py makemigrations\"" >>${VM_HOME}/.bashrc
echo "alias showmigrations=\"python manage.py showmigrations\"" >>${VM_HOME}/.bashrc
echo "alias shell_plus=\"python manage.py shell_plus\"" >>${VM_HOME}/.bashrc

# activate virtual environment when someone ssh into the VM
echo "source ${VIRTUAL_ENV_PATH}/bin/activate" >>${VM_HOME}/.bashrc

# Create env file
source ${VIRTUAL_ENV_PATH}/bin/activate
