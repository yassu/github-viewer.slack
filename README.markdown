======================
Github-Viewer.slack
======================

# How to setup in your slack team
1. Create a bot at [here](https://api.slack.com/apps?new_app=1)
2. Get OAuth API Token of the bot <a name="api_token">***!***</a>

# How to setup in the local
1. `pip install slackbot`
2. Modify config.json for your enviroment
    - API\_TOKEN should be set THE BOT's TOKEN

# How to run github\_viewer.slack
1. `cd github_viewer_slack && python github_viewer_run.py`
2. Send the message `@{bot_name} hi` in set CHANNEL
    - If @{bot\_name} replies some message, you finished to introduce github\_viewer.slack !

# LICENSE
[MIT](LICENSE)
