"""
Function of __init__

- Used as a 'Constructor': Initializes (assigns values) to the data members of the class
  when an object of the class is created. 

Syntax:

class ClassName:
    def __init__(self, variables...):
        ## body

Author: Akaash Deo
"""

class IT5010: 
    def __init__(self, name, userid, password):           # Constructor: Initializes name, userid, and password
        self.name = name                                  # Assigns the name parameter to the instance variable
        self.userid = userid                              # Assigns the userid parameter to the instance variable
        self.password = password                          # Assigns the password parameter to the instance variable

tech_support = IT5010('Rajiv', '20231400', 'vus7er')      # Creates an instance of IT5010 with provided arguments
print(tech_support.userid)                                # Outputs: 20231400

class Football:
    def __init__(self, name, jersey_number, position):    # Constructor: Initializes name, jersey_number, and position
        self.name = name                                  # Assigns the name parameter to the instance variable
        self.jersey_number = jersey_number                # Assigns the jersey_number parameter to the instance variable
        self.position = position                          # Assigns the position parameter to the instance variable

team_member = Football("Akaash", 10, "Midfielder")        # Creates an instance of Football with provided arguments

# Print attributes manually
print(f"Name: {team_member.name}")                        # Outputs: Name: Akaash
print(f"Jersey Number: {team_member.jersey_number}")      # Outputs: Jersey Number: 10
print(f"Position: {team_member.position}")                # Outputs: Position: Midfielder
