import pandas as pd
import os
tfile=os.path.abspath("https://github.com/sagarkumar3105/Go_Green/blob/907dd8eefaf8e46eb4c5b830fda5b807cdf6154c/Resource/tips.csv")
vfile=os.path.abspath("https://github.com/sagarkumar3105/Go_Green/blob/907dd8eefaf8e46eb4c5b830fda5b807cdf6154c/Resource/link.csv")
t=pd.read_csv("tfile")
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
