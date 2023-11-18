birds = [{'name':'mus','key':'m','count':0},
          {'name':'duif','key':'d','count':0},
          {'name':'koolmees','key':'k','count':0},
          {'name':'kraai','key':'i','count':0},
          ]

print('Bird counter until dot')
# TO DO:

# 1) print all birds with key and name
for x in range(len(birds)):
    print(f"{birds[x]['key']} : {birds[x]['name']}")



# 2) define function get_bird_by_key(birds: list, key:str) returns bird or None
def get_bird_by_key(birds: list, key:str):
    for bird in birds :
        if key == bird['key']:
            return bird
    return None

get_bird_by_key(birds,key='d')
    

# 3) repeat until given '.'
#       input key of bird 
#    find bird with get_bird_by_key
#    if bird found: 
#       increment bird count
#       show bird name and count
def birdinput(birds:list):
    while True:
        letterkey = input(" vul letter in ")
        bird = get_bird_by_key(birds,letterkey)
        if letterkey != None:
            bird['count'] += 1;
            for x in range(len(birds)):
                print(f"{birds[x]['name']}  :  {birds[x]['count']} ")
            
            
        else:
            print('')
            
        
        
birdinput(birds)
    
    


# 4) print all birds with name and count

# 5) print per bird also the percentage of the total count