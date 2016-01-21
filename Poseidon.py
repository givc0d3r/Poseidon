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
	print """\n              
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
                      - Coded By D3m0l1d0r & Pedro Souza -   
\n""" 

def Seach():
	target =  raw_input("Target =:>")
	word = raw_input("WordList =:>")
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
