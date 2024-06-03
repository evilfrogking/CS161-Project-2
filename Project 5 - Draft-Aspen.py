"""Project 5
West C
This program involves garden information"""

import string # imports the Python string module
'''------- Code Structure ----------
def main()
    user_flower = user_validation()

def user_flower_validation()
    # validate user input
    return flower


if __name__ == "__main__":
   main()
 -------------------------------- '''

print("This program collects information about your garden.\n")

# input validation
# flower_valid = False
# def user_validation() 
# while flower_valid == False:
user_input_flower = input ("Enter one flower to grow in your garden: " ) .lower() # asks for a user input for a flower
# Tulips == tulips
# T8lpis == ?? 
input_flower = user_input_flower # why do you copy the value to a new variable?

bad_chars = string.whitespace + string.punctuation + string.digits # check for punctation and white space and numbers
# will .isalpha() work?

for char in user_input_flower:
    # if char in bad_chars: 
    #     input_flower = input_flower.replace (char, ' ') # remove the bad characters replace with blank space
    if char != user_input_flower.isalpha():
        # either user_input_flowers = input_flower.replace (char, ' ')
        # or set up a while loop that requires the user to try again
        # print("Invalid input, please try again.")
    else:
        flower_valid = True
            
        


# input_vegetable = input ("Enter one vegetable to grow in your garden: ", []) . lower()


inventory_flowers = ["rose", "dahlia", "tulip", "daffodil"] # this line creates the list.
inventory_garden = ["tomato", "zucchini", "carrot"] # another list.


total_list = inventory_flowers + inventory_garden
print(f"Total defined list:  {total_list}\n")

inventory_flowers.append("sunflower") # append item to the end of the list.
inventory_flowers.append(input_flower) # append the user input flower to the end of the list.
print (f"Appended -Sunflower- and User_Input_Flower at end:  {inventory_flowers}\n")

inventory_garden.append (["green bean", "pumpkin", "squash"]) # append a list.
print (f"Append a list to the end:  {inventory_garden}\n")

herb_Tuple = ("basil", "thyme", "sage") # tuple list that will remain unchanged.
print (f"The herbs currently grown in this garden are: {herb_Tuple}")

#If I wanted to include the herb_Tuple into the rest of the list I would convert the Tuple into a list first.

herb_list = list(herb_Tuple)
total_complete_list = inventory_flowers + inventory_garden + herb_list
print (f"Total Complete List: , {total_complete_list}") # this will print all the lists together.

# sorted(total_complete_list) # this is where the list can be sorted alphabetically

inventory_flowers.remove ("tulip") # will remove the word tulip.
# the following line will remove the quote marks and add a comma between the words.
print (f"Remove quotes, add commas, and remove -Tulip- from the list: ", ", ".join(inventory_flowers))

# Rainfall - average
# define function measure_rainfall

# sunlight - minimum, maximum, average
#define function measure_sunlight


z = input ("Pause, CWest")

