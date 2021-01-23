import datetime
from plyer import notification
from jnius import autoclass




if __name__ == '__main__':
    notification.notify(title='service', message=str(datetime.datetime.now().time()))
    pyservice = autoclass('org.kivy.android.PythonService')
    pyservice.mService.setAutoRestartService(True)

