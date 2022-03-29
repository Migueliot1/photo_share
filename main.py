from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
import webbrowser
import time

from filesharer import FileSharer

Builder.load_file('frontend.kv')

class RootWidget(ScreenManager):
    pass

class CameraScreen(Screen):

    def start(self):
        self.ids.camera.play = True
        self.ids.camera_button.text = 'Stop Camera'
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        self.ids.camera.play = False
        self.ids.camera_button.text = 'Start Camera'
        self.ids.camera.texture = None

    def capture(self):
        current_time = time.strtime('%Y%m%d-%H%M%S')
        filepath = f'files/{current_time}.png'
        self.ids.camera.export_png(filepath)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = filepath

class ImageScreen(Screen):

    no_url_error_msg = 'Create a link first'
    
    def create_link(self):
        filepath = self.ids.img.source
        filesharer = FileSharer(filepath=filepath)
        self.url = filesharer.share()
        self.ids.link.text = self.url

    def copy_link(self):
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.link.text = self.no_url_error_msg

    def open_link(self):
        try:
            webbrowser.open(self.url)
        except:
            self.ids.link.text = self.no_url_error_msg


class MainApp(App):

    def build(self):
        return RootWidget()

MainApp().run()
