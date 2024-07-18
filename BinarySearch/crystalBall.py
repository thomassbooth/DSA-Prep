import math

# Given two crystal balls that will break if dropped from high enough distance
# determine the spot in which it will break in the most optimised way
# this is basicly looking at [f, f, f, f, t, t, t, t, t] we need to find where the first t is

#sol 1:
# since we have two crystal balls, we can drop the first ball at the mid point,
# if it breaks we know the spot is between 0 and mid, if it doesnt break we know the point is in the top half
# so we half it, check then linear search

#sol 2:
#


def two_crystal_balls(breaks):

    jumpAmount = math.floor(math.sqrt(len(breaks)))

    #find the point of breaks
    i = jumpAmount
    while i < len(breaks):

        if breaks[i] == True:
            break;

        i += jumpAmount

    #go back to the jump amount
    #we now need to go forward one by one to the break amount - jumpAmount

    for j in range(i-jumpAmount, i):
        if breaks[j] == True:
            return j

    return -1

if "__main__" == __name__:
    print(two_crystal_balls([False, False, False, False, True, True, True, True, True, True])) #4
    
