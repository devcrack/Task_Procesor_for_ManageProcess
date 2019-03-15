# Task Process for Process Manager
## Requirements :
* Rabittmq
* celery
* virtualenv
* python 3 or higher

## RabbitMQ configuration
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
## Celery broker configuration
In your Celery base configuration you have to add the parameters that we have configured 
```python
CELERY_BROKER_URL = 'amqp://<YOUR_USERNAME>:<YOUR_USERPASSWORD>@<BROKER_SERVER_ADDRESS>:5672'
```
A Result Backend if you have
```python
CELERY_RESULT_BACKEND = 'mongodb://user:mientras123@ds157574.mlab.com:57574/connect_to_mongo'
```
## Executing Task 
```bash
celery worker -A main.main.celery_instance --loglevel=info
```

# Todos
- [ ] Enable Lite Task for Task Process
    - [X] Codify the executiong of Hard Sphere
    - [ ] Codify the executiong of Soft Sphere
    - [ ] Codify the executiong of Yukawa
- [ ] Configure Broker  for connect microservice 
    - [ ] Configure User for connect to broker externally
- [ ] Execute with API and Celery