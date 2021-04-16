import discord
from discord.ext import commands
import json

class pinbot(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
        self.pinbot_channel_id=000000000000000000 #the id of the channel where the pins will be posted

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message_id=payload.message_id
        msg_channel_id=payload.channel_id
        emoji=payload.emoji
        channel=self.bot.get_channel(msg_channel_id)
        message=await channel.fetch_message(message_id)
        with open("required files/pins.json", "r") as f:
            data = json.load(f)
        pinned_messages = data["pins"]
        pinned_msgs = []
        for msg in pinned_messages:
            for _id in msg:
                pinned_msgs.append(int(_id))
        if message_id not in pinned_msgs:
            if emoji.name=="pushpin" or emoji.name==("📌"):  #you can add your custom emoji here
                reactions=message.reactions
                for item in reactions:
                    if str(item.emoji)=="📌":
                        reacters=await item.users().flatten()
                if len(reacters)>3:  #add your custom reaction amount here (default is above 3)
                    embed=discord.Embed(color=0xff0000)
                    if message.attachments:
                        embed.set_image(url=message.attachments[0].url)
                    embed.title=f"📌{len(reacters)}"
                    embed.description=f"{message.content}\n[View message]({message.jump_url})"
                    embed.set_author(icon_url=message.author.avatar_url_as(static_format="png"), name=message.author.name)
                    sb_channel=self.bot.get_channel(self.pinbot_channel_id)
                    embed.timestamp=message.created_at
                    new_pinned_message = await sb_channel.send(embed=embed)
                    data["pins"].append({f"{message_id}": [new_pinned_message.id, len(reacters)]})
                    with open("required files/pins.json", "w") as f:
                        json.dump(data, f)
                  
        else:
            with open("required files/pins.json", "r") as f:
                data = json.load(f)
            if emoji.name=="pushpin" or emoji.name==("📌"):
                for msgs in data["pins"]:
                    if str(message_id) in msgs:
                        rs = message.reactions
                        for item in rs:
                            if str(item.emoji)=="📌":
                                reacters=await item.users().flatten()
                        msgs[str(message_id)][1]=len(reacters)
                        sbc = self.bot.get_channel(self.pinbot_channel_id)
                        m = await sbc.fetch_message(msgs[str(message_id)][0])
                        emb = m.embeds[0]
                        emb.title=f"📌{msgs[str(message_id)][1]}"
                        await m.edit(embed=emb)
                    with open("required files/pins.json", "w") as f:
                        json.dump(data, f) 
    



def setup(bot):
    bot.add_cog(pinbot(bot))