# league-championFetcher 
###### v0.0.1-alpha
Script that was seen on [r/leagueoflegends/](https://www.reddit.com/r/leagueoflegends/comments/cctwey/i_created_a_program_to_calculate_how_many_times/)

### info
This is far from perfect so I'm open to improvements and suggestions. 
Feel free to add me on discord. ynk#8213 or to join my discord server: [Discord Invite link](https://discordapp.com/invite/gweJvhp)


-------------------------------------------------------------
## Web App Update
###### v0.0.2-alpha
Refer to this part of the readme on how to run this web app.

### How to run
* Open a python virtualenv using the following command (Or if you already know what you are doing)
    
```
virtualenv --python=python3 ~/.virtualenv/your_virtualenv_name
```
* Now Activate your environment
```
 source ~/.virtualenv/your_virtualenv_name/bin/activate
```
* Now Install all requirements from your project file.
```
pip install -r requirements.txt
```
* Lets start this app. (Run this command from the project directory). This will start the project on port 8080 (or any port you want).
<b> Make sure you are on the root directory of the project when you run the following command </b>
```
gunicorn --workers=10 --worker-class=gevent "app:create_app()" --bind=0.0.0.0:8080 --timeout 300
```

--workers command will create 10 processes to handle multiple request
--worker-class gevent will handle all the request asynchronously
--bind 0.0.0.0:8080 will bind the app. (self explanatory!)
--timeout 300 (self explanatory!)

This will be the output... 
```
[2019-07-21 11:15:55 +0600] [8077] [INFO] Starting gunicorn 19.9.0
[2019-07-21 11:15:55 +0600] [8077] [INFO] Listening at: http://0.0.0.0:8080 (8077)
[2019-07-21 11:15:55 +0600] [8077] [INFO] Using worker: gevent
[2019-07-21 11:15:55 +0600] [8080] [INFO] Booting worker with pid: 8080
[2019-07-21 11:15:55 +0600] [8081] [INFO] Booting worker with pid: 8081
[2019-07-21 11:15:55 +0600] [8082] [INFO] Booting worker with pid: 8082
[2019-07-21 11:15:55 +0600] [8084] [INFO] Booting worker with pid: 8084
[2019-07-21 11:15:55 +0600] [8085] [INFO] Booting worker with pid: 8085
[2019-07-21 11:15:55 +0600] [8086] [INFO] Booting worker with pid: 8086
[2019-07-21 11:15:55 +0600] [8089] [INFO] Booting worker with pid: 8089
[2019-07-21 11:15:56 +0600] [8091] [INFO] Booting worker with pid: 8091
[2019-07-21 11:15:56 +0600] [8092] [INFO] Booting worker with pid: 8092
[2019-07-21 11:15:56 +0600] [8094] [INFO] Booting worker with pid: 8094
```
* Now it's your job to port your server to connect with port 8080 (or any other port). For testing purpose,
check http://0.0.0.0:8080
* timeout 300 command will keep the connection open as long as 5 minutes aka 300 seconds.

-------------------------------------------------------

-- Happy Hacking (p1r_a_t3)
