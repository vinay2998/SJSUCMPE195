from pulsesensor import Pulsesensor
import time
from collections import Counter
import serial
import requests

BPMurl="https://us-central1-tempsense-b3bc5.cloudfunctions.net/addBPM"
SPO2url="https://us-central1-tempsense-b3bc5.cloudfunctions.net/addSPO2"

p = Pulsesensor()
p.startAsyncBPM()

i=0
BPMList=[72,72,72,72,72,72,72,72,72,72]
SPO2List=[96,96,96,96,96,96,96,96,96,96]


def most_frequent(List):
         occurence_count=Counter(List)
         return occurence_count.most_common(1)[0][0];
        
     


while i < 10:
    bpm = p.BPM
    spo2 = p.SPO2
    if bpm > 0 and spo2 >80 and bpm < 100 and i < 10:
        if spo2 >100:
            spo2 =100
        print("BPM: ",int(bpm),"SPO2 :",int(spo2),"i: ",int(i))
        BPMList[i]=int(bpm)
        SPO2List[i]=int(spo2)
        i=i+1
    else:
            
        print("No data received")
    time.sleep(1)


print("Most common bpm: ",most_frequent(BPMList))
print("Most common spo2: ",most_frequent(SPO2List))
print("Ready to send these values to http now")
i=0


Br=requests.post(BPMurl, data = most_frequent(BPMList))
Sr=requests.post(SPO2url, data=most_frequent(SPO2List))

print(Br.text)
print(Sr.text)

print("Data sent to https")

              
     
