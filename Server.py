### Server Script ###

import os
import time
import socket
from datetime import datetime
now = datetime.now()
dt = now.strftime("%m_%d_%Y_%H_%M_%S")

def decrypt(input):
    a = input.split("l")
    lista = []
    listb = []
    listc = []
    decrypt_key = str(a[0])
    decrypt_msg = str(a[-1])
    for elem in str(a[0]):
        lista.append(elem)
    for elemx in str(a[-1]):
        listb.append(elemx)
    num_adda = "".join(lista[10:13])
    num_multiplya = "".join(lista[13:24])
    a.remove(decrypt_key)
    a.remove(decrypt_msg)
    count = 0
    for elemy in a:
        x = "".join(listb[count:(count+int(elemy))])
        y = int(int(x)/int(num_multiplya))
        z = y - int(num_adda)
        listc.append(chr(z))
        count += int(elemy)
    finaloutput = "".join(listc)
    return finaloutput

def file_decrypt(x):
    a = open(x, 'r')
    lista = []
    for line in a.read():
        lista.append(line)
    a.close()
    encrypted_string = str("".join(lista))
    decrypted_string = decrypt(encrypted_string)
    ab = open(x, "w")
    ab.write(decrypted_string)
    ab.close()

def word_count(x): #gives a list of words and their occurances in all the txt reports with 'space X space' as their first entry in a directory
    wordcount = []
    for xddd in os.listdir("C:\\"+str(x)+"\\"):
        z = open("C:\\"+str(x)+"\\"+xddd, "r")
        p = z.read()
        plist = p.split(" ")
        if plist[0] == 'X':
            for elem in plist[6:-6]:
                wordcount.append([elem,1])
    finalwordcount = []
    for elemx in wordcount:
        if wordcount.count(elemx) > 1:
            wordcountt = 0
            for elemxy in finalwordcount:
                if [elemx[0],wordcount.count(elemx)] == elemxy:
                    wordcountt += 1
            if wordcountt == 0:
                finalwordcount.append([elemx[0],wordcount.count(elemx)])
    return finalwordcount

while True:
    try:
        print("starting sending command protocol")
        s = socket.socket()
        host = socket.gethostname()
        port = 8080
        s.bind((host, port))
        s.listen(1)
        conn, addr = s.accept()
        commands_file = open("C:\\programsummarize\\insert_commands\\command.txt", "r")
        command_read = commands_file.read()
        commands_file.close()
        filesizevariablexy = os.path.getsize("C:\\programsummarize\\insert_commands\\command.txt")
        msg = "}" + str(filesizevariablexy) + "}" + str(command_read)
        conn.send(bytes(msg, "utf-8"))
        conn.close()
        print("command sent")
        zzz = open("C:\\programsummarize\\insert_commands\\command.txt", "w")
        zzz.write("none")
        zzz.close()
        print("file rewritten")
    except:
        print("error in sending commands")
    try:
        print("beginnning listening")
        s = socket.socket()
        host = socket.gethostname()
        port = 8080
        s.bind((host, port))
        s.listen(1)
        conn, addr = s.accept()
        print("connected")
        lengthofmessage = 0
        count = 0
        connectioncount = 0
        full_msg = ""
        listadress = ""
        for elementadress in addr:
            listadress += str(elementadress)
        filename = "C:\\programreports\\" + listadress + "__" + dt + ".txt"
        print("address determined")
        print("beginning reception of files from the client")
        while True:
            print("loop1")
            msg = conn.recv(1024).decode("utf-8")
            if count == 0:
                msglen = str(msg).split("}")
                lengthofmessage = int(msglen[1])
                full_msg += str(msglen[2])
            if lengthofmessage > connectioncount and count > 0:
                full_msg += msg
            elif lengthofmessage < connectioncount:
                fulllistmsg = full_msg.split("}")
                file = open(filename, 'w')
                file.write(str(fulllistmsg[0]))
                file.close()
                print("file successfully written")
                break
            count += 1
            connectioncount += 20
        for elemxyy in os.listdir("C:\\programreports\\"):
            try:
                file_decrypt("C:\\programreports\\" + elemxyy)
            except:
                "done"
        try:
            print("begin wordcount")
            wordcountdoc = open("C:\\programsummarize\\report.txt", "w")
            wordcountdoc.write(str(word_count('programreports')))
            wordcountdoc.close()
        except:
            print("error in wordcount")
    except:
        print("error")
    time.sleep(1)

