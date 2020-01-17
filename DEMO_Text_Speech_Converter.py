#Step1: Import gtts (Google text to spech converter)
#Step2: Implement gTTS()(Constructor)
"""
Step3: Save file as Mp3
Step4: play file """
import gtts
import os
from gtts import gTTS
MyText = "Hello Everyone, Welcome to Python Workshop.I hope you are learning somethig new."
MySpeech = gTTS(MyText,lang='en',slow=False)
MySpeech.save("MySpeech.Mp3")
os.system("MySpeech.Mp3")
