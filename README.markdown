======================
Github-Viewer.slack
======================

# How to setup in your slack team
1. Create a bot user at [here](https://api.slack.com/apps?new_app=1)
2. Get OAuth API Token of the bot user <a name="api_token">***!***</a>

# How to setup in the local
1. `virtualenv .venv && . .venv/bin/activate` (if you need it)
2. `pip install slackbot`
3. Modify config.json for your enviroment
    - API\_TOKEN should be set [this value](#api_token)

# How to run github\_viewer.slack
1. `cd github_viewer_slack && python github_viewer_run.py`
2. Send the message `@{bot_user_name} hi` in set CHANNEL
    - If @{bot\_user\_name} replies some message, you finished to introduce github\_viewer.slack !
