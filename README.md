# Cdev Website

## About
This repo holds the code for the static website for Cdev. The static website will include the landing page, documentation, and general information 
about the project. The project is currently being developed using Hugo based on the agen-hugo theme purchased from https://themefisher.com/products/agen-hugo-agency-template/. 


The project follows the general structure of a `hugo` project, and to work with the codebase, you will need to [install hugo v0.93.3](https://gohugo.io/getting-started/installing/) (note if downloading the binary directly, you need to download the extended version to get live SCSS reload). Once installed, you should be able to run `hugo server` to run a local version of the project. 

## Install steps
wget https://github.com/gohugoio/hugo/releases/download/v0.93.3/hugo_0.93.3_Linux-64bit.deb
sudo dpkg -i hugo_0.93.3_Linux-64bit.deb
then make your directory, clone cdev-website then cd into it
hugo server


### Developing 

Once the live server is up, you can go to `/dev_playground/playground/` to see how the different components are currently rendered.