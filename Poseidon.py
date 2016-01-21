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
	                   .__=\__                  .__==__,                                                       
                      jf'      ~~=\,         _=/~'      `\,                                                     
                  ._jZ s0F_t_wAR-3 `\q,   /=~   vI._rU-5  `\__                                                  
                 j5(/          ...    `\./         AND...   V\\,                 
               .Z))' _____    dEv  c0De |   ...       .____, \)/\                          
              j5(K=~~     ~~~~\=_,      |      _/=~~~~'    `~~+K\\,                            
            .Z)\/                `~=L   |  _=/~                 t\ZL                             
           j5(_/.__/===========\__   ~q |j/   .__============___/\J(N,                                          
          4L#XXXL_________________XGm, \P  .mXL_________________JXXXW8L                                         
          ~~~~~~~~~~~~~~~~~~~~~~~~~YKWmmWmmW@~~~~~~~~~~~~~~~~~~~~~~~~~~ 
              
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
