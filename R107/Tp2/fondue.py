BASE=4
fromage=800.0
eau=2
ail=2
pain=400
nbConvives=int(input("Entrez le nombre de personnes pour à la fondue : "))
fromage *=nbConvives / BASE
eau *=nbConvives / BASE
ail *=nbConvives / BASE
pain *=nbConvives / BASE
print(f"Pour faire une fondue fribourgeoise pour {nbConvives} personnes, il vous faut :")
print(f"- {fromage:.1f} gr de fromage")
print(f"- {eau:.1f} dl d'eau")
print(f"- {ail:.1f} gousse(s) d'ail")
print(f"- {pain:.1f} gr de pain")
