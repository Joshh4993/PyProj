user_string = input("Enter a sentence: ")
FILTER = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
filtered_string = ""
counts = dict()

#### FILTER ####
filtered_string = user_string.lower()
for char in filtered_string:
    if char in FILTER:
        filtered_string = filtered_string.replace(char, "")
## DEBUG ##
print(filtered_string)

#### MOST COMMON ####
words = filtered_string.split()
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

counts_x = sorted(counts.items(), key=lambda kv: kv[1])
result = counts_x[-1]

print(result)

############################################################

# SET user_string TO "Hello!{}''}^%$ World world hello dog world"
# SET filtered_string TO ""
# SET counts TO dict
# 
# SET filtered_string TO LOWER(user_string)
# FOR EACH char FROM filtered_string DO
#   IF char in FILTER
#       SET filtered_string = REPLACE(filtered_string, char) WITH ""
#   END IF
# END FOREACH
# PRINT(filtered_string)
#
# SET words TO SPLIT(filtered_string)
# FOR EACH word FROM words DO
#   IF word IN counts
#       counts[word] += 1
#   ELSE
#       counts[word] = 1
#   END IF
# END FOREACH
#
# SET counts_x TO SORTED(counts.items(), key=lambda kv: kv[1])
# SET result TO counts_x[-1]
#
# PRINT result