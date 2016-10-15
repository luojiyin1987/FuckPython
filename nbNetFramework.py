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
                
            sock_state.buf_read +=one_read
            sock_state.have_read +=len(one_read)
            sock_state.need_read -=len(one_read)

            if sock_state.have_read == 10:
                head_said_need_read = int(sock_state.buff_read)
                if header_said_need_read <=0:
                    raise socket.error
                sock_state.need_read += header_said_need_read
                sock_state.buff_read=''
                return  "readcounttent"
            elif sock_state.need_read ==0:
                return "process"
            else:
                return "readmore"
        except(socket.error,ValueError),msg:
            try:
                if msg.errno == 11:
                    return "retry"
            except:
                pass
            return "closing"

    def write(self, fd):
        sock_state = self.comm_state[fd]
        conn = sock_state.sock_obj

        if  isinstance(sock_state.popen_pipe, file):
            try:
                output = sock_state.popen_pipe.read()
            except(IOError, ValueError),msg
                pass
        else:
            last_have_send = sock_state.have_write
            try:
                have_send = conn.send(sock_state.buff_write[last_have_send:])
                sock_state.have_write += have_send
                sock_state.need_write -= have_send
                if sock_state.need_write == 0  and  sock_state.have_write !=0:
                    return "writecomplete"
                else:
                    return "writemore"
            except socket.error, msg:
                return "closing"
    def run(self):
        while True:
            epoll_list = self.epoll_sock.poll()
            for fd , events in epoll_list:
                print self.conn_state
                print fd, events
                sock_state = self.conn_state[fd]
                if select.EPOLLHUP & events:
                    sock_state.state = "closing"
                elif select.EPOLLERR & events:
                    sock_state.state = "closing"
                self.state_machine(fd)

    def state_machine(self, fd):
        sock_state = self.conn_state[fd]
        self.sm[sock_state.state](fd)

class nbNet(nbNetBase):
    def __init__(self, addr, port, logic):
        self.conn_state = {}
        self.listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.listen_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listen_sock.bind(addr, port)
        self.listen_sock.listen(10)
        self.setFd(self.listen_sock)
        self.epoll_sock = select.epoll()

        self.epoll_sock.register(self.listen_sock.fileno(), select.EPOLLIN)
        self.logic = logic
        self.sm = {
            "accept" : self.accept2read,
            "read"   : self.read2process,
            "write"  : self.write2read,
            "process": self.process,
            "closing": self.close,
        }

    def process(self, fd):
        sock_state = self.conn_state[fd]
        response = self.logic(fd, sock_state.buff_read)
        if  response == None:
            conn = sock_state.sock_obj
            self.setFd(conn)
            self.conn_state[fd].state = "read"
            self.epoll_sock.modify(fd, select.EPOLLIN)
        else:
            sock_state.buff_write = "010d%s" %(len(response), response)
            sock_state.need_write = len(sock_state.buff_write)


            sock_state.state= "write"
            self.epoll_sock.modify(fd, select.EPOLLOUT)

    def accept2read(self, fd):
        conn = self.accept(fd)
        self.epoll_sock.register(conn.fileno(), select.EPOLLIN)
        self.setFd(conn)
        self.conn_state[conn.fileno()].state = "read"

    def read2process(self,fd):
        read_ret = ""
        try:
            read_ret = self.read(fd)
        except(Exception),msg:
            read_ret = "closing"
        if read_ret == "process":
            self.process(fd)
        elif read_ret =="readcontent"
            pass
        elif read_ret =="readmore":
            pass
        elif read_ret == "retry":
            pass
        elif read_ret =="closing":
            self.conn_state[fd].state = 'closing'
            self.state_machine(fd)
        else:
            raise Exception("impossible state returned by self.read")

    def write2read(self, fd):
        try:
            write_ret = self.write(fd)
        except socket.error, msg:
            write_ret = "closing"
        
        if write_ret == "writemore":
            pass
        elif write_ret =="writecomplete":
            sock_state = self.conn_state[fd]
            conn = sock_state.sock_obj
            self.setFd(conn)
            self.conn_state[fd].state = "read"
            self.epoll_sock.modify(fd, select.EPOLLIN)
        elif write_ret =="closing":
            self.conn_state[fd].state = "closing"
            self.state_machine(fd)

counter = 0
if __name__ '__main__':
    def logic(d_in):
    global counter
    counter += 1
    if counter % 100000 == 0:
        print counter, time.time()
    return("a")

    reverseD = nbNet('0.0.0.0',9090,logic)
    reverseD.run()
        
            


