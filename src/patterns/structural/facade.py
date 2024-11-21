"""
-------------------------------------------------
File: facade.py
Intent: 
    Facade is a structural design pattern that provides a simplified
    interface to a library, a framework, or any other complex set of classes.

Usage:
    Use the Facade pattern when you need to have a
    limited but straightforward interface to a complex subsystem.
-------------------------------------------------
"""

class LightSystem:
    def turn_on(self):
        print("Lights are turned ON.")

    def turn_off(self):
        print("Lights are turned OFF.")

    def dim_lights(self, level):
        print(f"Lights are dimmed to {level}% brightness.")

class Thermostat:
    def set_temperature(self, temperature):
        print(f"Thermostat is set to {temperature}°C.")

class SecurityCamera:
    def activate(self):
        print("Security cameras are activated.")

    def deactivate(self):
        print("Security cameras are deactivated.")

class EntertainmentSystem:
    def turn_on_tv(self):
        print("TV is turned ON.")

    def turn_off_tv(self):
        print("TV is turned OFF.")

    def play_movie(self, movie_name):
        print(f"Playing movie: {movie_name}")

class SmartHomeFacade:
    def __init__(self):
        self.thermostat = Thermostat()
        self.light_system = LightSystem()
        self.security_camera = SecurityCamera()
        self.entertainment_system = EntertainmentSystem()

    def morning_routine(self):
        print("\nStarting Morning Routine...")
        self.light_system.turn_on()
        self.light_system.dim_lights(75)
        self.thermostat.set_temperature(22)
        self.security_camera.deactivate()

    def night_routine(self):
        print("\nStarting Night Routine...")
        self.light_system.dim_lights(10)
        self.security_camera.activate()
        self.thermostat.set_temperature(18)

    def movie_time(self, movie_name):
        print("\nStarting Movie Time...")
        self.light_system.dim_lights(20)
        self.entertainment_system.turn_on_tv()
        self.entertainment_system.play_movie(movie_name)

    def leave_home(self):
        print("\nLeaving Home...")
        self.light_system.turn_off()
        self.security_camera.activate()
        self.thermostat.set_temperature(16)
        self.entertainment_system.turn_off_tv()

def facade_smart_home():
    smart_home = SmartHomeFacade()

    smart_home.morning_routine()
    smart_home.movie_time("Inception")
    smart_home.night_routine()
    smart_home.leave_home()