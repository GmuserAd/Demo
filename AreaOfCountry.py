def AreaOfCountry(name,area):
    EARTH_AREA=148940000 
    ContryAercentArea = ((area/EARTH_AREA)*100)
    print(f"{name}is {round(ContryAercentArea,2)}% of the total world's landmass")

AreaOfCountry("USA", 9372610)