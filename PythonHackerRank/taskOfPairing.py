# A company sells dumbbells in pairs. These are weights for exercising. They receive a shipment of dumbbells weighing anywhere from 1 unit up to a certain maximum. A pair can only be sold if their weights are sufficiently close: no greater than 1 unit difference. Given an inventory of various weights, determine the maximum number of pairs the company can sell.
 
# For example, if there are 2 dumbbells of weight 1, 4 of weight 2, 3 of weight 3 and 1 of weight 4, they can be paired as [1,1], [2,2], [2,2], [3,3], [3,4] for a total of 5 pairs.
 
# Function Description
# Complete the function taskOfPairing in the editor below. The function must return an integer representing the maximum number of similar pairs that can be made from the given supply of weights.
 
# taskOfPairing has the following parameter(s):
#     freq[0... n-1]:  a frequency array of integers where the ith element represents the number of dumbbells having a weight of i+1.
 
# Constraints
# 	• 1 ≤ n ≤  10^5
# 	• 0 ≤ freq[i] ≤  10^9