from Pet import Pet


class Owner(object):

    def __init__(self):
        self.feed_En = 5
        self.frisbee_En = -10
        self.walk_En = -15
        self.park_En = -20
        self.feed_Md = -1
        self.frisbee_Md = 2
        self.walk_Md = 3
        self.park_Md = 5

    def get_feed_energy(self):
        return self.feed_En

    def get_feed_mood(self):
        return self.feed_Md

    def get_frisbee_energy(self):
        return self.frisbee_En

    def get_frisbee_mood(self):
        return self.frisbee_Md

    def get_walk_energy(self):
        return self.walk_En

    def get_walk_mood(self):
        return self.walk_Md

    def get_park_energy(self):
        return self.park_En

    def get_park_mood(self):
        return self.park_Md

    def owners_inputs(self):
        '''
        this just asks and takes in what the player whants to do with or to dog.
        :return: owners action: this is the input of what action the player wants to take
        '''
        owners_action = input("what would you like to do with your dog")
        return owners_action

