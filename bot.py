import discord
import requests
import json

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  async def on_message(self, message):
    if message.author == self.user:
      return
    if message.content.startswith('$meme'):
      await message.channel.send(get_meme())
    if message.content.startswith('$leo'):
      await message.channel.send("esta lavando ropa o cocinando o chapeando btw tiene 0 pentakill lol")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTE0Nzk4Njc3MjAxMDIyMTY0OQ.G54rfv.4TIEJstxDawy5ak9VYYmr-rIuW3g3dzKcouHx0') # Replace with your own token


