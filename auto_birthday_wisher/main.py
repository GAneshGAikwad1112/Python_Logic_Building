import pandas as pd
import datetime

def sendEmail(to, sub, msg):
    print(f"Email to {to} sent with subject: {sub} and messag {msg}")
    

if __name__=="__main__":
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