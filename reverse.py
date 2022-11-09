#user_string = input("Type a word or sentence: ")
#user_string = user_string[::-1]
#print(user_string)

input_string = input("Enter your string: ")
result = ""

for i in range(len(input_string), 0, -1):
    result += input_string[i-1]

print(result)

############################################################

# SET user_string TO "Hello World"
# SET result TO ""
# 
# FOR EACH i FROM range(len(input_string), 0, -1) DO
#   SET result TO result + input_string[i-1]
# END FOREACH
#
# PRINT result