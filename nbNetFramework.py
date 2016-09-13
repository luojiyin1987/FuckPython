#!/usr/bin/env python
# coding:utf-8

from daemon import daemon
import socket
import select
import time
import import pdb

__all__ =["nbNet", "sendDate_mh"]
//DEBUG = True

from nbNetUtils import *

class nbNetBase:
    '''non-blocking Net'''
    def setFd(self, sock):
        """sock is class object of socket"""
        #dbgPrint("\n --setFd start!")
        tmp_state = STATE()
        tmp_state.sock_obj = sock
        self.conn_state[sock.fileno()] = tmp_state
        #self.conn_state[sock.fileno()].printState()
        #dbgPrint("\n --setFd end!")

    def accept(self, fd):
        """fd is fileno() of socket"""
        #dbgPrint("\n --accept start!")
        sock_state = self.conn_state[fd]
        sock = sock_state.sock_obj
        conn, addr = sock.accept()
        # set to non-blocking :0
        conn.setblocking(0)
        return conn

    def close(self, fd):
        """fd is fileno() of socket"""
        #pdb.set_trace()
        print "closing", fd, self.conn_state
        try:
            # cancel of listen to event
            sock = self.conn_state[fd].sock_obj
            self.epoll_sock.unregister(fd)
            sock.close()
            self.conn_state.pop(fd)
            tmp_pipe = self.popen_pipe
            self.popen_pipe = 0
            tem_pipe.close()
        except:
            #dbgPrint("Close fd: %s abnormal" %fd)
            pass
    #@profile
    def read(self, fd):
