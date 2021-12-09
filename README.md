# Tinder-Bot 2021
Tinder Bot: Automate your likes and dislikes. Increase match level! Totaly free and safe.

**DOWNLOAD HERE: https://github.com/stanfortonski/Tinder-Bot/releases/tag/v1.7.1**


## Description
This bot will help you automate giving likes and dislikes. The bot will also likely increase your matcha amount. It gives like/dislike depending on the chance given in the config in percent on like. You can set how much you want from 0 to 100 percent. It works randomly, the bot does not rate photos. That program can save log with **Instagram** and **Snapchat** nicks which those are downloaded from Tinder user description.

## Installation
1. Install Firefox. Link: https://www.mozilla.org
2. Install Python environment. Link: https://www.python.org
3. Add Python path to your system environment variables. 
4. Install Libraries (when you are in unpacked app folder)
```
pip install -r requirements.txt
```
5. Download driver for your Firefox version. Link: https://github.com/mozilla/geckodriver/releases and put it to source files.
5. Open and edit `config.json`.

## Configuration
In your `config.json` file have to change following things:
1. Change your login method. You can login via Facebook or Google.
- To login via Google set `"login_method": "google"`. That doesn't work at this moment! Probably this method will be delete in future.
- To login via Facebook set `"login_method": "facebook"`
2. Set your password to Facebook account or Google account.
```json
#...
"google": {
  "login": "your_google_login",
  "password": "your_google_password"
},
"facebook": {
  "login": "your_facebook_login",
  "password": "your_facebook_password"
}
#...
```
3. Set your chance to like in percent. 
- If `chance_to_like` is 0 It will give only dislikes.
- If `chance_to_like` is 100 It will give only likes.
- Default is 90.
4. To set wait time between give next like or dislike you have to change `max_wait_time_between_action_in_sec` for maximal time delay and 
`min_wait_time_between_action_in_sec` for minimal time delay. Default `min_wait_time_between_action_in_sec` is 2 and `max_wait_time_between_action_in_sec` is 5.
5. This option `amount_of_login_attempts` sets the number of attempts after which if you don't log in It will error occurs. Default is 15.
7. If you want to save Instagram nick from description set `allow_to_save_ig` to true. Default is true.
8. Choose path to your file with Instagram nicknames so change `ig_file_path`. Default is "logs/instagram.txt".
9. If you want to save Snapchat nick from description set `allow_to_save_snap` to True. Default is true.
10. Choose path to your file with Snapchat nicknames so change `snap_file_path`. Default is "logs/snap.txt".

## Usage
Open your terminal/CMD in Tinder-Bot directory and call: `python app.py` or `python3 app.py`. If you want find only Instagram/Snapchat nicknames you will call: `python app-finder.py` or `python3 app-finder.py`

**Created for scientific purposes only. This is not intended to harm anyone. I am not responsible for any damages resulting from the use of this program.**
