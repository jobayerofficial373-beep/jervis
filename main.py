from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (0.02, 0.03, 0.10, 1)

class JervisApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        title = Label(text='JERVIS AI', font_size=40)
        self.status = Label(text='Hello! I am Jervis.', font_size=22)
        button = Button(text='START JERVIS', font_size=22)
        button.bind(on_press=self.start)
        layout.add_widget(title)
        layout.add_widget(self.status)
        layout.add_widget(button)
        return layout

    def start(self, instance):
        self.status.text = 'Jervis is Ready!'

JervisApp().run()
# Jervis AI App
