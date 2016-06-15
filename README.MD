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
   
### Email service
The following applications will be installed during in the build. No manual work is needed.

See [here](http://rianjs.net/2013/08/send-email-from-linux-server-using-gmail-and-ubuntu-two-factor-authentication)
Install mailutils

    sudo apt-get install mailutils
    
Install and configure ssmtp
    
    sudo apt-get install ssmtp

See [Mailhog](https://github.com/mailhog/MailHog)
      
    docker build -t mailhog .
    docker run -d -p 1025:1025 -p 8025:8025 mailhog
      
Access Mailhog web page:

    http://192.168.100.100:8025
    
    
      
      