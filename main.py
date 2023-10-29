with open("Input/Letters/message.txt") as file:
    words = file.read()

with open("Input/Names/names.txt") as names:
    guests = names.read().split("\n")
    for name in guests:
        new_name = name + ","
        replaced = words.replace("[name],", new_name)
        with open(
            f"./Output/ReadyToSend/Message_to_{name}.txt", mode="w"
        ) as working_file:
            working_file.write(replaced)
