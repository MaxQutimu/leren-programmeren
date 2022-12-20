from fruitmand import fruitmand
from operator import itemgetter

fruitmand = sorted(fruitmand , key = itemgetter("weight"),reverse=True)
for x in fruitmand:
        print(x.get("weight"))



     