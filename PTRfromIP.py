import socket
import time

def ip_range(start_ip,end_ip):
        start = list(map(int,start_ip.split('.')))
        end = list(map(int,end_ip.split('.')))
        iprange=[]
        while start!=list(map(int,end_ip.split('.'))):
            for i in range(len(start)-1,-1,-1):
                if start[i]<255:
                    start[i]+=1
                    break
                else:
                    start[i]=0
            iprange.append('.'.join(map(str,start)))
        return iprange


start1 = time.time()
for myip in ip_range("193.221.195.1","193.221.195.254"):
    try:   
        ptr = socket.gethostbyaddr(myip)[0]
        # print(myip+"  =PTR=  "+ptr)
    except Exception as e:
         print(f"No PTR found for {myip}")
end1 = time.time()

print("Time = "+ str(round(end1 - start1,5)))




