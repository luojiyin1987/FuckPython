#!/usr/bin/env python
#coding:utf-8

import socket
import select
import time
import pdb

__all__ = ["nbNet", "sendata_mh"]
#DEBUG = True

class nbNetBase:
    '''non-blocking Net'''
    def setFd(self, sock):
        """sock is class object of socket"""
        #dbgPrint("\n --setFd start!")
        tmp_state = STATE()
        tmp_state.sock_obj = sock
        self.conn_state[sock.fileno()] = tmp_state
        #self.conn_state[sock.fileno()].printState()
        #dbgPrint("\n --setFd end")

    def accept(self, fd):
        """fd is fileno() of socket"""
        #dbgPrint("\n --accept start")
        sock_state = self.conn_state[fd]
        sock = sock_state.sock_obj
        conn, addr = sock.accept()
        conn.setblocking(0)
        return conn
    
    def close(self, fd ):
        """fd is fileno() of socket"""
        #pdb.set_trace()
        print "closing", fd, self.conn_state
        try:
            # cancal of listen to event
            sock = self.conn_state[fd].sock_obj
            self.epoll_sock.unregister(fd)
            sock.close()
            self.conn_state.pop(fd)
            tmp_pipe = self.popen_pipe
            self.popen_pipe = 0
            tem_pip.close()
        except:
            pass
     #@profile
     def read(self, fd):
        """fd is fineno() of socket"""
        #pdb.set_trace()
        try:
            sock_state = self.conn_state[fd]
            conn = sock_state.sock_obj
            if sock_state.need_read <= 0:
                raise socket.error

            one_read = conn.recv(sock_state.need_read)
            #dbgPrint("\tread func fd: %d, one_read: %s,need_read:%d" %(fd, one_read, sock_state.need_read))
            if len(one_read) == 0:
                raise socket.error
            #process recevied date
            sock_state.buff_read += one_read
            sock_state.have_read += len(one_read)
            sock_state.need_read -= len(one_read)
            #sock_state.printState()

            #read  protocal header
            if sock_state.have_read == 10:
                header_said_need_read = int(sock_state.buff_read)
                if header_said_need_read <= 0:
                    raise socket.error
                sock_state.need_read += header_said_need_read
                sock_state.buff_read = ''
                #call state machine, current state is read
                #after protocal header haven readed, read the real cmd content
                #call machine instead if call read() it self in common
                #sock_state.printState()
                return "readcontent"
            elif sock_state.need_read == 0:
            #recv complete, change state to process it 
                return "process"
            else:
                return "readmore"
        except (socket.error, ValueError),msg:
            try:
                if msg.errno == 11 :
                    #dbgPrint("11" + msg)
                    return "retry"
            except:
                pass
            return 'closing' 
    
    #@profile
    def write(self ,fd)
        sock_state = self.conn_state[fd]
        conn = sock_state.sock_obj
        #pdb.set_trace()

        if isinstance(sock_state.popen_pipe, file):
            try:
                output = sock_state.popen_pipe.read()
                #print output
            except:(IOError, ValueError), msg:
                pass
            #have_send = conn.send("%010d%s" %(len(output), output))
        else:
            last_have_send = sock_state.have_write
            try:
                #to send some Bytes, but have_send is the return num of send()
                have_send = conn.send(sock_state.buff_write[last_have_send:])
                sock_state.have_write += have_send
                sock_state.need_write -= have_send
                if sock_state.need_write == 0 and sock_state.have_write != 0:
                #send complete, re init status, and listen re-read
                #sock_state.printState()
                #dbgPrint('\n write data completed!')
                return "writecomplete"
            else:
                return "writemore"
        except socket.error, msg:
            return "closing"

    def run(self):
        while True:
            #dbgPrint("\nrun func loop:")
            #print conn_state
            #for i in self.conn-state.iterkeys():
                #dbgPrint("\n -state of fd: %d" %i)
                #self.conn_state[i].printState()

            epoll_list = self.epoll_sock.poll()
            for fd, envents in epoll_list:
                #dbgPrint('\n-- run epoll return fd: %d. event:%s' %(fd, events))
                print self.conn_state
                print fd , events
                sock_state = self.conn_state[fd]
                if select.EPOLLHUP & events:
                    #dbgPrint("EPOLLHUP")
                    sock_state.state = "closing"
                elif select.EPOLLEER & events:
                    #dbgPrint("EPOLLERR")
                    sock_state.state = "closing"
                self.state_matchine(fd)

    def state_machine(self, fd)
        #time.sleep(0.1)
        #dbgPrint("\n - state machine: fd: %d, status: %s"(fd, self.conn_state[fd].state))
        sock-state = self.conn_state[fd]
        self.sm[sock_state.state](fd)

class nbNet(nbNetBase):
    def __init__(self, addr, port , logic):
        #dbgPrint('\n__init__: start!')
        self.conn_state = {}
        self.listen_sock =socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
        self.listen_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listen_sock.bind((addr, port))
        self.listen_sock.listen(10)
        self.setFd(self.listen_sock)
        self.epoll_sock = select.epoll()
        #LT for default, ET add ' | select.EPOLLET'
        self.epoll_sock.register(self.listen_sock.fileno(), select.EPOLLIN )
        self.logic = logic
        self.sm ={
            "accept" : self.accept2read
            "read"   : self.read2process
            "write"  : self.process
            "closing": self.close
            }
            #dbgPrint('\n__init__: end, register no:%s' %self.listen_sock.fileno())
        





