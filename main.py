import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

class RepostBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!', intents=intents)
        self.reposted_messages = set()
        self.reaction_threshold = 1  # Default threshold

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_reaction_add(self, reaction, user):
        if reaction.emoji != '📌':  # Check if the emoji is a pushpin
            return

        message = reaction.message

        # Check if the message is from a bot, is already a repost or doesn't meet reaction threshold
        if message.author.bot or message.embeds or reaction.count < self.reaction_threshold:
            return

        # Check if the message has been reposted already
        if message.id in self.reposted_messages:
            return

        # Get the repost channel and send the message as an embed
        repost_channel = discord.utils.get(message.guild.channels, name='pinbot') #######################################
        if not repost_channel:
            return

        self.reposted_messages.add(message.id)
        message = await message.channel.fetch_message(message.id)  # Get the full message object
        if message.content:
            description = message.content
        else:
            description = " "
        embed = discord.Embed(description=description, color=0x00ff00)
        if message.attachments:
            attachment_url = message.attachments[0].url
            if attachment_url.endswith(('.png', '.jpg', '.jpeg', '.gif')):
                embed.set_image(url=attachment_url)
            elif attachment_url.endswith(('.mp4', '.webm', '.mov')):
                content = f"{description}\n{attachment_url}"
                await repost_channel.send(content=content)
                return
        if isinstance(message.author, discord.Member):
            embed.set_author(name=message.author.display_name, icon_url=message.author.avatar.url)
        else:
            embed.set_author(name=message.author.display_name)
        embed.add_field(name="original message", value=f"[jump here]({message.jump_url})", inline=True)
        embed.add_field(name="reactions", value=f"{reaction.count}", inline=True)
        await repost_channel.send(embed=embed)

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def pins(self, ctx, threshold: int):
        print("Setting threshold...")
        if threshold <= 0:
            await ctx.send("The threshold must be greater than 0.")
            return
        self.reaction_threshold = threshold
        await ctx.send(f"The reaction threshold has been set to {threshold}.")

    @pins.error
    async def pins_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have permission to use this command.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("The threshold must be an integer greater than 0.")

if __name__ == '__main__':
    bot = RepostBot()
    bot.run('yourTokenHere')