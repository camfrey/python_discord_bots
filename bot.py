import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    msg = message.content.split(" ")
    
    for word in msg:
        resp = "first of all..... "
        wordlen = len(word)
        print(wordlen)
        print(word)
        if(wordlen<=2):
            continue
        if(word=='liquor'):
            resp = resp + "lick her? I don't even know her!"
        elif (word[wordlen-1]=='a') or (word[wordlen-1]=='A'):
            resp = resp + word[:wordlen-1]+"er? I don't even know her!"
        elif (word[wordlen-1]=='r' or word[wordlen-1]=='R') and (word[wordlen-2]=='e' or word[wordlen-2]=='E'):
            resp = resp + word[:wordlen-2] +" her? I don't even know her!"
        # print(resp)
        if(word=='liquor' or (word[wordlen-1]=='a') or (word[wordlen-1]=='A')) or ((word[wordlen-1]=='r' or word[wordlen-1]=='R') and (word[wordlen-2]=='e' or word[wordlen-2]=='E')):
            await message.channel.send(resp)

        # await message.channel.send(word)

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('')
