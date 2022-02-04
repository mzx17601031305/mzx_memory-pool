import  threading
import  time
def fun_1(num):
    for i in range(num):
        print('我是线程1')
        time.sleep(1)

def fun_2(num):
    for i in range(num):
        print('我是线程2')
        time.sleep(2)

#
if __name__ == '__main__':
    # fun_1()
    # fun_2()
    fun1_thread = threading.Thread(target=fun_1,args=(3,))
    fun2_thread = threading.Thread(target=fun_2,args=(3,))

    fun1_thread.start()
    fun2_thread.start()