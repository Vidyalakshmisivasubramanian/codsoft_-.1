def to_do_list(a):
    if a==1:
        global b,task,l,pent,com
        b=int(input('Enter Number of Task: '))
        for i in range(b):
            task=input("Task "+str(i+1)+" : ")
            l.append(task)
            pent.append(task)
    if a==2:
        for i in range(b):
            print("task ",i+1,l[i])
        for i in range(b):
            ques=input("Have you completed Task "+str(i+1)+"(yes or no): ")
            if ques.lower()=="yes":
                m=l[i]
                if m in pent:
                    pent.remove(m)
                com.append(m)
            else:
                pass
        print('Completed:',com,'\nPending:',pent)
        #add or delete..
    if a==3:
        ad=input("Have you want modify ?(add or delete): ")
        if ad=="add":
            v=input("Enter the Task:")
            l.append(v)
            pent.append(v)
            print('Task Added Sucessfully..!')
        elif ad=="delete":
            for i in range(len(l)):
                print("Task ",i+1,l[i])
            s=int(input("Enter the task you want to delete: "))
            q=l[s-1]
            if q in l and q in pent:
                pent.remove(q)
                l.remove(q)
                print('Task Deleted Sucessfully..!')
        else:
            pass
                    

l=[]
com=[]
pent=[]
while True:
    print("\n\t\tTO DO LIST")
    print("MENU:")
    print("1)ADD TASK\n2)TRACK  TASK\n3)MODIFY TASK")
    a=int(input('Enter your choice: '))
    to_do_list(a)

    
