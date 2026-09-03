"""
EXERCISE 3: RPG Hero Evolution
------------------------------
Requirements:
1. Create a base class 'Hero':
   - __init__ takes 'name' and 'hp'.
   - Method 'attack(self)' prints: "[name] strikes for standard physical damage!"
2. Create a child class 'Mage' that inherits from Hero:
   - __init__ takes (name, hp, mana). Inherit them properly and then set self.mana.
   - Override 'attack(self)' to REPLACE the parent behavior and print:
     "[name] consumes [mana] mana and casts a massive Fireball!"
3. Create a child class 'Paladin' that inherits from Hero:
   - __init__ takes (name, hp) andInherit them properly.
   - Override 'attack(self)' to EXTEND the parent behavior with existing method function.
     and print also: "[name] heals for 5 HP in a radiant burst of holy light!"
4. Create one Hero, one Mage, and one Paladin, and call attack() on all three.
"""






class Hero:

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self):
        print(f"{self.name} strike physically")



class Mage(Hero):

    def __init__(self, name, hp, mana):
        super().__init__(name, hp)
        self.mana = mana

    def attack(self):
        print(f"{self.name} strike Magically!!!")



class Paladin(Hero):

    def __init__(self, name, hp):
        super().__init__(name, hp)


    def attack(self):
        super().attack()
        print(f"{self.name} heals 5HP")





# Testing ----------
hero1 = Hero("Aragon", 100)
hero1.attack()

print("------------------")

mage1 = Mage("Gandalf", 500, 30)
mage1.attack()

print("------------------")

paladin1 = Paladin("Frodo", 40)
paladin1.attack()
