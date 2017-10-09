# gh_slogan.py
# 2017, polarysekt


from random import randint

g_ghSloganList = [ "DEFAULT SLOGAN", "It's a secret to everyone.", "CTOR BLOGGEN", "Welcome Back" ]

def getSlogan():
    return g_ghSloganList[randint(0,3)]

def test_units():
    
    print( getSlogan() )
    return True


def main():
    test_units()

if __name__ == "__main__":
    main()
