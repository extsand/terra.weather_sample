#!/bin/bash

sudo apt update
sudo apt install ca-certificates -y
sudo apt update
sudo apt install apt-transport-https -y

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

sudo apt update
sudo apt install docker.io -y

sudo apt install docker-compose -y

#Will chek it. Important for Jenkins
# sudo usermod -aG docker $USER
sudo usermod -aG docker ubuntu

mkdir /home/ubuntu/docker_workplace
sudo chown -R ubuntu /home/ubuntu/docker_workplace

sudo reboot now


