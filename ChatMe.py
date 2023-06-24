from Chat import TaskExe
print("Welcome to chat me.")
print("")
while True:
    print("")
    data = input("Chat with me : ")
    data1 = TaskExe(data)
    query = str(data1).lower()