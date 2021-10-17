import random

# Bubble Sort Algorithm
def int_sort( list_ints ):

    m = len( list_ints )

    is_sorted = False
    while( is_sorted == False ):
        is_sorted = True
        for i in range( m-1 ):

            temp_int = 0
            if ( list_ints[i] > list_ints[i+1] ):
                temp_int = list_ints[i]

                list_ints[i] = list_ints[i+1]
                list_ints[i+1] = temp_int
                is_sorted = False

    return list_ints

# Constructs a list of length size consisting of random integers
def make_random_list( size, max_int ):
    rand_list = []
    for i in range( size ):
        rand_list.append( random.randint(0, max_int) )

    return rand_list

# EXAMPLE

rand_list_ints = make_random_list( 20, 1000 )
print( rand_list_ints )

sorted_rand_list = int_sort( rand_list_ints )
print( sorted_rand_list )
