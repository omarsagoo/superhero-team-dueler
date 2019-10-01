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

class Hero:
    def __init__(self, name, starting_health=100):
        '''Instance properties:
          abilities: List
          armors: List
          name: String
          starting_health: Integer
          current_health: Integer
        '''
        self.name = name
        self.starting_health = starting_health
        self.max_health = starting_health
        self.current_health = starting_health
        self.armors = list()
        self.abilities = list()
        self.kills = 0
        self.deaths = 0

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        self.abilities.append(weapon)
        

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
        self_is_alive = True
        opp_is_alive = True
        draw = False

        ''' while loop to run the fight, commented prints are for error handling '''
        while self_is_alive == True and opp_is_alive == True:
            # print("Start!")
            self_is_alive = self.is_alive()
            # print(f"6 {self_is_alive}")
            opp_is_alive = opponent.is_alive()
            # print(f"5 {opp_is_alive}")

            if self.abilities == [] and opponent.abilities == []:
                print("Draw!")
                return  draw == True
            
            val2 = self.take_damage(opponent.attack())
            self_is_alive = self.is_alive()
            # print(f"4 {self_is_alive}")
            # print(f"3 {val2}")
            if self_is_alive == False:
                return self_is_alive
            else: 
                self_is_alive = True
                return self_is_alive

           
            val1 = opponent.take_damage(self.attack())
            opp_is_alive = opponent.is_alive()

            if opp_is_alive == False:
                return opp_is_alive
            else:
                opp_is_alive = True
                return opp_is_alive

            # print(f"2 {opp_is_alive}")
            # print(f"1 {val1}")
            
            
        if self_is_alive == True and opp_is_alive == False:
            print(f"{self.name} has Won!")
            self.add_kill()
            opponent.add_death()
        elif opp_is_alive == True and self_is_alive == False:
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
        
        self.heroes.append(hero)

    def team_kills(self):
        total_kills = 0

        for hero in self.heroes:
            kill = hero.kills + total_kills
            total_kills = kill

        return total_kills

    def attack(self, other_team):
        ''' Battle each team against each other.'''
        heroes_fought = list()
        while len(heroes_fought) != len(self.heroes) + len(other_team.heroes):
            
            for hero1, hero2 in zip(self.heroes, other_team.heroes):
                hero1.fight(hero2)
                heroes_fought.append(hero1)
                heroes_fought.append(hero2)
    
    def team_won(self, other_team):
        if self.team_kills() > other_team.team_kills():
            print(f"{self.name} has won!")
        elif self.team_kills() < other_team.team_kills():
            print(f"{other_team.name} has won!")
        else:
            print("draw!!")

    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        for hero in self.heroes:
            hero.current_health = health
    

    def stats(self):
        '''Print team statistics'''
        print("Stats: ")
        for hero in self.heroes:
            print(f'''    {hero.name}: 
            kills: {hero.kills}
            deaths: {hero.deaths}
            k/d: {hero.kills}/{hero.deaths}
            ''')

