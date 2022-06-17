fil = open("texting",'r')

newfil = open("newtexting","w")
for data in fil:
    newfil.write(data)