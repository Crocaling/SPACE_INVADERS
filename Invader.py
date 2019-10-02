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
END_SCREEN_NAME = 'end'
WIN_SCREEN_NAME = 'win'

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
class OverScreen(Screen):
    def __init__(self, **kwargs):
        super(OverScreen, self).__init__(**kwargs)
    def setColor(self):
        Window.clearcolor = (1, 0, 0, 1)


class WinScreen(Screen):
    def __init__(self, **kwargs):
        super(WinScreen, self).__init__(**kwargs)

    def setColor(self):
            Window.clearcolor = (1, 0, 1, 1)


class MainScreen(Screen):

    joystick = Joystick(0, True)
    ship_x_val = ObjectProperty()
    ship_y_val = ObjectProperty()
    bdgy_pos = ObjectProperty()
    wave_count = ObjectProperty()
    global array3
    global end
    global event1
    global event2
    global array
    global array2
    global lives
    global bad
    global bruh
    global win_count
    end = False
    bruh = 0
    bad = 0
    global array3
    lives = 5
    array = []
    array2 = []

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.wave_count = 5
        global event1
        global event2
        global array3
        global win_count
        global win
        win = True
        win_count = 0
        array3 = [self.ids.bdgy0, self.ids.bdgy2, self.ids.bdgy3, self.ids.bdgy4, self.ids.bdgy5, self.ids.bdgy6,
                  self.ids.bdgy7, self.ids.bdgy8, self.ids.bdgy9, self.ids.bdgy10, self.ids.bdgy11, self.ids.bdgy12,
                  self.ids.bdgy13, self.ids.bdgy14, self.ids.bdgy15, self.ids.bdgy16, self.ids.bdgy17, self.ids.bdgy18,
                  self.ids.bdgy19, self.ids.bdgy20, self.ids.bdgy21, self.ids.bdgy22, self.ids.bdgy23, self.ids.bdgy24,
                  self.ids.bdgy25, self.ids.bdgy26, self.ids.bdgy27]
        event1 = Clock.schedule_interval(self.fire, 1/4)
        event2 = Clock.schedule_interval(self.fire2, 1/(len(array3)/2))
        # I just used clock scheduling to see if it would work but you turn this into a thread instead if you want. if the fire function needs to be canceled, do event1.cancel()
        self.bdgy_pos = .1

    global xin
    xin = 0
    global x
    def close(self):
        global event2
        global event1
        global end
        event1.cancel()
        event2.cancel()
        end = True
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
        global win
        global end
        global event2
        global event1
        global array3
        global array
        global bruh
        global bad
        global win_count
        for labels in array:
            if(labels.y > 300):
                array.remove(labels)
                self.remove_widget(labels)
            for riseups in array3:
                if labels.text == "(^^^^^^)":
                    if abs(labels.y - (riseups.y)) < 50 and abs(labels.x - riseups.x) < 50:
                        self.remove_widget(riseups)
                        array3.remove(riseups)
                        Clock.unschedule(event2)
                        event2 = Clock.schedule_interval(self.fire2, 1 / (len(array3) / 2 + .0001))
                        win_count += 1
                        if win_count == 27 and win == True:
                            Clock.unschedule(event1)
                            Clock.unschedule(event2)
                            end = True
                            SCREEN_MANAGER.current = WIN_SCREEN_NAME
                        bruh = bruh +1
                        if bruh == 3:
                            bruh = 0
                            self.remove_widget(labels)
                            bad = 1

                if (abs(labels.y - (riseups.y)) < 20 and abs(labels.x - riseups.x) < 20):
                    self.remove_widget(riseups)
                    array3.remove(riseups)
                    self.remove_widget(labels)
                    bad = 1
                    win_count += 1
                    Clock.unschedule(event2)
                    event2 = Clock.schedule_interval(self.fire2, 1 / (len(array3) / 2 + .0001))
                    if win_count == 27 and win == True:
                        Clock.unschedule(event1)
                        Clock.unschedule(event2)
                        SCREEN_MANAGER.current = WIN_SCREEN_NAME
                        end = True
            if(bad == 1):
                array.remove(labels)
                bad = 0



            labels.y = labels.y + 10

    def moveup2(self):
        global end
        global event1
        global event2
        global lives
        global array2
        global win
        for labels2 in array2:
            if(labels2.y < -250):
                array2.remove(labels2)
                self.remove_widget(labels2)
            if(abs(labels2.y-(self.ids.spaceship.y))<20 and abs(labels2.x-self.ship_x_val)<20):
                lives = lives - 1
                self.ids.life.text = "Health:%d" % lives
                labels2.text = ">><<"
                labels2.color = (1,0,0,1)
                sleep(1/10)
                self.remove_widget(labels2)
                array2.remove(labels2)
                print("u were hit")
                if(lives <= 0):
                    self.ids.spaceship.y = -1000
                    win = False
                    SCREEN_MANAGER.current = END_SCREEN_NAME
                    end = True
                    Clock.unschedule(event1)
                    Clock.unschedule(event2)
                    print("lmao u ded")
            labels2.y = labels2.y - 7
    def fire(self,dt):
        if(self.joystick.get_button_state(0)==1):
            global array
           # print("fired")
            labels = Label(text = "|", x = self.joystick.get_axis('x')*400, y = self.height * -.38)
            array.append(labels)
            self.add_widget(labels)

        if (self.joystick.get_button_state(1) == 1 and self.wave_count > 0):
            # print("fired")
            labels = Label(text="(^^^^^^)", x=self.joystick.get_axis('x') * 400, y=self.height * -.1)
            array.append(labels)
            self.add_widget(labels)
            self.wave_count -= 1
            self.ids.power.text = "Powerups:%d" % self.wave_count

        if (self.joystick.get_button_state(6) == 1):
            self.ids.spaceship.x -= .05

    def fire2(self,dt):
        global array3
        global array2
        # print("fired")
        #Basic random shooting. In the future, we should automatically create a series of identical "ships" aka labels and put them in the array instead of
        # manually filling in the array like I did here.
        if not array3 == []:
            labels2 = Label(text = "@", x = array3[int(random.random()*(len(array3)-1))].x, y = array3[int(random.random()*(len(array3)-1))].y)
            array2.append(labels2)
            self.add_widget(labels2)

    def space_update(self): # This should be inside the MainScreen Class
        global end
        while end == False:
            self.ship_x_val = self.joystick.get_axis('x') * 400
            self.ids.spaceship.x = self.ship_x_val
            self.moveup()
            self.moveup2()
            #self.ship_y_val = self.joystick.get_axis('y') * -300
            #self.ids.spaceship.y = self.ship_y_val
            sleep(.01)

    def bdgy_move(self):
        anim = Animation(pos=(80, 1000), duration=.3) + Animation(pos=(-80, 1000), duration=.5) + Animation(
            pos=(0, 1000), duration=.35)
        anim.repeat = True
        anim.start(self.ids.bdgy1)

    def start_space_thread(self):  # This should be inside the MainScreen Class
        Thread(target=self.space_update).start()
        Thread(target=self.bdgy_move).start()
        Thread.daemon = True






Builder.load_file('Invader.kv')
SCREEN_MANAGER.add_widget(MainScreen(name=MAIN_SCREEN_NAME))
SCREEN_MANAGER.add_widget(OverScreen(name=END_SCREEN_NAME))
SCREEN_MANAGER.add_widget(WinScreen(name=WIN_SCREEN_NAME))
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