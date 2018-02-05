import time

class Pet(object):

    def __init__(self):
        self.energy_lvl = 60
        self.mood_lvl = 30

        self.sleep_En= 10
        self.sleep_Md= -5

    def get_energy_lvl(self):
        return self.energy_lvl

    def get_mood_lvl(self):
        return self.mood_lvl

    def get_sleep_energy(self):
        return self.sleep_En

    def get_sleep_mood(self):
        return self.sleep_Md

    def activity_manager(self, energy, mood):
        '''
        this takes away or adds to energy/mood
        :param energy: this is the amount of energy that is lost from the task or gained from task
        :param mood: this is the amount of the mood that is lost form the task or gained from task
        :return: none
        '''
        self.energy_lvl += energy
        self.mood_lvl += mood
        if self.energy_lvl > 100:
            self.energy_lvl = 100

        if self.mood_lvl > 30:
            self.mood_lvl = 30
        print("your dogs current energy level is ",self.energy_lvl, " and its mood level is ", self.mood_lvl)


    def energy_and_mood_depleter(self):
        '''
        this takes down the dogs energy and mood lvls by a certain number ever 30 seconds
        :return:
        '''
        while True:
            self.energy_lvl -= 2
            self.mood_lvl -= 1
            print("your dogs energy has gone dow to ",self.energy_lvl, " and your dogs mood has gone down to", self.mood_lvl)
            time.sleep(30)

