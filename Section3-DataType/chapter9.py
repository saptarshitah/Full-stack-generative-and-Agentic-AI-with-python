ingrdients = ["water", "milk", "black tea"]

ingrdients.append("suger")

print(f"Ingredience : {ingrdients}")

ingrdients.remove("water")

print(f"Ingrdince : {ingrdients}")

chai_ingredients = ["water", "black tea"]
spice_ingredients = ["ginger", "suger"]

chai_ingredients.extend(spice_ingredients)  # marge list
print(f"get all ingredients : {chai_ingredients}")

chai_ingredients.insert(1, "milk")
print(f"get all ingredients : {chai_ingredients}")

last_ingredient = chai_ingredients.pop()    # delete last element from list
print(f"Last element : {last_ingredient}")
print(f"All elements : {chai_ingredients}")

chai_ingredients.reverse()
print(f"All reverse elements : {chai_ingredients}")

chai_ingredients.sort()
print(f"Shorted list : {chai_ingredients}")

print(f"max element in list : {max(chai_ingredients)}")
print(f"min element in the list : {min(chai_ingredients)}")