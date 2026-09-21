# Tuples
spices_variety = ("Chilli", "Ginger", "Red Chilli")

(spice1, spice2, spice3) = spices_variety

print(f"The spices are mentioned : {spice1}, {spice2} and {spice3}")

chilli_ratio, ginger_ratio = 1 , 2

print(f" chilli ratio : ginger ratio = {chilli_ratio} : {ginger_ratio}")

chilli_ratio, ginger_ratio = ginger_ratio, chilli_ratio

print(f" chilli ratio : ginger ratio = {chilli_ratio} : {ginger_ratio}")

# Membership
print(f"Does ginger present in the spices_variety ? {'ginger' in spices_variety}")

print(f"Does Chilli present in the spices variety ? {'Chilli' in spices_variety}")