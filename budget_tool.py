import pandas as pd




class Budget:
    
    def __init__(self,budget_name,gsheets_location) -> None:
        self.name = budget_name
        self.gsheets_location = gsheets_location
        
    