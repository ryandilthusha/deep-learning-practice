"""
EXERCISE 4: Amphibious Explorer Drone
------------------------------------
Requirements:
1. Create class 'LandRover' with a method 'drive(self)' printing a driving message.
2. Create class 'Boat' with a method 'sail(self)' printing a sailing message.
3. Create child class 'AmphibiousRover' that inherits from BOTH LandRover and Boat:
   - Add a custom method 'transform(self)' printing a transformation message.
   - Add a method 'navigate(self, destination, speed=None)':
     * If speed is provided, print: "Navigating to [destination] at [speed] km/h."
     * If speed is None, print: "Navigating to [destination] at default eco-cruising speed."
4. Instantiate AmphibiousRover and demonstrate calling drive(), sail(), transform(),
   and navigate() with both 1 argument and 2 arguments.
"""





class Landrover:

    def drive(self):
        print("Driving Landrover")


class Boat:

    def sail(self):
        print("Sailing  Boat")

class AmphibiousRover( Landrover , Boat ):

    def transform(self):
        print("Transforming")

    def navigate(self, destination, speed=None):
        if speed is not None:
            print(f"Navigating {destination} with speed {speed}")
        elif speed is None:
            print("No speed")





#Testing ----------

landrover1 = Landrover()
landrover1.drive()

boat1 = Boat()
boat1.sail()

both1 = AmphibiousRover()
both1.navigate("Finland", 100)
both1.navigate("Finland")
