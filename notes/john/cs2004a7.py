#!/usr/bin/env python3
from array import array
from itertools import chain
from threading import Thread, get_ident, Lock 
from random import randint
from time import sleep

mutexlock = Lock()
MIN_PID = 300
MAX_PID = 5000
pids = array('I', )
# last_pid = MIN_PID
last_pid = 0
def allocate_map():
    global last_pid
    if len(pids) == 0:
        last_pid = MIN_PID
        return 1
    return -1

def allocate_pid():
    global last_pid
    search_list = chain(range(last_pid, MAX_PID+1), range(MIN_PID, last_pid)) 
    for i in search_list:
        if i not in pids:
            pids.append(i)
            last_pid = i
            return(i)
    return(-1)

def release_pid(pid):
    pids.remove(pid)

def runner():
    global mutexlock
    mypid = allocate_pid()
    # print("Starting thread %d", get_ident()) 
    print(f"Got PID: {mypid}") 
    sleep(randint(0,10))
    # print("End of thread %d", get_ident()) 
    release_pid(mypid)
    print(f"Released PID: {mypid}")
    mutexlock.release()

if __name__ == "__main__":
    allocate_map()
    tids = []
    
    for i in range(22):
        
        tid = Thread(target=runner, )
        tids.append(tid)
        mutexlock.acquire()
        tid.start()
        

    for tid in tids: 
        tid.join()