import speech_recognition as sr

r=sr.Recognizer()

demo=sr.AudioFile('C:\\Users\\Gulumkar\\Downloads\\sample audio 36.wav')

with demo as source:
    audio=r.record(source) #offset=4,duration=3

print(r.recognize_google(audio))
