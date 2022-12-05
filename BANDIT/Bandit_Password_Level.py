#!/usr/bin/python3
# SITIO WEB: https://overthewire.org/wargames/bandit/bandit0.html
# Autor: Cyb3r4l3
# Colaborador: Kek1us
# Fecha: 13/11/2022


import os
import paramiko
import string


# DIRECCION
host = "bandit.labs.overthewire.org"
port = "2220"


# SESION SSH
client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.client.WarningPolicy())
time_ssh = 100


# CREAR CARPETA, COMPROBAR CARPETA
if os.path.isdir("/tmp/Bandit"):
    os.system("rm -rf /tmp/Bandit")
    path = "/tmp/Bandit"
    os.system("mkdir -p " + path)
    os.chdir(path)
else:
    path = "/tmp/Bandit"
    os.system("mkdir -p " + path)
    os.chdir(path)
    

# FICHEROS
file_flag = "flag.txt"
flag = open(file_flag, 'w')


# FLAG LEVEL
name_pass = "Pass Level "


def banner():

    print ("\x1b[0;32m"+"      ______   ___   _   _ ______  _____  _____ ")
    print ("      | ___ \ / _ \ | \ | ||  _  \|_   _||_   _|")
    print ("      | |_/ // /_\ \|  \| || | | |  | |    | |")
    print ("      | ___ \|  _  || . ` || | | |  | |    | |")
    print ("      | |_/ /| | | || |\  || |/ /  _| |_   | |")
    print ("      \____/ \_| |_/\_| \_/|___/   \___/   \_/")
    print ("\x1b[1;33m"+"\n            ### PASSWORD LEVEL BANDIT ###       \n"+"\x1b[0;37m")


def flag_level():
    # Abrir y modificar archivo con contraseñas, leer ultima contraseña, devolver contraseña.
    flag = open(file_flag , 'r+')
    readflag = flag.readlines()
    readflag = readflag[-1]
    readflag = readflag.strip('\n')
    return readflag


def Bandit_level(level : str, user : str, password : str, command : str):

    flag = open(file_flag , 'r+')

    if not password:
        readflag = flag_level()
    else:
        readflag = password
    
    try:
        client.connect(host, port, username=user, password=readflag, timeout=time_ssh)
    except Exception as e:
        print(e)

    stdin, stdout, stderr = client.exec_command(command)

    for line in stdout:
        print("\x1b[1;37m"+"#---------------------------------------------------#"+"\x1b[0;37m")
        if int(level) < 10:
            print("| " + name_pass + level + ": " + line.strip("\n") + "    |")
        else:
            print("| " + name_pass + level + ": " + line.strip("\n") + "   |")
        flag.write(line) 
     
    client.close()


def bandit_12(level : str, user : str, password : str, command : str):

    # Decompress subido a github, solo descargar y ejecutar
    # TODO: Intentar mejorar y automatizar
  
    os.system(command)

    readflag = flag_level()
    
    print("\x1b[1;37m"+"#---------------------------------------------------#"+"\x1b[0;37m")
    print("| " + name_pass + level + ": " + readflag.strip("\n") + "   |")


def bandit_13(level : str, user : str, password : str, command : str):

    # TODO: Intentar mejorar y autmatizar

    os.system(command)
    
    readflag = flag_level()
    
    print("\x1b[1;37m"+"#---------------------------------------------------#"+"\x1b[0;37m")
    print("| " + name_pass + level + ": " + readflag.strip("\n") + "   |")


def bandit_14(level : str, user : str, password : str, command : str):

    # TODO: Intentar mejorar y automatizar

    os.system(command)
    
    readflag = flag_level()

    print("\x1b[1;37m"+"#---------------------------------------------------#"+"\x1b[0;37m")
    print("| " + name_pass + level + ": " + readflag.strip("\n") + "   |")


def bandit_16(level : str, user : str, password : str, command : str):
    
    os.system(command)

    readflag = flag_level()

    print("\x1b[1;37m"+"#---------------------------------------------------#"+"\x1b[0;37m")
    print("| " + name_pass + level + ": " + readflag.strip("\n") + "   |")


