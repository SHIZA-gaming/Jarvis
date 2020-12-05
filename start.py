import functions
import time
import datetime

now = datetime.datetime.now()

if now.hour >= 6 and now.hour < 12:
    functions.speak("Доброе утро!")
elif now.hour >= 12 and now.hour < 18:
    functions.speak("Добрый день!")
elif now.hour >= 18 and now.hour < 23:
    functions.speak("Добрый вечер!")
else:
    functions.speak("Доброй ночи!")

functions.listen()