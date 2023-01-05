from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import time

from filesharer import FileSharer

Builder.load_file('frontend.kv')        # Metodo que conecta el KV file con el Python File

class CameraScreen(Screen):
    def start(self):
        self.ids.camera.play = True
        self.ids.camera_button.text = "Stop Camera"
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        self.ids.camera.play = False
        self.ids.camera_button.text = "Start Camera"
        self.ids.camera.texture = None

    def capture(self):
        current_time = time.strftime('%Y%m%d-%H%M%S')
        self.filepath = f"files/{current_time}.png"
        self.ids.camera.export_to_png(self.filepath)  # self.ids nos da acceso a los widgets de la clase donde esta escrito el código
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.filepath # self.manager.current_screen.ids nos da acceso a la pantalla del usuario actual (la que esta mirando el usuario)

class ImageScreen(Screen):
    def create_link(self):
        file_path = App.get_running_app().root.ids.camera_screen.filepath
        fileshare = FileSharer(filepath = file_path)
        url = fileshare.share()
        self.ids.link.text = url

class RootWidget(ScreenManager):
    pass



class MainApp(App):

    def build(self):
        return RootWidget()

MainApp().run()