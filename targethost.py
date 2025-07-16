import socket

trgtlst = []

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
                return "This port is open!"
            else:
                return "This port is not open." 
     #exception handling   
    except socket.timeout:
        return "Connection Time out"
    except socket.error:
        return "Port Unreachable"

#function to run scanner and allow users to enter target machine and port

def portscanner():
#lists for storing input and cleaned input
    
    uIPlst = []
    tIPlst = []

#Prompt for input, clean and store in finalized list

    uIPlst.append(input("Enter IP (Seperate by Commas for multiples: "))

    for i in uIPlst[0].split(','):
        tIPlst.append(i.strip())

#Prompt for port number and scan
    
    for t in tIPlst:
        print("For", t, ScanPort(t, int(input("Enter Port Number: "))))

portscanner()
