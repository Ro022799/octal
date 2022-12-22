#!/usr/bin/env/ python
import re
import sys
def octal_file():
	lista = []
	filename = sys.argv[1]
	with open(filename, mode ='r') as file:
		for line in file.readlines():
			pattern = r'^[d|l|\-](\w{3}|.{3})(\w{3}|.{3})(\w{3}|.{3}) '
			result = re.search(pattern, line)
			if result == None:
				continue
			lista.append(line)
		return lista
def valores():
	value_letters=[(4,"r"),(2,"w"),(1,"x"), (0,'-')]
	return value_letters
def octal_line(lista):
	usuarios, grupos, otros = [], [], []
	for line in lista:
		pattern = r'^[d|l|\-](\w{3}|.{3})(\w{3}|.{3})(\w{3}|.{3}) '
		result = re.search(pattern, line)
		usuario = result.groups()[0]
		grupo = result.groups()[1]
		otro =  result.groups()[2]
		usuarios.append(usuario)
		grupos.append(grupo)
		otros.append(otro)
	return usuarios, grupos, otros
def conversion_usuario( usuarios, value_letters):
	cont_user = []
	for codigo in usuarios:
		cont = 0
		for letter in codigo:
			for value, lett in value_letters:
				if letter == lett:
					cont += value
		cont_user.append(cont)
	return cont_user
def conversion_grupos(grupos, value_letters):
        cont_groups = []
        for codigo in grupos:
                cont = 0
                for letter in codigo:
                        for value, lett in value_letters:
                                if letter == lett:
                                        cont += value
                cont_groups.append(cont)
        return cont_groups
def conversion_otros(otros, value_letters):
        cont_otros = []
        for codigo in grupos:
                cont = 0
                for letter in codigo:
                        for value, lett in value_letters:
                                if letter == lett:
                                        cont += value
                cont_otros.append(cont)
        return cont_otros
def numero_octal(cont_user,cont_groups, cont_otros):
	lista = []
	for i in range (len(cont_user)):
		numero_octal= str(cont_user[i])+str(cont_groups[i])+str(cont_otros[i])
		lista.append(numero_octal)
	return lista
lista = octal_file()
usuarios, grupos, otros =octal_line(lista)
valor = valores()
group1=conversion_usuario(usuarios,valor)
group2=conversion_grupos(grupos,valor)
group3=conversion_otros(otros,valor)
print(numero_octal(group1, group2, group3))
