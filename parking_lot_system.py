import sys
class parking:
        
    def __init__(self, v_id, v_type):
        self.v_id= v_id
        self.v_type= v_type

class p_allot:
    def __init__(self, v_id, v_type, p_id):
        if(p_id == -1):
            self.p_id="Could not allocate parking space" 
        else:
            self.p_id=str(p_id)

        self.v_id= v_id
        self.v_type= v_type
        
    

p_space={}
for i in range (0,21):
    p_space[i]=0;

while(1):
    
    v_name= input("Enter your vehicle type (Bus/Car/MotorCycle):")
    v_id= input("Enter your vehicle ID:")
    p= parking(v_id, v_name)
    i=0  
    if p.v_type=="MotorCycle":
        for i in range(1,21):
            if(p_space[i]==0):
                p_space[i]=p.v_id
                break
            else:
                i=-1
    if p.v_type=="Car":
        for i in range(11,18):
            if(p_space[i]==0):
                p_space[i]=p.v_id
                break
            else:
                i=-1
    if p.v_type=="Bus":
        for i in range(18,21):
            if(p_space[i]==0):
                p_space[i]=p.v_id
                break
            else:
                i=-1
    if p.v_type!="Bus" and p.v_type!="Car" and p.v_type!="MotorCycle":
        print(" Please enter the type of vehicle")
        sys.exit(1)
           
    pa= p_allot(v_id, v_name, i) 
    print("\n*********************")
    if(pa.p_id == -1):
        print(pa.v_id +"\n"+ pa.v_type+ "\n"+ " ")
    else:
        print(pa.v_id +"\n"+ pa.v_type+ "\n" + pa.p_id)
    print("*********************\n")
    a=input("\n Would you like to park? (Y/N):")
    if (a =='Y'):
        continue
    else:
        break
