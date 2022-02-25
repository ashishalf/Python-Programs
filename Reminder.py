import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title=" Reminder ",
            message="Hello Ashish",
            app_icon="D:\Programming\Python\icon.ico",
            timeout=10
        )
        time.sleep(60*60)

    
    