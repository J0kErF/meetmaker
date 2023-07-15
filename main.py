#TIME_WINDOWS = [00:00,00:15,00:30,00:45,
#                01:00,01:15,01:30,01:45,
#                02:00,02:15,02:30,02:45,
#                03:00,03:15,03:30,03:45,
#                04:00,04:15,04:30,04:45,
#                05:00,05:15,05:30,05:45,
#                06:00,06:15,06:30,06:45,
#                07:00,07:15,07:30,07:45,
#                08:00,08:15,08:30,08:45,
#                09:00,09:15,09:30,09:45,
#                10:00,10:15,10:30,10:45,
#                11:00,11:15,11:30,11:45,
#                12:00,12:15,12:30,12:45,
#                13:00,13:15,13:30,13:45,
#                14:00,14:15,14:30,14:45,
#                15:00,15:15,15:30,15:45,
#                16:00,16:15,16:30,16:45,
#                17:00,17:15,17:30,17:45,
#                18:00,18:15,18:30,18:45,
#                19:00,19:15,19:30,19:45,
#                20:00,20:15,20:30,20:45,
#                21:00,21:15,21:30,21:45,
#                22:00,22:15,22:30,22:45,
#                23:00,23:15,23:30,23:45]
#                       24 X 4 = 96 
#   FOR EACH PERSON THERE IS AN ARRAY WITH LENGTH=96 
#   EACH CELL CONTAINS THE VALUE OR 0 OR 1
#   -> 0 PRESENTS THE FREE SLOTS
#   -> 1 PRESENTS THE TAKEN SLOTS
from person import Person


def freeWindows(persons):
    tmp = [persons[0].timesTable[i]&persons[1].timesTable[i] for i in range(96)]
    for p in persons:
        tmp = [tmp[i]&p.timesTable[i] for i in range(96)]
    return tmp

p1 = Person("mohammad")
p2 = Person("salah")
p3 = Person("swalha")

p1.setWorkingHours("08:00","16:00")
p2.setWorkingHours("09:00","17:00")
p3.setWorkingHours("10:15","17:00")

p1.addMeeting("08:15","10:00")
p1.addMeeting("10:15","11:00")
p1.addMeeting("11:00","11:45")
p1.addMeeting("11:45","12:00")
p1.addMeeting("12:15","13:00")

p2.addMeeting("09:15","10:00")
p2.addMeeting("10:15","11:00")
p2.addMeeting("11:00","11:45")
p2.addMeeting("11:45","12:15")
p2.addMeeting("13:45","16:00")

p3.addMeeting("09:15","10:00")
p3.addMeeting("10:15","11:00")
p3.addMeeting("11:00","11:45")
p3.addMeeting("11:45","12:15")
p3.addMeeting("13:45","16:00")
persons=[p1,p2,p3]
# lets say that we want to do a meeting between p1 and p2
# the concept is to do AND bitwise operation with the timestable for both of p1 and p2

tmp = freeWindows(persons)
freeWindow=""
for i in range (96):
    if tmp[i]==1 and freeWindow=="":
        freeWindow=i
    if tmp[i]==0 and freeWindow!="":
        print ("[",int(freeWindow/4),":",int((freeWindow%4)*15)," ---> ",int((i-1)/4),":",int(((i-1)%4)*15),"]")
        freeWindow=""
