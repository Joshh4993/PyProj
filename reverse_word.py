user_string = input("Type sentence: ")
args = []
reverse_args = []
result = ""

args = user_string.split(" ")

for i in range(len(args), 0, -1):
    reverse_args.append(args[i-1])

result = " ".join(reverse_args)

print(result)

############################################################

# SET user_string TO "Hello World"
# SET args TO []
# SET reverse_args TO []
# SET result TO ""
# 
# SET args TO SPLIT(user_string)
# 
# FOR EACH i FROM range(len(args), 0, -1) DO
#   APPEND TO reverse_args VALUE args[i-1]
# END FOREACH
#
# SET result TO JOIN(reverse_args)
#
# PRINT result