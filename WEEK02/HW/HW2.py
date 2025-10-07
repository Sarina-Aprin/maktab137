import json 
from json import JSONDecodeError

#1
#We have to define a class called invalidconfigerror.

class InvalidConfigError(Exception):
    pass 

#2
#First we define a function for part 2.
#For part 3 first we have to write a try except code to export FileNotFound error with an appropriate message.
#For next line in part 3 we have to write an except to manage JSONDecodeError.
#Then we have to make a json file as it is not given to us, and make a dictionary in it.
#If any of the elements of the dictionary was not found, we have to raise an error.so we need ifs and elifs.
#Because if we add the ifs of last part to the ifs of latter part the code may not read it,
# we add it to another with open so that it can be read without any problem. 

def load_config(filepath):
    try:
        with open("config.json", "w") as f:
            dictionary = json.load(f)
            if "api_key" not in dictionary:
                raise InvalidConfigError("API key not available.")
            elif "mode" not in dictionary:
                raise InvalidConfigError("Mode not found.")
            elif "database_url" not in dictionary:
                raise InvalidConfigError("Database not found.")
        with open("config.json", "w") as f:
            dictionary = json.load(f)
            if dictionary["mode"] != "debug" and dictionary["mode"] != "production":
                raise InvalidConfigError("Mode not valid.")
    except FileNotFoundError:
        print("File not found!")
    except JSONDecodeError:
        print("JSON is not valid!")

try:
    load_config("config.json")
except FileNotFoundError: 
    print("We can't find your file.")
except JSONDecodeError:
    print("Your json file is invalid.")
except InvalidConfigError:
    print("Config is not valid.")


