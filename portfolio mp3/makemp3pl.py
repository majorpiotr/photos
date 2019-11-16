from gtts import gTTS
import json
import os
import time

url="./text"

def walk(url):
    listDir=os.listdir(url)
    for dir in listDir:
        path=url+"/"+dir
        if os.path.isfile(path):
            #print(path)
            file=open(path).read()
            data=json.loads(file)
            text=""
            saveUrl=path.replace(".json","")
            
            saveUrl=saveUrl.replace("text","audio")
            saveUrlDir=saveUrl
            #saveUrlDir=saveUrl.split("/")
            #saveUrlDir=saveUrlDir[0:-1]
            #saveUrlDir="/".join(saveUrlDir)
            if not os.path.exists(saveUrlDir):
                #time.sleep(10)
                os.makedirs(saveUrlDir)
                print(saveUrlDir)

            for line in data:
                #print(line["text"])
                saveFile=line["line"]
                saveFile=saveUrlDir+"/"+str(saveFile)
                if not os.path.exists(saveFile+".mp3"):
                    time.sleep(1)
                    #saveFile=open(saveFile,"w+")
                    text= line["text"] 
                    if not text=="":
                        print( saveFile+".mp3")
                        tts = gTTS(text=text, lang='pl')
                        tts.save(saveFile+".mp3")
                    else:
                        print("No text")
                else:
                    print(saveFile," exists")
        else:
            walk(path)

walk(url)