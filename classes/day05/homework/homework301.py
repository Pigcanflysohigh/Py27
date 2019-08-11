# -*- coding:utf-8 -*-
import re

def format_string(string):
    string = string.replace("--", "+")
    string = string.replace("-+", "-")
    string = string.replace("++", "+")
    string = string.replace("+-", "+")
    string = string.replace("*-", "*")
    string = string.replace("*+", "*")
    string = string.replace("/+", "/")
    string = string.replace(' ', '')
    return string

def calc_mul_div(string):
    regular='\d+\.?\d*([*/]|\*\*)[\-]?\d+\.?\d*'
    while re.findall(regular, string):
        expression = re.search(regular, string).group()

        if expression.count("*")==1:
            x,y = expression.split("*")
            mul_result = str(float(x) * float(y))
            string = string.replace(expression, mul_result)
            string = format_string(string)

        if expression.count("/"):
            x,y = expression.split("/")
            div_result = str(float(x) / float(y))
            string = string.replace(expression, div_result)
            string = format_string(string)

        if expression.count('*')==2:
            x,y=expression.split('**')
            pow_result=1
            for i in range(int(y)):
                pow_result*=int(x)
            string=string.replace(expression,str(pow_result))
            string=format_string(string)
        return string

def calc_add_sub(string):
    add_sub= regular='[\-]?\d+\.?\d*([+-][\-]?\d+\.?\d*'

    while re.findall(add_sub, string):
        add_sub_ex = re.search(add_sub, string).group()

        if add_sub_ex.count("+")==1:
            x,y = add_sub_ex.split("+")
            add_result = str(float(x) + float(y))
            string = string.replace(add_sub_ex, add_result)
            string = format_string(string)

        if add_sub_ex.count("-"):
            sub_list = re.search(add_sub, string)
            for sub_str in sub_list:
                numbers = sub_str.split("-")
                if len(numbers) == 3:
                    result = 0
                    for v in numbers:
                        if v:
                            result -= float(v)
                else:
                    x,y = numbers
                    result = float(x) - float(y)
                string = string.replace(sub_str, "+" + str(result))
            string = format_string(string)
        return string

def check_expression(string):
    check_result = True
    if not string.count("(") == string.count(")"):
        print("表达错误,括号示闭合！")
        check_result = False
    if re.findall('[a-z]+', string.lower()):
        print("表达式错误,包含非法字符！")
        check_result = False
    return check_result

#source='1 - 2 * ((60-30 +(-40/5) * (-9-2-5-4*5-6/3-40/8+5*9) - (-4*3)/ (16-3*2))'
source = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'

if check_expression(source):
    print("source: ", source)
    print("eval result: ", eval(source))
    source = format_string(source)
    print(source)

    while source.count("(") > 0:
        strs = re.search('\([^()]*\)', source).group()
        replace_str = calc_mul_div(strs)
        replace_str = calc_add_sub(replace_str)
        source = format_string(source.replace(strs, replace_str[1:-1]))

    else:
        replace_str = calc_mul_div(source)
        replace_str = calc_add_sub(replace_str)
        source = source.replace(source, replace_str)
    print("my result: ", source.replace("+",""))