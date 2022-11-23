#!/usr/bin/python3
# SITIO WEB: https://overthewire.org/wargames/bandit/bandit0.html
# Autor: Cyb3r4l3
# Colaborador: Kek1us
# Fecha: 13/11/2022

import os
import paramiko
import string
from subprocess import call
import os

# DIRECCION
host = "bandit.labs.overthewire.org"
port = "2220"

# SESION SSH
client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.client.WarningPolicy())
time_ssh = 100

# CREAR CARPETA
path = "/tmp/Bandit"
os.system("mkdir -p " + path)
os.chdir(path)

# FICHEROS
file_flag = "file_flag"
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

#def flag_level():
#
#    readflag = flag.readlines()
#    readflag = readflag[-1]
#    readflag = readflag.strip('\n')

def BANDIT(level : str, user : str, password : str, command : str):

        flag = open(file_flag , 'r+')

        if not password:
            
            # TODO: Preguntar a Kek1us; crear una funcion para lectura de la flag para leer dentro de una funcion.

            ################################
            readflag = flag.readlines()
            readflag = readflag[-1]
            readflag = readflag.strip('\n')
            ################################

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


def bandit_12(level : str, user : str, password : str):

    # Decompress subido a github, solo descargar y ejecutar
    # TODO: Intentar mejorar y automatizar

    cmd = "sshpass -p " + password + " scp -q -P " + port + " " + user + "@" + host + ":data.txt " + path
    call(cmd.split(" "))
    
    os.system("wget -q https://raw.githubusercontent.com/ARMoreno99/OverTheWire/main/BANDIT/scripts/decompress.sh  && chmod +x decompress.sh")
    os.system("/bin/bash decompress.sh data.txt >> " + file_flag)

    ################################
    flag = open(file_flag , 'r+')
    readflag = flag.readlines()
    readflag = readflag[-1]
    readflag = readflag.strip('\n')
    ################################
    
    print("\x1b[1;37m"+"#---------------------------------------------------#"+"\x1b[0;37m")
    print("| " + name_pass + level + ": " + readflag.strip("\n") + "   |")


def bandit_13(level : str, user : str, password : str):

    # TODO: Intentar mejorar y autmatizar

    os.system("sshpass -p " + password + " ssh -q " + user +"@" + host + " -oStrictHostKeyChecking=no -p" + port + " ssh -q -i sshkey.private bandit14@localhost -oStrictHostKeyChecking=no -p" + port + " cat /etc/bandit_pass/bandit14 >> " + file_flag)
    
    ################################
    flag = open(file_flag , 'r+')
    readflag = flag.readlines()
    readflag = readflag[-1]
    readflag = readflag.strip('\n')
    ################################

    print("\x1b[1;37m"+"#---------------------------------------------------#"+"\x1b[0;37m")
    print("| " + name_pass + level + ": " + readflag.strip("\n") + "   |")


def bandit_14(level : str, user : str, password : str):

    # TODO: Intentar mejorar y automatizar

    os.system("sshpass -p " + password + " ssh -q " + user + "@" + host + " -p" + port + " \"echo fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq | nc localhost 30000 | tail -n2 | head -n1\" >> " + file_flag)
    
    ################################
    flag = open(file_flag , 'r+')
    readflag = flag.readlines()
    readflag = readflag[-1]
    readflag = readflag.strip('\n')
    ################################

    print("\x1b[1;37m"+"#---------------------------------------------------#"+"\x1b[0;37m")
    print("| " + name_pass + level + ": " + readflag.strip("\n") + "   |")
    

if __name__ == '__main__':
    
    banner()
    
    BANDIT("0", "bandit0", "bandit0", "cat readme")
    BANDIT("1", "bandit1", "", "cat $(pwd)/-")
    BANDIT("2", "bandit2", "", "cat spaces\ in\ this\ filename")
    BANDIT("3", "bandit3", "", "cat inhere/.hidden")
    BANDIT("4", "bandit4", "", "cat inhere/-file07")
    BANDIT("5", "bandit5", "", "cat inhere/maybehere07/.file2 | tr -d ' '")
    BANDIT("6", "bandit6", "", "cat /var/lib/dpkg/info/bandit7.password")
    BANDIT("7", "bandit7", "", "grep \"millionth\" data.txt | awk '{print $NF}'")
    BANDIT("8", "bandit8", "", "sort data.txt | uniq -u")
    BANDIT("9", "bandit9", "", "strings data.txt | grep \"===\" | tail -n1 | awk '{print $NF}'")
    BANDIT("10", "bandit10", "", "cat data.txt | base64 -d | awk '{print $NF}'")
    BANDIT("11", "bandit11", "", "cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m' | awk '{print $NF}'")
    bandit_12("12", "bandit12", "JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv") # TODO: Revisar con Kek1us, Intentar quitar la contraseña y automatizarlo
    bandit_13("13", "bandit13", "wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw") # TODO: Revisar con Kek1us, Intentar quitar la contraseña y automatizarlo
    bandit_14("14", "bandit14", "fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq") # TODO: Revisar con Kek1us, Intentar quitar la contraseña y automatizarlo
    BANDIT("15", "bandit15", "", "echo jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt | openssl s_client -quiet -connect localhost:30001 2>/dev/null | grep -v Correct! | tr -d '\n'")
    
    print("\x1b[1;37m"+"#---------------------------------------------------#"+"\x1b[0;37m")
    
    flag.close()
