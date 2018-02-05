from Pet import Pet
from Owner import Owner
owner = Owner()
pet = Pet()

from threading import Thread
import sys
import asyncio

def welcome():
    '''
    this just gives the instructions
    :return: none
    '''
    print("welcome to text based Tamagotchi \nyou will have the responsibility of taking care of a dog")
    print("In this game your dog has a amount different moods and a certain of energy ")
    print("your dog starts with 60 energy and will loose energy every 30 seconds")
    print("in order to gain energy you can let your dog rest by typing rest or by feeding your dog by typing feed")
    print("but as time progresses your dogs mood goes down so you must make sure to play with your dog")
    print("you can play with dog by typing frisbee, walk, or go to park")

def input_converter(input):
    '''

    :param input: this is the input for what action the player wants to take
    :return: none
    '''
    if input == "frisbee":
        energy = owner.get_frisbee_energy()
        mood = owner.get_frisbee_mood()
        pet.activity_manager(energy, mood)
    elif input == "walk":
        energy = owner.get_walk_energy()
        mood = owner.get_walk_mood()
        pet.activity_manager(energy, mood)
    elif input == "go to park":
        energy = owner.get_park_energy()
        mood = owner.get_park_mood()
        pet.activity_manager(energy, mood)
    elif input == "rest":
        energy = pet.get_sleep_energy()
        mood = pet.get_sleep_mood()
        pet.activity_manager(energy, mood)
    elif input == "feed":
        energy = owner.get_feed_energy()
        mood = owner.get_feed_mood()
        pet.activity_manager(energy, mood)

def main():
    welcome()
    while True:
        nput = Thread(target=input_converter(owner.owners_inputs()))
        nput.start()
    #deplete = Thread(target=pet.energy_and_mood_depleter())
    #deplete.start()




if __name__ == '__main__':
        main()
