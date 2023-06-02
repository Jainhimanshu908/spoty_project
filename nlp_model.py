import streamlit as st
import numpy as np
import pandas as pd 
import sklearn

import pickle 

model_1 = pickle.load(open('model_knn.pkl','rb'))
from PIL import Image 
def log_data():
    st.title('welcome! listner!')
    img1 =Image.open('image2.png')
    img1 = img1.resize((250,150))
    st.image(img1,use_column_width=False)
    st.sidebar.header('About')
    st.text('''Music consumption habits have changed dramatically with the rise of 
streaming services like Spotify, Apple Music, and Tidal. The skip button plays 
a large role in the user’s experience, as they are free to abandon songs as they 
choose. Music providers are also incentivized to recommend songs that their 
users like in order to increase user experience and time spent on the platform''')
    ######
    
    
    st.text_input("Enter your name")
    st.text_input("Enter your mail")


log_data()
log_id =st.button("sign up")
if log_id:
    st.text('Thankyou ')

# mic=st.button("explore")
# def expo():
#     img2 =Image.open('m1.png')
#     img2 = img2.resize((250,150))
#     st.image(img1,use_column_width=False)
 
#     img3 =Image.open('m2.png')
#     img3 = img3.resize((250,150))
#     st.image(img1,use_column_width=False)
#     img4 =Image.open('m3.png')
#     img4 = img4.resize((250,150))
#     st.image(img1,use_column_width=False)
    



# if mic:
#     expo()
def model_e():
    # for prmium membership or not 
    st.title('welcome!')
    img1 =Image.open('image1.png')
    img1 = img1.resize((350,250))
    st.image(img1,use_column_width=False)
    ########
    st.sidebar.text("This model can predict yow will skip the song or you will continue with song ") 
    premium =['Yes','No']
    
    prem = st.selectbox("Are you a premium member ?",premium)
    if prem=='Yes':
       pre=1
    if prem =='No':
       pre=0
        
       
    # for time or hour of day
    day_hour=st.slider('please tell me the time when you are listening song ?',1,24)

    # cotext type 

    cont= {'catalog': 0, 'charts': 1, 'editorial_playlist': 2, 'personalized_playlist': 3, 'radio': 4, 'user_collection': 5}

    sta= {'catalog', 'charts', 'editorial_playlist','personalized_playlist', 'radio','user_collection'}
    capi = st.selectbox("your song context ?",sta)
    st_p = cont[capi]

    # behavioue to start 
#     st.text("most import factor to predict is why you are listning song ")

    beha={'appload': 0, 'backbtn': 1, 'clickrow': 2, 'endplay': 3, 'fwdbtn': 4, 'playbtn': 5, 'remote': 6, 'trackdone': 7, 'trackerror': 8}
    behavi={'appload', 'backbtn', 'clickrow', 'endplay', 'fwdbtn', 'playbtn', 'remote', 'trackdone', 'trackerror'}

    be=st.selectbox("why you play new song (most important factor to predict is why you are listning song)  ?",behavi)
    be_i=beha[be]

#popularity
    popular=st.slider('want to give rating in 100 stars ?',1,100)

    # song duration
    dura =st.slider('song duration in seconds  ?',1,360)
# reason end 
#     st.text("most important factor why you end listning song ")

    end_reason= {'backbtn': 0, 'clickrow': 1, 'endplay': 2, 'fwdbtn': 3, 'logout': 4, 'remote': 5, 'trackdone': 6}
    endo ={'backbtn', 'clickrow', 'endplay', 'fwdbtn', 'logout', 'remote', 'trackdone'}
    en= st.selectbox('why you stopped the song (most important factor to predict is why you are end listning song)?',endo)
    en_i=end_reason[en]

    # mode
    ene = {'major': 1, 'minor': 0}
    enem ={'major', 'minor'}
    ee= st.selectbox('please select the mode of song',enem)
    en_k=ene[ee]

    # energy 
    energo =st.slider('energy of song ?',0,100)
    energymy = 0.01*energo

    # speccheness
    spicho = st.slider('song is like a speech',0,100)
    spi=spicho*0.01

    sub=st.button("submit")
    if sub:
        input_data =(day_hour,pre,st_p,be_i,en_i,dura,popular,energymy,en_k,spi)
        input_data_as_numpy_array = np.asarray(input_data)
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

        prediction = model_1.predict(input_data_reshaped)
        k=list(prediction)
        result=k[0]
        our_result={0 :'skipped',1:'not skipped'}
        final_r=our_result[result]
        st.write('your song will be : ',final_r)


        if final_r=='skipped':
            img1 =Image.open('skips_1.png')
            img1 = img1.resize((250,150))
            st.image(img1,use_column_width=False)
        else:
            img1 =Image.open('no_skip.png')
            img1 = img1.resize((250,150))
            st.image(img1,use_column_width=False)


     






model_e()
