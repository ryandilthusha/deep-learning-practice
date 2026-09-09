"""
EXERCISE 1: Starship Fleet Management
--------------------------------------
Requirements:
1. Create a class named 'Starship'.
2. Add a shared class variable 'fleet_name' set to "Intergalactic Armada".
3. Write an __init__ method that takes:
   - ship_name (string)
   - shield_power (number)
   Save both as instance attributes using 'self'.
4. Write a method 'take_damage(self, damage_amount)':
   - Define a local variable 'shield_efficiency = 0.8'.
   - Calculate actual damage: damage_amount * shield_efficiency.
   - Subtract actual damage from self.shield_power.
   - Print the ship name and the updated shield power.
5. Create two starship objects:
   - "Millennium Falcon" (shield: 100)
   - "Enterprise" (shield: 150)
6. Call take_damage(50) on the Falcon and print both ships' shields and fleet names
   to verify that Falcon's shield dropped, Enterprise remained untouched, and
   both still share the exact same fleet name.
"""


class Starship:

    fleet_name = "Inter-Galactic Armada"

    def __init__(self, ship_name, shield_power):
        self.ship_name = ship_name
        self.shield_power = shield_power

    def take_damage(self, damage_amount): 
        shield_efficiency = 0.8
        actual_damage = (damage_amount * shield_efficiency)
        new_shield_power = self.shield_power - actual_damage
        
        return new_shield_power


ship1 = Starship("Mil", 100)
ship2 = Starship("Ent", 100)

print(ship1.take_damage(10))
print(ship2.take_damage(50))

