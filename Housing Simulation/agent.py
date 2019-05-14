__author__ = 'julian'

import numpy as np
from house import House

class Agent():

    agent_count = 0

    def __init__(self, endowment):

        self.id = Agent.agent_count + 1
        self.endowment = endowment
        self.house = None
        self.decisions = []
        self.time_decisions = []

        Agent.agent_count += 1

        #print 'Agent %d created' %(self.id)
    '''
    Random decisions with a given probability "prob" of non-accept (0)
    '''
    def doRandomDecisions(self, num_rounds, prob):
        self.decisions = np.random.choice([0, 1], size=num_rounds, p=[prob, 1-prob])
        self.time_decisions = np.random.rand(num_rounds)*10

    '''
    Total agents created
    '''
    def countAgents(self):
        print "Total Agents %d" % Agent.agent_count

    '''
    Display agents informations
    '''
    def displayAgent(self):
        print 'id: %d' %(self.id)
        print 'endowment: %d' %(self.endowment)
        print 'decisions: %s' %(self.decisions)
        print 'time_decisions: %s' %(self.time_decisions)

        if self.house: print 'house: %d' %(self.house.id)

    '''
    Update endowment
    '''
    def updateEndowment(self, value):
        self.endowment += value
        print "New endowment : %.2f" %(self.endowment)



