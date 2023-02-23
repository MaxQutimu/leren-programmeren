def berekenen_poten():
    GiraffenPoten = 4
    StruisvogelsPoten = 2
    zebrasPoten = 4

    Giraffen = int(input('aantal giraffen'))
    Struisvogel = int(input('aantal struisvogels'))
    zebras = int(input('aantal zebras'))

    totaal = (GiraffenPoten * Giraffen) + (StruisvogelsPoten * Struisvogel) + (zebrasPoten * zebras)
    return totaal

poten = berekenen_poten()
print(f'totaal aantal poten is', poten)