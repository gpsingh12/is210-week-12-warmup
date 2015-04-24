#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    """CustomLogger represents a simple logging class.
    Attributes:
        None
    """

    def __init__(self, logfilename):
        """Constructor for CustomLogger class.
        Args:
            logfilename(str): input string value
        Attributes:
            logfile(str):input string value
            msgs(str):messages stored
        """
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """Function log the error encountered while opening a file.
        Args:
            msg(str): message while file does not open
            timestamp: defaults to None
        Return:
            return log error if file does not open
        """
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """Function opens files and stores messages.
        Args:
            None
        Return:
            returns the erros if the file can not be opened.
        """
        handled = []
        try:
            fhandler = open(self.logfilename, 'a')
            for index, entry in enumerate(self.msgs):
                fhandler.write(str(entry) + '\n')
                handled.append(index)

            fhandler.close()
        except (IOError, self.log(IOError)):
            print "file can't be opened"
            raise IOError

        for index in handled[::-1]:
            del self.msgs[index]
