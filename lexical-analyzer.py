# This is a Lexical Analyzer Program
#
# It takes as input strings of variable length containing the following -  
# 		1. variables ( contains A-Z,a-z,0-9,_ ) [Doesn't start/end with _, Doesn't start with number] 
#		2. Numbers (0-9 only)
#		3. parenthesis "()"
#		4. operators "*" and "+"
#		5. space between the above in any length 
#	
#	If input string has any irregularities (outside points mentioned above), Then show ERROR message.  
# 
#  	Else, 
#		1. Replace strings and numbers by id's and print the string (Spaces Regular)
#		2. Maintain a Look-up table for id's to variable/numbers. 
#
#	Example -
# 
#		Input:
#		String 			" (  var_a + var_b  )*var_c +  num_a " 
#
#		Output:
#
#		String - 		" (ID_1 + ID_2 ) * ID_3 + ID_4 "
#		Look-up Table - 
#
#					ID_1 -> var_a
#					ID_2 -> var_b
#					ID_3 -> var_c
#					ID_4 -> var_d