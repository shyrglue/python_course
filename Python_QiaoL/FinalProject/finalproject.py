import random

ID=[] #existing ID

student_records = {} #existing student

def id_generator():
    for n in range(100001,1000000):
        if n not in ID:
            return n

def question_generator():
    operators=['+','-','*','/']
    while True:
        op=random.choice(operators)
        a=random.randint(0,99)
        b=random.randint(0,99)
        #make sure questions are valid
        if op=='+':
            if a+b>=0 and a+b<100:
                print(str(a)+op+str(b))
                return a+b
        elif op=='-':
            if a-b>=0 and a-b<100:
                print(str(a)+op+str(b))
                return a-b
        elif op=='*':
            if a*b>=0 and a*b<100:
                print(str(a)+op+str(b))
                return a*b
        else:
            if b!=0 and a%b==0 and a/b<100:
                print(str(a)+op+str(b))
                return a/b

def test(id,name):
    score=0
    print("TEST STARTS")
    for i in range(10):
        a=question_generator()
        ans=int(input())
        #compare the answer and give the score
        if ans==a:
            print("Correct!")
            score+=1
        else:
            print("Wrong!")
    return score

class STUDENT:
    def __init__(self,name,id):
        self.rec=[]
        self.ave=0
        self.name=name
        self.id=id
    def average(self):#calculate average score
        self.ave=round(sum(self.rec)/len(self.rec),2)

def load():
    try:
        with open("record.txt",'r') as file:
            file.readlines()
    except FileNotFoundError:
        print("There's no record. Creating a new file.")
        with open("record.txt","w") as file:
            file.close()
        #create a new file if not found
    with open("record.txt",'r') as file:
        text=file.readlines() 
    for t in text:
        record=t.strip().split(',')
        id=int(record[0])
        name=record[1]
        score=int(record[2])
        if name not in student_records.keys():
            student_records[name]=STUDENT(name,id)
            student_records[name].rec.append(score)
            ID.append(id)
        else:
            student_records[name].rec.append(score)
        #analyze existing data and load

def record(s):
    with open('record.txt','a') as file:
        file.write(str(s.id)+','+s.name+','+str(s.rec[-1])+'\n')
        #save the newest score

def query(ion):
    if ion in student_records.keys():#by name
        student_records[ion].average()
        print(','.join(str(s)for s in student_records[ion].rec))
        print("Average score: "+str(student_records[ion].ave))
        return
    else:
        #by id
        for s in student_records.values():
            if s.id==int(ion):
                print(','.join(str(p)for p in s.rec))
                s.average()
                print("Average score: "+str(s.ave))
                return

def rank():
    for s in student_records.values():
        s.average()
    rank=[]
    rank=sorted(student_records.values(),key=lambda n:(n.ave,999999-n.id),reverse=True)
    r=1
    for i in range(0,len(rank)):
        if rank[i-1].ave>rank[i].ave and i>0:
            r=i+1
        print(str(r)+' '+rank[i].name+' '+str(rank[i].id)+' '+str(rank[i].ave))

def main():
    load()
    while True:
        print("1. Start test")
        print("2. Check score")
        print("3. Check rank")
        print("4. Quit")
        c=input("Please choose:")
        if c=='1':
            name=input("Please enter your name: ")
            if name in student_records.keys():
                print("Welcome!")
            else:
                id=id_generator()
                ID.append(id)
                student_records[name]=STUDENT(name,id)
                print("Welcome!")
            student_records[name].rec.append(test(id,name))
            record(student_records[name])
        elif c=='2':
            query(input("Enter your ID or name: "))
        elif c=='3':
            rank()
        elif c=='4':
            break
        else:
            print("Invalid input, please try again!")

if __name__=="__main__":
    main()