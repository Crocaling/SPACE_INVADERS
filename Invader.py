import os

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.label import Label
from kivy.uix.image import Image

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
BOSS_SCREEN_NAME = 'boss'
START_SCREEN_NAME = 'start'
CREDIT_SCREEN_NAME = 'credit'
OPTION_SCREEN_NAME = 'option'
HOW_SCREEN_NAME = 'how'
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
        Window.clearcolor = (0, 0, 0, 1)

    def go_back(self):
        SCREEN_MANAGER.current = START_SCREEN_NAME


class WinScreen(Screen):
    def __init__(self, **kwargs):
        super(WinScreen, self).__init__(**kwargs)

    def setColor(self):
            Window.clearcolor = (1, 0, 0, 1)


class StartScreen(Screen):
    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)

    def setColor(self):
            Window.clearcolor = (0, 0, 0, 1)

    def startGame(self):
        SCREEN_MANAGER.current = MAIN_SCREEN_NAME

    def credit(self):
        SCREEN_MANAGER.current = CREDIT_SCREEN_NAME

    def option(self):
        SCREEN_MANAGER.current = OPTION_SCREEN_NAME

    def how(self):
        SCREEN_MANAGER.current = HOW_SCREEN_NAME


class CreditScreen(Screen):
    def __init__(self, **kwargs):
        super(CreditScreen, self).__init__(**kwargs)

    def setColor(self):
            Window.clearcolor = (0, 0, 0, 1)

    def go_back(self):
        SCREEN_MANAGER.current = START_SCREEN_NAME


class HowScreen(Screen):
    def __init__(self, **kwargs):
        super(HowScreen, self).__init__(**kwargs)

    def setColor(self):
            Window.clearcolor = (0, 0, 0, 1)

    def go_back(self):
        SCREEN_MANAGER.current = START_SCREEN_NAME


class OptionScreen(Screen):
    def __init__(self, **kwargs):
        super(OptionScreen, self).__init__(**kwargs)

    def setColor(self):
            Window.clearcolor = (0, 0, 0, 1)

    def go_back(self):
        SCREEN_MANAGER.current = START_SCREEN_NAME


class MainScreen(Screen):

    joystick = Joystick(0, True)
    ship_x_val = ObjectProperty()
    ship_y_val = ObjectProperty()
    bdgy_pos = ObjectProperty()
   # wave_count = ObjectProperty()
    global wave_count
    global end
    global counte
    counte = 1
    global idslist
    idslist = []
    global event1
    global event2
    global array
    global array2
    global apples2
    global lives
    global bad
    global bruh
    global win_count
    global array3
    global array5
    array3 = []
    array5 = []

    end = False
    bruh = 0
    bad = 0
    array = []
    array2 = []
    def clockStart(self):
        global event1
        global event2
        event1 = Clock.schedule_interval(self.fire, 1 / 4)
        event2 = Clock.schedule_interval(self.fire2, 1 / (len(array3)-1 / 2))

    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)

        # I just used clock scheduling to see if it would work but you turn this into a thread instead if you want. if the fire function needs to be canceled, do event1.cancel()


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
        global idslist
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
                        event2 = Clock.schedule_interval(self.fire2, 1 / (len(array3)-1 / 2 + .000000001))
                        win_count += 1
                        if win_count == 27 and win == True:
                            Clock.unschedule(event1)
                            Clock.unschedule(event2)
                            end = True
                            SCREEN_MANAGER.current = BOSS_SCREEN_NAME
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
                    event2 = Clock.schedule_interval(self.fire2, 1 / (len(array3)-1 / 2 + .000000001))
                    if win_count == 27 and win == True:
                        event1.cancel()
                        event2.cancel()
                        SCREEN_MANAGER.current = BOSS_SCREEN_NAME
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
        global array
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
                    for applest in array2:
                        self.remove_widget(applest)
                    array2 = []
                    for apples2t in array:
                        self.remove_widget(apples2t)
                    array = []
                    SCREEN_MANAGER.current = END_SCREEN_NAME
                    end = True
                    Clock.unschedule(event1)
                    Clock.unschedule(event2)
                    print("lmao u ded")
            labels2.y = labels2.y - 7
    def fire(self,dt):
        global wave_count
        if(self.joystick.get_button_state(0)==1):
            global array
            #print("fired")
            labels = Label(text ="|", x = self.joystick.get_axis('x')*400, y = self.height * -.38)
            array.append(labels)
            self.add_widget(labels)

        if (self.joystick.get_button_state(1) == 1 and wave_count > 0):
            # print("fired")
            labels = Label(text="(^^^^^^)", x=self.joystick.get_axis('x') * 400, y=self.height * -.1)
            array.append(labels)
            self.add_widget(labels)
            wave_count -= 1
            self.ids.power.text = "Powerups:%d" % wave_count

        if (self.joystick.get_button_state(6) == 1):
            self.ids.spaceship.x -= .05

    def fire2(self,dt):
        global array3
        global array2
        #print("fired")
        #Basic random shooting. In the future, we should automatically create a series of identical "ships" aka labels and put them in the array instead of
        # manually filling in the array like I did here.
        if SCREEN_MANAGER.current == MAIN_SCREEN_NAME:
            if not array3 == []:
                labels2 = Label(text = '@', x = array3[int(random.random()*(len(array3)-1))].x, y = array3[int(random.random()*(len(array3)-1))].y)
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
        global counte
        if counte == 1:
            anim = Animation(pos=(80, 1000), duration=.3) + Animation(pos=(-80, 1000), duration=.5) + Animation(
                pos=(0, 1000), duration=.35)
            anim.repeat = True
            anim.start(self.ids.bdgy1)

    def start_space_thread(self):  # This should be inside the MainScreen Class
        global win_count
        global apples2
        global win
        global end
        global lives
        global array3
        global counte
        global wave_count
        wave_count = 5
        global idslist
        idslist = (self.ids.bdgy0, self.ids.bdgy2, self.ids.bdgy3, self.ids.bdgy4, self.ids.bdgy5, self.ids.bdgy6,
                   self.ids.bdgy7, self.ids.bdgy8, self.ids.bdgy9, self.ids.bdgy10, self.ids.bdgy11, self.ids.bdgy12,
                   self.ids.bdgy13,
                   self.ids.bdgy14, self.ids.bdgy15, self.ids.bdgy16, self.ids.bdgy17, self.ids.bdgy18, self.ids.bdgy19,
                   self.ids.bdgy20, self.ids.bdgy21, self.ids.bdgy22,
                   self.ids.bdgy23, self.ids.bdgy24, self.ids.bdgy25, self.ids.bdgy26, self.ids.bdgy27)
        global array3
        global win_count
        global win
        win = True
        win_count = 0
        end = False
        lives = 5
        wave_count = 5
        win = True
        win_count = 0
        apples2 = len(array3) - 1
        if(counte == 0):
            for appe in array3:
                self.remove_widget(appe)
            for aplt in idslist:
                self.add_widget(aplt)
        array3 = list(idslist)
       # print("%d + %d" % (len(array3), len(idslist)))
        self.ids.life.text = "Health:%d" % lives
        self.ids.power.text = "Power:%d" % wave_count
        self.ids.spaceship.y = - self.height*.38
        self.bdgy_pos = .1
        Thread(target=self.space_update).start()
        Thread(target=self.bdgy_move).start()
        self.clockStart()
        counte = 0
        Thread.daemon = True
