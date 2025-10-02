
def doing_json_creates():
    while True:
        creating_writing_or_reading = input("Write(w) Create(c) or Read(r): ")
        if creating_writing_or_reading == "c":
            users_file_name = input("Give your file a name: ")
            users_file_name_in_a_file = open(users_file_name + ".json" , "x")
            continue_or_no = input("Continue(yes) or no(no)?: ")
            if continue_or_no == "no":
                break
            # with open (users_file_name, "x") as users_file_name:

        if creating_writing_or_reading == "r":
            finding = input("Put in the key you want")
            with open(users_file_name_in_a_file, "r") as users_file_name_in_a_file:
                finding_the_word = users_file_name_in_a_file.find(finding)
                if finding_the_word == finding:
                    print(f"Found your inputted word: {finding}")
                    continue_or_no = input("Continue(yes) or no(no)?: ")
                    if continue_or_no == "no":
                        break
                else:
                    print("word not found")
                    continue_or_no = input("Continue(yes) or no(no)?: ")
                    if continue_or_no == "no":
                        break


        if creating_writing_or_reading == "w":
            user_input = input("What file do you want to add to?: ")
            if user_input == users_file_name_in_a_file:
                with open(users_file_name_in_a_file, "w") as users_file_name_in_a_file:
                    users_file_name_in_a_file.write(user_input)
                    continue_or_no = input("Continue(yes) or no(no)?: ")
                    if continue_or_no == "no":
                        break
            else:
                print("File not found")
                break

doing_json_creates()