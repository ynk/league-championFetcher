# league-championFetcher 
###### v0.0.1-alpha
Script that was seen on [r/leagueoflegends/](https://www.reddit.com/r/leagueoflegends/comments/cctwey/i_created_a_program_to_calculate_how_many_times/)

# info
This is far from perfect so I'm open to improvements and suggestions. 
Feel free to add me on discord. ynk#8213 or to join my discord server: [Discord Invite link](https://discordapp.com/invite/gweJvhp)


-------------------------------------------------------------
# Web App Update
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
gunicorn "app:create_app()" --bind=0.0.0.0:8080 --timeout 300
```

This will be the output... 
```
[2019-07-17 15:41:56 +0600] [25590] [INFO] Starting gunicorn 19.9.0
[2019-07-17 15:41:56 +0600] [25590] [INFO] Listening at: http://0.0.0.0:8080 (25590)
[2019-07-17 15:41:56 +0600] [25590] [INFO] Using worker: sync
[2019-07-17 15:41:56 +0600] [25593] [INFO] Booting worker with pid: 25593
```
* Now it's your job to port your server to connect with port 8080 (or any other port). For testing purpose,
check http://0.0.0.0:8080
* timeout 300 command will keep the connection open as long as 5 minutes aka 300 seconds.

-------------------------------------------------------

-- Happy Hacking (p1r_a_t3)
