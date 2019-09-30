import os

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label

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
import random

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
    ship_x_val = ObjectProperty()
    ship_y_val = ObjectProperty()
    bdgy_pos = ObjectProperty()
    global event1
    global array
    global array2
    array = []
    array2 = []

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        global event1
        event1 = Clock.schedule_interval(self.fire, 1/4)
        event2 = Clock.schedule_interval(self.fire2, 1/2)
        # I just used clock scheduling to see if it would work but you turn this into a thread instead if you want. if the fire function needs to be canceled, do event1.cancel()
        self.bdgy_pos = .1

    global xin
    xin = 0
    global x

    def counter(self):
        global xin
        global x
        xin = xin + 1
        if xin == 100:
            xin = 0
        else:
            # print ("%d" % xin)
            x = "%d" % xin

    def moveup(self):
        for labels in array:
            if(labels.y > 290):
                array.remove(labels)
                self.remove_widget(labels)
            labels.y = labels.y + 10
    def moveup2(self):
        for labels2 in array2:
            if(labels2.y < -290):
                array2.remove(labels2)
                self.remove_widget(labels2)
            labels2.y = labels2.y - 7
    def fire(self,dt):
        if(self.joystick.get_button_state(0)==1):
            global array
           # print("fired")
            labels = Label(text = "|", x = self.joystick.get_axis('x')*400, y = self.height * -.38)
            array.append(labels)
            self.add_widget(labels)
    def fire2(self,dt):

        global array2
        # print("fired")
        labels2 = Label(text = "!", x = self.ids.bdgy1.x, y = self.height * .35)
        array2.append(labels2)
        self.add_widget(labels2)

    def space_update(self):  # This should be inside the MainScreen Class
        while True:
            self.ship_x_val = self.joystick.get_axis('x') * 400
            self.ids.spaceship.x = self.ship_x_val
            self.moveup()
            self.moveup2()
            #self.ship_y_val = self.joystick.get_axis('y') * -300
            #self.ids.spaceship.y = self.ship_y_val
            sleep(.01)

    def bdgy_move(self):
        while True:
            for r in range(0, 8):
                self.ids.bdgy1.x += 10
                sleep(.03)
            for w in range(0, 16):
                self.ids.bdgy1.x -= 10
                sleep(.02)
            for l in range(0, 8):
                self.ids.bdgy1.x += 10
                sleep(.05)

    def start_space_thread(self):  # This should be inside the MainScreen Class
        Thread(target=self.space_update).start()
        Thread(target=self.bdgy_move).start()






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