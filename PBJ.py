#Making a PB&J sandwich -- still a work in progress

bread = 11
pb = 5
jelly = 10



# First Goal: Create a program that can tell you whether or not you can make a peanut butter and jelly sandwich
def make_pbj_one(bread, pb, jelly):
    if bread >= 2 and pb >= 1 and jelly >= 1:
        print "You can make a PB&J sandwich!"
    else:
        print "Looks like you can't have lunch today."



# Second Goal: Modify that program to tell you: if you can make a sandwich, how many you can make
def make_pbj_two(bread, pb, jelly):
    if bread >= 2 and pb >= 1 and jelly >= 1:
        bread = bread/2
        if bread > 0 and pb > jelly:
            print "You can have",jelly,"sandwiches."
        elif bread > 0 and jelly > pb:
            print "You can have",pb,"sanwiches."    
    else:
        print "Looks like you can't have lunch today."


# Third Goal: Modify that program to allow you to make open-face sandwiches if you have an odd number of slices of bread
def make_pbj_three(bread, pb, jelly):
    if bread >= 2 and pb >= 1 and jelly >= 1:
        bread2 = bread/2
        if bread2 > 0 and pb > jelly:
            print "You can have",jelly,"sandwiches."
            if bread % 2 != 0:
                open_face = bread % 2
                print "and you can have",open_face,"open face sandwiches."
        elif bread2 > 0 and jelly > pb:
            print "You can have",pb,"sanwiches."
            if bread % 2 != 0:
                open_face = bread % 2
                print "and",open_face,"open face sandwich."
    else:
        print "Looks like you can't have lunch today."
print make_pbj_three(bread, pb, jelly)

# Fourth Goal: Modify that program to tell you: if you're missing ingredients, which ones you need to be able to make your sandwiches
def make_pbj_four(bread, pb, jelly):
    if bread <= 2:
        print "You don't have enough bread."
    elif pb < 1:
        print "You don't have enough peanut butter."
    elif jelly < 1:
        print "You don't have enough jelly."
    else:
        print "You can make a PB&J sandwich!"



# Fifth Goal: Modify that program to tell you: if you have enough bread and peanut butter but no jelly, that you can make a peanut butter sandwich but you should take a hard, honest look at your life.  Wow, your program is kinda judgy.
def make_pbj_five(bread, pb, jelly):
    if bread >= 2 and pb >= 1 and jelly >= 1:
        sandwiches = bread/2 #total sandwiches
        pb_sandwich = sandwiches - jelly #total number of pb sandwiches
        no_jelly = sandwiches - pb_sandwich #number of sandwiches w/pb after PB&J
        if bread >= 2 and pb >= 1 and jelly == 0:
            print "You can't make a PB&J, but you can make a peanut butter sandwich. But you can make" ,pb_sandwich, "sandwiches."
        elif bread/2 + pb > jelly:
            print "You can make",sandwiches, " PB&J sandwiches or", pb_sandwich, " peanut butter sandwiches.", no_jelly
    else:
        print "Looks like you can't have lunch today."

          
