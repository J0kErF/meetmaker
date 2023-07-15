class Person:
    def __init__(self,Name):
        self.timesTable = [0]*96
        self.name=Name
    def setWorkingHours(self,startH,endH):
        startM=int(startH[3]+""+startH[4])/15
        startH=int(startH[0]+""+startH[1])%24
        endM=int(endH[3]+""+endH[4])/15
        endH=int(endH[0]+""+endH[1])%24
        index=int(startH*4+startM)
        end=int(endH*4+endM)
        while index!=end:
            self.timesTable[index]=1
            index=index+1
            if index>=96:
                index=index%96
    def addMeeting(self,startH,endH):
        startM=int(startH[3]+""+startH[4])/15
        startH=int(startH[0]+""+startH[1])%24
        endM=int(endH[3]+""+endH[4])/15
        endH=int(endH[0]+""+endH[1])%24
        index=int(startH*4+startM)
        end=int(endH*4+endM)
        while index!=end:
            self.timesTable[index]=0
            index=index+1
            if index>=96:
                index=index%96
    def removeMeeting(self,startH,endH):
        startM=int(startH[3]+""+startH[4])/15
        startH=int(startH[0]+""+startH[1])%24
        endM=int(endH[3]+""+endH[4])/15
        endH=int(endH[0]+""+endH[1])%24
        index=int(startH*4+startM)
        end=int(endH*4+endM)
        while index!=end:
            self.timesTable[index]=1
            index=index+1
            if index>=96:
                index=index%96
    def resetTimeTable(self):
        self.timesTable=[0]*96
    def printTimeTable(self):
        freeWindow=""
        for i in range (96):
            if self.timesTable[i]==1 and freeWindow=="":
                freeWindow=i
            if self.timesTable[i]==0 and freeWindow!="":
                print ("[",int(freeWindow/4),":",int((freeWindow%4)*15)," ---> ",int((i-1)/4),":",int(((i-1)%4)*15),"]")
                freeWindow=""
                
            