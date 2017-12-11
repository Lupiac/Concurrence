from common.map.case import Case
from threading import Semaphore


class LockCase(Case):

    def __init__(self, value):
        super(LockCase, self).__init__(value)
        self.sem = Semaphore(1)

    def lock(self):
        self.sem.acquire()

    def unlock(self):
        self.sem.release()
