class Customer():
    '''
    Customer class for movement, activity and something
    '''

    def __init__(self, prob_matrix, targe_location, coordinates):
        self.prob_matrix = prob_matrix
        self.target_location = targe_location
        self.coordinates = coordinates
        
    def get_location(self):
        return self.target_location
    
    def get_coordinates(self):
        return self.coordinates