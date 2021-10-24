import csv
import pandas as pd
itemFile="userItem.csv"
remFile="userRemark.csv"
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
    iData=pd.read_csv("userItem.csv")
    return iData
def readRemarkData():
    rData=pd.read_csv("userRemark.csv")
    return rData
def readItemList():
    iData=pd.read_csv("userItem.csv")
    l=iData['Items'].str.split("_")
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

def Reset(st):
    if st.button("Reset All"):
        remAll()
        return st.success("Removed All Data")