import socket
import threading
import os
import shlex


HOST=''
IP=''
PORT=0
rfc_list=list()
rfc_title=list()
a=list()

class RFCRecord:
    def __init__(self,rfc_number=-1,rfc_title='None'):
        self.rfc_number=rfc_number
        self.rfc_title=rfc_title

    def __str__(self):
        return str(self.rfc_number)+' '+str(self.rfc_title)

    def getrfc_number(self):
        return self.rfc_number


def requestRFC(message,rfc_number,peer_name,peer_port,file_name):
    s=socket.socket()
    #peer_ip='127.0.0.1'
    peer_ip=peer_name
    s.connect((peer_ip,peer_port))
    print "clinet connected"
    s.send(message)
    reply=s.recv(1024)
    #s1='1'
    #s.send(s1)
    reply_list=shlex.split(reply)
    os.chdir(os.getcwd())
    file_name=file_name+".txt"
    #print str(file_name)
    if str(reply_list[1])=='200':
        #open the file here
        file1=open(file_name,'wb')
        while True:
            q=s.recv(1024)
            if q:
                #print q
                file1.write(q)
                break
            else:
                file1.close()
                break
    else:
        print "File Not Found"
    s.close()


def RetrRFC(name, sock):
    request=sock.recv(1024)
    print request
    rfc_number=shlex.split(request)
    file_found = 0
    for x in a:
        #print x
        t = x.split("-")
        if int(t[0])==int(rfc_number[2]):
            print t[0]
            file_found=1
            file_name=str(x)+".txt"

    if file_found==0:
        print "File not found"
        file_data="P2P-CI/1.0 404 FILE NOT FOuND"+"\n"
        sock.send(file_data)
    else:
        file_data="P2P-CI/1.0 200 OK"+"\n"
        sock.send(file_data)
        #with open("E:\ebooks\NCSU\ECE 573\Projects\p1\""+file_name,'rb') as f:
        with open(file_name,'r') as f:
            bytesToSend = f.read(1024)
            sock.send(bytesToSend)
            while bytesToSend != "":
                bytesToSend = f.read(1024)
                sock.send(bytesToSend)
    #filename=sock.recv(1024)
    #if os.path.isfile(filename):
        #sock.send("EXISTS" + str(os.path.getsize(filename)))
        #userResponse = sock.recv(1024)
        #if userResponse[:2]=='OK':
            #with open(filename,'rb') as f:
                #bytesToSend = f.read(1024)
                #sock.send(bytesToSend)
                #while bytesToSend != "":
                    #bytesToSend = f.read(1024)
                    #sock.send(bytesToSend)
    #else:
        #sock.send("ERR")
    sock.close()


def RetrRFC_initial():
    s=socket.socket()
    s.bind(('127.0.0.0',5000))
    s.listen()
    while True:
        c,addr = s.accept()
        print "Client connected ip: "+str(addr)
        t=threading.Thread(target=RetrRFC,args=("retrThread",c))
        t.start()
    s.close()
    

def initial_rfc_add():
    global a
    #print os.path.dirname(os.path.realpath(__file__))
    #print os.getcwd()
    #file_list = os.listdir("E:\ebooks\NCSU\ECE 573\Projects\p1")
    file_list = os.listdir(os.getcwd())
    temp_rfc = list()
    temp_title = list()
    for file_name in file_list:
        #print file_name
        files = file_name.split(".")
        if files[1] == "txt":
            w = str(files[0])
            a.append(w)
            files1 = w.split("-")
            temp_rfc.append(int(files1[0]))
            temp_title.append(files1[1])
    return temp_rfc,temp_title
    #for x in temp:
        #print x

def file_send(self):
    request=self.recv(1024)
    print request
    rfc_number=shlex.split(request)
    file_name=str(rfc_number[2])+".txt"
    for x in a:
        print x

    if str(rfc_number[2]) not in a:
        print "File not found"
        file_data="P2P-CI/1.0 404 FILE NOT FOuND"+"\n"
        self.send(file_data)
    else:
        data=subprocess.check_output(['date'])
        uname=subprocess.check_output(['uname'])
        t1=['ls','-lrt']
        t2=['grep','-w',file_name]
        t3=['tr','-s','" "']
        t4=['awk','{print $6,$7,$8}']
        t12=['ls','-lrt']
        t22=['grep','-w',file_name]
        t32=['tr','-s','" "']
        t42=['awk','{print $5}']
        p1=subprocess.Popen(t1,stdout=subprocess.PIPE)
        p2=subprocess.Popen(t2,stdin=p1.stdout,stdout=subprocess.PIPE)
        p3=subprocess.Popen(t3,stdin=p2.stdout,stdout=subprocess.PIPE)
        p4=subprocess.Popen(t4,stdin=p3.stdout,stdout=subprocess.PIPE)
        p3.stdout.close()
        lastupdate=p4.communicate()
        print lastupdate

        p12=subprocess.Popen(t12,stdout=subprocess.PIPE)
        p22=subprocess.Popen(t22,stdin=p12.stdout,stdout=subprocess.PIPE)
        p32=subprocess.Popen(t32,stdin=p22.stdout,stdout=subprocess.PIPE)
        p42=subprocess.Popen(t42,stdin=p32.stdout,stdout=subprocess.PIPE)
        p32.stdout.close()
        file_size=p42.communicate()
        print file_size

        f=open(file_name,'r')
        file_data="P2P-CI/1.0 200 OK"+"\n"+"Date: "+str(date)+"\n"+"OS: "+uname+"\n"+"Last-Modified: "+lastupddate[0]+"\n"+"Content-Length: "+str(file_size[0])+"\n"+"Content-Type: text/text"+"\n"
        self.send(file_data)

        stat=self.recv(1)

        while True:
            line=f.read(1024)
            self.send(line)
            if not len(line):
                break

        f.close()
    return 0       
    


