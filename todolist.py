
import os


todo_file = open("tasklist.txt", "r+") 
read_list = todo_file.readlines()
try:
    read_list = read_list[0].split(',')
except(IndexError):          
    print("")

read_list.pop(len(read_list)-1)
todolist = []
i = 0
while(i != len(read_list)):
    module_task = []
    module_task.append(read_list[i])
    module_task.append(read_list[i+1])
    module_task.append(read_list[i+2])
    todolist.append(module_task)
    i = i + 3  
#     todo_file.close()
# except (FileNotFoundError, IndexError):
#     print("makefile")   
#     todo_file = open("tasklist.txt", "w+")   
#     todolist = []

todo_file.close()
print(todolist)


def new_task():
    module_task = []
    inp = input("task?")
    module_task.append("Task: " + inp) 
    inp = input("date 00.00.00")
    module_task.append("duedate " + inp)
    module_task.append(2)
    todolist.append(module_task)
    write_file()
def mark_task_done():
    refresh()
    selection = input("Select")
    module = todolist[int(selection)]
    module[2] = 0
    write_file()
def refresh():
    i = 0
    for item in todolist:
        print(str(i)+str(item))
        i = i + 1

def delete_task():
    i = 0
    for module in todolist:
        print(str(i)+" "+str(module))  
        i = i + 1      
    inp = input("item number")
    todolist.pop(int(inp))
    write_file() 
    
def edit_task():
    i = 0
    for module in todolist: #ADDS THE INDEX OF THE ARRAY TO THE BEGINNING
        print(str(i)+ " " +str(module))  
        i = i + 1  
    inp = int(input("item number"))
    item = (todolist[inp])
    
    print(str(item) + " : Selected....")
    print(item[0]+ " : Change Task?")
    inp = input("Y/N")
    if inp == "Y":
        inp = input("Task")
        item[0] = "Task: " + inp
    print(item[1]+" : Change Date?")
    inp = input("Y/N")
    if inp == "Y":
        inp = input("Date?")
        item[1] = "duedate " + inp      
    write_file()  
def write_file():
    todo_file = open("tasklist.txt", 'w+')
    for item in todolist:
        for obj in item:
            todo_file.write(str(obj)+',')
            print(obj)
    todo_file.close()
def print_pretty():
    for item in todolist:
        print('{0:30s} : {1:10s} : {2:3}'.format(item[0], item[1], item[2]))
inp = 0
while inp != 'q': 
    os.system("clear") 
#     refresh() 
    print_pretty() 
    print("new item:  1")
    print("check off: 2")
    print("refresh:   3")
    print("delete:    4")
    print("Edit :     5") 
    inp = input("")
    if inp == '1':
        new_task()
    if inp == '2':
        
        mark_task_done()
    if inp == '3':
        refresh()
    if inp == '4':
        delete_task()
    if inp == '5':
        edit_task()


