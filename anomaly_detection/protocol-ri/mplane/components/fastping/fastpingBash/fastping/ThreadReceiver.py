#!/usr/bin/env python

import logging
from PingListener import PingListener
import threading,time,sys

class ThreadReceiver (threading.Thread):
    #id, name, sharedVariable, lock
    def __init__(self, threadID, name,event,shared):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.shared=shared
        self.receive=PingListener(shared)
        logging.basicConfig(filename='fastPing.log',level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')#credo si possa passare come argomento a tutti e 3
        self.event=event   



    def run(self):
        print "Starting " + self.name
        self.receive.initialize()
        self.shared.check_killed("Receiver",self.event)     
        self.receive.state_sync()
        self.shared.check_killed("Receiver",self.event)      
        while  not self.shared.finishCycle:                   
            self.receive.state_listen()  
            #print time.time()-a            
            self.shared.check_killed("Receiver",self.event)           
        print "Receiver: Finished"
       
