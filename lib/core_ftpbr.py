#!/usr/bin/python2
import os, platform, time, random
sembarang = random.randint(1,2)

err_keyint = "[!] Keyboard Interrupted by User !!!"
err_invld = "[!] Error: Invalid number selected !"
err_invalid = "[!] Error: Invalid option !"
err_blank = "[!] Error: Don't leave it blank !"
err_cantcon = "[!] Error: Can't connect with Target !"
err_cantconp = '''[!] Error: Can't connect to Target's Port !
	Are You sure that Port is opened and allow connection ?
	Try to scan it with IP-PORT Modules or with Nmap'''
err_cantfind = '''[!] Error: Can't reach Target ! Are You sure Your Target
	is Online ? Are the URL is correct ? Are You Online ?'''
err_cantbck = "[!] Error: Can't go back ! this is the main Modules !"
err_notavai = '''[!] Sorry: This Modules is currently not available right now...
	This Modules maybe Unlocked in the next Version of M-Evil Tools :)
	so...stay with Me :)'''
err_bukalst = '''[!] Error: Can't open List File ! The file is too large
	or the File is not exists or corrupted !
	Please Try Again !'''
err_bacalst = '''[!] Error: Can't read List File ! The file is too large
	or the File is not exists or corrupted !
	Please Try Again !'''
banner1 = '''
   _______ _______ ______       ______                          
  (_______|_______|_____ \     (____  \               _         
   _____      _    _____) )____ ____)  ) ____ _   _ _| |_ _____ 
  |  ___)    | |  |  ____(_____)  __  ( / ___) | | (_   _) ___ |
  | |        | |  | |          | |__)  ) |   | |_| | | |_| ____|
  |_|        |_|  |_|          |______/|_|   |____/   \__)_____)

            { FTP-Brute v1 }==={ Coded by M-XacT-666 }
'''
banner2 = '''
      dBBBBP  dBBBBBBP dBBBBBb          dBBBBb dBBBBBb   dBP dBP  dBBBBBBP dBBBBP 
                          dB'             dBP     dBP   dBP dBP    dBP    dBP    
   dBBBP      dBP     dBBBP'          dBBBK'  dBBBBK   dBP dBP    dBP   dBBBBP
  dBP        dBP     dBP    dBBBBBP  dB' db  dBP  BB  dBP_dBP    dBP   dBP
 dBP        dBP     dBP             dBBBBP' dBP  dB' dBBBBBP    dBP   dBBBBP

                     { FTP-Brute v1 }==={ Coded by M-XacT-666 }
'''
def clearscreen(x):
	if x == "Windows":
		os.system('CLS')
	else:
		os.system('clear')
def tidur(x):
	time.sleep(x)
def keluar():
	print ""
	print "[*] Closing Tools..."
	tidur(1)
	print "[^] Thanks for using My Tools !"
	exit()
def banner(x):
	if x == 1:
		print banner1
	elif x == 2:
		print banner2
	elif x == 3:
		print banner3
def judul():
	banner(sembarang)