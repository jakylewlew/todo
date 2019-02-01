'''
Created on Jan 31, 2019
 
@author: jlewis
'''
import os

todo_file = open("tasklist.txt", "r+")
 
todolist = todo_file.readlines()
try:
    todolist = todolist[0].split(',')
except(IndexError):        
    print("")
print(todolist)
todolist.pop(len(todolist)-1)
i = 0
while(i != len(todolist)-3):
    module_task = []
    module_task.append(todolist[i])
    module_task.append(todolist[i+1])
    module_task.append(todolist[i+2])
    todolist.append(module_task)
    i = i + 3  
#     todo_file.close()
# except (FileNotFoundError, IndexError):
#     print("makefile")   
#     todo_file = open("tasklist.txt", "w+")   
#     todolist = []

todo_file.close()


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
    module = (3 * selection)+2
    todolist[module] = 0
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
    for module in todolist:
        print(str(i)+ " " +str(module))  
        i = i + 1  
    inp = input("item number")
    print(todolist[inp][0])
    inp = input("Y/N")
    if inp == "Y":
        inp = input("Task")
        todolist[inp][0] = inp
    print(todolist[inp][1])
    inp = input("Y/N")
    if inp == "Y":
        inp = input("date")
        todolist[inp][1] = inp      
    write_file()  
def write_file():
    todo_file = open("tasklist.txt", 'w+')
    for item in todolist:
        for obj in item:
            todo_file.write(str(obj)+',')
            print(obj)
    todo_file.close()
inp = 0
while inp != 'q': 
    os.system("clear") 
    refresh()  
    print("new item:  1")
    print("check off: 2")
    print("refresh:   3")
    print("delete:    4")
    print("Edit :     5")
    inp = input("")
    if inp == '1':
        new_task()
    if inp == '2':
        
        mark_task_done(inp)
    if inp == '3':
        refresh()
    if inp == '4':
        delete_task()
    if inp == '5':
        edit_task()


