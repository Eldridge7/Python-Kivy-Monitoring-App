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
from ..auth.user import validate_user, is_valid_email, is_valid_password


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

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
        self.email = MDTextField(hint_text='Email', multiline=False, size_hint_y=None, height=40)
        self.grid.add_widget(self.email)

        # Password field
        self.password = MDTextField(hint_text='Password', password=True, multiline=False, size_hint_y=None, height=40)
        self.grid.add_widget(self.password)

        # Login button
        self.login = MDRaisedButton(text="Log In")
        self.login.bind(on_press=self.validate_user)
        self.grid.add_widget(self.login)

        self.layout.add_widget(self.grid)

        # Error message
        self.error = MDLabel(text='', markup=True, size_hint_y=None, height=30)
        self.layout.add_widget(self.error)

        # Links for forgot password and sign up
        self.link_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=30)
        
        self.forgot_password = MDFlatButton(text="Forgot Password?")
        self.forgot_password.bind(on_press=self.reset_password)
        self.link_layout.add_widget(self.forgot_password)

        self.signup = MDFlatButton(text="Sign Up")
        self.signup.bind(on_press=self.create_account)
        self.link_layout.add_widget(self.signup)

        self.layout.add_widget(self.link_layout)

    def validate_user(self, instance):
        if not is_valid_email(self.email.text) or not is_valid_password(self.password.text):
            self.error.text = '[color=ff3333]Invalid email or password format.[/color]'
            return
        if validate_user(self.email.text, self.password.text):
            self.manager.current = "dashboard_screen"
            print("Logged in successfully!")
        else:
            self.error.text = '[color=ff3333]Invalid email or password.[/color]'

    def reset_password(self, instance):
        print("Reset password link clicked!")

    def create_account(self, instance):
        self.manager.current = 'register'
