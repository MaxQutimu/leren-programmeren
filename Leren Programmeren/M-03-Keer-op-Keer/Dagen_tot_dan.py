Dag = input("Welke dag? ma,di,wo,do,vr,za of zo ")

Variable_Voor_Loop = True
lijst = ["ma","di","wo","do","vr","za","zo"]

uitlijst_pakken = lijst.index(Dag)
tot_en_met = lijst[:uitlijst_pakken+1]
    
print(str(tot_en_met))