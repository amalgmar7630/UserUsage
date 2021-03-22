#!/usr/bin/env bash

UBUNTU_PACKAGES=(
  "build-essential"
  "git"
  "python3-dev"
  "python3-pip"
  "python3-venv"
  "python3-setuptools"
  "python3-wheel"
  "python3-cffi"
  "libcairo2"
  "libpango-1.0-0"
  "libpangocairo-1.0-0"
  "libgdk-pixbuf2.0-0"
  "libffi-dev"
  "shared-mime-info"
  "binutils"
  "libgeos-dev"
  "libgeos++-dev"
  "libproj-dev"
  "libgdal-dev"
  "gdal-bin"
  "python3-gdal"
)

# install ubuntu packages
apt-get update
export DEBIAN_FRONTEND=noninteractive
apt-get install -yq ${UBUNTU_PACKAGES[*]}
