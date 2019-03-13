# Task Process for Process Manager
## Requirements :
First of all you need to have install the broker. For this we going use RabbitQM server.

For install this: ```sudo apt install rabbitmq-server``` :+1:

You can also install the management plugin for make more easy to peek into a running RabbitQM instance. Let's install the management plugin as follows: 
```bash
   sudo rabbitmq-plugins enable rabbitmq_management
    [OUTPUT]:
    .
    .
    .
    .
    The following plugins have been enabled:  
    mochiweb  
    webmachine  
    rabbitmq_web_dispatch  
    amqp_client  
    rabbitmq_management_agent  
    rabbitmq_managementPlugin configuration has changed. 
    Restart RabbitMQ for changes to take effect.
```
As invited by the installer, we need to restart rabbitMQ as follows:
```bash
sudo service rabbitmq-server restart
*Restarting message broker rabbitmq-server         [OK]
```
Now using the web browser we can now reach the home page of the management console by navigating to *http://\<hostname\>:15672*

### Configuring users 
We need to configure an administrator user in the Broker as follows:
```bash
sudo rabbitmqctl add_user <YOU_USERNAME> <YOUR_PASSWORD>
[Output]:
Creating user "ccm-admin" ......done.

sudo rabbitmqctl set_user_tags <YOUR_USERNAME> administrator
[Output]:
Setting tags for user "ccm-admin" to [administrator] ......done.

rabbitmqctl set_permissions -p / <YOUR_USERNAME> ".*" ".*" ".*"

```
