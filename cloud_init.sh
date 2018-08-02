#!/bin/bash

sudo apt-get update

sudo apt-get install git -y

cd /home/ubuntu/

git clone https://github.com/azat-co/nodejs-hello-world

sudo apt-get install nodejs -y

cd nodejs-hello-world/

sudo apt-get install npm -y

nodejs server.js &
