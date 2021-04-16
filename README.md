# duck (v1)
this is a discord.py bot that can help avoid the pin limit on discord by pinning messages and images to a custom channel in your server.

![unknown](https://user-images.githubusercontent.com/20116149/115082297-fb051800-9f05-11eb-9027-c649e1365751.png)

- pins messages to a custom channel 
- keeps track of how many reacters the message has got
- provides a link to jump to the message.
# Running your own instance
- in the main.py file and at the last line add your bot token from https://discord.com/developers/applications
- in the pinbot.py file at self.pinbot_channel= add the id of the channel (right click on a discord channel and Copy ID),
at emoji.name= add your own emoji or use the default one, and also you can change the required amount of reactions for a message to be pinned at len(reacters)>3
- to use a custom emoji you have to rename the emoji.name to str(emoji)=="<:custom_emoji:id>" (replace custom_emoji with the emoji name and change the id to the one of the emoji)
# Support
for any questions or issues, contact me on discord: viks#5591
