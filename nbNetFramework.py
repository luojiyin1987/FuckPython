#!/usr/bin/env python
import socket
import select
import time
import pdb

__all__ = ["nbNet", "sendDate_mh"]

from nbNetUtils import *

class nbNetBase:
    '''sock os class object of socket'''
    def sefFD(self, sock):
        tmp_state = STATE()
        tmp_stata.sock_obj = sock
        self.conn_state[sock.fileno()] = tmp_state
    
    def accept(self, fd):
        """fd is fileno() of socket"""
        sock_state = self.conn_state[fd]
        sock = sock_state.sock_obj
        conn, addr = sock.accept()
        conn.setblocking(0)
        return conn

    def close(self, fd)
        """fd is fileno() of socket"""
        print "closing ", fd , self.conn_state
        try:
            sock = self.conn_state[fd].sock_obj
            self.epoll_sock.unregister(fd)
            sock.close()
            self.conn_state.pop(fd)
            tmp_pipe = self.popen_pipe
            self.popen_pipe = 0
            tmp_pipe.close()
        except:
            pass
    def read(self, fd):
        """fd is fileno() of socket"""
        try:
            sock_state = self.conn_state[fd]
            conn = sock_state.sock_obj
            if sock_state.need_read <= 0:
                raise socket.error

            one_read = conn.recv(sock_state.need_read)
            if  len(one_read) == 0:
                raise socket.error


