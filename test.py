import threading
import logging

class LoopTest():
        loop = True
        def do_loop(self):
            while self.loop:
                print(self.loop)
            print("Getting out")

        def thread_loop(self):
            x = threading.Thread(target = self.do_loop)
            x.start()
            y=threading.Thread(target = self.update)
            y.start()
        def update(self):
            s = input("Enter value to exit")
            if s:
                self.loop=False

if __name__ == "__main__":
    y = LoopTest()
    y.thread_loop()
