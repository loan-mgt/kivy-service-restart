# coding: utf8
__version__ = '0.2'

from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.utils import platform

from jnius import autoclass


from plyer import notification


SERVICE_NAME = u'{packagename}.Service{servicename}'.format(
    packagename=u'org.kivy.oscservice',
    servicename=u'Pong'
)


KV = '''
BoxLayout:
    orientation: 'vertical'
    BoxLayout:
        
        
        Button:
            text: 'start service'
            on_press: app.start_service()
        

'''

class ClientServerApp(App):
    def build(self):
        self.service = None
        # self.start_service()

        self.root = Builder.load_string(KV)
        return self.root

    def start_service(self):

        if platform == 'android':
            service = autoclass(SERVICE_NAME)
            
            mActivity = autoclass(u'org.kivy.android.PythonActivity').mActivity
            argument = ''
            
            service.start(mActivity, argument)




            

            notification.notify(title='main', message='service starting')


       



if __name__ == '__main__':
    ClientServerApp().run()
