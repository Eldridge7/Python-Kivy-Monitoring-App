from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.textfield import MDTextField

from myapp.auth.admin import validate_admin, is_valid_email, is_valid_password, get_admin_id

class AdminLoginScreen(Screen):
    def __init__(self, **kwargs):
        super(AdminLoginScreen, self).__init__(**kwargs)

        self.layout = MDBoxLayout(orientation='vertical', padding=[50, 100], spacing=10)
        self.add_widget(self.layout)

        Window.clearcolor = (1, 1, 1, 1)  # set white background
        Window.size = (400, 800)  # set window size

        # App logo
        self.logo = Image(source='logo.png', size_hint=(1, .2), height=200)
        self.layout.add_widget(self.logo)

        # Grid layout for inputs
        self.grid = GridLayout(cols=1, size_hint_y=None)
        self.grid.bind(minimum_height=self.grid.setter('height'))

        # Email field
        self.email = MDTextField(hint_text='Admin Email', multiline=False, size_hint_y=None, height=40)
        self.grid.add_widget(self.email)

        # Password field
        self.password = MDTextField(hint_text='Admin Password', password=True, multiline=False, size_hint_y=None, height=40)
        self.grid.add_widget(self.password)

        # Login button
        self.login = MDRaisedButton(text="Admin Log In")
        self.login.bind(on_press=self.validate_admin)
        self.grid.add_widget(self.login)

        # Spacer widget
        self.spacer = MDLabel()  # Empty label acts as a spacer.
        self.grid.add_widget(self.spacer)
        
        # User Login button
        self.user_login = MDFlatButton(text="User Login")
        self.user_login.bind(on_press=self.switch_to_user_login)
        self.grid.add_widget(self.user_login)

        self.layout.add_widget(self.grid)

        # Error message
        self.error = MDLabel(text='', markup=True, size_hint_y=None, height=30)
        self.layout.add_widget(self.error)

    def validate_admin(self, instance):
        if not is_valid_email(self.email.text) or not is_valid_password(self.password.text):
            self.error.text = '[color=ff3333]Invalid email or password format.[/color]'
            return
        if validate_admin(self.email.text, self.password.text):
            self.manager.admin_id = get_admin_id(self.email.text)
            self.manager.current = "admin_dashboard_screen"  # Change this to admin dashboard
            print("Admin logged in successfully!")
        else:
            self.error.text = '[color=ff3333]Invalid email or password.[/color]'


    def switch_to_user_login(self, instance):
        self.manager.current = 'login_screen'  # Change this to your user login screen
