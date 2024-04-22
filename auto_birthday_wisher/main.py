import pandas as pd
import datetime
import smtplib
import os

os.chdir(r"C:\Users\Test\Music\Python_Logic_Building\auto_birthday_wisher")

GMAIL_ID = ''
GMAIL_PWD = ''

def sendEmail(to, sub, msg):
    print(f"Email to {to} sent with subject: {sub} and messag {msg}")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(GMAIL_ID,GMAIL_PWD)

    s.sendmail(GMAIL_ID, to,f"Subject: {sub}\n\n{msg}")
    s.quit()


if __name__=="__main__":
    # sendEmail(GMAIL_ID,"subject", "text message")
    
    
    df = pd.read_excel("data.xlsx") 
    today = datetime.datetime.now().strftime("%d-%m")
    yearNow  = datetime.datetime.now().strftime("%Y")
    # print(type(today))

    writeInd = []
    for index, item in df.iterrows():
        print(index, item['Birthday'])
        bday = item['Birthday'].strftime("%d-%m")
        #print(bday)
        if (today == bday) and yearNow not in str(item['Year']):
            sendEmail(item['Email'], "Happy Birthday", item['Dialogue'])
            writeInd.append(index)

    for i in writeInd:
        yr = df.loc[i,'Year']
        yr = df.loc[i,'Year'] = yr +','+str(yearNow)

    print(df)
    df.to_excel('data.xlsx', index = False)