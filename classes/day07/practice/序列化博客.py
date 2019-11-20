# import json
# dic = {'name':'mlg','pwd':'123456','operate':'login'}
# ret = json.dumps(dic)   # 把dic类型数据序列化为字符串类型数据
#
# print('dic:',dic,type(dic))
# print('ret:',ret,type(ret))
#
# byte_ret = ret.encode('utf-8')  # 把字符串类型数据编译成byte类型数据
# print('byte_ret:',byte_ret,type(byte_ret))
#
# print('-'*10+'我是网络'+'-'*10)
#
# ret_rev = byte_ret.decode('utf-8')  # 把byte类型的数据解码成字符串
# print('ret_rev:',ret_rev,type(ret_rev))
#
# dic_rev = json.loads(ret_rev)   # 将json格式对字符串反序列为dic
# print('dec_rev:',dic_rev,type(dic_rev))
#
# '''输出'''
# # dic: {'name': 'mlg', 'pwd': '123456', 'operate': 'login'} <class 'dict'>
# # ret: {"name": "mlg", "pwd": "123456", "operate": "login"} <class 'str'>
# # byte_ret: b'{"name": "mlg", "pwd": "123456", "operate": "login"}' <class 'bytes'>
# # ----------我是网络----------
# # ret_rev: {"name": "mlg", "pwd": "123456", "operate": "login"} <class 'str'>
# # dec_rev: {'name': 'mlg', 'pwd': '123456', 'operate': 'login'} <class 'dict'>


# import json
#
# dic = {'北京':{'朝阳':{},'海淀':{}}}
#
# str_dic = json.dumps(dic)
# print(str_dic,type(str_dic))    # {"\u5317\u4eac": {"\u6d77\u6dc0": {}, "\u671d\u9633": {}}} <class 'str'>
#
# with open('test.txt',mode='w',encoding='utf-8') as f:
#     f.write(str_dic)
#
# with open('test.txt',mode='r',encoding='utf-8') as f:
#     str_dic = f.read()
#     print(str_dic)  # {"\u5317\u4eac": {"\u6d77\u6dc0": {}, "\u671d\u9633": {}}}
#     dic_get = json.loads(str_dic)
#
# print(dic_get)  # {'北京': {'朝阳': {}, '海淀': {}}}


# import json
# # dic = {'北京':{'朝阳':{},'海淀':{}}}
# # str_dic = json.dumps(dic,ensure_ascii=False)
# #
# # with open('test2.txt',mode='w',encoding='utf-8') as f:
# #     f.write(str_dic)


# import json
# lst = ['a','b','c']
# lst_str = json.dumps(lst)
# print(lst_str,type(lst_str))    # ["a", "b", "c"] <class 'str'>
#
# var = 'a'
# var_str = json.dumps(var)
# print(var_str,type(var_str))  # "a" <class 'str'>
#
# num = 22
# num_str = json.dumps(num)
# print(num_str,type(num_str))    # 22 <class 'str'>
#
# flag = True
# flag_str = json.dumps(flag)
# print(flag_str,type(flag_str))  # true <class 'str'>


# import json
# l = ['mlg',1,2]
# with open('test3.txt',mode='w',encoding='utf-8') as f:
#     json.dump(l,f)
#
# with open('test3.txt',mode='r',encoding='utf-8') as f:
#     ret = json.load(f)
#     print(ret)      # ['mlg', 1, 2]


# import pickle
# #
# # dic = {'北京':{'朝阳','海淀'},('天津','河北'):[1,2,3]}
# # dic_byte = pickle.dumps(dic)
# # print(dic_byte,type(dic_byte))
# #
# # dic_new = pickle.loads(dic_byte)
# # print(dic_new)
# #
# # '''输出'''
# # # b'\x80\x03}q\x00(X\x06\x00\x00\x00\xe5\xa4\xa9\xe6\xb4\xa5q\x01X\x06\x00\x00\x00\xe6\xb2\xb3\xe5\x8c\x97q\x02\x86q\x03]q\x04(K\x01K\x02K\x03eX\x06\x00\x00\x00\xe5\x8c\x97\xe4\xba\xacq\x05cbuiltins\nset\nq\x06]q\x07(X\x06\x00\x00\x00\xe6\xb5\xb7\xe6\xb7\x80q\x08X\x06\x00\x00\x00\xe6\x9c\x9d\xe9\x98\xb3q\te\x85q\nRq\x0bu.' <class 'bytes'>
# # # {('天津', '河北'): [1, 2, 3], '北京': {'海淀', '朝阳'}}

# import pickle
#
# dic = {'北京':{'朝阳','海淀'},('天津','河北'):[1,2,3]}
# dic_byte = pickle.dumps(dic)
#
# with open('test4.txt',mode='wb') as f:
#     f.write(dic_byte)
#
# with open('test4.txt',mode='rb') as f:
#     ret = f.read()
#     dic_new = pickle.loads(ret)
# print(dic_new)  # {'北京': {'朝阳', '海淀'}, ('天津', '河北'): [1, 2, 3]}


import pickle

dic = {'北京':{'朝阳','海淀'},('天津','河北'):[1,2,3]}

with open('test5.txt','wb') as f:
    pickle.dump(dic,f)
with open('test5.txt','rb') as f:
    ret = pickle.load(f)
    print(ret)  # {('天津', '河北'): [1, 2, 3], '北京': {'海淀', '朝阳'}}