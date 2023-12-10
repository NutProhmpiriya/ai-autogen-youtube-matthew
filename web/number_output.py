# filename: number_output.py

with open("desired_filename.py", "w") as file:
    for i in range(1, 101):
        file.write(str(i) + "\n")