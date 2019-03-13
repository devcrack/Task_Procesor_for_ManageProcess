# Task Process for Process Manager
## Requirements :
First of all you need to have install the broker. For this we going use RabbitQM server.

For install this: ```sudo apt install rabbitmq-server``` :+1:

You can also install the management plugin for make more easy to peek into a running RabbitQM instance. Let's install the management plugin as follows: 
```
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
    

