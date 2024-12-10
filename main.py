import sys

def progress_bar(progress, total, bar_length=50):   #Displays a progress bar
    fraction = progress / total
    filled_length = int(bar_length * fraction)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    percent = fraction * 100
    sys.stdout.write(f'\r|{bar}| {percent:.2f}% Complete')
    sys.stdout.flush()
    if progress == total:
        print()  # Move to the next line when complete.


print("NOTE: Enter comma separated values  as input!!")
print("DOB format: XX-XX-XXXX (11-12-2006)!\n")
try:
    x = input("ENTER name,age,D.O.B :").split(",")
except:
    print("Error: Enter the input in correct format!")
x[0] = x[0].capitalize()
x.append(x[0].upper())
x.append(x[0].lower())
x.append(x[0].swapcase())


# Convert DOB to a list of integers
try:
    dob = [int(i) for i in x[2].split("-")]
    x.pop(2)
except:
    print("Values in D.O.B should be separated by '-'")


lst1 = []        #List with all combinations
for i in range(27):    #DOB combos
    a = i % 3
    b = (i + 1) % 3
    c = (i + 2) % 3
    local_list = [f"{dob[a]}{dob[b]}{dob[c]}"]
    lst1.append(int((local_list)[0]))

lst1.append(x[1]) #AGE


#Special chrs
special_chars = [
    '@', '!', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '=', '+', 
    '{', '}', '[', ']', '|', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/'
]

#FILE HANDLING

try:
    with open("numerical.txt","r+") as file:
        data = file.read()
        list_local = (data.split("\n"))
        lst1.extend(list_local[:len(list_local)-1])
        file.close()

  
    total_combinations = len(x) * len(special_chars) * len(lst1)
    progress_update_interval = total_combinations // 20  # Update progress 20 times

    all_passwords = []  # Store all passwords in array
    progress = 0
    
    print(f"\nTotal key combinations: {total_combinations:,}")
    print("Generating keys:--->")
    for i in x:
        for j in special_chars:
            for k in lst1:
                passkey = f"{i}{j}{k}\n"
                if len(passkey) > 6:
                    all_passwords.append(passkey)
                progress += 1
                # Update progress bar occasionally
                if progress % progress_update_interval == 0 or progress == total_combinations:
                    progress_bar(progress, total_combinations)
    
     # Write all passwords at once to minimize I/O
    print("WRITING KEYS PLEASE WAIT!!")
    with open("pass.txt", "w") as f:
        f.writelines(all_passwords)
    print("KEYS STORED in pass.txt!!!")
except Exception as e:
    print(f'ERROR:{e}')
