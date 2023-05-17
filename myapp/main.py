from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from myapp.dashboard.dashboard_screen import DashboardScreen

from .ui.login_screen import LoginScreen
from .ui.register_screen import RegistrationScreen


class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegistrationScreen(name='register'))
        sm.add_widget(DashboardScreen(name="dashboard_screen"))
        return sm
    
    def logout(self):
        self.root.current = "login"

if __name__ == '__main__':
    MyApp().run()

