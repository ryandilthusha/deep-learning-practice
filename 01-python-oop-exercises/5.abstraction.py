"""
EXERCISE 5: Smart Home Appliance Interface
------------------------------------------
Requirements:
1. From 'abc', import 'ABC' and 'abstractmethod'.
2. Create an abstract base class named 'SmartDevice' with two abstract methods:
   - Create abstract method name: def turn_on(self): do nothing
   - Create abstract method name: def get_status(self): do nothing
3. Create a valid child class 'SmartLight inherits SmartDevice:
   - __init__(self, brightness=100) setting self.brightness and self.is_active = False.
   - Implement turn_on(self) -> sets is_active = True and prints light is on.
   - Implement get_status(self) -> returns "Light is ON" or "Light is OFF".
4. Create an incomplete child class 'BrokenDevice(SmartDevice)':
   - Implement turn_on(self), but DO NOT implement get_status(self).
5. Test your code:
   - Successfully create and run a SmartLight instance.
   - Wrap the creation of BrokenDevice() in a try/except block to catch and print the TypeError.
"""




from abc import ABC, abstractmethod

class SmartDevice(ABC):

   @abstractmethod
   def turn_on(self):
      pass

   @abstractmethod
   def get_status(self):
      pass



class SmartLight(SmartDevice):

   def __init__(self, brightness=100):
      self.brightness = brightness
      self.isactive = False

   def turn_on(self):
      self.isactive = True
      print("Light On")

   def get_status(self):
      if self.isactive == False:
         print("Status: Light is Off")
      elif self.isactive == True:
         print("Status: Light is On")



# Testing ----------

light1 = SmartLight()
light1.get_status()

light1.turn_on()
light1.get_status()


    