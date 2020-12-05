import requests
import functions

def translate():
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
    key = 'trnsl.1.1.20190227T075339Z.1b02a9ab6d4a47cc.f37d50831b51374ee600fd6aa0259419fd7ecd97'
    text = functions.voice.split()[1:]
    lang = 'en-ru'
    r = requests.post(url, data={'key': key, 'text': text, 'lang': lang}).json()
    try:
        functions.speak(r["text"])
    except:
        functions.speak("Обратитесь к переводчику, начиная со слова 'Переводчик'")