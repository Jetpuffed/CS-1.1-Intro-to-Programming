import random


class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        random_value = random.randint(0, self.max_damage)
        return random_value


class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        random_value = random.randint(0, self.max_block)
        return random_value


class Weapon(Ability):
    def attack(self):
        random_value = random.randint(self.max_damage//2, self.max_damage)
        return random_value


class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def take_damage(self, damage):
        defense = self.defend()
        self.current_health -= damage - defense

    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True

    def fight(self, opponent):
        if not (self.abilities or opponent.abilities):
            return "Draw"
        else:
            while self.is_alive() and opponent.is_alive():
                opponent.take_damage(self.attack())
                self.take_damage(opponent.attack())

                if self.is_alive() is False:
                    print(f"{opponent.name} has won!")
                    self.add_death(1)
                    opponent.add_kill(1)
                if opponent.is_alive() is False:
                    print(f"{self.name} has won!")
                    opponent.add_death(1)
                    self.add_kill(1)

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self, num_deaths):
        self.deaths += num_deaths


class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):
        foundHero = False

        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        if not foundHero:
            return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print('{}'.format(hero.name))

    def stats(self):
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print('{} Kills/Deaths:{}'.format(hero.name, kd))

    def revive_heroes(self):
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            fighting_hero = random.choice(living_heroes)
            fighting_opponent = random.choice(living_opponents)

            if fighting_hero.is_alive() is True and fighting_opponent.is_alive() is True:
                fighting_hero.fight(fighting_opponent)
            elif fighting_hero.is_alive() is True and fighting_opponent.is_alive() is False:
                living_opponents.remove(fighting_opponent)
            elif fighting_hero.is_alive() is False and fighting_opponent.is_alive() is True:
                living_heroes.remove(fighting_hero)
            else:
                break


class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        name = input("What is the ability name? ")
        max_damage = int(input("What is the max damage of the ability? "))

        return Ability(name, max_damage)

    def create_weapon(self):
        name = input("What is the weapon name? ")
        max_damage = int(input("What is the max damage of the weapon? "))

        return Weapon(name, max_damage)

    def create_armor(self):
        name = input("What is the armor name? ")
        max_block = int(input("What is the max defense of the weapon? "))

        return Armor(name, max_block)

    def create_hero(self):
        hero_name = input("What is your hero's name? ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input(
                "[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                hero.add_ability(self.create_ability())
            elif add_item == "2":
                hero.add_weapon(self.create_weapon())
            elif add_item == "3":
                hero.add_armor(self.create_armor())
        return hero

    def build_team_one(self):
        team_name = input("Enter team name: ")
        team_size = int(input("Enter team size: "))
        self.team_one = Team(team_name)

        for hero in range(team_size):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        team_name = input("Enter team name: ")
        team_size = int(input("Enter team size: "))
        self.team_two = Team(team_name)

        for hero in range(team_size):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        self.team_one.attack(self.team_two)

    def team_kd(self, team):
        team_kills = 0
        team_deaths = 0

        for hero in team.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths

        if team_deaths <= 0:
            team_kd = team_kills // 1
        else:
            team_kd = team_kills // team_deaths

        return team_kd

    def win(self):
        if self.team_kd(self.team_one) > self.team_kd(self.team_two):
            return self.team_one
        else:
            return self.team_two

    def lose(self):
        if self.team_kd(self.team_one) < self.team_kd(self.team_two):
            return self.team_one
        else:
            return self.team_two

    def alive_heroes(self):
        alive_heroes = list()

        for hero in self.win().heroes:
            alive_heroes.append(hero)

        for hero in alive_heroes:
            if hero.is_alive():
                return hero.name

    def show_stats(self):
        print(f"Survivors: {self.alive_heroes()}")
        print(f"Winner: {self.win().name}")
        print(f"Winner KDA: {self.team_kd(self.win())}")
        print(f"Loser KDA: {self.team_kd(self.lose())}")


game_is_running = True

arena = Arena()
arena.build_team_one()
arena.build_team_two()

while game_is_running:

    arena.team_battle()
    arena.show_stats()
    play_again = input("Play Again? Y or N: ")

    if play_again.lower() == "n":
        game_is_running = False
    else:
        arena.team_one.revive_heroes()
        arena.team_two.revive_heroes()
