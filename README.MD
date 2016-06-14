# Vagrant LEMP for Magento 2

### Start/build the environment
Open ./Vagrantfile.dist and check all the configurations.
Rename ./Vagrantfile.dist to './Vagrantfile' if everything is right.
Inside './Vagrantfile', change 'DIR_TO_SHARE_FROM_YOUR_LOCAL' to the actual directory on your local machine that you want to share into the vagrant box.
Then run:
    
    vagrant up
    
All the applications (nginx, php, mysql) will be installed but NOT started.
The environment is configured in ./setting.py. Feel free to update it to match your case.        
    
### LEMP configurations    
All configuration files are under ./conf
Update configuration: vagrant ssh into the VM, switch to root user and then
    
    # Update all the applications
    pagrant config
    
    # Update a specific one. The application will be automatically restarted.
    pagrant config -a php
    
### Install Blackfire
Run

    vagrant ssh
    
and then [Install Blackfire](https://blackfire.io/docs/up-and-running/installation)    