# This looks through the User_Ids list and check to see if a user exists starting from 0, if it does, it increments the
# id until it finds one that does not exist and then assigns a new id. It then returns the new id as a string.
def unique_id(max_id=0):
    max_id = max_id
    with open("User_Ids.txt", "r") as file:
        for line in file:
            for index, element in enumerate(line[7:15]):
                temp = []
                if int(element) != 0:
                    for number in line[7+index:15]:
                        temp.append(number)

                    num = int("".join(temp))
                    if num > max_id:
                        max_id = num

        new_id = max_id + 1
        num_len = len(str(new_id))
        zeros_list = ['0' for i in range(8 - num_len)]
        zeros = "".join(zeros_list)
        # !CHANGE! f-string to "Userid" WHEN IN PRODUCTION, USING "Testid" IN DEVELOPMENT
        return f"Testid_{zeros}{new_id}"


# This function takes user id and a requisition id and writes them to a file "User_Ids.txt" in a specific format.
def add_entry(userid, requisition_id = "8126e9fb-93c9-4228-937c-68f0383c2df7"):
    with open("User_Ids.txt", "a") as file:
        file.write(f"{userid} {requisition_id}\n")








