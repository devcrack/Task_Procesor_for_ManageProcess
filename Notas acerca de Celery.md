# Notas de Celery y Rabbitmq

## Errores y Soluciones 

### Login was refused using authentication mechanism
Note that : **user 'guest' can only connect via localhost**

## Others Notes

#### My_User and Passwords

user: devcrack

password:mientras123


## Usefull links 
[Markdown cheatsheet_#1](https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf)

[Markdown cheatsheet_#2](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

[Markdown cheatsheet_#3](https://www.markdownguide.org/cheat-sheet/)

# Celery and Rabbitmq Architecture and Workflow
### Producers 
Place jobs in the task queue 
### Consumers
Check the head of the task queue for awaiting jobs.

Producers are commonly the web nodes or whatever system placing jobs in the task queue.

The queue is commonly referred as **Broker** and Consumers as **Workers** 

**Note** that a worker can also place new task the queue so  its behave is a producer too.



