# input :
    # recv recvfrom input read load
# output:
    # send sendto print write dump
# 输入输出是不占用CPU的
# 计算机是多少cpu : 4c 8c 16c
# 纯计算 :就是不涉及任何输入输出,单纯对内存中数据进行操作
# 只要涉及到输入输出都要占一大笔时间
    # 7200r : 7200转每分钟
    # 从硬盘上找到一个数据的时间 0.9ms = 0.0009s
    # 0.3s
# CPU指令的计算速度 500000000 = 5亿 每一秒钟可以执行5亿条指令
# 50000 * 9s = 45w
# 读一次硬盘的时间够CPU执行45w条指令了

# pycharm qq EV录屏 浏览器 飞秋 360 vnc 搜狗输入法
# n多程序同时工作在计算机中,这些程序都需要CPU处理
    # 1.CPU如何为超过本身个数的服务们提供服务
    # 2.服务于服务之间是怎么分配的内存
# 所有的程序在没执行起来之前叫程序\文件,执行起来之后叫进程
# 什么叫做进程process? 进行中的程序
# 每一个进程在运行的过程中会被分配一块属于他自己的内存,进程之间的内存隔离
# CPU在多个进程之间进行轮转执行进程的任务
# 如果两个进程在CPU上同时被执行 -- 并行
# 如果两个进程看起来是同时执行的,但实际上在一块儿CPU上轮流被执行 -- 并发

# 进程 : 内存的隔离
# 线程 : 具体代码的执行进度
# 协程










