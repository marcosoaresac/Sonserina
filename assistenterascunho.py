from playsound import playsound
import pyttsx3
import datetime

texto_fala = pyttsx3.init()

def falar(audio):

    rate = texto_fala.getProperty('rate')
    texto_fala.setProperty('rate',230) #velocidade de reprodução da voz
    voices = texto_fala.getProperty('voices')
    texto_fala.setProperty('voice',voices[0].id) #escolhendo a voz
    texto_fala.say(audio)
    texto_fala.runAndWait()

def horario():

    tempo = datetime.datetime.now().strftime("%I:%M")
    falar('Agora são exatamente '+tempo)

def data():
    ano = str(datetime.datetime.now().year)
    mes = str(datetime.datetime.now().month)
    dia = str(datetime.datetime.now().day)
    falar('Hoje é dia ' +dia+ ' do '+mes+' de '+ano)

def boas_vindas():
    falar('Olá Chefe, Seja Bem Vindo de volta !')
    horario()
    data()
    hora = datetime.datetime.now().hour
    print(hora)

    if hora >= 6 and hora < 12:
        falar('Tenha um bom dia Chefe')
    elif hora >= 12 and hora > 18:
        falar('Tenha uma boa tarde Chefe')
    elif hora >= 18 and hora <= 24:
        falar('Tenha uma boa noite Chefe')
    else:
        falar('Ainda essa hora Chefe? Precisa descansar !')
    
    falar('Como Posso ajudar?')

boas_vindas()


