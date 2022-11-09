integers = [45, 76, 2, 6, 4]
biggest_num = 0
second_num = 0
for i in integers:
    if i > biggest_num:
        second_num = biggest_num
        biggest_num = i

print(f'Biggest: {biggest_num} | Second: {second_num}')

############################################################

# SET integers TO [45, 76, 2, 6, 4]
# SET biggest_num TO 0
# SET second_num TO 0
# 
# FOR EACH i FROM integers DO
#   IF i > biggest_num THEN
#       SET second_num TO biggest_num
#       SET biggest_num TO i
#   END IF
# END FOREACH
#
# PRINT biggest_num
# PRINT second_num