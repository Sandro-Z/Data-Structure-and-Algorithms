import random
from pythonds3.basic import Queue

class Printer:
    def __init__(self,ppm):
        self.page_rate=ppm
        self.current_task=None
        self.time_remaining=0

    def tick(self):#打印1秒的操作
        if self.current_task!=None:
            self.time_remaining-=1
            if self.time_remaining<=0:self.current_task=None

    def busy(self):
        return self.current_task!=None

    def start_next(self,new_task):
        self.current_task=new_task
        self.time_remaining=new_task.get_pages()*60/self.page_rate

class Task:
    def __init__(self,time):
        self.timestamp=time
        self.pages=random.randint(1,20)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self,current_time):
        return current_time-self.timestamp

def simulation(num_seconds,pages_per_minute):
    lab_printer=Printer(pages_per_minute)
    print_queue=Queue()
    waiting_times=[]

    for current_second in range(num_seconds):
        if new_print_task():
            task=Task(current_second)
            print_queue.enqueue(task)
        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            nexttask=print_queue.dequeue()
            waiting_times.append(nexttask.wait_time(current_second))
            lab_printer.start_next(nexttask)

        lab_printer.tick()

    average_wait=sum(waiting_times)/len(waiting_times)
    print("Average wait {0:.2f} secs {1} tasks remaining".format(average_wait,print_queue.size()))

def new_print_task():
    num=random.randint(1,180)
    return num==180

for i in range(10):simulation(3600,10)