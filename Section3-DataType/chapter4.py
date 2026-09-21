#boolean
is_boiling = True
stri_count = 5
total_actions = is_boiling + stri_count # upcasting
print(f"Total actions : {total_actions}")

have_milk = None
print(f"have milk : {bool(have_milk)}")

water_hot = True;
tea_added = False;

can_serve_tea = water_hot and tea_added
print(f"can serve tea : {can_serve_tea}")