import speech_recognition as sr 
import pyttsx3
import datetime
from playsound import playsound

audio = sr.Recognizer()
maquina = pyttsx3.init()

DIAS = ['Segunda-Feira','Terça-Feira','Quarta-Feira','Quita-Feira','Sexta-Feira','Sábado','Domingo']

def executar_comandos():
    try:
        with sr.Microphone() as source:
            print('Ouvindo...')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'google' in comando:
                comando = comando.replace('byona','')
                maquina.say(comando)
                maquina.runAndWait()
    except:
        print('Microfone não está ok.')
    return comando

def comando_de_voz():
    comando = executar_comandos()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são '+ hora)
        maquina.runAndWait()
    if 'dia é hoje' in comando:
        dia = datetime.date.today().strftime('%d')
        mes = datetime.date.today().strftime('%B')
        ano = datetime.date.today().strftime('%Y')
        maquina.say('Hoje é dia '+ dia+' de '+mes+' de '+ano)
        maquina.runAndWait()
    if 'dia da semana' in comando:
        dia_da_semana = datetime.date.today().strftime('%A')
        #print(dia_da_semana)
        if dia_da_semana == 'Wednesday':
            maquina.say('Hoje é '+dia_da_semana)
            maquina.runAndWait()
            playsound("wandinha.mp3")
            maquina.runAndWait()
        


comando_de_voz()
