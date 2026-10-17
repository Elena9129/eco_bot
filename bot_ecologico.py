import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


QUIZ = [
    {
        "domanda": "1. Come ti sposti di solito?",
        "opzioni": "A: Automobile\nB: Mezzi pubblici, a piedi o in bici",
        "corretta": "B",
        "consiglio": "Consiglio: L'uso dell'automobile aumenta le emissioni. Quando puoi, usa i mezzi pubblici o la bici."
    },
    {
        "domanda": "2. Cosa fai quando lasci una stanza?",
        "opzioni": "A: Lascio le luci accese\nB: Spengo le luci",
        "corretta": "B",
        "consiglio": "Consiglio: Lo spreco di energia influisce sull'ambiente. Ricordati di spegnere le luci."
    }
]

@bot.event
async def on_ready():
    print(f"Hai fatto l'accesso come {bot.user}")

@bot.command()
async def eco(ctx):
    await ctx.send(f'Hey,che ne dici di verificare se stai aiutando a inquinare di meno? Rispondi scrivendo A o B')

    
    punteggio = 0
    consigli = []
    
    
    def controlla_utente(messaggio):
        return messaggio.author == ctx.author and messaggio.channel == ctx.channel

    for dati in QUIZ:
      
        await ctx.send(f"\n**{dati['domanda']}**\n{dati['opzioni']}")
        
        
        risposta = await bot.wait_for('message', check=controlla_utente)
        
       
        scelta = risposta.content.upper()
        
        if scelta == dati["corretta"]:
            punteggio += 1
        else:
            consigli.append(dati["consiglio"])

    
    risultato = f"\nQuiz finito, {ctx.author.name}.\nPunteggio: {punteggio}/{len(QUIZ)}\n"
    
    if punteggio == len(QUIZ):
        risultato += "Ottimo lavoro. Non stai inquinando."
    else:
        risultato += "Ecco come puoi migliorare:\n"
        for c in consigli:
            risultato += f"- {c}\n"
            
    await ctx.send(risultato)


bot.run("")
