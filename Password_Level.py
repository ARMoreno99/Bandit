#!/usr/bin/python3

import os
import paramiko
import string


def banner():
	print ("______   ___   _   _ ______  _____  _____ ")
	print ("| ___ \ / _ \ | \ | ||  _  \|_   _||_   _|")
	print ("| |_/ // /_\ \|  \| || | | |  | |    | |")
	print ("| ___ \|  _  || . ` || | | |  | |    | |")
	print ("| |_/ /| | | || |\  || |/ /  _| |_   | |")
	print ("\____/ \_| |_/\_| \_/|___/   \___/   \_/")

	print ("\n      ###PASSWORD LEVEL BANDIT###       \n")

def bandit0():
        flag = open('flag.txt', 'w')
        host = "bandit.labs.overthewire.org"
        port = 2220
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.client.WarningPolicy())
        try:
            client.connect(host, port, username='bandit0', password='bandit0', timeout=30)
        except Exception as e:
            print(e)
        stdin, stdout, stderr = client.exec_command('cat readme')
        for line in stdout:
            print('> Flag Level 1: ' + line.strip('\n'))
            
            flag.write(line)

        flag.close()
        client.close()

def bandit1():
        flag = open('flag.txt' , 'r+')
        readflag = flag.readline()
        readflag = readflag.strip('\n')
        host = "bandit.labs.overthewire.org"
        port = 2220
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.client.WarningPolicy())
        try:
            client.connect(host, port, username='bandit1', password=readflag, timeout=30)
        except Exception as e:
            print(e)
        stdin, stdout, stderr = client.exec_command('cat $(pwd)/-')
        for line in stdout:
            print('> Flag Level 2: ' + line.strip('\n'))
            flag.write(line)

        flag.close()
        client.close()

def bandit2():
        flag = open('flag.txt' , 'r+')
        readflag = flag.readlines()
        readflag = readflag[-1]
        readflag = readflag.strip('\n')
        host = "bandit.labs.overthewire.org"
        port = 2220
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.client.WarningPolicy())
        try:
            client.connect(host, port, username='bandit2', password=readflag, timeout=30)
        except Exception as e:
            print(e)
        stdin, stdout, stderr = client.exec_command("cat spaces\\ in\\ this\\ filename")
        for line in stdout:
            print('> Flag Level 3: ' + line.strip('\n'))
            flag.write(line)

        flag.close()
        client.close()

def bandit3():
        flag = open('flag.txt' , 'r+')
        readflag = flag.readlines()
        readflag = readflag[-1]
        readflag = readflag.strip('\n')
        host = "bandit.labs.overthewire.org"
        port = 2220
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.client.WarningPolicy())
        try:
            client.connect(host, port, username='bandit3', password=readflag, timeout=30)
        except Exception as e:
            print(e)
        stdin, stdout, stderr = client.exec_command("cat inhere/.hidden")
        for line in stdout:
            print('> Flag Level 4: ' + line.strip('\n'))
            flag.write(line)

        flag.close()
        client.close()

def bandit4():
        flag = open('flag.txt' , 'r+')
        readflag = flag.readlines()
        readflag = readflag[-1]
        readflag = readflag.strip('\n')
        host = "bandit.labs.overthewire.org"
        port = 2220
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.client.WarningPolicy())
        try:
            client.connect(host, port, username='bandit4', password=readflag, timeout=30)
        except Exception as e:
            print(e)
        stdin, stdout, stderr = client.exec_command("cat inhere/\-file07")
        for line in stdout:
            print('> Flag Level 5: ' + line.strip('\n'))
            flag.write(line)

        flag.close()
        client.close()

def bandit5():
        flag = open('flag.txt' , 'r+')
        readflag = flag.readlines()
        readflag = readflag[-1]
        readflag = readflag.strip('\n')
        host = "bandit.labs.overthewire.org"
        port = 2220
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.client.WarningPolicy())
        try:
            client.connect(host, port, username='bandit5', password=readflag, timeout=30)
        except Exception as e:
            print(e)
        stdin, stdout, stderr = client.exec_command("find inhere/ -readable -size 1033c ! -executable 2>/dev/null | xargs cat | tr -d ' '")
        for line in stdout:
            print('> Flag Level 6: ' + line.strip('\n'))
            flag.write(line)

        flag.close()
        client.close()