def bandit_18(level : str, user : str, password : str, command : str):
    os.system(command)

    readflag = flag_level()

    print("\x1b[1;37m"+"#---------------------------------------------------#"+"\x1b[0;37m")
    print("| " + name_pass + level + ": " + readflag.strip("\n") + "   |")


if __name__ == '__main__':
    
    banner()
    #USE = BANDIT("LEVEL", "USER", "", "COMMAND")
    # TODO: Agregar COMMAND_LOCAL, para optimizar
    Bandit_level("0", "bandit0", "bandit0", "cat readme")
    Bandit_level("1", "bandit1", "", "cat $(pwd)/-")
    Bandit_level("2", "bandit2", "", "cat spaces\ in\ this\ filename")
    Bandit_level("3", "bandit3", "", "cat inhere/.hidden")
    Bandit_level("4", "bandit4", "", "cat inhere/-file07")
    Bandit_level("5", "bandit5", "", "cat inhere/maybehere07/.file2 | tr -d ' '")
    Bandit_level("6", "bandit6", "", "cat /var/lib/dpkg/info/bandit7.password")
    Bandit_level("7", "bandit7", "", "grep \"millionth\" data.txt | awk '{print $NF}'")
    Bandit_level("8", "bandit8", "", "sort data.txt | uniq -u")
    Bandit_level("9", "bandit9", "", "strings data.txt | grep \"===\" | tail -n1 | awk '{print $NF}'")
    Bandit_level("10", "bandit10", "", "cat data.txt | base64 -d | awk '{print $NF}'")
    Bandit_level("11", "bandit11", "", "cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m' | awk '{print $NF}'")
    # TODO: Modificar "bandit" para optimizar los niveles "especiales" o Intentar ajustarlo a "Bandit_level"
    bandit_12("12", "bandit12", "", "sshpass -p JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv scp -q -P 2220 bandit12@bandit.labs.overthewire.org:data.txt /tmp/Bandit/ && wget -q https://raw.githubusercontent.com/ARMoreno99/OverTheWire/main/BANDIT/scripts/decompress.sh  && /bin/bash decompress.sh data.txt >>" + file_flag) 
    bandit_13("13", "bandit13", "", "sshpass -p wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw ssh -q bandit13@bandit.labs.overthewire.org -oStrictHostKeyChecking=no -p2220 ssh -q -i sshkey.private bandit14@localhost -oStrictHostKeyChecking=no -p2220 cat /etc/bandit_pass/bandit14 >> " + file_flag) 
    bandit_14("14", "bandit14", "", "sshpass -p fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq ssh -q bandit14@bandit.labs.overthewire.org -p2220 \"echo fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq | nc localhost 30000 | tail -n2 | head -n1 \">> " + file_flag) 
    Bandit_level("15", "bandit15", "", "echo jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt | openssl s_client -quiet -connect localhost:30001 2>/dev/null | grep -v Correct! | tr -d '\n'")
    bandit_16("16", "bandit16", "", "sshpass -p JQttfApK4SeyHwDlI9SXGR50qclOAil1 ssh -q bandit16@bandit.labs.overthewire.org -p2220 'cat /etc/bandit_pass/bandit16 | openssl s_client -connect localhost:31790 -quiet 2>/dev/null | grep -v Correct!' > id_key && chmod 400 id_key && ssh -q -i id_key bandit17@bandit.labs.overthewire.org -p 2220 'cat /etc/bandit_pass/bandit17' >> " + file_flag)
    Bandit_level("17", "bandit17", "", "diff passwords.new  passwords.old | head -n2 | tail -n1 | awk '{print $NF}'")
    bandit_18("18", "bandit18", "", "sshpass -p hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg ssh -q bandit18@bandit.labs.overthewire.org -p2220 cat readme >> " + file_flag)
    Bandit_level("19", "bandit19", "", "./bandit20-do cat /etc/bandit_pass/bandit20")

    print("\x1b[1;37m"+"#---------------------------------------------------#"+"\x1b[0;37m")
    
    flag.close()
