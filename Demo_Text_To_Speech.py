import gtts

import os

MyText = "Hi Everyone, Welcome to Python Session. I hope you are learning Something New "
MyVoice =gtts.gTTS(text=MyText,lang='en',slow="True")
MyVoice.save("Speech.mp3")
os.system("Speech.mp3")