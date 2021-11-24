from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.lang import Builder
import qrcode
import webbrowser


Window.size = (800, 600)
Window.minimum_width, Window.minimum_height = Window.size

class MyLayout(ScreenManager):
    def generate_qr_code(self, args):
        if self.ids.link_text.text != "" and self.ids.img_name.text != "":
            qr = qrcode.QRCode(version=1,box_size=15,border=5)
            qr.add_data(self.ids.link_text.text)
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')
            img.save(f"{self.ids.img_name.text}.png")
        print("Generate Button is pressed")
        
    def view_qr(self, app):
        if self.ids.img_name.text != "":
            self.ids.qr_code_.source = f"{self.ids.img_name.text}.png"
        else:
            self.ids.qr_code_.source = "images/preview.png"
    
    def show_first_page(self, root):
        root.current = "first"
            
    def show_second_page(self, root):
        root.current = "second"
    
    data = {
        'Portfolio': 'account',
        'Github': 'github'
    }

class QR_Generator(MDApp):  
    def callback(self, instance):
        if instance.icon == 'account':
            webbrowser.open("https://vuklekic.herokuapp.com/")
        if instance.icon == 'github':
            webbrowser.open("https://github.com/vukilis")
    
    Builder.load_file('box.kv', encoding='utf8')   
    def build(self):
        self.icon = "images/logo.png"
        self.theme_cls.theme_style = "Dark"
        self.primary_dark_hue="Yellow"
        self.theme_cls.primary_palette = "DeepOrange"
        self.theme_cls.primary_hue = "400"

        return MyLayout()
    
QR_Generator().run()
