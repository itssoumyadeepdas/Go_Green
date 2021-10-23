import pandas as pd

t=pd.read_csv("https://github.com/sagarkumar3105/Go_Green/blob/2b413d4d7e78cab16d38b5a50cc51e9b753bb6c0/Resource/tips.csv")
v=pd.read_csv("https://github.com/sagarkumar3105/Go_Green/blob/907dd8eefaf8e46eb4c5b830fda5b807cdf6154c/Resource/link.csv")
def getLink(item):
    d=v.loc[v['Item']==item]
    return (d.iloc[0,1])

def getTips(cat):
    tip=t.loc[t['Category']==cat]
    tip=tip['Remarks']
    tip=tip.str.split("-")
    tip=list(tip)
    tip=sum(tip,[])
    tipStr=('<br>'.join(tip))
    return (tipStr)
