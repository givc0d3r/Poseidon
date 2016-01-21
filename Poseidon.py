#!/usr/bin/python
#_*_ coding:utf-8 _*_

from urllib import urlopen
from os import name, system

def Main():
	System()
	Banner()
	Seach()


def System():
	if name == 'nt':
		system("cls")
	else:
		system("clear")

def Banner():
	print """\n\033[1;32m              
	                       .                                                      .
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'          `98v8P'          `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d'
                               `             ' 
              
                  \033[0;36m- Coded By D3m0l1d0r & Pedro Souza -\033[0m 

\n\033[0m""" 

def Seach():
	target =  raw_input("\033[0;37mTarget =:>\033[0m")
	word = raw_input("\033[0;37mWordList =:>\033[0m")
	wordp = open(word, "r").readlines()

	for i in wordp:
		i = i.replace("\n", "").replace("\r", "")
		seach = urlopen(target+i)
		if seach.getcode() == 200:
			seach = seach.read()
			if 'Login' or 'Senha' in seach:
				print "\033[0;32m[+] Encontrada: "+target+i+"\033[0m"
		else:
			print "\033[0;31m[-] Não Encontrada : "+target+i+"\033[0m"



Main()
