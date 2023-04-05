# Accept a string and use list comprehension to generate as many strings of that word
# in an array as many letters are in the given string. For example:
# string = "Code" (4 letters in the string) --> ["Code", "Code", "Code", "Code"]


def create_list(morewords):
    numchar = len(morewords)
    result = []
    for letter in range(numchar):
        result.append(morewords)
    return result


print(create_list("Code"))
print(create_list("lovely"))
