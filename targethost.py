import socket

def ScanPort(target, port):
    
    try:
        #creating socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        #set a timeout
            s.settimeout(1.0)

        #Try connecting - returns 0 if successful
            result = s.connect_ex((target, port))

        #Clean Shutdown
            s.shutdown(socket.SHUT_RDWR)

            if result == 0:
                return "Open!"
            else:
                return "Closed." 
     #exception handling   
    except socket.timeout:
        return "Connection Time out"
    except socket.error:
        return "Unreachable"

#function to run scanner and allow users to enter target machine and port

def portscanner():
#lists for storing input and cleaned input
    
    uIPlst = []
    tIPlst = []
    uPrlst = []
    tPrlst = []

#Prompt for input, clean and store in finalized lists

    uIPlst.append(input("Enter IP (Seperate by Commas for multiples): "))

    for i in uIPlst[0].split(','):
        tIPlst.append(i.strip())

    uPrlst.append(input("Enter Port(seperate by Commas for multiples): "))

    for p in uPrlst[0].split(','):
        tPrlst.append(p.strip())

    for ip in tIPlst:
        print("results for", ip + ":")
        
        for prt in tPrlst:
            print(" Port:", prt,"--->",ScanPort(ip,int(prt)))

#Prompt for port number and scan
    
    #for t in tIPlst:
        #print("For", t, ScanPort(t, int(input("Enter Port Number: "))))

portscanner()
