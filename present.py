import cv2,os
import numpy as np
import zbar
import pyzbar.pyzbar as pyzbar
import sys
import datetime, time


fob=open('attendence.txt','a')
names=[]
def main():
# starting the webcam using opencv 
    cap = cv2.VideoCapture(0)
    #function for writing the data into text file
    #function for check the data is present or not
    
    while True:
        _, frame = cap.read() 

        decodedObjects = pyzbar.decode(frame)
        for obj in decodedObjects:
            checkData(obj.data)
            time.sleep(1)
        
        cv2.imshow("Frame", frame)

        #closing the program when s is pressed
        if cv2.waitKey(1)& 0xFF == ord('s'):
            cap.release()
            cv2.destroyAllWindows()
            #os.system('kill %d' % os.getpid())
            break
    
    fob.close()


def enterData(z):
        if z in names:
            pass
        else:
            z=''.join(str(z))
            names.append(z)
            sen = str(datetime.datetime.now())+'-'+z[2:len(z)-1]+'\n'
            print(str(z[2:len(z)-1]))
            fob.write(sen)

def checkData(data):
        data=str(data)
        if data in names:
            #print('Already Present')
            pass
        else:
            enterData(data)
            #print('\n'+str(len(names)+1)+'\n'+data)
            exit()
        

if __name__ == "__main__":
    main()