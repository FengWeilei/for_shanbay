tabby_cat = "\tI'm typed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


## \t Horizontal Tab
## \n Linefeed
## \\ will print just one backslash


##a tiny piece of fun code
while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
