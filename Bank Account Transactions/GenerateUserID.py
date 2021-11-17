def Unique_id():
    Max_id = 0
    with open("User_Ids.txt", "r") as file:
        for line in file:
            for index, element in enumerate(line[7:15]):
                temp = []
                if int(element) !=0:
                    for number in line[7+index:15]:
                        temp.append(number)

                    Num = int("".join(temp))
                    if Num > Max_id:
                        Max_id = Num

        New_id = Max_id + 1
        Num_len = len(str(New_id))
        zeros_list = ['0' for i in range(8 - Num_len)]
        zeros = "".join(zeros_list)

        return f"Userid_{zeros}{New_id}"

def Add_Entry(UserId, Requisition_Id = "8126e9fb-93c9-4228-937c-68f0383c2df7"):
    with open("User_Ids.txt", "a") as file:
        file.write(f"\n{UserId} {Requisition_Id}")

UserId = Unique_id()
print(UserId)
Add_Entry(UserId)








