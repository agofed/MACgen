import random

macbyte = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

guu = ['0','4','8','C'] # global unique unicast
gum = ['1','5','9','D'] # global unique multicast
lau = ['2','6','A','E'] # locally administered unicast
lam = ['3','7','B','F'] # locally administered multicast

def macgenerator (prefix = guu):
    macaddress = random.choice(macbyte)+random.choice(prefix)
    for x in range(5):
        macaddress += ':'+random.choice(macbyte)+random.choice(macbyte)
    return macaddress

def main():
    mac = macgenerator() # global unique unicast (guu) - default
    # mac = macgenerator(gum)
    # mac = macgenerator(lau)
    # mac = macgenerator(lam)
    print(mac)

if __name__ == "__main__":
    main()
