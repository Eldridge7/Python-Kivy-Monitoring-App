# ui/consent_form.py
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from myapp.loggers.cliplogger import ClipLogger
from myapp.loggers.keylogger import KeyLogger
from myapp.loggers.screenlogger import ScreenLogger
import threading

class ConsentForm(Screen):
    def __init__(self, **kwargs):
        super(ConsentForm, self).__init__(**kwargs)

        self.layout = BoxLayout(orientation="vertical", spacing=20, padding=[10,10,10,10])
        self.add_widget(self.layout)

        self.keylogger_layout = BoxLayout(orientation="vertical", spacing=10)
        self.keylogger_label = MDLabel(text="Keylogger", size_hint_y=None, height=30, theme_text_color="Secondary")
        self.keylogger_layout.add_widget(self.keylogger_label)
        self.keylogger_info = MDLabel(text="[b]This will track and log all your keystrokes.[/b] It can help diagnose issues with the keyboard input.", markup=True, theme_text_color="Hint")
        self.keylogger_layout.add_widget(self.keylogger_info)
        self.keylogger_check = MDCheckbox(size_hint_y=None, height=30)
        self.keylogger_layout.add_widget(self.keylogger_check)
        self.layout.add_widget(self.keylogger_layout)

        self.cliplogger_layout = BoxLayout(orientation="vertical", spacing=10)
        self.cliplogger_label = MDLabel(text="Clipboard Logger", size_hint_y=None, height=30, theme_text_color="Secondary")
        self.cliplogger_layout.add_widget(self.cliplogger_label)
        self.cliplogger_info = MDLabel(text="[b]This will monitor your system's clipboard.[/b] It's helpful for understanding the data you frequently copy and paste.", markup=True, theme_text_color="Hint")
        self.cliplogger_layout.add_widget(self.cliplogger_info)
        self.cliplogger_check = MDCheckbox(size_hint_y=None, height=30)
        self.cliplogger_layout.add_widget(self.cliplogger_check)
        self.layout.add_widget(self.cliplogger_layout)

        self.screenlogger_layout = BoxLayout(orientation="vertical", spacing=10)
        self.screenlogger_label = MDLabel(text="Screen Logger", size_hint_y=None, height=30, theme_text_color="Secondary")
        self.screenlogger_layout.add_widget(self.screenlogger_label)
        self.screenlogger_info = MDLabel(text="[b]This will take screenshots at regular intervals.[/b] It allows for a visual record of your activity.", markup=True, theme_text_color="Hint")
        self.screenlogger_layout.add_widget(self.screenlogger_info)
        self.screenlogger_check = MDCheckbox(size_hint_y=None, height=30)
        self.screenlogger_layout.add_widget(self.screenlogger_check)
        self.layout.add_widget(self.screenlogger_layout)

        self.buttons_layout = BoxLayout(spacing=10)
        self.confirm_button = MDRaisedButton(text="Accept")
        self.confirm_button.bind(on_release=self.on_confirm)
        self.buttons_layout.add_widget(self.confirm_button)
        
        self.decline_button = MDRaisedButton(text="Decline")
        self.decline_button.bind(on_release=self.on_decline)
        self.buttons_layout.add_widget(self.decline_button)
        self.layout.add_widget(self.buttons_layout)

    def on_confirm(self, instance):
        # Retrieve the user_id from the ScreenManager
        user_id = self.manager.user_id

        if not self.keylogger_check.active and not self.cliplogger_check.active and not self.screenlogger_check.active:
            dialog = MDDialog(title="Consent Form Validation",
                  text="Please consent to at least one logger",
                  size_hint=(0.8, 1),
                  overlay_color=(0, 0, 0, 0.4),  # A value is 0.4 here
                  buttons=[MDRaisedButton(text="OK",
                                          on_release=lambda x: self.dialog_close(x, dialog))])
            dialog.open()
            return
        
        if self.keylogger_check.active:
            self.keylogger = KeyLogger(user_id)
            self.keylogger.start()

        if self.cliplogger_check.active:
            self.cliplogger = ClipLogger(user_id)
            self.cliplogger.start()

        if self.screenlogger_check.active:
            self.screenlogger = ScreenLogger(user_id)
            self.screenlogger.start()

        # Switch to the dashboard after accepting
        self.manager.current = 'dashboard_screen'

    def dialog_close(self, instance, dialog):
        dialog.dismiss()

    def on_decline(self, instance):
        # Switch to the login screen after declining
        self.manager.current = 'login_screen'