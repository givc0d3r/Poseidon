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

               . '@(@@@@@@@)@. (@@) `  .   '
     .  @@'((@@@@@@@@@@@)@@@@@)@@@@@@@)@ 
     @@(@@@@@@@@@@))@@@@@@@@@@@@@@@@)@@` .
  @.((@@@@@@@)(@@@@@@@@@@@@@@))@\@@@@@@@@@)@@@  .
 (@@@@@@@@@@@@@@@@@@)@@@@@@@@@@@\\@@)@@@@@@@@)
(@@@@@@@@)@@@@@@@@@@@@@(@@@@@@@@//@@@@@@@@@) ` 
 .@(@@@@)##&&&&&(@@@@@@@@)::_=(@\\@@@@)@@ .   .'
   @@`(@@)###&&&&&!!;;;;;;::-_=@@\\@)@`@.
   `   @@(@###&&&&!!;;;;;::-=_=@.@\\@@     '
      `  @.#####&&&!!;;;::=-_= .@  \\
            ####&&&!!;;::=_-        `
             ###&&!!;;:-_=
              ##&&!;::_=
             ##&&!;:=
            ##&&!:-
           #&!;:-
          #&!;= 
          #&!- 
           #&=
           #&-
            \\#/'
 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            - Coded By D3m0l1d0r - \n""" 

def Seach():
	target =  raw_input("Target =:>")
	word = raw_input("Wordlist =:>")
	wordp = open(word, "r").readlines()

	for i in wordp:
		i = i.replace("\n", "").replace("\r", "")
		seach = urlopen(target+i)
		if seach.getcode() == 200:
			seach = seach.read()
			if 'Login' or 'Senha' in seach:
				print "[+] Encontrada: "+target+i+""
		else:
			print "[-] Não Encontrada : "+target+i+""



Main()
