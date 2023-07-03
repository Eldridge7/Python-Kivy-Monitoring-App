from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from myapp.admin.admin_dashboard import AdminDashboardScreen
from myapp.admin.admin_login import AdminLoginScreen
from myapp.dashboard.dashboard_screen import DashboardScreen
from myapp.ui.consent_form import ConsentForm

from .ui.login_screen import LoginScreen
from .ui.register_screen import RegistrationScreen


class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login_screen'))
        sm.add_widget(RegistrationScreen(name='register_screen'))
        sm.add_widget(DashboardScreen(name="dashboard_screen"))
        sm.add_widget(ConsentForm(name="consent_form_screen"))
        sm.add_widget(AdminLoginScreen(name='admin_login_screen'))
        sm.add_widget(AdminDashboardScreen(name='admin_dashboard_screen'))

        return sm

    def stop_loggers(self):
        consent_form_screen = self.root.get_screen('consent_form_screen')
        if hasattr(consent_form_screen, 'cliplogger'):
            consent_form_screen.cliplogger.stop()
        if hasattr(consent_form_screen, 'keylogger'):
            consent_form_screen.keylogger.stop()
        if hasattr(consent_form_screen, 'screenlogger'):
            consent_form_screen.screenlogger.stop()

    def logout(self):
        self.stop_loggers()
        self.root.current = "login_screen"
    
    def on_stop(self):
        # stop the loggers when the app is about to stop
        self.stop_loggers()

if __name__ == '__main__':
    MyApp().run()
