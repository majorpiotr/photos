from gtts import gTTS
import os
import time
from langdetect import detect


def mp3(saveFile,text,lang):
    if not text=="":
        print( saveFile+".mp3")
        tts = gTTS(text=text, lang=lang)
        tts.save(saveFile+".mp3")
    else:
        print("No text")


def DetectLanguage(text):
	return detect(text)

def MkAudioDir(item,language):
	if not os.path.exists(item.replace(".txt","")+"Audio_"+language):
		os.makedirs(item.replace(".txt","")+"Audio_"+language)
		return item.replace(".txt","")+"Audio_"+language+"/"
	else:
		return False

def toSeparatedSentences(text,patch,language):
	sentenceNumber=0
	for sentence in text.split("."):
		if not sentence.strip()=="":
			mp3(patch+str(sentenceNumber),sentence,language)
			sentenceNumber+=1
		else:
			print("Empty sentence")

def toOneFile(text,patch,language):
	if not text.strip()=="":
		mp3(patch,text,language)
	else:
		print("Empty sentence")


listDir=os.listdir('.')
for item in listDir:
	if  os.path.isfile(item):
		if '.txt' in item:
			file = open(item).read()
			text= file
			language=DetectLanguage(text)
			patch=MkAudioDir(item,language)
			if patch:
				#toSeparatedSentences(text,patch,language)
				fileName=item.replace(".txt","")
				toOneFile(text,patch+fileName,language)
		else:
			print("it is not txt file")
	else:
		print('it is not a file')












