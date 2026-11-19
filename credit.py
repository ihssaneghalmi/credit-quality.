import os
2 import math
3
4
5 def calculate_risk ( income , debt , age ) :
6 if income <= 0:
7 return -1
8
9 ratio = debt / income
10
11 if ratio > 0.6:
12 return " HIGH "
13 elif ratio > 0.3:
14 return " MEDIUM "
15 else :
16 return " LOW "
17
18
19 def calculate_risk2 ( income , debt , age ) :
20 if income <= 0:
21 return -1
22
23 ratio = debt / income
24
25 if ratio > 0.6:
26 return " HIGH "
27 elif ratio > 0.3:
28 return " MEDIUM "
29 else :
30 return " LOW "