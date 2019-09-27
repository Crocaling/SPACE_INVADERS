import os

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from pidev.MixPanel import MixPanel
from pidev.kivy.PassCodeScreen import PassCodeScreen
from pidev.kivy.PauseScreen import PauseScreen
from pidev.kivy import DPEAButton
from pidev.kivy import ImageButton
from kivy.properties import ObjectProperty
from kivy.uix.slider import Slider
from kivy.animation import Animation
from kivy.clock import Clock
from pidev.Joystick import Joystick
import logging
import threading
from threading import Thread
from time import sleep

MIXPANEL_TOKEN = "x"
MIXPANEL = MixPanel("Project Name", MIXPANEL_TOKEN)

SCREEN_MANAGER = ScreenManager()
MAIN_SCREEN_NAME = 'main'

class ProjectNameGUI(App):
    """
    Class to handle running the GUI Application
    """

    def build(self):
        """
        Build the application
        :return: Kivy Screen Manager instance
        """
        return SCREEN_MANAGER


Window.clearcolor = (0, 0, 0, 1)  # Black

class MainScreen(Screen):

    joystick = Joystick(0, False)
    space_x_val = ObjectProperty()
    space_y_val = ObjectProperty()

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

    def space_update(self):  # This should be inside the MainScreen Class
        while True:
            self.ship_x_val = self.joystick.get_axis('x') * 400
            self.ids.spaceship.x = self.ship_x_val
            self.ship_y_val = self.joystick.get_axis('y') * -300
            self.ids.spaceship.y = self.ship_y_val
            sleep(.01)

    def bdgy_move(self):
        while True:
            for r in range (0, 10):
                self.ids.bdgy1.x += .1
            for w in range(0, 20):
                self.ids.bdgy1

    def start_space_thread(self):  # This should be inside the MainScreen Class
        Thread(target=self.space_update).start()




Builder.load_file('Invader.kv')
SCREEN_MANAGER.add_widget(MainScreen(name=MAIN_SCREEN_NAME))

def send_event(event_name):
    """
    Send an event to MixPanel without properties
    :param event_name: Name of the event
    :return: None
    """
    global MIXPANEL

    MIXPANEL.set_event_name(event_name)
    MIXPANEL.send_event()


if __name__ == "__main__":
    # send_event("Project Initialized")
    # Window.fullscreen = 'auto'
    ProjectNameGUI().run()