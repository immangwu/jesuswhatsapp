import pyautogui as pg
import webbrowser as web
import time
import pandas as pd
data = pd.read_csv("leads.csv",encoding= 'unicode_escape')
data_dict = data.to_dict('list')
leads = data_dict['LeadNumber']
messages = data_dict['Message']
Filenames = data_dict['Filename']
combo = zip(leads,Filenames)
first = True

for lead,Filename in combo:
    time.sleep(4)
    message = ''' Dear {},\n

  Greetings from Sri Ramakrishna Institute of Technology, Coimbatore, Tamil Nadu, India.\n\v

We are glad to inform you that we are organizing Virtual Innovation Product Expo, VIPE 2021 for the students to promote and kindle the young minds of our society towards Research and development.\n\v


//Last Date for Registration : 08.02.2021//\n\v
//Submission of Presentation : 15.02.2021//\n\v
//Result Date : 17.02.2021//\n

We request you to kindly encourage young students from your School to participate in this event and make it a grand success.\n\v
Registration Link - https://forms.gle/hGewup9i28Dk2HpP8\n\v

To see Promo Video : https://youtu.be/2ufp9I5rxdc\n\v

 Thank you!!.  \n\v

With Regards 
Dr.S.Nagarani, 9842693221\n\v
Mr.E.Ramkumar, 9655888810\n\v
Mr.R.Immanual, 9677817992\n\v
Dr.K.Sheela Shobana Rani,9442933334'''.format(Filename)
    web.open("https://web.whatsapp.com/send?phone="+lead+"&text="+message)
    if first:
        time.sleep(10)
        first=True
    
    pg.moveTo(490, 694, duration=1)
    pg.click()
    pg.moveTo(486, 632, duration=1)
    pg.click()
    time.sleep(1)
    mediafile="1.png"
    pg.typewrite(mediafile)
    time.sleep(1)
    pg.press('enter')
    time.sleep(1)
    width,height = pg.size()
    pg.click(width/2,height/2)
    time.sleep(8)
    
    pg.press('enter')
    time.sleep(8)
    pg.hotkey('ctrl', 'w')
