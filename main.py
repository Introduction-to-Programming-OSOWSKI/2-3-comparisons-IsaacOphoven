#WRITE YOUR CODE IN THIS FILE
#ok

def greaterThan(x,y):
    if x > y:
        return True
    else:
        return False

def lessThan(x,y):
    if x < y:
        return True
    else:
        return False

def equalTo(x,y):
    if x == y:
        return True
    else:
        return False

def greaterOrEqual(x,y):
    if x > y:
        return True
    elif x == y:
        return True
    else:
        return False

def lessOrEqual(x,y):
    if x < y:
        return True
    elif x == y:
        return True
    else:
        return False

print(greaterOrEqual(4,2))

