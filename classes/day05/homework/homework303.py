# -*- coding:utf-8 -*-
'''
思路：
1.判断公式格式是否有误，无误则继续
2.替换公式中多余的空格或tab
3.当存在括号时，先通过循环和正则匹配，优先计算最内层括号（即括号里无括号）的情况
4.括号内，先计算 乘除，再计算 加减
5.将当前步骤计算出来当结果替换之前匹配当表达式部分，进而进行下一步运算(循环)

其他补充操作：
    1.符号的替换，应对--等情况
    2.小数的匹配 '\d+\.?\d*[8/]\d+\.?\d*'

    (-8.0)如何处理

'''

import re

source = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'

def check_exp(exp):
    flag = True
    if re.findall('[a-zA-Z]',exp):
        print('存在非法字符')
        flag = False
    if exp.count('(') != exp.count(')'):
        print('表达式未闭合')
        flag = False
    return flag

def fmt_exp(exp):
    exp = exp.replace('++','+')
    exp = exp.replace('+-','-')
    exp = exp.replace('-+','-')
    exp = exp.replace('--','+')
    exp = exp.replace(' ','')
    #print(exp)
    return exp


def calc_mul(exp):
    regular = '\d+\.?\d*([*/]|\*\*)\d+\.?\d*'
    while re.findall(regular,exp):
        expression = re.search(regular,exp).group() #匹配乘除即乘方
        if expression.count('*') == 1:  #乘法
            x,y = expression.split('*')
            exp_result = str(float(x) * float(y))
            exp = exp.replace(expression,exp_result)    #用乘法计算所得结果替换原匹配到当表达式
            exp = fmt_exp(exp)  #格式化
        if expression.count('/') == 1:
            x,y = expression.split('/')
            exp_result = str(float(x) / float(y))
            exp = exp.replace(expression,exp_result)
            exp = fmt_exp(exp)
        if expression.count('*') == 2:
            x,y = expression.split('**')
            exp_result = 1
            for i in int(y):
                exp_result *= int(x)
            exp = exp.replace(expression,str(exp_result))
            exp = fmt_exp(exp)
        return(exp)


def calc_add(exp):
    regular = '[\-]?\d+\.?\d*([+-][\-]\d+\.?\d*)?'    #在执行加减之前会先执行乘除，乘除函数会对最后结果进行格式化操作，因此无需考虑（++）这种情况
    while re.findall(regular,exp):
        expression = re.search(regular,exp).group()
        expression = fmt_exp(expression)    #提前对表达式格式化，替换+- +- -- -+ 等情况，按照单个加减运算符计算
        if '+' in expression:
            x,y = expression.split('+')
            exp_result = str(float(x) + float(y))
            exp = exp.replace(expression,exp_result)
            exp = fmt_exp(exp)
        if '-' in expression:
            exp_member = expression.split('-')
            #print(len(exp_member))
            if len(exp_member) == 3:
                x,y = expression.split('-')
                #print(x,y)
                exp_result = str(float(x) - float(y))
                exp = exp.replace(expression,exp_result)
                exp = fmt_exp(exp)
            if len(exp_member) == 2:
                exp = expression
        return exp


# calc_mul(source)

if check_exp(source):
    source = fmt_exp(source)
    # print(source)
    # print('eval_source:',eval(source))
    while source.count('(') > 0:
        strs = re.search('\([^()]*\)',source).group()
        replace_exp = calc_mul(strs)
        #print(replace_exp)
        replace_exp = calc_add(replace_exp)
        #print(replace_exp)
        source = fmt_exp(source.replace(strs,replace_exp[1:-1]))    #原表达式中，将带括号的表达式部分，用计算后的结果代替，并去掉括号。返回最新的source表达式，方便进行下一步不带括号的运算
    else:
        replace_exp = calc_mul(source)
        replace_exp = calc_add(replace_exp)
        source = source.replace(source,replace_exp)
    print('calc_source:',source)

while '-' in source:
    replace_exp = calc_mul(source)
    replace_exp = calc_add(replace_exp)
    source = source.replace(source, replace_exp)


print(source)