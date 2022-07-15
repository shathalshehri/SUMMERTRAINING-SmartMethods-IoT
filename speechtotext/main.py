from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as src:
    print('say something...')
    audio = r.listen(src)
    try:
        t = r.recognize_google(audio, language='ar-AR')
        print(t)
        f = open('text.text', 'a', encoding='utf-8') #I'll upload the text file that have been saved on my computer
        f.writelines(t + '\n')
        f.close()
        obj = gTTS(text=t, lang='ar', slow=False)
        obj.save('text.mp3') #I'll upload the audio file that have been saved on my computer
        playsound('text.mp3')
    except sr.UnknownValueError as U:
       print(U)
    except sr.RequestError as R:
        print(R)