class BossScreen(MainScreen):
    joystick = Joystick(0, True)
    ship_x_val = ObjectProperty()
    ship_y_val = ObjectProperty()
    wave_count = ObjectProperty()
    global end
    global event1
    global event2
    global array
    global array2
    global lives
    global bad
    global bruh
    global win_count
    global count
    global count2
    end = False
    array = []
    array2 = []
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        print("hi")
        #event1 = Clock.schedule_interval(self.fire, 1 / 4)
        # I just used clock scheduling to see if it would work but you turn this into a thread instead if you want. if the fire function needs to be canceled, do event1.cancel()

    def start_space_thread(self):
        Window.clearcolor = (0, 0, 0, 1)
        Thread(target=self.space_update).start()
        Thread(target=self.boss_move).start()
        self.clockStart()
        idslist = (self.ids.bdgy0, self.ids.bdgy2, self.ids.bdgy3, self.ids.bdgy4, self.ids.bdgy5, self.ids.bdgy6,
                   self.ids.bdgy7, self.ids.bdgy8, self.ids.bdgy9, self.ids.bdgy10, self.ids.bdgy11,
                   self.ids.bdgy12,
                   self.ids.bdgy13,
                   self.ids.bdgy14, self.ids.bdgy15, self.ids.bdgy16, self.ids.bdgy17, self.ids.bdgy18,
                   self.ids.bdgy19,
                   self.ids.bdgy20, self.ids.bdgy21, self.ids.bdgy22,
                   self.ids.bdgy23, self.ids.bdgy24, self.ids.bdgy25, self.ids.bdgy26, self.ids.bdgy27)
        for bruhs in idslist:
            print("this runs")
            self.remove_widget(bruhs)
        global end
        end = False
        Thread.daemon = True
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
        global idslist
        for labels in array:
            if(labels.y > 300):
                array.remove(labels)
                self.remove_widget(labels)
            labels.y = labels.y + 10

    def fire2(self, dt):
        dsafsd = 1
        print("hi")
    def boss_move(self):
        global count
        global count2
        self.count = 0
        self.count2 = 0
        while True:
            movement = random.randrange(0, 5, 1)
            print(movement)
            if movement == 1:
                print("movement1")
                anim1 = Animation(pos=(-300, 200), size=(50, 50), duration=1)
                anim1.start(self.ids.bossship)
                sleep(1)
                if self.count < 6:
                    print("1-Firing " + str(self.count))
                    labels2 = Label(text="YY", x=self.ids.bossship.x, y=self.ids.bossship.y)
                    array2.append(labels2)
                    self.add_widget(labels2)
                    self.ids.bossship.x += 50
                    sleep(1)
                    self.count += 1

            if movement == 2:
                print("movement2")
                anim2 = Animation(pos=(-300, 200), duration=1)
                anim2.start(self.ids.bossship)
                sleep(1)
                if self.count < 6:
                    print("2-Firing " + str(self.count))
                    anim2 = Animation(pos=(random.randrange(-300, 300, 10), 150), size=(100, 100), duration=5) + Animation(pos=(random.randrange(-300, 300, 10), 150), size=(5, 5), duration=5)
                    anim2.start(self.ids.bossship)
                    labels2 = Label(text="YY", x=self.ids.bossship.x, y=self.ids.bossship.y)
                    array2.append(labels2)
                    self.add_widget(labels2)
                    sleep(1)
                    self.count += 1
            if movement == 3:
                print("movement3")
                if self.count < 6:
                    anim3 = Animation(pos=(random.randrange(-300, 300, 10), self.height * -.1), duration=2)
                    anim3.start(self.ids.bossship)
                    print("3-firing")
                    sleep(1)
                    labels2 = Label(text="(######)", x=self.ids.bossship.x, y=self.ids.bossship.y)
                    array2.append(labels2)
                    self.add_widget(labels2)
                    print("3-fired" + str(self.count))
                    sleep(1)
                    self.count += 1
            if movement == 4:
                print("movement4")
                if self.count < 6:
                    anim4 = Animation(pos=(self.ids.spaceship.x, self.ids.bossship.y), size=(75, 75), duration=2)
                    anim4.start(self.ids.bossship)
                    sleep(1)
                    if self.count2 < 6:
                        print("4-Blast it " + str(self.count2))
                        labels2 = Label(text="YYYY", x=self.ids.bossship.x, y=self.ids.bossship.y)
                        array2.append(labels2)
                        self.add_widget(labels2)
                        sleep(1)
                        self.count2 += 1
                    self.count2 = 0
                    self.count += 1
                self.count = 0
            if movement == 5:
                print("movement5")
                if self.count < 6:
                    anim5 = Animation(pos=(random.randrange(-300, 300, 10), self.ids.bossship.y), size=(1, 1), duration=2)
                    anim5.start(self.ids.bossship)
                    sleep(1)
                    if self.count2 < 6:
                        print("5-Firing " + str(self.count2))
                        labels2 = Label(text="(######)", x=self.ids.bossship.x, y=self.ids.bossship.y)
                        array2.append(labels2)
                        self.add_widget(labels2)
                        sleep(1)
                        self.count2 += 1
                    self.count2 = 0
                    self.count += 1
                self.count = 0
            anim6 = Animation(pos=(random.randrange(-300, 300, 10), self.ids.bossship.y), size=(75, 75), duration=2)
            anim6.start(self.ids.bossship)


    def space_update(self): # This should be inside the MainScreen Class
        global end
        global wave_count
        while end == False:
            self.ship_x_val = self.joystick.get_axis('x') * 400
            self.ids.spaceship.x = self.ship_x_val
            self.moveup()
            self.moveup2()
            self.ids.life.text = "Health:%d" % lives
            self.ids.power.text = "Power:%d" % wave_count
            #self.ship_y_val = self.joystick.get_axis('y') * -300
            self.ids.spaceship.y = self.height * -.38
            sleep(.01)






Builder.load_file('Invader.kv')
SCREEN_MANAGER.add_widget(StartScreen(name=START_SCREEN_NAME))
SCREEN_MANAGER.add_widget(MainScreen(name=MAIN_SCREEN_NAME))
SCREEN_MANAGER.add_widget(OverScreen(name=END_SCREEN_NAME))
SCREEN_MANAGER.add_widget(WinScreen(name=WIN_SCREEN_NAME))
SCREEN_MANAGER.add_widget(BossScreen(name=BOSS_SCREEN_NAME))
SCREEN_MANAGER.add_widget(CreditScreen(name=CREDIT_SCREEN_NAME))
SCREEN_MANAGER.add_widget(OptionScreen(name=OPTION_SCREEN_NAME))
SCREEN_MANAGER.add_widget(HowScreen(name=HOW_SCREEN_NAME))

def send_event(event_name):
    global MIXPANEL

    MIXPANEL.set_event_name(event_name)
    MIXPANEL.send_event()


if __name__ == "__main__":
    # send_event("Project Initialized")
    # Window.fullscreen = 'auto'
    ProjectNameGUI().run()