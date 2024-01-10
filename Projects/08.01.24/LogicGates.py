def AND(a,b):
    return True if a == 1 and b == 1 else False

def NAND(a,b):
    return False if AND(a,b) else True

def OR(a,b):
    return True if a == 1 or b == 1 else False

def XOR(a,b):
    return True if a != b else False

def NOT(a):
    return not a

def NOR(a,b):
    return not OR(a,b)

def XNOR(a,b):
    return not XOR(a,b)


