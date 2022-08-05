

import random


class RoomsManager:

    
    def __init__(self):

        self.n_available = random.randint(0,4)

        
    def find_rooms(self, n_rooms):

        if self.n_available < n_rooms:
            return False
        else:
            return True