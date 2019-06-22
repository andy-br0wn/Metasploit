#Coded by @Andy_Brown
#@Kali_Linuxxx
'''
Please Join my channel and support us ;)
'''
#Copy this script on your system and just type( python andy.py)
#Import Reqs
import os,sys,platform
os.system("reset")
#Colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print bcolors.BOLD+bcolors.WARNING + "MetaSploit Installer Coded by @Andy_Brown"+ bcolors.ENDC
#Sys req installition
os.system("reset")
os.system("pkg install git  ruby ruby-dev make clang autoconf curl wget ncurses-utils libsqlite-dev postgresql postgresql-dev libpcap-dev libffi-dev libxslt-dev pkg-config")
os.system("reset")
print bcolors.BOLD+bcolors.WARNING + "MetaSploit Installer Coded by @Andy_Brown\n"+ bcolors.ENDC
print bcolors.BOLD+bcolors.OKGREEN + "[1]..........Install MetaSploit"+ bcolors.ENDC
print bcolors.BOLD+bcolors.OKGREEN + "[0]..........Exit\n"+ bcolors.ENDC
ui=raw_input("Choose one Option :")
if ui == '1':
	print bcolors.BOLD+bcolors.FAIL + "Installing MetaSploit\n" +bcolors.ENDC
	os.system("git clone https://github.com/Hax4us/Metasploit_termux.git")
	os.system("cd Metasploit_termux") 
	os.system("chmod +x metasploit.sh")
	os.system("./metasploit.sh")
if ui == '0':
	os.system("reset")
	print bcolors.BOLD+bcolors.FAIL + "Coded by Andy Brown\nHave a good day ;)" +bcolors.ENDC
	os.system("exit")
else:
	os.system("reset")
	print bcolors.BOLD+bcolors.FAIL + "You have Two options Please type 1 or 0 \n" +bcolors.ENDC
	os.system("exit")
	

	





#END
#Coded by Andy Brown
#channel: @KALI_LINUXXX

		
		
		
	
