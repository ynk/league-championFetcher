# league-championFetcher
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


### Update
To run the updated web app

    gunicorn "app:create_app()"
    
**Purpose**: If this webapp is hosted on a domain/heroku.com (www.heroku.com), it will be easier.
Noone needs to install anything. Entire app is configured to be directly installed and used in heroku.
- Pirate
