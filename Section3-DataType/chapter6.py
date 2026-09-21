# String
full_word = "Amazing and fantistic"

print(f"First character : {full_word[0]}")
print(f"First word : {full_word[:7]}")
print(f"Last word : {full_word[12:]}")

label_text = "Tea spécial"
label_text_encoded = label_text.encode("utf-8")

print(f"Without encode : {label_text}")
print(f"With encode : {label_text_encoded}")

lebel_text_decode = label_text_encoded.decode("utf-8")

print(f"With decode : {lebel_text_decode}")