class Arena:
    def __init__(self):
        '''Instantiate properties
        team_one: None
        team_two: None
        '''
        self.team_one = []
        self.team_two = []

    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''
        ability = Ability(input_handler("What is the name of the ability? "), int(input_handler("Give a strength value: ")))
        return ability

    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        weapon = Weapon(input_handler("What is the name of the Weapon? "), int(input_handler("Give a strength value: ")))
        return weapon

    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        armor = Armor(input_handler("What is the name of the armor? "), int(input_handler("Give a strength value: ")))
        return armor
        
    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        hero = Hero(input_handler("What is the name of your hero? "))

        number = int(input_handler("how many abilities do you want?"))
        for _ in range(number):
            ability = self.create_ability()
            hero.add_ability(ability)

        number = int(input_handler("how many pieces of armor do you want?"))
        for _ in range(number):
            armor = self.create_armor()
            hero.add_armor(armor)

        number = int(input_handler("how many weapons do you want?"))
        for _ in range(number):
            weapon = self.create_weapon()
            hero.add_ability(weapon)

        return hero

    def add_hero_team(self, team):
        # create_hero()
        team.add_hero(self.create_hero())

        yes_no = input_handler("Do you want to add more heroes? ")
        if yes_no.lower() == "yes":
            return self.add_hero_team(team)

    def build_team_one(self):
        '''Prompt the user to build team_one '''
        print("lets build the team now! ")
        self.team_one = Team(input_handler("What is your team name? "))
        self.add_hero_team(self.team_one)

        return self.team_one

    def build_team_two(self):
        '''Prompt the user to build team_two '''
        print("lets build the team now! ")
        self.team_two = Team(input_handler("What is your team name? "))
        self.add_hero_team(self.team_two)

        return self.team_two

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        
        self.team_one = self.build_team_one()
        self.team_two = self.build_team_two()

        return self.team_one.attack(self.team_two)
    
    def show_stats(self):
        '''Prints team statistics to terminal.'''
        self.team_one.team_won(self.team_two)
        print(self.team_one.stats())
        print(self.team_two.stats())
            
  
def input_handler(prompt):
    user_input = input(prompt)

    if user_input == '':
        print('you must provide some information!')
        return input_handler(prompt)
    elif "Give a" in prompt and has_nums_and_letters(user_input) == True:
        print('You must input a number!')
        return input_handler(prompt)
    elif "how many" in prompt and has_nums_and_letters(user_input) == True:
        print('You must input a number! ')
        return input_handler(prompt)
    else:
        return user_input

def has_nums_and_letters(input_val):
    if any(num.isdigit() for num in input_val) and any(letter.isalpha() for letter in input_val):
        return True
    elif any(letter.isalpha() for letter in input_val):
        return True
    else:
        return False


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    # Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
    
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
    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")
    # ability1 = Ability("Super Speed", 3523514353)
    # ability2 = Ability("Super Eyes", 101243215)
    # ability3 = Ability("Wizard Wand", 80000352350)
    # ability4 = Ability("Wizard Beard", 20005123500)
    # hero1.add_ability(ability1)
    # hero1.add_ability(ability2)
    # hero2.add_ability(ability3)
    # hero2.add_ability(ability4)
    # hero1.fight(hero2)
    # print(f"{hero1.name} has {hero1.kills} kills and {hero1.deaths} deaths")

    

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

    ''' this checks the stats of the teams as well as the team fighting'''
    # redTeam = Team("Red Team")
    # blueTeam = Team("blue Team")
    # tas = Hero("Tas")
    # luke = Hero("Luke")
    # omar = Hero("Omar")
    # anthony = Hero("Anthony")
    # ability1 = Ability("Super Speed", 300)
    # ability2 = Ability("Super Eyes", 130)
    # ability3 = Ability("Wizard Wand", 80)
    # ability4 = Ability("Wizard Beard", 20)
    # tas.add_ability(ability1)
    # tas.add_ability(ability2)
    # luke.add_ability(ability3)
    # luke.add_ability(ability4)
    # omar.add_ability(ability1)
    # omar.add_ability(ability2)
    # anthony.add_ability(ability3)
    # anthony.add_ability(ability4)
    # redTeam.add_hero(tas)
    # redTeam.add_hero(luke)
    # blueTeam.add_hero(omar)
    # blueTeam.add_hero(anthony)
    # # print(redTeam.name)
    # redTeam.view_all_heroes()
    # redTeam.attack(blueTeam)
    # redTeam.stats()
    # blueTeam.stats()
    # print(redTeam.team_kills())
    # redTeam.team_won(blueTeam)
    # print(omar.current_health)

    # hero = Hero("omar", 100)
    # hero.take_damage(40)
    # print(hero.current_health)

    ''' checks the arena class '''
    # arena = Arena()
    # arena.build_team_one()
    # print(arena.team_one.view_all_heroes())
    # arena.build_team_two()
    # print(arena.team_two.view_all_heroes())
    # arena.team_battle()
    # arena.show_stats()