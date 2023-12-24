import discord
from discord.ext import commands
import os



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)
client = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
async def hello(ctx):
    await ctx.send(f'Привет! Я Eco_bot, который поможет вам найти ближайшие центры переработки мусора, а также расскажет как правильно сортировать мусор{bot.user}')
    await ctx.send(f'Напишите "/1", если хотите узнать, где ближайший центр переработки. "/2", если хотите узнать, как правильно сортировать мусор. "/3", если хотите получить доп.информацию{bot.user}')

@client.event
async def on_message(message):
    if message.content.startwith("/1"):
        @bot.command()
        async def function(ctx):
            await ctx.send(f'Recyclemap — удобная интерактивная карта раздельного сбора мусора в Москве и других городах России от Greenpeace, где можно найти ближайший к Вам пункт приема отходов. {bot.user}')
            await ctx.send(f'Наши услуги доступны на территории  Москвы, Санкт-Петербурга.  Напишите свой город, если он есть в этом списке{bot.user}')
    elif message.content.startwith("Москва"):
        @bot.command()
        async def function(ctx):
            await ctx.send(f'Экотрейд по адресу Дорожная ул., 3, корп. 1; Экоцентр Собиратор по адресу Кавказский бул., 56, стр. 12; Вторсырьепереработка по адресу Краснопрудная ул., 3-5с1; ГК управление Отходами по адресу Варшавское ш., 1, стр. 17{bot.user}')
    elif message.content.startwith("Санкт-Петербург"):
            @bot.command()
            async def function(ctx):
                await ctx.send(f'Переработкинская по адресу Кожевенная линия, 34Е; 7other по адресу Софийская ул., 127, корп. 11, посёлок Петро-Славянка; Зелёнка по адресу просп. Науки, 17, корп. 8; Экострой по адресу Волхонское ш., 116, корп. 3{bot.user}')
         

#инструкция как правильно сортировать мусор
@client.event
async def on_message(message):
    if message.content.startwith("/2"):
        @bot.command()
        async def instruction(ctx):
            images = (os.listdir('bot_ecology'))
            with open(f'bot_ecology/{instruction1}', 'rb') as f:
                    picture = discord.File(f)
        
            await ctx.send(file=picture)


@client.event
async def on_message(message):
     if message.content.startwith('/3'):
          @bot.command()
          async def usefuk_links(ctx):
                await ctx.send(f'Chinadialogue - независимая некоммерческая организация, занимающаяся продвижением общего понимания экологических проблем Китая, базирующаяся в Лондоне, Пекине и Сан-Франциско {bot.user}')
                await ctx.send(f'Green.TV - широкополосный телевизионный канал для показа фильмов по экологическим проблемам{bot.user}')
                await ctx.send(f'YouTube-канал Экология без фанатизма - здесь публикуют видео, в которых в лёгкой форме рассказывается о различных инициативах по защите окружающей среды. {bot.user}')
                await ctx.send(f'YouTube-канал Our Changing Climate - на этом канале раз в две недели выходят видео в формате небольшого эссе на тему, имеющие отношение к экологии. Они похожи на небольшие документальные фильмы. Каждое длится не больше 10 минут{bot.user}')
                await ctx.send(f'YouTube-канал Going zero waste - на русском YouTube практически нет каналов, посвящённых экологии, так что этот канал также на английском, но можно легко включить субтитры. Здесь девушка с энтузиазмом рассказывает о том, как можно уменьшить свой экологический след.{bot.user}')
                await ctx.send(f'Ecowiki - портал об экологичном образе жизни и экоактивизме в России{bot.user}')
                await ctx.send(f'ЭкоПорт - арсенал знаний и опыта для решения проблемы отходов{bot.user}')
                await ctx.send(f'Экокласс.рф — общероссийские экологические экоуроки для школьников{bot.user}')  
                await ctx.send(f'MyPlasticDiary — приложение, которое помогает посчитать все пластиковые упаковки, в которых мы покупаем еду и другие товары, и сократить их потребление. Здесь можно узнать не только точное количество и состав выброшенного пластика, но и поставить себе цели по сокращению пластиковых отходов.{bot.user}')
                await ctx.send(f'Carbon clock — счетчик выбросов от Bloomberg, наглядно показывающий как именно человечество повлияло (и продолжает влиять) на повышение уровня СО2 в атмосфере. Информация и графики регулярно обновляются.{bot.user}')
                await ctx.send(f'Ecosia — браузер, прибыль от которого идет на посадку новых деревьев. По утверждениям разработчиков, каждый поисковый запрос «удаляет» 1 кг углекислого газа в атмосфере, так как их сервера на 100% работают от источников возобновляемой энергии, а посаженные деревья помогают вытягивать углекислый газ из атмосферы.{bot.user}')
                await ctx.send(f'SOS!Воздух — новая интерактивная карта Greenpeace демонстрирует, сколько источников загрязнения воздуха находится вокруг, и помогает объединить усилия, чтобы сделать воздух чище.{bot.user}')

client.run('MTE1Mjk2MTIzMzM2NDk4NzkzNQ.GC9a9T.N2TuOMMyca75exGp7Q-iYRO4Ec-meyNVmLwWhI ')
bot.run('MTE1Mjk2MTIzMzM2NDk4NzkzNQ.GC9a9T.N2TuOMMyca75exGp7Q-iYRO4Ec-meyNVmLwWhI ')