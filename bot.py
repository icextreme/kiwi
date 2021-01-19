import discord
import asyncio
import os
import random
import sqlite3
from discord.ext import commands, tasks

#TODO: Have bot add members to database with according values when it is run
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = ',',intents=intents)
client.remove_command('help')

conn = sqlite3.connect('members.db')
c = conn.cursor()
rolesList = ['Dodo Red','Dodo Orange','Dodo Yellow','Dodo Green','Dodo Teal','Dodo Copyright','Dodo Bluev2','Dodo Blue','Dodo Purplev2','Dodo Purple','Dodo Pinkv2','Dodo Pink']
activateRoles = ['Red','Orange','Yellow','Green','Teal','Copyright','Bluev2','Blue','Purplev2','Purple','Pinkv2','Pink']

@client.command()
async def load(ctx,extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx,extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_ready():
    print("Bot is Ready")
    guild = client.get_guild(744817281871249428)
    channel = guild.get_channel(800965152132431892)
    print(f"{guild}")
    memberList = guild.members
    print(memberList)
    for m in memberList:
        c.execute(f"""INSERT INTO dodos 
                      VALUES ('{m.id}',0,0,0,0,0,0,0,0,0,0,0,0,0)
                      """)
        conn.commit()

        print(f"Adding {m} into database as {m.id}")
        c.execute(f"""SELECT *
                      FROM dodos
                      WHERE id = {m.id}
        """)
        conn.commit()
        print(c.fetchall())


    for m in memberList:
        user = str(m)
        embed=discord.Embed(title= user + "'s Roles" , color=0xe392fe)
        embed.set_thumbnail(url=m.avatar_url)
        for role in rolesList:
            roleDiscord = discord.utils.get(guild.roles, name=role)
            if (roleDiscord in m.roles):
                if((m.id == "264645255427522560") and role == ("Dodo Copyright")):
                    role = role.split(" ")
                    c.execute(f"""UPDATE dodos
                                SET {role[1]} = 2
                                WHERE id = {m.id}

                        """)
                    roleCount = (c.fetchone()[0])
                    roleCount = str(roleCount)
                    roleCount = roleCount + " Dodo " + str(role[0]) + " " + str(role[1]) + " roles"
                    embed.add_field(name=roleCount, value="Information about how many of this role you have", inline=False)

                elif((m.id == "233048072375107584") and (role == "Dodo Yellow")):
                    role = role.split(" ")
                    role = role.split(" ")
                    c.execute(f"""UPDATE dodos
                                SET {role[1]} = 2
                                WHERE id = {m.id}

                        """)
                    roleCount = (c.fetchone()[0])
                    roleCount = str(roleCount)
                    roleCount = roleCount + " Dodo " + str(role[0]) + " " + str(role[1]) + " roles"
                    embed.add_field(name=roleCount, value="Information about how many of this role you have", inline=False)

                elif((m.id == "632326508949798925") and (role == "Dodo Bluev2")):
                    role = role.split(" ")
                    c.execute(f"""UPDATE dodos
                                SET {role[1]} = 2
                                WHERE id = {m.id}

                        """)
                    role = role.split(" ")
                    roleCount = (c.fetchone()[0])
                    roleCount = str(roleCount)
                    roleCount = roleCount + " Dodo " + str(role[0]) + " " + str(role[1]) + " roles"
                    embed.add_field(name=roleCount, value="Information about how many of this role you have", inline=False)
                
                elif((m.id == "200035991598268416") and (role == "Dodo Pinkv2")):
                    role = role.split(" ")
                    c.execute(f"""UPDATE dodos
                                SET {role[1]} = 2
                                WHERE id = {m.id}

                        """)
                    role = role.split(" ")
                    roleCount = (c.fetchone()[0])
                    roleCount = str(roleCount)
                    roleCount = roleCount + " Dodo " + str(role[0]) + " " + str(role[1]) + " roles"
                    embed.add_field(name=roleCount, value="Information about how many of this role you have", inline=False)
                    
                else:
                    role = role.split(" ")
                    c.execute(f"""UPDATE dodos
                                SET {role[1]} = 1
                                WHERE id = {m.id}

                        """)
                    conn.commit()
                    c.execute(f"""SELECT {role[1]}
                                FROM dodos
                                WHERE id = {m.id}
                    """)
                    roleCount = (c.fetchone()[0])
                    roleCount = str(roleCount)
                    roleCount = roleCount + " Dodo " + str(role[0]) + " " + str(role[1]) + " roles"
                    embed.add_field(name=roleCount, value="Information about how many of this role you have", inline=False)
        await channel.send(embed=embed)


@client.event
async def on_member_join(member):
    c.execute(f"""INSERT INTO dodos 
                  VALUES ('{member.id}',0,0,0,0,0,0,0,0,0,0,0,0,0)
              """)
    conn.commit()
    guild = client.get_guild(744817281871249428)
    channel = guild.get_channel(800965152132431892)
    user = str(member)
    embed=discord.Embed(title= user + "'s Roles" , color=0xe392fe)
    embed.set_thumbnail(url=member.avatar_url)
    for role in activateRoles:
        c.execute(f"""SELECT {role}
                        FROM dodos
                        WHERE id = {member.id}
        """)
        roleCount = str(c.fetchone()[0]) + " Dodo " + role + " roles"
        embed.add_field(name=roleCount, value="Information about how many of this role you have", inline=False)
    await channel.send(embed=embed)

@client.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Please pass in all required arguments. Use ,help for a list of commands")
    elif isinstance(error,commands.CommandOnCooldown):
        pass
    elif isinstance(error,commands.CommandNotFound):
        await ctx.send(f"That command does not exist. Use ,help for a list of commands")

@client.event
async def on_command_completion(ctx):
    if ctx.command == "collect":
        guild = client.get_guild(744817281871249428)
        channel = guild.get_channel(800965152132431892)
        user = str(ctx.message.author)
        embed=discord.Embed(title= user + "'s Roles" , color=0xe392fe)
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        for role in activateRoles:
            c.execute(f"""SELECT {role}
                            FROM dodos
                            WHERE id = {ctx.message.author.id}
            """)
            roleCount = str(c.fetchone()[0]) + " Dodo " + role + " roles"
            embed.add_field(name=roleCount, value="Information about how many of this role you have", inline=False)
        await channel.send(embed=embed)


@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="All Commands For Kiwi Bot",color=0x59cbf0)
    embed.set_thumbnail(url="https://i.imgur.com/Yx2cH7O.png")
    embed.add_field(name="Help Commands", value="**,help** - shows this message \n**,ping** - check if kiwi is still up", inline=False)
    embed.add_field(name="Mention A User Commands", value="**,waves @user** - waves at a user \n**,wavesRole @role** - waves at a group \n**,hugs @user** - gives the selected user a hug \n**,hugsRole @role** - group hug", inline=False)
    embed.add_field(name="Determine An Outcome Commands", value="**,8ball question** - ask Kiwi a question \n**,coinflip** - flip a coin", inline=False)
    embed.add_field(name="Role Based Commands", value="**,collect** - obtain a role! 12 hour cooldown \n**,activate \"role\"** - activate a ,collect role\n**,trade \"your role\" @user \"their role\"**\n**,myroles** - display a list of your roles \n**,roles** - display a list of collectable roles", inline=False)
    embed.add_field(name="String Manipulation", value="**,fw message** - add sparkles between words \n**,spaced message** - space our your message \n**,spongebob message** - SpOnGeBoB MeMe", inline=False)
    embed.add_field(name="Other", value="**,randomnumber a b ** - display rng [a,b]", inline=False)
    await ctx.send(embed=embed)

client.run(os.environ['TOKEN'])
