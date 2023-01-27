"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

# TODO: define the 'EXPECTED_BAKE_TIME' constant
EXPECTED_BAKE_TIME = 40; 

# TODO: consider defining the 'PREPARATION_TIME' constant
#       equal to the time it takes to prepare a single layer
PREPARATION_TIME = 2; 
# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(num):

    """"Calculate the bake time remaining.
 
   :param elapsed_bake_time: int baking time already elapsed
   :return: int remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'
 
   Function that takes the actual minutes the lasagna has been in the oven as
   an argument and returns how many minutes the lasagna still needs to bake   
   based on the `EXPECTED_BAKE_TIME`.
   """
    return EXPECTED_BAKE_TIME - num; 



# TODO: define the 'preparation_time_in_minutes()' function
#       and consider using 'PREPARATION_TIME' here
def preparation_time_in_minutes(lasagna_layers):
     
    """ Preparation time of lasagna 
    param num1: layers of the lasagna to be made
    
    returns result of multiplication with the lasagna layers      and the constant PREPARATION_TIME giving the exact 
    minutes to prepare the layers that were input. 
    """
    return PREPARATION_TIME * lasagna_layers; 

# TODO: define the 'elapsed_time_in_minutes()' function
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """ 
        elapsed time baking a lasagna. 
        :param num1: int the number of layers
        :param num2: passed time cooking the lasagna

        call's preparation_time_in_minutes with param num1 and 
        sum it with param num2
    """
    return  preparation_time_in_minutes(number_of_layers) + elapsed_bake_time; 

print(elapsed_time_in_minutes.__doc__); 
     
   

