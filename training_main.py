from Training import *
import time
Start_time = ['8:30','11:0','14:0']
End_time = ['10:30','13:0','17:0']
while(1):
    if(time.localtime().tm_hour == int(Start_time[0].split(":")[0]) and time.localtime().tm_min >= int(Start_time[0].split(":")[1])):
        main(End_time[0])
    elif(time.localtime().tm_hour == int(Start_time[1].split(":")[0]) and time.localtime().tm_min >= int(Start_time[1].split(":")[1])):
        main(End_time[1])
    elif(time.localtime().tm_hour == int(Start_time[2].split(":")[0]) and time.localtime().tm_min >= int(Start_time[2].split(":")[1])):
        main(End_time[2])
        break