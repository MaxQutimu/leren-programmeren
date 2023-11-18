# def hello(aantal: int = 0):
#     lijst = []
#     for x in range(aantal):
#         var = f"Hello from function town {x +1}"
#         lijst.append(var)
#         var2 = '\n'.join(lijst)
#     return var2


# var = hello(4)
# print(var)

def hello(aantal: int = 0):
    lijst = ""
    for x in range(aantal):
        var = f"Hello from function town {x +1}"
        lijst += var + "\n"
    return lijst


var = hello(4)
print(var)