def main():

    global HOST
    global PORT
    global IP

    print "Enter IP address of the host"
    IP=raw_input()
    print "Enter Host name"
    HOST=raw_input()
    #HOST=socket.gethostname()
    print "Enter Upload Port number"
    PORT=int(raw_input())
    #initial_rfc_add()
    try:
        thread_first = threading.Thread(target=client_as_server)
        thread_second = threading.Thread(target=option_list)
        thread_first.daemon=True
        thread_second.daemon=True
        thread_first.start()
        thread_second.start()

        thread_first.join()
        thread_second.join()

    except KeyboardInterrupt:
        sys.exit(0)


def client_as_server():

    cs_socket = socket.socket()
    cs_ip=IP
    cs_port=PORT
    cs_socket.bind((cs_ip,cs_port))
    # Here I will have to make changes according to other laptops
    cs_socket.listen(2)

    cs_thread = threading.current_thread()
    while(1):

        (peer_socket,peer_addr)=cs_socket.accept()
        print "Connected to", peer_addr
        thread_third=threading.Thread(target=RetrRFC,args=("retrThread",peer_socket))
        thread_third.start()
        thread_third.join()
    cs_socket.close()
    return


def option_list():
    temp_rfc=list()
    temp_title=list()
    print "Enter Host name of the Centralised Server"
    serverIP=raw_input()
    #serverIP='192.168.0.9'#socket.gethostbyname(raw_input())
    print "Enter Port number of the Centralised Server"
    serverPort=int(raw_input())
    message="REGISTER P2P-CI/1.0 Host: "+HOST+" Port: "+str(PORT)+"\n"
    client(message,serverIP,serverPort)
    temp_rfc, temp_title=initial_rfc_add()
    print temp_rfc
    for x in range(len(temp_rfc)):
        #print temp_rfc[x]
        message="ADD"+" "+str(temp_rfc[x])+" P2P-CI/1.0"+"\n"+" Host: "+HOST+"\n"+" Port: "+str(PORT)+"\n"+" Title: "+temp_title[x]
        client(message,serverIP,serverPort)
    #client("hello-server",serverIP,serverPort)
    while(1):
        print "Select from the List"
        #print "0. Register Host"
        print "1. List all RFC"
        print "2. Lookup RFC"
        print "3. Add RFC"
        print "4. Get RFC file"
        print "5. Exit"
        print "6. Remove a RFC"

        choice=int(raw_input())
        #if choice==0:
            #message="REGISTER P2P-CI/1.0 Host: "+HOST+" Port: "+str(PORT)+"\n"
            #client(message,serverIP,serverPort)

        if choice==1:
            message="LISTALL P2P-CI/1.0"+"\n"+"Host: "+HOST+"\n"+" Port: "+str(PORT)
            client(message,serverIP,serverPort)
            
        if choice==2:
            print "Enter RFC number"
            rfc_number = int(raw_input())
            print "Enter RFC title"
            rfc_title=raw_input()
            message="LOOKUP"+" "+str(rfc_number)+" P2P-CI/1.0"+"\n"+"Host: "+HOST+"\n"+"Port: "+str(PORT)+"\n"+"Title:"+rfc_title
            client(message,serverIP,serverPort)
        if choice==3:
            print "Enter RFC number"
            rfc_number=raw_input()
            print "Enter the title for the RFC"
            rfc_title=raw_input()
            a.insert(0,str(rfc_number))
            message="ADD"+" "+rfc_number+" P2P-CI/1.0"+"\n"+" Host: "+HOST+"\n"+" Port: "+str(PORT)+"\n"+" Title: "+rfc_title
            client(message,serverIP,serverPort)
                
        if choice==4:
            print "Enter RFC number"
            rfc_number=int(raw_input())
            print "Enter the title for the RFC"
            rfc_title=raw_input()
            print "Enter Peer Name"
            name_peer=raw_input()
            print "Enter Peer port number"
            port_peer=int(raw_input()) 
            message="GET RFC"+" "+str(rfc_number)+" "+"P2P-CI/1.0"+"\n"+"Host: "+name_peer+"\n"+"OS: Windows"
            file_name=str(rfc_number)+"-"+rfc_title
            requestRFC(message,rfc_number,name_peer,port_peer,file_name)

        if choice==5:
            message="EXIT P2P-CI/1.0 Host: "+HOST+" Port: "+str(PORT)
            client(message, serverIP, serverPort)

        if choice==6:
            print "Enter RFC number"
            rfc_number = int(raw_input())
            print "Enter RFC title"
            rfc_title = raw_input()
            str_file_name = str(rfc_number)+"-"+rfc_title+".txt"
            os.remove(str_file_name)
            message="REMOVE"+" "+str(rfc_number)+" P2P-CI/1.0"+"\n"+" Host: "+HOST+"\n"+" Port: "+str(PORT)+"\n"+" Title: "+rfc_title
            client(message, serverIP, serverPort)

    return            


def client(message, serverIP, serverPort):
    sock = socket.socket()
    sock.connect((serverIP,serverPort))
    sock.send(message)
    reply=sock.recv(16384)
    print "***********************************"
    print "Response received from Server:"
    print reply
    print "***********************************"
    sock.close()



if __name__=="__main__":
    main()
