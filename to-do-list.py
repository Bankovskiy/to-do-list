to_do_list = {}

repeat = True

while repeat:
    to_do = input("What do you want to add to your to-do list?: ")
    time = input("And when? (hh:mm): ")
    
    if to_do and time:
        to_do_list[to_do] = time
    else:
        print("Please provide the task AND the time")
        
    user_input = input("Do you want to add more to your to-do-list? (y/n): ")
    if user_input.lower() == "y":
        repeat = True
    elif user_input.lower() == "n":
        repeat = False
    else:
        print("Error, wrong value")
        repeat = False
    
print("Here's your to-do-list:")
for task, time in to_do_list.items():
    print(f"{task} in {time}")