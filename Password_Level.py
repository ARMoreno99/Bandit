#!/usr/bin/python3

import os
import paramiko
import string

# VARIABLES GLOBALES
host = "bandit.labs.overthewire.org"
port = 2220

# SESION SSH
client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.client.WarningPolicy())

# FICHEROS
flag = open('flag.txt', 'w')


def banner():
	print ("______   ___   _   _ ______  _____  _____ ")
	print ("| ___ \ / _ \ | \ | ||  _  \|_   _||_   _|")
	print ("| |_/ // /_\ \|  \| || | | |  | |    | |")
	print ("| ___ \|  _  || . ` || | | |  | |    | |")
	print ("| |_/ /| | | || |\  || |/ /  _| |_   | |")
	print ("\____/ \_| |_/\_| \_/|___/   \___/   \_/")

	print ("\n      ###PASSWORD LEVEL BANDIT###       \n")


def bandit_init(user : str, password : str, command : str):
        
        try:
            client.connect(host, port, username=user, password=password, timeout=30)
        except Exception as e:
            print(e)

        stdin, stdout, stderr = client.exec_command(command)

        for line in stdout:
            print("#------------------------------------------------#")
            print("| Flag Level 0: " + line.strip('\n') + " |")
            flag.write(line)

        flag.close()
        client.close()
        

def BANDIT(level : str, user : str, command : str):
        
        flag = open('flag.txt' , 'r+')
        readflag = flag.readlines()
        readflag = readflag[-1]
        readflag = readflag.strip('\n')
        
        try:
            client.connect(host, port, username=user, password=readflag, timeout=30)
        except Exception as e:
            print(e)
        stdin, stdout, stderr = client.exec_command(command)
        for line in stdout:
            print("#------------------------------------------------#")
            print("| Flag Level " + level + ": " + line.strip("\n") + " |")
            flag.write(line)

        client.close()


if __name__ == '__main__':

    banner()
    bandit_init("bandit0", "bandit0", "cat readme")
    BANDIT("1", "bandit1", "cat $(pwd)/-")
    BANDIT("2", "bandit2", "cat spaces\ in\ this\ filename")
    BANDIT("3", "bandit3", "cat inhere/.hidden")
    BANDIT("4", "bandit4", "cat inhere/-file07")
    print("#------------------------------------------------#")
    flag.close()
    
    
