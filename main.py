from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

from filesharer import FileSharer

Builder.load_file('frontend.kv')

class RootWidget(ScreenManager):
    pass

class CameraScreen(Screen):

    def start(self):
        pass

    def stop(self):
        pass

    def capture(self):
        pass

class ImageScreen(Screen):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()

MainApp().run()
