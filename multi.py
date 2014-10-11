from tasks import IVTask
from tasks import EVTask
import multiprocessing

class Consumer(multiprocessing.Process):
    def __init__(self, task_queue, result_queue):
        multiprocessing.Process.__init__(self)
        self.task_queue = task_queue
        self.result_queue = result_queue

    def run(self):
        proc_name = self.name
        while True:
            next_task = self.task_queue.get()
            if next_task is None:
                self.task_queue.task_done()
                print("{}: Exiting.".format(proc_name))
                break
            print("{}: Starting {}.".format(proc_name, next_task))
            answer = next_task()
            self.task_queue.task_done()
            self.result_queue.put(answer)
        return

def setter():
    """Returns list of unique tuples of EVs and IVs"""
    ev_max = 252
    tasks = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()

    num_consumers = 7
    consumers = []
    for i in range(num_consumers):
        consumers.append(Consumer(tasks, results))
    for w in consumers:
        w.start()

    _min = 0
    num_tasks = 50
    for i in range(num_tasks):
        if _min+int(ev_max/num_tasks) <= ev_max:
            tasks.put(EVTask(_min, _min+int(ev_max/num_tasks)))
        else:
            tasks.put(EVTask(_min, ev_max+1))
        if i == num_tasks-1:
            tasks.put(EVTask(_min, ev_max+1))
        _min += int(ev_max/num_tasks)

    for i in range(7):
        tasks.put(None)

    tasks.join()
    
    ev_lists = []
    while num_tasks:
        ev_lists.append(results.get())
        num_tasks -= 1
    
    iv_max = 31
    tasks = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()

    num_consumers = 7
    consumers = []
    for i in range(num_consumers):
        consumers.append(Consumer(tasks, results))
    for w in consumers:
        w.start()

    _min = 0
    num_tasks = 31
    for i in range(num_tasks):
        if _min+int(iv_max/num_tasks) <= iv_max:
            tasks.put(IVTask(_min, _min+int(iv_max/num_tasks)))
        else:
            tasks.put(IVTask(_min, iv_max+1))
        if i == num_tasks-1:
            tasks.put(IVTask(_min, iv_max+1))
        _min += int(iv_max/num_tasks)

    for i in range(7):
        tasks.put(None)

    tasks.join()

    iv_lists = []
    while num_tasks:
        iv_lists.append(results.get())
        num_tasks -= 1
    
    return ev_lists, iv_lists

