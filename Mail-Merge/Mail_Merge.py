

with open("Mail_Merge_Data.txt", mode="r") as file:
    contents = file.readlines()

for name in contents:
    strip_name = name.strip()
    with open(f"{strip_name}.txt", mode="w" ) as completed_letter:
        completed_letter.write(f"\nDear {strip_name},\nYou are invited to my birthday this Saturday.\nHope you can make it!\nCasey")