# -*- coding:utf-8 -*-

'''
lstfirst = []
dictfirst = {}
with open('p0102',mode='r',encoding='utf-8') as f:
    for line in f:
        lst = line.strip().split(' ')
        lstfirst = lstfirst + lst
    print(lstfirst)
    lsttwo = list(set(lstfirst))
    for k in lsttwo:
        dictfirst[k] = lstfirst.count(k)
    print(dictfirst)


dic = {}
with open('p01',mode='r',encoding='utf-8') as f:
    contents = f.read()
    ch = ''
    for char in contents:
        if char.isalpha():
            ch +=char
        else:
            if ch in dic:
                dic[ch] +=1
            else:
                dic[ch] = 1
                ch = ''
print(dic)
'''

def count_words(file):
	dic = {}
	with open(file,encoding='utf-8') as f:
		content = f.read()
		ch = ''
		for char in content:
			if char.isalpha():
				ch += char
			else:
				if ch in dic:
					dic[ch] += 1
				else:
					dic[ch] = 1
				ch = ''
	return dic
ret = count_words('file.txt')
print(ret)