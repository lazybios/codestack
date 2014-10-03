#!/usr/bin/python
# coding:utf-8

class FiniteStateMachine:
    def __init__(self):
        self.handlers = {}
        self.startState = None
        self.endStates = []

    def add_state(self,name,handler,end_state=0):
        name = name.upper()
        self.handlers[name] = handler
        if end_state:
            self.endStates.append(name)

    def set_start(self,name):
        self.startState = name.upper()

    def run(self,state,inpt):
        try:
            handler = self.handlers[state.upper()]
        except:
            raise InitializationError("must call has a start state")
        #cause of has expire tiem so unnecessary end state limited
        return handler(inpt)

