#!/usr/bin/python
#_*_ coding:utf-8 _*_

import urllib
import os 
import sys 
import argparse

def System():
	if sys.platform != "linux2":
		os.system("clear")
	else:
		os.system("cls")

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

\n""" 

def int_():
	target =  raw_input("Target =:>")
	word = raw_input("WordList =:>")

def seach():
	   
    wordp = open(word, "r").readlines()
	for i in wordp:
		i = i.replace("\n", "").replace("\r", "")
		seach = urllib.urlopen(target+i)
		if seach.getcode() == 200:
			seach = seach.read()
			if 'Login' or 'Senha' in seach:
				print "[+] Encontrada: "+target+i+""
			else:
				print "[-] Não Encontrada"+target+i+""

Banner()
int_()
System()
seach()
