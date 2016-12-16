from vehicle import Vehicle



class Truck(Vehicle):

    def __init__(self,carry_limit = None,current_carriage_weight = None, *args):
        self.carry_limit = carry_limit
        self.current_carriage_weight = current_carriage_weight
        super(Truck, self).__init__(*args)

    def has_carriage(self):
        return self.current_carriage_weight != None

    def attach_carriage(self,current_carriage_weight):
        self.current_carriage_weight = current_carriage_weight
        return self.current_carriage_weight <= self.carry_limit
       

    def detach_carriage(self):
        self.current_carriage_weight = None

