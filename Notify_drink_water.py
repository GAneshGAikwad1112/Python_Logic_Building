# creating a Drink Water Notification Reminder App using Python........

import time
from plyer import notification

if __name__=="__main__":
    while True:

        notification.notify(
            title = "Please Drink Water",
            message = "The National Academies of Science, Engineering and medicine determinded that an adequate daily fluid intake is: About 15.5 cups(3.7 liters) of fluids for men. About 11.5 cups(2.7 liters) of fluids a day for women.",
            timeout = 5
        )
        time.sleep(60*60)