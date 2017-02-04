import asyncio
import discord
import random
import aiohttp

class CompOWBot(discord.Client):
    def __init__(self):
        super().__init__()
        self.prefix = '!'
        self.lockroles = ['Moderator', 'Lite Moderator', 'Competitive Manager']
        self.token = 'TOKEN HERE'
        self.ignore_user_pms = []

    # noinspection PyMethodOverriding
    def run(self):
        try:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(self.start(self.token))
            loop.run_until_complete(self.connect())
        except Exception:
            loop.run_until_complete(self.close())
        finally:
            loop.close()

    async def on_ready(self):

        print('Connected!\n')
        print('Username: ' + self.user.name)
        print('ID: ' + self.user.id)

    async def on_member_join(self, member):
        if member.server.id == '106464638656335872':
            await self.send_message(member, 'Hey! and welcome to the Competitive Overwatch Discord Server! (aka COW)\n'
                                            'Please make sure you read <#108330035563261952> and get some tags so people '
                                            'can identify you and you can post in all the channels!')
        if member.server.id == '227607905602371584':
            await self.send_message(member, 'Hey! and welcome to the Competitive Battlerite Discord Server!\n'
                                            'Please make sure you read <#227608995488202757> and get some tags so people '
                                            'can identify you and you can post in all the channels!')

    async def on_message(self, message):

        if message.author == self.user:
            return
        if message.channel.is_private and message.author.id not in self.ignore_user_pms:
            await self.send_message(discord.utils.get(discord.utils.get(self.servers, id='106464638656335872').channels, id='107388041135452160'), 'I was pm\'d by idiot **{}#{}**:```{}```'.format(message.author.name, message.author.discriminator, message.content))
            if message.author in discord.utils.get(self.servers, id='106464638656335872').members:
                await self.send_message(message.author, 'Please don\'t PM me, I\'m a bot and I don\'t read them. Please post in <#108330035563261952>')
                self.ignore_user_pms.append(message.author.id)
            elif message.author in discord.utils.get(self.servers, id='227607905602371584').members:
                await self.send_message(message.author, 'Please don\'t PM me, I\'m a bot and I don\'t read them. Please post in <#227608995488202757>')
                self.ignore_user_pms.append(message.author.id)
            return
        if '!spamidiots' in message.content.lower() and message.author.id == '77511942717046784':
            members = list(discord.utils.get(self.servers, id='106464638656335872').members)
            for member in members:
                try:
                    async for msg in self.logs_from(member, limit=1):
                        if msg.startswith('Hello from COW League') or [role for role in member.roles if role.id in ['203687868516794368','108343960367296512', '192648741428133888']]:
                            return
                except:
                    pass
                print('spamming idiot {}'.format(member.name))
                try:
                    await self.send_message(member, 'Hello from COW League,\n\nThis is a message to let you know the Minutemen Invitational is happening THIS SATURDAY! This is a Solo-Q styled event that seeds teams randomly by a bot based on roles. Sign-ups are only available to winners of COW Events (COW MVPs), Top 500 (Season 1 and/or Season 2), and pros/top tier competitors. The event is on Saturday, October 29th at 1:00 PM EST and check-in starts at 12:00 EST. Watch the games on Twitch at https://www.twitch.tv/cowleague !\n\nThis tournament is sponsored by Gamer Link (<https://gamerlink.gg>) Gamer Link is your best resource for finding people to play with across multiple games. Download their app for free on your iPhone or Android phone today! \n\n<http://gamerlink.gg/cowleague.html?_branch_match_id=319967885803437000>\n\nShould you have any questions, concerns, or issues with the Minutemen Invitational, please contact .Reclan, Tulimeister, and/or anybody part of the COW Staff. You will be contacted as soon as possible. Please be aware that this is a friendly message from your neighbourhood COWBot, and you will not be messaged again about this event.\n\nThank you,\nCOW League')
                    await asyncio.sleep(0.1)
                except:
                    pass
        if '!setname' in message.content.lower() and message.author.id == '77511942717046784':
            string_name = message.content[9:]
            await self.edit_profile(username=string_name)
        if '!setavi' in message.content.lower() and message.author.id == '77511942717046784':
            string_avi = message.content[8:]
            async with aiohttp.get(string_avi) as r:
                data = await r.read()
                await self.edit_profile(avatar=data)
        if '!restart' in message.content.lower() and message.author.id == '77511942717046784':
            self.logout()
        if message.channel.id == '227608995488202757':
            role_boolean = False
            doit = True
            roles_to_be_added = []
            try:
                arg_list = message.content.split()
            except:
                try:
                    item1, item2 = message.content.split()
                except:
                    self.send_message(message.author, 'Please include more information as detailed in <#108330035563261952>!')
                    self.delete_message(message)
                    return
            for args in arg_list:
                if args.lower() in ['na', 'us']:
                    roles_to_be_added.append(discord.utils.get(message.server.roles, id='227637417341878282'))
                    print('Giving %s NA' % message.author.name)
                    role_boolean = True
                if args.lower() == 'eu':
                    roles_to_be_added.append(discord.utils.get(message.server.roles, id='227637761539178508'))
                    print('Giving %s EU' % message.author.name)
                    role_boolean = True
                if args.lower() == 'ru':
                    roles_to_be_added.append(discord.utils.get(message.server.roles, id='227643158832480266'))
                    print('Giving %s RU' % message.author.name)
                    role_boolean = True
                if args.lower() in ['asia']:
                    roles_to_be_added.append(discord.utils.get(message.server.roles, id='228053512766881792'))
                    print('Giving %s ASIA' % message.author.name)
                    role_boolean = True
                if args.lower() == 'sa':
                    roles_to_be_added.append(discord.utils.get(message.server.roles, id='234422958309900288'))
                    print('Giving %s SA' % message.author.name)
                    role_boolean = True
            if role_boolean:
                role_list = [role for role in message.author.roles if role.name in ['NA', 'EU', 'ASIA', 'RU', 'SA']]
                if role_list:
                    await self.replace_roles(message.author, *list([role for role in message.author.roles if role.name not in ['NA', 'EU', 'ASIA', 'Console', 'PC']]))
                if roles_to_be_added:
                    await self.add_roles(message.author, *roles_to_be_added)
                await self.send_message(message.author, 'I\'ve assigned you the roles `%s`!' % ', '.join([roles.name for roles in roles_to_be_added]))
                try:
                    await self.delete_message(message)
                except:
                    pass
        if message.channel.id == '108330035563261952':
            role_boolean = False
            doit = True
            roles_to_be_added = []
            try:
                arg_list = message.content.split()
            except:
                try:
                    item1, item2 = message.content.split()
                except:
                    self.send_message(message.author, 'Please include more information as detailed in <#108330035563261952>!')
                    self.delete_message(message)
                    return
            for args in arg_list:
                if args.lower() in ['pc', 'computer', 'comp']:
                    roles_to_be_added.append(discord.utils.get(message.server.roles, id='106484246419382272'))
                    print('Giving %s PC' % message.author.name)
                    role_boolean = True
                if args.lower() == 'na':
                    roles_to_be_added.append(discord.utils.get(message.server.roles, id='106492244130807808'))
                    print('Giving %s NA' % message.author.name)
                    role_boolean = True
                if args.lower() == 'asia':
                    roles_to_be_added.append(discord.utils.get(message.server.roles, id='106492261419761664'))
                    print('Giving %s ASIA' % message.author.name)
                    role_boolean = True
                if args.lower() in ['aus', 'australia', 'oce', 'anz']:
                    roles_to_be_added.append(discord.utils.get(message.server.roles, id='222599525473189908'))
                    print('Giving %s ANZ/OCE' % message.author.name)
                    role_boolean = True
                if args.lower() == 'eu':
                    roles_to_be_added.append(discord.utils.get(message.server.roles, id='106492178007621632'))
                    print('Giving %s EU' % message.author.name)
                    role_boolean = True
                if args.lower() in ['console', 'xbox', 'ps4', 'play', 'station']:
                    roles_to_be_added.append(discord.utils.get(message.server.roles, id='186972812328697857'))
                    print('Giving %s Console' % message.author.name)
                    role_boolean = True
            if role_boolean:
                role_list = [role for role in message.author.roles if role.name in ['NA', 'ANZ/OCE' 'EU', 'ASIA', 'Console', 'PC']]
                if role_list:
                    await self.replace_roles(message.author, *list([role for role in message.author.roles if role.name not in ['NA', 'EU', 'ASIA', 'Console', 'PC']]))
                if roles_to_be_added:
                    await self.add_roles(message.author, *roles_to_be_added)
                await self.send_message(message.author, 'I\'ve assigned you the roles `%s`!' % ', '.join([roles.name for roles in roles_to_be_added]))
                try:
                    await self.delete_message(message)
                except:
                    pass

if __name__ == '__main__':
    bot = CompOWBot()
    bot.run()
