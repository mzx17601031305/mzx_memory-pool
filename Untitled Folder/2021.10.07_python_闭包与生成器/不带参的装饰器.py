'''
项目名称：2021.10.07_python_闭包与生成器
项目说明：2021.10.07_python_闭包与生成器
项目环境：python 3.9.7
作者所属：马梓轩
'''
#不带参
import time
def time1(fun):
    def timer():
        strat_time = time.time()
        fun()
        stop_time =time.time()
        print(strat_time-stop_time)
    return timer
@time1
def test1():
    time.sleep(2)
    print('aaa')
test1()


