## Pull Request Monitor Bot

Bot that monitors Pull requests in the specified repository, and notifies via Telegram


## Setup

### Creating a Telegram Bot

To learn how to create a telegram Bot access [this link](https://core.telegram.org/bots)

![photo_2021-03-27_00-11-48](https://user-images.githubusercontent.com/72465364/112708591-98ce6f80-8e91-11eb-9f59-536c5b681c9f.jpg)

After the creation of a Telegram Bot, you must run [get_chat_id.py](https://github.com/wesley587/Pull-Request-Monitor-Bot/blob/main/get_chat_id.py) with your API token that the bot father generated

![photo_2021-03-26_23-59-18](https://user-images.githubusercontent.com/72465364/112708208-8bb08100-8e8f-11eb-9acf-6031790cd9a4.jpg)
### Create Github Secrets

To learn how to create the needed secrets, click [here](https://docs.github.com/pt/actions/reference/encrypted-secrets#creating-encrypted-secrets-for-a-repository), make sure there are no blanks spaces 

**it is needed to create two secrets keys:**
-   Create TELEGRAM_TOKEN (the field value must receive the token with quotation marks)
-   Create CHAT_ID

![photo_2021-03-27_00-45-10](https://user-images.githubusercontent.com/72465364/112709177-be5d7800-8e95-11eb-9558-da4cdbda9121.jpg)
## Usage

### Add bot in your repository

The final step is to add these files to your repository:
-  monitor_bot.yml
-  send_message.py

**I recommend using the copy and paste method**

Path File [Pull-Request-Monitor-Bot/.github/workflows/monitor_bot.yml](https://github.com/wesley587/Pull-Request-Monitor-Bot/blob/main/.github/workflows/monitor_bot.yml), copy all code and paste in your repository with the similar path

![photo_2021-03-27_01-59-07](https://user-images.githubusercontent.com/72465364/112710447-1600e100-8ea0-11eb-9b64-6b2cd769bb76.jpg)
 
 Copy the content of the [Pull-Request-Monitor-Bot\send_notice.py](https://github.com/wesley587/Pull-Request-Monitor-Bot/blob/main/send_notice.py) and create a file with the same name (send_notice.py) on the repository's root. If you need to change the path or file name, you need a change in your workflow file.

 
 ![photo_2021-03-27_02-26-47](https://user-images.githubusercontent.com/72465364/112710999-f53a8a80-8ea3-11eb-9850-13bc164e01a2.jpg)
 
 
Now you have the bot monitoring your pull requests.
---
![photo_2021-03-28_14-24-13](https://user-images.githubusercontent.com/72465364/112761358-5318c080-8fd1-11eb-815e-39296da5728f.jpg)
---
To learn more about Git Actions, access [this link](https://github.com/features/actions)


To learn more about Git Actions, access [this link](https://github.com/features/actions).
