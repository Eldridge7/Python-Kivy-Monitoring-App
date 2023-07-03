from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.scrollview import ScrollView
from myapp.db.db import Database

class AdminDashboardScreen(Screen):
    def __init__(self, **kwargs):
        super(AdminDashboardScreen, self).__init__(**kwargs)

        self.layout = MDBoxLayout(orientation='vertical', padding=[50, 50], spacing=10)
        self.add_widget(self.layout)

        self.user_list = MDBoxLayout(orientation='vertical')
        scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))

        # Assuming you have a method to get all users from your database
        db = Database()
        cursor = db.connection.cursor()
        cursor.execute("SELECT email FROM users")
        users = cursor.fetchall()

        for user in users:
            self.user_list.add_widget(OneLineListItem(text=user[0]))

        scroll_view.add_widget(self.user_list)
        self.layout.add_widget(scroll_view)

        # You can add more features to your dashboard like creating users, 
        # deleting users, updating users etc.
