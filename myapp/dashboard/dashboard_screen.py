from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty
from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.list import OneLineAvatarIconListItem, IconLeftWidget
from ping3 import ping, verbose_ping
from kivy_garden.graph import Graph, MeshLinePlot
import time
import psutil
import asyncio
import threading


class DashboardScreen(Screen):
    network_uptime = StringProperty('Loading...')
    latency = StringProperty('Loading...')
    packet_loss = StringProperty('Loading...')
    cpu_usage = StringProperty('Loading...')  # Add CPU usage property
    memory_usage = StringProperty('Loading...')  # Add memory usage property
    disk_io = StringProperty('Loading...')  # Add disk I/O property

    def __init__(self, **kwargs):
        super(DashboardScreen, self).__init__(**kwargs)
        # Initialize network uptime with a thread
        self.network_uptime_thread = threading.Thread(target=self.get_network_uptime, args=(60,))
        self.network_uptime_thread.start()
        # Schedule the update_metrics function to run every 60 seconds
        Clock.schedule_interval(self.update_metrics, 5)

    def get_network_metrics(self):
        net_io_start = psutil.net_io_counters()
        time.sleep(1)  # Wait for one second
        net_io_end = psutil.net_io_counters()
        
        sent_rate = net_io_end.bytes_sent - net_io_start.bytes_sent
        recv_rate = net_io_end.bytes_recv - net_io_start.bytes_recv
        
        return sent_rate, recv_rate

    def get_network_uptime(self, count):
        # Send one ping per second for count seconds
        successful_pings = 0
        for _ in range(count):
            if ping('8.8.8.8'):  # Google's DNS server
                successful_pings += 1
            time.sleep(1)
        self.network_uptime = f'{(successful_pings / count) * 100:.1f}%'

    def get_latency(self):
        return ping('8.8.8.8')

    def update_metrics(self, *args):
        # Check if the uptime thread is alive
        if not self.network_uptime_thread.is_alive():
            # If it's not, start a new one
            self.network_uptime_thread = threading.Thread(target=self.get_network_uptime, args=(60,))
            self.network_uptime_thread.start()

        sent_rate, recv_rate = self.get_network_metrics()

        # Convert to kilobytes per second and round to two decimal places
        sent_rate_kb = round(sent_rate / 1024, 2)
        recv_rate_kb = round(recv_rate / 1024, 2)

        latency = self.get_latency()

        # Get CPU usage
        cpu_usage = psutil.cpu_percent()
        # Get memory usage
        memory_usage = psutil.virtual_memory().percent
        # Get disk I/O
        disk_io = psutil.disk_io_counters()

        self.latency = f'{latency:.1f} ms'  # Milliseconds
        self.packet_loss = f'Upload: {sent_rate_kb} KB/s, Download: {recv_rate_kb} KB/s'
        self.cpu_usage = f'{cpu_usage}%'  # Update CPU usage
        self.memory_usage = f'{memory_usage}%'  # Update memory usage
        self.disk_io = f'Read: {disk_io.read_count}, Write: {disk_io.write_count}'  # Update disk I/O
    
dashboard_kv = """
<DashboardScreen>:
    BoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "Dashboard"
        ScrollView:
            do_scroll_x: False
            MDList:
                OneLineAvatarIconListItem:
                    text: "Network Uptime: " + root.network_uptime
                    IconLeftWidget:
                        icon: "update"
                OneLineAvatarIconListItem:
                    text: "Latency: " + root.latency
                    IconLeftWidget:
                        icon: "speed"
                OneLineAvatarIconListItem:
                    text: "Packet Loss: " + root.packet_loss
                    IconLeftWidget:
                        icon: "alert"
                OneLineAvatarIconListItem:
                    text: "CPU Usage: " + root.cpu_usage
                    IconLeftWidget:
                        icon: "memory"
                OneLineAvatarIconListItem:
                    text: "Memory Usage: " + root.memory_usage
                    IconLeftWidget:
                        icon: "memory"
                OneLineAvatarIconListItem:
                    text: "Disk I/O: " + root.disk_io
                    IconLeftWidget:
                        icon: "disk"

        MDRaisedButton:
            text: "Logout"
            on_release: app.logout()
"""

Builder.load_string(dashboard_kv)