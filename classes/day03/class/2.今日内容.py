# 集合-扩展
# 文件操作
    # 打开文件
        # f = open(r'文件路径',mode='r',encoding='utf-8')   # *****
        # f = open(r'文件路径',mode='w',encoding='utf-8')
        # f = open(r'文件路径',mode='a',encoding='utf-8')   # *****
        # read(n) n表示字符 a表示1字符 你也表示1字符
    # 读文件
        # f.read()
        # f.realine()
        # for line in f:      # *****
    # 追、写文件
        # f.write('alex\n')   # *****
    # 关闭文件
        # f.cloes()
    # 修改文件
        # 打开文件读
        # 修改
        # 打开另一个文件写
        # 删除文件 os.remove('文件路径')
        # 修改文件 os.rename('源名','目的名')
    # 参数的介绍
        # 以字节的形式打开文件，并读，写
        # 图片和视频文件如果要处理的话 是不能通过指定编码的形式打开的
        # mode = 'rb' 读字节
        # mode = 'wb' 写字节
        # read(n)  n表示读n个字节
    # 文件的上下文管理
        # with open() as f:     # ******
            # 对应的文件操作，不需要我们自己处理文件的关闭了
    # 文件的指针
        # f.tell() 查看指针
        # f.seek(0)修改指针位置
# 函数
    # 定义
        # def 函数名(形参):
            # 在函数中执行的代码
            # return 返回值
    # 调用
        # 函数名(实参)
    # 返回值
        # return的作用
            # 1.结束一个函数
            # 2.返回值给调用者
    # 参数
        # 站在调用者（实参）角度
            # 按照位置传参数   : 1,2,3    *(1,2,3)
            # 按照关键字传参数 :a=1,b=2   **{'a':1,'b':2}
            # 按照位置和关键字传参数 : 1,2,c='r'
        # 站在定义者(形参)角度
            # 位置参数 *args 默认参数 **kwargs
    # 命名空间和作用域
        # 命名空间
            # 内置命名空间
            # 全局命名空间
            # 局部命名空间
        # 作用域
            # 全局作用域:内置命名空间\全局命名空间
            # 局部作用域:内置命名空间\全局命名空间\局部命名空间
                # 在局部函数中是不可以修改全局变量的
                # global关键字完成修改 -- 尽量少用
    # 函数的嵌套调用:调用和返回值的问题
    # 高阶函数
        # 函数的嵌套定义
        # 定义在内层的函数如何被调用
    # global和nonlocal
        # global关键字完成修改 -- 尽量少用
        # nonlocal只能在二阶函数中用，能够改变内层函数的外一层函数中变量的值



















