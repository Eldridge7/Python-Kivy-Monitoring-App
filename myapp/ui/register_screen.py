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

from ..auth.user import  register_user, is_valid_email, is_valid_password, get_user_id

class RegistrationScreen(Screen):
    def __init__(self, **kwargs):
        super(RegistrationScreen, self).__init__(**kwargs)
        self.layout = MDBoxLayout(orientation='vertical', padding=[50, 100], spacing=10)
        self.add_widget(self.layout)
       

        Window.clearcolor = (1, 1, 1, 1)  # set white background
        Window.size = (400, 800)  # set window size

        # App logo
        self.logo = Image(source='logo.png', height=200)
        self.layout.add_widget(self.logo)

        # Grid layout for inputs
        self.grid = GridLayout(cols=1, size_hint_y=None)
        self.grid.bind(minimum_height=self.grid.setter('height'))

        # Username field
        # self.username = MDTextField(hint_text='Username', multiline=False, size_hint_y=None, height=40)
        # self.grid.add_widget(self.username)

        # Email field
        self.email = MDTextField(hint_text='Email', multiline=False, size_hint_y=None, height=40)
        self.grid.add_widget(self.email)

        # Password field
        self.password = MDTextField(hint_text='Password', password=True, multiline=False, size_hint_y=None, height=40)
        self.grid.add_widget(self.password)

        # Confirm password field
        self.confirm_password = MDTextField(hint_text='Confirm Password', password=True, multiline=False, size_hint_y=None, height=40)
        self.grid.add_widget(self.confirm_password)

        # Register button
        self.register = MDRaisedButton(text="Register")
        self.register.bind(on_press=self.register_user)
        self.grid.add_widget(self.register)

        self.layout.add_widget(self.grid)

        # Error message
        self.error = MDLabel(text='', markup=True, size_hint_y=None, height=30)
        self.layout.add_widget(self.error)

        # Link for login
        self.login_link = BoxLayout(orientation='horizontal', size_hint_y=None, height=30)
        
        self.login = MDFlatButton(text="Already have an account? Log In")
        self.login.bind(on_press=self.go_to_login)
        self.login_link.add_widget(self.login)

        self.layout.add_widget(self.login_link)

    def register_user(self, instance):
        if self.password.text != self.confirm_password.text:
            self.error.text = '[color=ff3333]Passwords do not match.[/color]'
            return
        if not is_valid_email(self.email.text) or not is_valid_password(self.password.text):
            self.error.text = '[color=ff3333]Invalid email or password format.[/color]'
            return
        if register_user(self.email.text, self.password.text):
            self.manager.user_id = get_user_id(self.email.text)
            self.manager.current = "consent_form_screen"
            print("Registered successfully!")
            print("Logged in successfully!")
        else:
            self.error.text = '[color=ff3333]Registration failed. Try again.[/color]'

    def go_to_login(self, instance):
        self.manager.current = 'login_screen'
