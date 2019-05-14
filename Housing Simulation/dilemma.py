__author__ = 'julian'

from agent import Agent
from house import House

class Dilemma():

    dilemma_count = 0
    final_round = 0

    def __init__(self, num_rounds, num_houses):

        self.id = Dilemma.dilemma_count + 1
        self.round = 0
        self.final_round = None # Final round with rented houses
        self.number_rented_house = 0 # Number of rented houses

        self.num_rounds = num_rounds
        self.num_houses = num_houses


    def runDilemma(self, agents, house, price_diff):

        self.house = house
        self.agents = agents

        for r in range(self.num_rounds):
            is_rented = self.doActions(r)

            if (is_rented): # increment o decrement function of the last action
                new_price = self.house.price * price_diff
                self.house = House(new_price)

            else:
                new_price = self.house.price / price_diff
                self.house.price = new_price


    def doActions(self, round):

        self.round = round

        idx_renter = None # index_renter
        is_rented = False

        #print '---- Round %d ----' %(round)

        for index, a in enumerate(self.agents):

            if a.decisions[round] == 1 and a.house is None:

                # First choice
                if idx_renter is None:
                    idx_renter = index

                if self.agents[idx_renter].time_decisions[round] > a.time_decisions[round]:
                    idx_renter = index

        if idx_renter is not None:
            is_rented = True

            self.agents[idx_renter].house = self.house
            self.agents[idx_renter].endowment = self.agents[idx_renter].endowment - self.house.price

            self.number_rented_house += 1

            if self.number_rented_house == self.num_houses:
                self.final_round = self.round

            print '<<<<<<<<<< Round %d >>>>>>>>>>' %(round)
            self.agents[idx_renter].displayAgent()

        else:
            'Non-agent'

        return is_rented







