myName = 'Huu Hoang'
myAge = 35
myHeight = 76
myWeight = 60
myEyes = 'blue'
myTeeth  =  'white'
myHair = 'Brown'

print "Let's talk about %s. " %myName
print "He's %d inches tall." % myHeight
print "He's %d pounds heavy." % myWeight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (myEyes, myHair)
print "His teeth are usually %s depending on the coffee." % myTeeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    myAge, myHeight, myWeight, myAge + myHeight + myWeight)
