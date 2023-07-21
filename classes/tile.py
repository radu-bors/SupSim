class Tile():
    """_summary_
    """
    
    def __init__(self, location, coordinates, customer, is_accessible):
        self.location = location
        self.coordinates = coordinates
        self.has_customer = customer
        self.is_accessible = is_accessible
        
    def __repr__(self):
        return f'<Tile has section {self.location} at {self.coordinates}, has customer {self.has_customer} and has accesibility {self.is_accessible}>'