import cv2
import pickle
import numpy


rectW,rectH=107,48

# we ll use try and except to increase performance
try:
    with open('carParkPos','rb') as f:
        posList=pickle.load(f)
except:
    posList=[]

def mouseClick(events,x,y,flags,params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x,y))
    
    if events ==cv2.EVENT_RBUTTONDOWN:
        for i,pos in enumerate(posList):
            x1,y1=pos
            if x1 < x < x1+rectW and y1 < y < y1+rectH:
                posList.pop(1)
    with open('carParkPos','wb') as f:
        pickle.dump(posList,f)


#with while loop it even works for side view and others
while True:
    img=cv2.imread('parkImage.png')
    for pos in posList:
        cv2.rectangle(img,pos,(pos[0]+rectW,pos[1]+rectH),(0,0,255),3)
    cv2.imshow('image',img)
    cv2.setMouseCallback("image",mouseClick)
    cv2.waitKey(1)


