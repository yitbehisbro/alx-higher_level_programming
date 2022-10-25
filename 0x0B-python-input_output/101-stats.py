#!/usr/bin/python3
""" Log parsing module """
import sys


class LogParsing:
    """ Reads stdin line by line and computes metrics """
    def __init__(self):
        """ Initalization method """
        self.dic = {}
        self.size = 0

    def create_dic(self):
        """ Initialization of dict """
        self.dic['200'] = 0
        self.dic['301'] = 0
        self.dic['400'] = 0
        self.dic['401'] = 0
        self.dic['403'] = 0
        self.dic['404'] = 0
        self.dic['405'] = 0
        self.dic['500'] = 0

    def create_status_code(self, status):
        """ Creates repeated number to the status code """
        if status in self.dic:
            self.dic[status] += 1

    def display(self, sig=0, frame=0):
        """ Print status code """
        print("File size: {:d}".format(self.size))
        for key in sorted(self.dic.keys()):
            if self.dic[key] != 0:
                print("{}: {:d}".format(key, self.dic[key]))


if __name__ == "__main__":
    log = LogParsing()
    log.create_dic()
    nlines = 0

    try:
        for line in sys.stdin:
            if nlines % 10 == 0 and nlines != 0:
                log.display()

            try:
                list_line = [x for x in line.split(" ") if x.strip()]
                log.create_status_code(list_line[-2])
                log.size += int(list_line[-1].strip("\n"))
            except Exception:
                pass
            nlines += 1
    except KeyboardInterrupt:
        log.display()
        raise
    log.display()