def bandit6():
        flag = open('flag.txt' , 'r+')
        readflag = flag.readlines()
        readflag = readflag[-1]
        readflag = readflag.strip('\n')
        host = "bandit.labs.overthewire.org"
        port = 2220
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.client.WarningPolicy())
        try:
            client.connect(host, port, username='bandit6', password=readflag, timeout=30)
        except Exception as e:
            print(e)
        stdin, stdout, stderr = client.exec_command("find / -user bandit7 -group bandit6 -size 33c 2>/dev/null | xargs cat")
        for line in stdout:
            print('> Flag Level 7: ' + line.strip('\n'))
            flag.write(line)

        flag.close()
        client.close()

def bandit7():
        flag = open('flag.txt' , 'r+')
        readflag = flag.readlines()
        readflag = readflag[-1]
        readflag = readflag.strip('\n')
        host = "bandit.labs.overthewire.org"
        port = 2220
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.client.WarningPolicy())
        try:
            client.connect(host, port, username='bandit7', password=readflag, timeout=30)
        except Exception as e:
            print(e)
        stdin, stdout, stderr = client.exec_command("grep \"millionth\" data.txt | awk '{print $2}'")
        for line in stdout:
            print('> Flag Level 8: ' + line.strip('\n'))
            flag.write(line)

        flag.close()
        client.close()

def bandit8():
        flag = open('flag.txt' , 'r+')
        readflag = flag.readlines()
        readflag = readflag[-1]
        readflag = readflag.strip('\n')
        host = "bandit.labs.overthewire.org"
        port = 2220
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.client.WarningPolicy())
        try:
            client.connect(host, port, username='bandit8', password=readflag, timeout=30)
        except Exception as e:
            print(e)
        stdin, stdout, stderr = client.exec_command("sort data.txt | uniq -u")
        for line in stdout:
            print('> Flag Level 9: ' + line.strip('\n'))
            flag.write(line)

        flag.close()
        client.close()

def bandit9():
        flag = open('flag.txt' , 'r+')
        readflag = flag.readlines()
        readflag = readflag[-1]
        readflag = readflag.strip('\n')
        host = "bandit.labs.overthewire.org"
        port = 2220
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.client.WarningPolicy())
        try:
            client.connect(host, port, username='bandit9', password=readflag, timeout=30)
        except Exception as e:
            print(e)
        stdin, stdout, stderr = client.exec_command("strings data.txt | grep \"===\" | tail -n1 | awk \'{print $2}\'")
        for line in stdout:
            print('> Flag Level 10: ' + line.strip('\n'))
            flag.write(line)

        flag.close()
        client.close()


def bandit10():
        flag = open('flag.txt' , 'r+')
        readflag = flag.readlines()
        readflag = readflag[-1]
        readflag = readflag.strip('\n')
        host = "bandit.labs.overthewire.org"
        port = 2220
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.client.WarningPolicy())
        try:
            client.connect(host, port, username='bandit10', password=readflag, timeout=30)
        except Exception as e:
            print(e)
        stdin, stdout, stderr = client.exec_command("base64 -d data.txt | awk '{print $NF}'")
        for line in stdout:
            print('> Flag Level 11: ' + line.strip('\n'))
            flag.write(line)

        flag.close()
        client.close()

def bandit11():
        flag = open('flag.txt' , 'r+')
        readflag = flag.readlines()
        readflag = readflag[-1]
        readflag = readflag.strip('\n')
        host = "bandit.labs.overthewire.org"
        port = 2220
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.client.WarningPolicy())
        try:
            client.connect(host, port, username='bandit11', password=readflag, timeout=30)
        except Exception as e:
            print(e)
        stdin, stdout, stderr = client.exec_command("cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m' | awk '{print $NF}'")
        for line in stdout:
            print('> Flag Level 12: ' + line.strip('\n'))
            flag.write(line)

        flag.close()
        client.close()




if __name__ == '__main__':

	banner()

	bandit0()
	bandit1()
	bandit2()
	bandit3()
	bandit4()
	bandit5()
	bandit6()
	bandit7()
	bandit8()
	bandit9()
	bandit10()
	bandit11()
