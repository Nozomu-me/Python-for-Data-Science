import math


def NULL_not_found(object: any) -> int:
    flag = 0
    if object is None:
        print(f"Nothing: {object} {type(object)}")
    elif isinstance(object, float) and math.isnan(float(object)):
        print(f"Cheese: {object} {type(object)}")
    elif type(object) == int and object == 0:
        print(f"Zero: {object} {type(object)}")
    elif object == "":
        print(f"Empty: {object} {type(object)}")
    elif type(object) == bool and object == False:
        print(f"Fake: {object} {type(object)}")
    else:
        print("Type not Found")
        flag = 1
    return flag
