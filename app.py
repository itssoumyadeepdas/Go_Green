import streamlit as st
import pandas as pd
from link_tip import *
from file import *
from auth import *

st.set_page_config(page_title="Go Green",page_icon="logo.png")

s=pd.read_csv("Resource/items.csv")
lItem=s['Item Name'].tolist()
lItem.insert(0,"None")

col1, col2, col3 = st.columns(3)
with col1:
    st.write("")
with col2:
    st.image("Logo.png")
with col3:
    st.write("")

st.markdown("<h1 style='text-align: center; color: green; text-shadow: 2px 2px #BDD9B5'>Go Green</h1><hr>", unsafe_allow_html=True)

item=""#st.selectbox("Choose an Item",lItem)
d=pd.DataFrame()

def getComp(df):
    comp=df['Composition'].str.split("-")
    comp=list(comp)
    comp=sum(comp,[])
    outList=(', '.join(comp))
    return(outList) 

def checkStatus(df):
    stat="Not Eco-Friendly"
    if df.iloc[0][-1]==1:
        stat="Eco-Friendly"
    return stat

def contactUs():
    st.sidebar.title("Contact us")
    name=st.sidebar.text_input("Name")
    email=st.sidebar.text_input("Email id")
    rb=st.sidebar.radio("Do you want to",("None","Suggest Item","Give Remarks"))
    if rb=="None":
        pass
    elif rb=="Suggest Item":
        i=st.sidebar.text_input("Item Name",value="item1_item2_...")
    elif rb=="Give Remarks":
        sug=st.sidebar.text_area("Give your remarks/Suggestions")
    bt=st.sidebar.button("Submit")
    if bt and rb=="Suggest Item":
        writeItem([name,email,i])
        st.sidebar.success("Response Collected")
        st.balloons()
    elif bt and rb=="Give Remarks":
        writeRem([name,email,sug])
        st.sidebar.success("Response Collected")
        st.balloons()
    elif bt and rb=="None":
        st.sidebar.error("Please select an action!")
    else:
        pass
def admin():
    st.markdown("<h3 style='text-align: center;'>Admin's Dashboard</h3>", unsafe_allow_html=True)

    st.sidebar.title("Admin Page")
    un=st.sidebar.text_input("Username")
    pw=st.sidebar.text_input("Password",type="password")
    login=st.sidebar.button("Login")
    if login:
        if not checkUsername(un):
            st.sidebar.error("Wrong Username")
        if not checkPassword(pw):
            st.sidebar.error("Wrong Password")
        if checkUsername(un) and checkPassword(pw):
            c1,c2=st.columns(2)
            with c1:
                st.subheader("Item suggested")
                st.dataframe(readItemData(),width=500)
            with c2:
                st.subheader("Remarks")
                st.dataframe(readRemarkData(),width=500)
            
            allResetCol,iResetCol,rResetCol=st.columns(3)
            with allResetCol:
                if st.button("Clear All Data"):
                    remAll()
            with iResetCol:
                iReset=st.button("Clear Items Data")
            with rResetCol:
                remReset=st.button("Clear Remarks Data")

            '''if allReset:
                remAll()
                st.success("Successe fully cleared all")'''
                
            if iReset:
                remItem()
                st.success("Successe fully cleared Item Data")
            
            if remReset:
                remRemarks()
                st.success("Successe fully cleared Remark data")
           # st.info(allReset)

def home():
    item=st.selectbox("Choose an Item",lItem)
    d=s.loc[s['Item Name']==item]

    if item!="None":
        col="green"
        bcol="#d4fce5"
        st.success("**Made up of:  **"+getComp(d))
        if(checkStatus(d)=="Eco-Friendly"):
            st.success("**Type: **"+checkStatus(d))
        else:
            st.error("**Type: **"+checkStatus(d))
            col="darkred"
            bcol="#fcd5d4"
        tips=getTips(d.iloc[0,2])
    
        st.markdown('''<p style="font-size:20px">What you can do?</p>''',unsafe_allow_html=True)
        st.markdown(f'''<p style="border:{col}; color:{col}; background: {bcol}; border-radius: 10px 10px; padding: 15px; border-width:1px; border-style:solid;">{tips}</p>''',unsafe_allow_html=True)
            
        if (checkStatus(d)!="Eco-Friendly"):
            tipButton=st.button("Want some help for upcyling it?")
            if tipButton:
                st.markdown(f'''<p style="font-size:20px">Check out this video for some inspiration and ideas. You can also go to this video link directly from <a href="{getLink(item)}"> here</a></p>''',unsafe_allow_html=True)
                st.video(getLink(item))

options=["Home","Admin","Contact Us"]
x=st.sidebar.selectbox("Goto",options)
st.sidebar.markdown("---")
if x=="Admin":
    admin()
elif x=="Contact Us":
    contactUs()
else:
    home()
