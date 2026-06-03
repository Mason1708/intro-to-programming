search_name = input("Enter a name to search for: ").strip().lower()

found_lines = []
line_number = 0

with open("names.txt", "r") as file:
    for line in file:
        line_number += 1
        name = line.strip().lower()

        if name == search_name:
            found_lines.append(line_number)

if len(found_lines) > 0:
    print(f"{search_name.title()} was found!")

    for line in found_lines:
        print(f"Found on line {line}")
else:
    print(f"{search_name.title()} was not found...")