import random
import operator

class Creature:
  def __init__(self,name,vitality,wound):
    while True:
      try:
        self.starting_vit = int(vitality)
        self.starting_wound = int(wound)
        self.vitality = int(vitality)
        self.wound = int(wound)
        self.initiative = 0
        break
      except ValueError:
        print("Bad number, try again\n")
    self.name = name
  
  def attack(self, damage):
    if self.vitality >= damage:
      self.vitality -= damage
      print(self.name + " has his vitals reduced to " + str(self.vitality)+" points\n")
      if self.vitality == 0:
        print(self.name + " is critically wounded!\n")
    else:
      self.vitality = 0
      print(self.name + " has been critically wounded!\n")
      
  def initiative_roll(self,roll = 0):
    if roll == 0:
      self.initiative = random.randint(1,20)
    else:
      self.initiative = roll

def int_checker(starting_statement):
  while True:
    try:
      return_value = int(input(starting_statement))
      break
    except ValueError:
      print("Bad Number, try again")
  return return_value
num_players = 0
players = []
def player_initiate():
    num_players = int_checker("How many players: ")
    
    for player in range(num_players):
      players.append(Creature(input("Player name " + str(player+1) + ": "),int_checker("Vitality: "),int_checker("Wound points: ")))

def dice_roll(die,die_quantity,misc = 0):
    return_val = misc
    for roll in range(0,die_quantity):
        rolled_die = random.randint(1,die)
        return_val += rolled_die
        print("Roll "+str(roll+1)+": "+str(rolled_die))
    print("------------")
    print("Result: "+str(return_val))
    print("\n")
    return return_val
  

def dice_interpreter():
    while True:
        try:
            die_value = input("Enter die value (ex: 4d6+2): ")
            if ("d" in die_value):
                if("+" in die_value):
                    die_type = int(die_value[die_value.find("d")+1:die_value.find("+")])
                    misc_val = int(die_value[die_value.index("+")+1:])
                else:
                    die_type = int(die_value[die_value.find("d")+1:])
                    misc_val = 0
                die_multiple = int(die_value[:die_value.index('d')])
                return dice_roll(die_type,die_multiple,misc_val)
            else:
                return int(die_value)
            break;
        except ValueError:
            print("Bad dice input, try again")
    
        
    


def combat_round():
  combat = True
  while(combat):
    enemies = []
    all_combatants = []
    command = ""
    num_enemies = int_checker("How many enemies: ")
    for name in range(int(num_enemies)):
      enemies.append(Creature(input("Enemy " + str(name+1) + ": "),int_checker("Vitality: "),int_checker("Wound Points: ")))
  
    while True:
      for player in players:
        player.initiative_roll(int_checker(("Initiative Roll for "+player.name+": ")))
      for enemy in enemies:
        enemy.initiative_roll()
      all_combatants = players + enemies
    
      print("Sorted list: \n\n")
      all_combatants.sort(key=operator.attrgetter('initiative'),reverse = True)
      for item in all_combatants:
        print(item.name +" - "+ str(item.initiative))
      break
    round_num = 1
    
    while combat:
      print("\n\nROUND " + str(round_num)+"\n\n")
      for character in all_combatants:
        if combat == False:
          break
        try_again = True
        
        while try_again:
          command = input(character.name + " command: ")
          if command == 'a':
            victim = input("Attack who: ")
            for pot_victim in all_combatants:
              if(victim == pot_victim.name):
                victim = pot_victim
                victim.attack(dice_interpreter())
              
                try_again = False
            
              
          elif command == 's':
            print(character.name + " skipped\n")
            try_again = False
            
          elif command == 'end':
            print("combat ended")
            combat = False
            try_again = False
          else:
            print("command not recognized, try again")
      round_num +=1
  
def heal_players(who_to_heal):
  if who_to_heal == 'all':
    amount_healed = int_checker("How much: ")
    for player in players:
      player.wounds = player.starting_wound
      player.vitality += amount_healed
      if player.vitality > player.starting_vit:
        player.vitality = player.starting_vit
    print("All players healed " + str(amount_healed)+ " hit points, and all wounds restored")
  else:
    for player in players:
      if who_to_heal == player.name:
        amount_healed = int_checker("How much: ")
        player.vitality += amount_healed
        if player.vitality > player.starting_vit:
          player.vitality = player.starting_vit
        print(player.name + " healed for " + str(amount_healed))
        print("Vitality: "+str(player.vitality) + "| Wounds: "+str(player.wound))
  
