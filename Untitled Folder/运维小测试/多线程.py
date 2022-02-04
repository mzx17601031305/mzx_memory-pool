import multiprocessing
import time
import os

# def fun_1(num):
#     while 1:
#         for i in  range(num):
#             print('我是进程1',os.getpid())
#             time.sleep(0.5)
#
#
# def fun_2(num):
#     while 1:
#         for i in range(num):
#             print('我是进程2',os.getpid())
#             time.sleep(0.5)
#
#
#
# if __name__ == '__main__':
#     print('主进程',os.getppid())
#     test_1 = multiprocessing.Process(target=fun_1,args=(3,))
#     test_2 = multiprocessing.Process(target=fun_2,kwargs={'num':2})
#     test_1.start()
#     test_2.start()

def work():
    for i in range(10):
        print('工作中····')
        time.sleep(0.2)

if __name__ == '__main__':
    work_mul = multiprocessing.Process(target=work)
    work_mul.daemon = True
    work_mul.start()
    time.sleep(1)
    print('主进程提醒。。')
