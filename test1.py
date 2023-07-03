value = (input("Does the engine start? "))
engine_start = ""
engine_run = ""







if value != "yes":
    print("Engine does not start")
    engine_start = "no"
elif value == "no":
    print("Engine starts")
    engine = "yes"

if engine_start == "yes":
    print("Does the engine run normally?")
    
