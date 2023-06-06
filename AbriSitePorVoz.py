# Importação das bibliotecas
import speech_recognition as sr
import webbrowser

# Configuração do reconhecimento de voz
r = sr.Recognizer()

# Reconhecimento de voz
with sr.Microphone() as source:
    print("Diga o nome da página que você quer abrir: ")
    audio = r.listen(source)

# Transcrição do áudio
try:
    text = r.recognize_google(audio, language='pt-BR')
    print("Você disse: {}".format(text))
    # Abertura da página na internet
    url = 'https://www.' + text + '.com'+'.br'
    webbrowser.open(url)
except:
    #mensagem de erro caso não consiga reconhecer a voz
    print("Não foi possível reconhecer sua voz. Por favor, tente novamente.")
