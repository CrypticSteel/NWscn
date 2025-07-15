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
        
    except socket.timeout:
        return "Connection Time out"
    except socket.error:
        return "Port Unreachable"
#create function to allow users to enter target and IP

def portscanner():
    print(ScanPort(input("Enter Target: "), int(input("Enter Port: "))))

portscanner()
