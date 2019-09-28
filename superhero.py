import random

class Ability:
    def __init__(self, name, attack_strength):
        '''Create Instance Variables:
          name:String
          max_damage: Integer
        '''
        self.name = name
        self.max_damage = attack_strength

    def attack(self):
      ''' Return a value between 0 and the value set by self.max_damage.'''
      # Return an attack value between 0 and the full attack.
      return random.randint(0,self.max_damage)

class Armor:
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        self.name = name
        self.max_block = max_block

    def block(self):
        ''' Return a random value between 0 and the initialized max_block strength. '''
        return random.randint(0, self.max_block)

class Hero(Ability, Armor):
    def __init__(self, name, starting_health=100):
        '''Instance properties:
          abilities: List
          armors: List
          name: String
          starting_health: Integer
          current_health: Integer
        '''
        self.name = name
        self.max_health = starting_health
        self.current_health = self.max_health
        self.armors = list()
        self.abilities = list()
        self.kills = 0
        self.deaths = 0

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
          return: total:Int
        '''
        damage = 0

        for ability in self.abilities: 
            new_damage = damage + ability.attack()
            damage = new_damage

        return damage

    def add_armor(self, armor):
        '''Add armor to self.armors
            Armor: Armor Object
        '''
        self.armors.append(armor)

    def defend(self):
        '''Runs `block` method on each armor.
            Returns sum of all blocks
        '''
        blocked = 0
        for armor in self.armors:
            new_block = armor.block() + blocked
            blocked = new_block 
        return blocked 

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense. '''
        blocked = self.defend()

        if damage - blocked > 0:
            damage_taken = damage - blocked
        else:
            damage_taken = 0

        self.current_health = self.current_health - damage_taken
         
        return self.current_health

    def is_alive(self):  
        '''Return True or False depending on whether the hero is alive or not.
        '''
        if self.current_health <= 0:
            return False
        else:
            return True

    def add_kill(self):
        ''' Adds 1 to the amount of kills the hero has '''
        self.kills += 1

    def add_death(self):
        ''' adds 1 to the amount of deaths the hero has '''
        self.deaths += 1
        

    def fight(self, opponent):  
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        if self.abilities == [] and opponent.abilities == []:
            print("Draw!") 

        while self.is_alive == True and opponent.is_alive == True:
            self.take_damage(opponent.attack)
            opponent.take_damage(self.attack)
            
        if self.is_alive() == True:
            print(f"{self.name} has Won!")
            self.add_kill()
            opponent.add_death()
        elif opponent.is_alive == True:
            print(f"{opponent.name} has Won!")
            opponent.add_kill()
            self.add_death()
        else:
            print("Both Players have died. It is a draw!")
            self.add_death()
            opponent.add_death()

            
class Weapon(Ability):
    def attack(self):
        '''  This method returns a random value
        between one half to the full attack power of the weapon.
        '''
        return random.randint(self.max_damage//2, self.max_damage)

class Team(Hero, Ability):
    def __init__(self, name):
        ''' Initialize your team with its team name
        '''
        self.name = name
        self.heroes = list()
        
    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        # return self.heroes.remove(name) if name in self.heroes else 0 
        if name in self.heroes:
            return self.heroes.remove(name)
        else:
            return 0
    
    def view_all_heroes(self):
        print('These are your heroes: ')
        for hero in self.heroes:
            print(" --       ", hero.name)
        

    def add_hero(self, hero):
        '''Add Hero object to self.heroes.'''
        # TODO: Add the Hero object that is passed in to the list of heroes in
        # self.heroes
        self.heroes.append(hero)

        



if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    
    ''' This checks if the hero.attack() method works'''
    # ability = Ability("Great Debugging", 50)
    # another_ability = Ability("Smarty Pants", 90)
    # hero = Hero("Grace Hopper", 200)
    # hero.add_ability(ability)
    # hero.add_ability(another_ability)
    # print(hero.attack())
    
    ''' This checks if the hero.current_health is being stored properly '''
    # hero = Hero("Grace Hopper", 200)
    # shield = Armor("Shield", 50)
    # hero.add_armor(shield)
    # hero.take_damage(50)
    # print(hero.current_health)

    ''' this checks if the is_alive function is working'''
    # hero = Hero("Grace Hopper", 200)
    # hero.take_damage(150)
    # print(hero.is_alive())
    # hero.take_damage(15000)
    # print(hero.is_alive())

    ''' This checks the fight method '''
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
    print(f"{hero1.name} has {hero1.kills} kills and {hero1.deaths} deaths")
    print(f"{hero2.name} has {hero2.kills} kills and {hero2.deaths} deaths")
    

    ''' this checks the Weapon polymorphic code '''
    # weapon = Weapon("sword", 4)
    # print(weapon.attack())

    ''' This checks the heroes list. '''
    # redTeam = Team("Red Team")
    # tas = Hero("Tas")
    # redTeam.add_hero(tas)
    # print(redTeam.name)
    # redTeam.view_all_heroes()
    # redTeam.remove_hero(tas)
    # redTeam.view_all_heroes()
    # redTeam.remove_hero("omar")
    # test = redTeam.remove_hero("omar")
    # print(test)
    # print(len(redTeam.heroes))