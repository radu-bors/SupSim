class Customer():
    '''
    Customer class for movement, activity and something
    '''

    def __init__(self, prob_matrix, target_location, coordinates):
        self.prob_matrix = prob_matrix
        self.target_location = target_location
        self.coordinates = coordinates
        
    def get_location(self):
        return self.target_location
    
    def get_coordinates(self):
        return self.coordinates
    
    def move(self, coordinates):
        self.coordinates = coordinates