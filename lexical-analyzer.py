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

# Defines all useful group of Characters as lists 

alphabets = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
numerals = ['0','1','2','3','4','5','6','7','8','9','10']
underscore = ['_']
var_name_tokens = alphabets + numerals + underscore

add_op = ['+']
mul_op = ['*']
ops = add_op + mul_op
space = [' ']
start_paren = ['(']
end_paren = [')']
non_var_name_tokens = ops + space + start_paren + end_paren

# Takes string Input from Command Line

print("Enter Input String")
input_string = str(input()) 

# Initializing Variables

output_string = ''
var_table = {}
num_table = {}
num_of_vars = 0
num_of_nums = 0
var_name = ''
num_name = ''
idx = 0

# Initializing FLags
error_flag = False
repeat_var_num = False
repeat_op = False
paren_num = 0

input_string = input_string + ' '

while ( (error_flag is False) and (idx < len(input_string)) ) :
    
    token = input_string[idx]
    
    if token in non_var_name_tokens: 

        if token in start_paren:
            paren_num = paren_num + 1
        elif token in end_paren:
            paren_num = paren_num -1

        if ((token in ops) and (repeat_op is True)):
            print("ERROR : Operator repeats")
            error_flag = True
            break

        # If not Space it goes to output String
        if token not in space:
            repeat_var_num = False
            output_string = output_string + token + ' '

            if token in ops:
                repeat_op = True

    
    elif repeat_var_num is True:

        print("ERROR : Variable/Number repeats without operator ")
        error_flag = True

    elif token in alphabets:
        
        repeat_op = False
        while (1):
            
            # End Variable Name Case
            if token in non_var_name_tokens:
                id_string = 'var' + str(num_of_vars)
                num_of_vars = num_of_vars + 1
                var_table[id_string] = var_name
                output_string = output_string + var_name + ' '
                var_name = ''
                idx = idx - 1
                repeat_var_num = True
                break
        
            # Variable ending with Underscore Case    
            elif token in underscore:
                next_token = input_string[idx+1]
                if next_token in non_var_name_tokens:
                    print("ERROR : Variable Name cannot end with Underscore")
                    error_flag = True
                    break
            
            #Normal Variable Character Case
            var_name = var_name + token
            idx = idx + 1
            token = token = input_string[idx]
            
    elif token in numerals:
        
        repeat_op = False
        while (1):
            
            # End Numeral Name Case
            if token in non_var_name_tokens:
                id_string = 'num' + str(num_of_nums)
                num_of_nums = num_of_nums + 1
                num_table[id_string] = num_name
                output_string = output_string + num_name + ' '
                num_name = ''
                idx = idx - 1
                repeat_var_num = True
                break
            elif ( (token in alphabets) or (token in underscore) ):
                print("ERROR : Variable Name cannot start with number")
                error_flag = True
                break
                
            num_name = num_name + token
            idx = idx + 1
            token = token = input_string[idx]

    elif token in underscore:
        print("ERROR : Variable Name cannot start with Underscore")
        error_flag = True
        
    else:
        error_flag = True

    idx = idx + 1

if repeat_op is True:
	print("ERROR : Operator At Last")
	error_flag = True

if paren_num is not 0:
	print("ERROR : Parenthesis Mismatch")
	error_flag = True
    
if error_flag is False:
    print("Your Output String is")
    print(output_string)
    print(" ---------------- ")
    print("Your Lexical Table is")
    print(num_table)
    print(var_table)
else:
    print("ERROR at token/character")
    print(token)