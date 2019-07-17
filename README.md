# league-championFetcher 
###### v0.0.1-alpha
Script that was seen on [r/leagueoflegends/](https://www.reddit.com/r/leagueoflegends/comments/cctwey/i_created_a_program_to_calculate_how_many_times/)

I have made a discord server dedicated to things like this  [Discord Invite link](https://discordapp.com/invite/gweJvhp) (Updated)


# Requirments
* A [Development API Key](https://developer.riotgames.com/) 
* pip 
* [python 3+](https://www.python.org/downloads/)
* requests (pip install requests)

# Usage

1) Run the file generate a working [Development API Key](https://developer.riotgames.com/)
2) Download and install [python 3+](https://www.python.org/downloads/) 
3) **Make sure to enable python Path checkbox**: 

![img1](https://i.imgur.com/2sfqDju.png)

4) Install python.
5) Install requests trough pip

![img1](https://i.imgur.com/M3nhH0M.png)

5) Download or clone the repositry 

6) Edit [championFetcher.py](https://github.com/YannickDC/league-championFetcher/blob/master/championFetcher.py) 

![img1](https://i.imgur.com/Ld9EPp0.png)

7) Copy & Paste **your api key!**: 

![img1](https://i.imgur.com/kSpXkyO.png)

![img1](https://i.imgur.com/L8oeLEF.png)

8) Press either **F5** or go hover over the **Run** box and select **Run Module** 

![img1](https://i.imgur.com/HBilqob.png)

9) Enjoy!

![img1](https://i.imgur.com/GYNjDf9.png)


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
* Lets start this app. (Run this command from the project directory). This will start the project on port 8080 (or any port you want)
```
gunicorn "app:create_app() --bind=0.0.0.0:8080
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

-------------------------------------------------------

-- Happy Hacking (p1r_a_t3)
