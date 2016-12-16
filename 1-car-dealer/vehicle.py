class Vehicle():
    def __init__(self,is_running = None,ccm = None,top_speed = None):
        self.is_running = is_running
        self.ccm = ccm
        self.top_speed = top_speed
    def start_engine(self):
        self.is_running = True
    def stop_engine(self):
        self.is_running = False