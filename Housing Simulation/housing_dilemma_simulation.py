__author__ = 'julian'

from agent import Agent
from house import House
from dilemma import Dilemma

if __name__ == '__main__':

    print '---- Running Housing Dilemma Simulation ----'

    num_agents = 6
    num_houses = 6
    num_rounds = 12
    prob = .5 # probability of non-zero decisions
    price_diff = 1.10 # increment of 10%

    num_sim = 100 # number of simulation

    endowments = 1200
    house_price_average = 700

    agents = []
    houses = []


    '''
    Outputs:
    final_rounds = []
    '''

    final_rounds = []

    for i in range(num_sim):
        '''
        Creation of 'num_agents' agents
        '''
        for a in range(num_agents):

            agent = Agent(endowments)
            agent.doRandomDecisions(num_rounds, prob) # Agents with random selections
            agents.append(agent)

        '''
        Creation of 'first house'
        '''
        house = House(house_price_average) # first house

        '''
        Create dilemma
        '''
        dilemma = Dilemma(num_rounds, num_houses)
        dilemma.runDilemma(agents, house, price_diff)

        print '<<<<<<<<<< End Dilemma >>>>>>>>>>'

        final_rounds.append(dilemma.final_round)


    print final_rounds


