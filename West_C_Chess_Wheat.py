"""Chess_Wheat.py
C West
This program will calculate a game of chess and a reward of wheat.
"""

import math

 # This introduces the player to the game.
print ("In this game of chess a reward of wheat goes to the man who invented chess.")
print ("For each movement of a square they will receive one grain of wheat")
print ("that is then doubled for each additional movement of chess piece up to 64 squares on the board. \n")

# Total grains of wheat paid to the inventor of chess.
total_grains_wheat = ((2 ** 64) - 1)
print("The sum of grains of wheat the ruler paid to the inventor:  ", total_grains_wheat)

# Total weight of the grains of wheat.
total_wheat_weight = (total_grains_wheat * 50) # take first answer and times by 50 mg
print("If a wheat grain weights approximaetly 50 mg.  This wheat weighed:  ", total_wheat_weight, "mg")

""" one grain of wheat measures approximately 7 height x 3 width x 4 length
the formula to calculate the surface area is 
2((3 x 4) + (7 x 4) + (7 x 3)) = 122 mm squared surface area of one grain of wheat.

To convert the total surface area of Oregon 254806 km squared
times one million converts to mm squared. 
"""

# surface area of one grain of wheat.
surface_area_wheat = int(((3 * 4) + (7 * 4) + (7 * 3))*2)
# print("The surface area of one grain of wheat is:  ", surface_area_wheat, "mm ^2")

# total surface area of total wheat.
total_surface_area_total_wheat = surface_area_wheat * total_grains_wheat
# print("Total surface are of total wheat:  ", total_surface_area_total_wheat)

# convert 254806 km squared Oregon times one million equals conversion to mm squared.
oregon_covert = int(254806 * 1000000)
# print("Oregon surface area km ^2 converted to mm ^2:  ", oregon_covert, "mm ^2")

# total surface area of the total amount of what divided by the total surface area of Oregon.
depth_of_wheat = total_surface_area_total_wheat // oregon_covert
print("The state of Oregon would be covered ", depth_of_wheat, "mm ^2 by this amount of wheat.")


z = input("end, CWest")