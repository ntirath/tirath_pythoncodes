# Assignment 35 :  Check whether string is a number(float) : Author Tirath

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

print(isfloat('s12'))
print(isfloat('1.123'))
