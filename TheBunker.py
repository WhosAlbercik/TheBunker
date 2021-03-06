import curses
import sys,os
import random
import threading
from tkinter import mainloop

from Player import Player

class Game():
    player = object()

    

    def __init__(self):
        self.loadingComplete = True
        self.loadingThreadClosed = True

        self.statsDrop = False
        self.statsThreadClosed = True

        self.screen = curses.initscr()

        screenSize = self.screen.getmaxyx()
        self.screenSize = screenSize
        screenSize = list(screenSize)

        middle = []
        middle.append(screenSize[0] / 2)
        middle.append(screenSize[1] / 2)

        middle[0] = int(middle[0])
        middle[1] = int(middle[1])
        self.middle = tuple(middle)

        topLeft = [0, 0]
        self.topLeft = tuple(topLeft)

        topRight = [0, screenSize[1]]
        self.topRight = tuple(topRight)

        bottomLeft = [screenSize[0], 0]
        self.bottomLeft = tuple(bottomLeft)

        bottomRight = [screenSize[0], screenSize[1]]
        self.bottomRight = tuple(bottomRight)

        curses.start_color()
        curses.noecho()

        self.MainMenu()
    
    def StatsDrop(self):
        self.statsDrop = True

        self.StatsDraw()
        while self.statsDrop == True:
            curses.napms(random.randint(24000, 72000))
            self.player.thirst -= 1
            self.StatsDraw()
            curses.napms(random.randint(33000, 84000))
            self.player.hunger -= 1
            self.StatsDraw()

            if self.player.thirst == 0 or self.player.hunger == 0:
                foodDeath = threading.Thread(target=self.foodDeath)
                foodDeath.start()
                break

        self.statsDrop = False
        self.statsThreadClosed == True



    def MainLoop(self):
        while True:
            curses.napms(2000)
            if self.player.health <= 0:
                self.GameOver()
            if self.player.hunger <= 0 or self.player.thirst <= 0:
                foodDeath = threading.Thread(target=self.foodDeath)
                foodDeath.start()

    def foodDeath(self):
        while self.player.hunger <= 0 or self.player.thirst <= 0:
            self.player.health -= 4
            self.StatsDraw()
            curses.napms(4000)
            if self.player.health == 0:
                self.GameOver()
                break
                

        
    def StatsDraw(self):
        self.statsWindow = curses.newwin(int(self.screenSize[0] - (self.screenSize[0] / 3 * 2)), self.screenSize[1] - 2, int(self.screenSize[0] / 3 * 2), 1)
        self.statsWindowSize = (int(self.screenSize[0] - (self.screenSize[0] / 3 * 2)), self.screenSize[1] - 2)

        self.statsWindow.border()

        self.statsWindow.addstr(int(self.statsWindowSize[0] / 2), int(self.statsWindowSize[1] / 2 - 15), f"Hunger {self.player.hunger}  Thirst {self.player.thirst}  Health {self.player.health}")
        self.statsWindow.refresh()




    def NewGame(self):
        screen = self.screen
        self.loadingComplete = False
  
        loading = threading.Thread(target=self.LoadingScreen)
        loading.name = "Loading Screen"                                     
        loading.start()

        self.player = Player()
        player = self.player
        self.loadingComplete = True
        
        while self.loadingThreadClosed == False:
            pass

        self.Print([{'text':f"{player.name} {player.surname}", 'cords': (self.topLeft[0] + 2, self.topLeft[1] + 7)}])
        curses.napms(2000)
        
        screen.addstr(self.topLeft[0] + 2, self.topLeft[1], "name = ")
        screen.addstr(self.bottomRight[0] - 1, self.bottomRight[1] - 2, ".")
        screen.refresh()


        statsDrop = threading.Thread(target=self.StatsDrop)
        statsDrop.start()

        # NOTE THE STATSDROP THREAD IS CURRENTLY DISABLED DUE TO A SERIOUS OPTIMILAZTION ISSUE (WILL BE ENABLED IN FUTURE)

        return
        
    def Print(self, strings):
        screen = self.screen
        # [{'text':"hello", 'cords':(126, 75)}]
        
        
        for x in strings:
            text = "" 
            for letter in x['text']:
                text += letter
                screen.addstr(x['cords'][0], x['cords'][1], text)
                screen.refresh()
                curses.napms(100)
            

    def LoadingScreen(self):
        screen = self.screen
        screen.erase()

        while True:
            self.loadingThreadClosed = False
            screen.addstr(self.middle[0], self.middle[1] - 5, "Loading..")
            screen.refresh()
            curses.napms(500)
            screen.erase()

            screen.addstr(self.middle[0], self.middle[1] - 5, "Loading.")
            screen.refresh()
            curses.napms(500)
            screen.erase()

            screen.addstr(self.middle[0], self.middle[1] - 5, "Loading")
            screen.refresh()
            curses.napms(500)
            screen.erase()
            if self.loadingComplete:
                screen.erase()
                self.loadingThreadClosed = True
                break

    

    def MainMenu(self):
        screen = self.screen
        
        screen.erase()

        screen.addstr(self.middle[0] - 2, self.middle[1] - 4, "TheBunker")
        screen.addstr(self.middle[0], self.middle[1] -  9, "PRESS ENTER TO START", curses.A_BLINK)
        screen.addstr(self.bottomRight[0]- 10, self.bottomRight[1] - 10, str(self.screenSize))
        screen.refresh()

        while True:
            key = screen.getch()
            if key == 10: # Enter key
                screen.erase()
                break
        if self.screenSize[0] >= 24 and self.screenSize[1] >= 70:
            screen.addstr(self.topLeft[0], self.topLeft[1], """                                                                                                                                                                        
                                                                                                                                                                          
         tttt         hhhhhhh                               BBBBBBBBBBBBBBBBB                                     kkkkkkkk                                                
      ttt:::t         h:::::h                               B::::::::::::::::B                                    k::::::k                                                
      t:::::t         h:::::h                               B::::::BBBBBB:::::B                                   k::::::k                                                
      t:::::t         h:::::h                               BB:::::B     B:::::B                                  k::::::k                                                
ttttttt:::::ttttttt    h::::h hhhhh           eeeeeeeeeeee    B::::B     B:::::Buuuuuu    uuuuuunnnn  nnnnnnnn     k:::::k    kkkkkkk eeeeeeeeeeee    rrrrr   rrrrrrrrr   
t:::::::::::::::::t    h::::hh:::::hhh      ee::::::::::::ee  B::::B     B:::::Bu::::u    u::::un:::nn::::::::nn   k:::::k   k:::::kee::::::::::::ee  r::::rrr:::::::::r  
t:::::::::::::::::t    h::::::::::::::hh   e::::::eeeee:::::eeB::::BBBBBB:::::B u::::u    u::::un::::::::::::::nn  k:::::k  k:::::ke::::::eeeee:::::eer:::::::::::::::::r 
tttttt:::::::tttttt    h:::::::hhh::::::h e::::::e     e:::::eB:::::::::::::BB  u::::u    u::::unn:::::::::::::::n k:::::k k:::::ke::::::e     e:::::err::::::rrrrr::::::r
      t:::::t          h::::::h   h::::::he:::::::eeeee::::::eB::::BBBBBB:::::B u::::u    u::::u  n:::::nnnn:::::n k::::::k:::::k e:::::::eeeee::::::e r:::::r     r:::::r
      t:::::t          h:::::h     h:::::he:::::::::::::::::e B::::B     B:::::Bu::::u    u::::u  n::::n    n::::n k:::::::::::k  e:::::::::::::::::e  r:::::r     rrrrrrr
      t:::::t          h:::::h     h:::::he::::::eeeeeeeeeee  B::::B     B:::::Bu::::u    u::::u  n::::n    n::::n k:::::::::::k  e::::::eeeeeeeeeee   r:::::r            
      t:::::t    tttttth:::::h     h:::::he:::::::e           B::::B     B:::::Bu:::::uuuu:::::u  n::::n    n::::n k::::::k:::::k e:::::::e            r:::::r            
      t::::::tttt:::::th:::::h     h:::::he::::::::e        BB:::::BBBBBB::::::Bu:::::::::::::::uun::::n    n::::nk::::::k k:::::ke::::::::e           r:::::r            
      tt::::::::::::::th:::::h     h:::::h e::::::::eeeeeeeeB:::::::::::::::::B  u:::::::::::::::un::::n    n::::nk::::::k  k:::::ke::::::::eeeeeeee   r:::::r            
        tt:::::::::::tth:::::h     h:::::h  ee:::::::::::::eB::::::::::::::::B    uu::::::::uu:::un::::n    n::::nk::::::k   k:::::kee:::::::::::::e   r:::::r            
          ttttttttttt  hhhhhhh     hhhhhhh    eeeeeeeeeeeeeeBBBBBBBBBBBBBBBBB       uuuuuuuu  uuuunnnnnn    nnnnnnkkkkkkkk    kkkkkkk eeeeeeeeeeeeee   rrrrrrr     """)
            screen.addstr(self.topLeft[0] + 24, self.topLeft[1], "1) New Game" )
            screen.addstr(self.topLeft[0] + 25, self.topLeft[1], "2) Quit")

        else: # Smaller Terminals
            screen.addstr(self.topLeft[0], self.topLeft[1], "theBunker")
            screen.addstr(self.topLeft[0] + 2, self.topLeft[1], "1) New Game" )
            screen.addstr(self.topLeft[0] + 3, self.topLeft[1], "2) Quit")

        
        screen.refresh()

        while True:
            key = screen.getch()
            if key == 49: # 1 key
                self.NewGame()
                break
            elif key == 50: # 2 key
                break

    def GameOver(self):
        self.screen.erase()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        self.Print([{'text':"{GAME OVER}", 'cords': (self.middle[0], self.middle[1] )}])
        self.screen.addstr(self.middle[0], self.middle[1], "{GAME OVER}", curses.color_pair(1))
        self.screen.refresh()

        curses.napms(10000)

    



Game()

