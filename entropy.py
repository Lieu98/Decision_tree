import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as m

total=int(input("total points:"))

P_yes=int(input("probability of yes:"))
P_y=P_yes/total
P_no=1-(P_yes/total)
if(P_no > 0):

	answer_entropy=-(P_y*m.log(P_y,2))-(P_no*m.log(P_no,2))
	print(answer_entropy)
else:
	print("entropy = 0")	

if(P_no > 0):

	answer_gini_impurity=-P_y*(1-P_y)-P_no*(1-P_no)
	print(answer_gini_impurity)
else:
	print("gini_impurity = 0")	
