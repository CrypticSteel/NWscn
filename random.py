UpLst = []
TpLst = []

UpLst.append(input("Enter Port: "))
#p.split(',').strip().append(pLst)
for prt in UpLst[0].split(','):
    TpLst.append(prt.strip())


print("Port(s)", TpLst)