from re import search
text = "samurai"
ending = "ai"

# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

# Examples:

# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false

def solution(text, ending):
    if ending in text:
        print("true")
       
    else:
        print("False")
        
    pass
solution(text,ending)
print(text)
print(ending)   
    # return text.endswith(ending)


    