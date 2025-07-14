import socket

###def target():
    #trgt = input ("Enter IP or name: ")
    #print(f"Scanning: {trgt}")

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

            return result == 0

    except socket.timeout:
        return False
    except socket.error:
        return False
#target()

print(ScanPort("scanme.nmap.org", 80))
