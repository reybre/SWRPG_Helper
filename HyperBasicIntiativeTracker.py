from tkinter import *
from tkinter import ttk

player_list = []
baddie_list = []


class Player:
    def __init__(self):
        self.place_in_line = len(player_list) + 1

        self.ded = False
        self.initiative = IntVar()
        self.nameEntry = Entry(playerTab)
        self.killButton = Button(playerTab, text="Kill Player :(", command=self.killplayer)
        self.battleLabel = Label(battleTab,text = self.nameEntry.get())
        self.initiativeLabel = Label(battleTab,text=self.nameEntry.get())
        self.initiativeEntry = Entry(battleTab)
    def killplayer(self):
        self.nameEntry.destroy()
        self.killButton.destroy()
        self.battleLabel.destroy()
        self.ded = True
        setup_buttons()
    def button_build(self):
        if not self.ded:
            self.nameEntry.grid(row=self.place_in_line, column=0)
            self.killButton.grid(row=self.place_in_line, column=1)
    def battle_build(self,row_to_place):
        if not self.ded:
            self.battleLabel.config(text=self.nameEntry.get())
            self.battleLabel.grid(row=row_to_place,column=1)
    def initiative_build(self,row_to_place):
        if not self.ded:
            self.initiativeLabel.config(text=self.nameEntry.get())
            self.initiativeLabel.grid(row=row_to_place, column=1)
            self.initiativeEntry.grid(row=row_to_place, column=2)

class BadBoy:
    def __init__(self):
        self.place_in_line = len(baddie_list) + 2

        self.ded = False
        self.initiative = IntVar()
        self.hitpoints = IntVar()
        
        self.nameEntry = Entry(enemyTab)
        self.hitpointsEntry = Entry(enemyTab, textvariable=self.hitpoints)
        self.initiativeEntry = Entry(enemyTab, textvariable=self.initiative)
        self.killButton = Button(enemyTab, text="Kill baddie", command=self.killplayer)
        self.battleLabel = Label(battleTab,text = self.nameEntry.get())
        
    def killplayer(self):
        self.nameEntry.destroy()
        self.killButton.destroy()
        self.hitpointsEntry.destroy()
        self.battleLabel.destroy()
        self.ded = True
        setup_buttons()
    def button_build(self):
        if not self.ded:
            self.nameEntry.grid(row=self.place_in_line, column=0)
            self.hitpointsEntry.grid(row=self.place_in_line, column=1)
            self.initiativeEntry.grid(row=self.place_in_line, column=2)
            self.killButton.grid(row=self.place_in_line, column=3)
    def battle_build(self,row_to_place):
        if not self.ded:
            self.battleLabel.config(text=self.nameEntry.get())
            self.battleLabel.grid(row=row_to_place,column=4)
def setup_buttons():
    for creature in (player_list + baddie_list):
        creature.button_build()


def add_player():
    player_list.append(Player())
    #print(str(len(player_list) + 1))
    setup_buttons()


def add_baddie():
    baddie_list.append(BadBoy())
    setup_buttons()


def initiative_grab():
    playerIntiativeLabel = Label(battleTab, text="Enter player Intiatives to the \nright of each player name")
    playerIntiativeLabel.grid(row=1, column=0)

    playerrowcount = 2
    baddierowcount = 2

    for creature in (player_list):
        creature.battle_build(playerrowcount)

        playerrowcount += 1
    for creature in baddie_list:
        creature.battle_build(baddierowcount)
        baddierowcount+=1


root = Tk()
note = ttk.Notebook(root)

battleTab = Frame(note)
playerTab = Frame(note)
enemyTab = Frame(note)

note.add(battleTab, text="Battle!", compound=TOP)
note.add(playerTab, text="Players")
note.add(enemyTab, text="Enemies")

# Add Players Button

playerAddButton = Button(playerTab, text="Add Player", command=add_player)
playerAddButton.grid(row=0, column=0)
baddieAddButton = Button(enemyTab, text="Add Enemy", command=add_baddie)
baddieAddButton.grid(row=0, column=0)
initiativeButton = Button(battleTab, text="start", command=initiative_grab)
initiativeButton.grid(row=0, column=0)
baddieNameLabel = Label(enemyTab, text="Baddie Name")
baddieNameLabel.grid(row=1, column=0)
baddieHitpointLabel = Label(enemyTab,text="Hit Points")
baddieHitpointLabel.grid(row=1,column=1)
baddieInitiativeLabel = Label(enemyTab,text="Initiative Mod (0 by def.)")
baddieInitiativeLabel.grid(row=1,column=2)
note.pack()
root.mainloop()
exit()

