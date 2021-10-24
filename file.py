import csv
import pandas as pd
import os
from Resource.resourcePath import getResourcePath
itemFile=os.path.join(getResourcePath(),"Resource/userItem.csv")
remFile=os.path.join(getResourcePath(),"Resource/userRemark.csv")
def writeItem(l): #name,email,item
    with open(itemFile,'a',newline="") as iFile:
        write=csv.writer(iFile)
        write.writerow(l)
        iFile.close()
def writeRem(l):
    with open(remFile,'a',newline="") as rFile:
        write=csv.writer(rFile)
        write.writerow(l)
        rFile.close()
def readItemData():
    iData=pd.read_csv(itemFile)
    return iData
def readRemarkData():
    rData=pd.read_csv(remFile)
    return rData
def readItemList():
    iData=pd.read_csv(itemFile)
    l=iData['Items'].str.split("-")
    l=list(l)
    l=sum(l,[])
    outList=(', '.join(l))
    return(outList)

def remAll():
    with open(itemFile,'w+') as iFile:
        write=csv.writer(iFile)
        iFile.truncate()
        write.writerow(["Name","Email","Items"])
        iFile.close
    
    with open(remFile,'w+') as rFile:
        write=csv.writer(rFile)
        rFile.truncate()
        write.writerow(["Name","Email","Remarks"])
        rFile.close
    
