__author__ = 'julian'

from agent import Agent
from house import House

import pandas as pd

class Dilemma():

    dilemma_count = 0

    def __init__(self, num_rounds, num_houses):

        self.id = Dilemma.dilemma_count + 1
        self.round = 0
        self.final_round = None # Final round with rented houses
        self.number_rented_house = 0 # Number of rented houses

        self.num_rounds = num_rounds
        self.num_houses = num_houses

        self.house = None

        self.agents = []
        self.houses = []

        self.treatment = None
        self.high_limit = None
        self.low_limit = None

        Dilemma.dilemma_count +=1

    # Running the dilemma
    def runDilemma(self, agents, house, price_diff, treatment, **kwargs):

        self.high_limit = kwargs.get('high_limit', None)
        self.low_limit = kwargs.get('low_limit', None)

        self.house = house # first house of the session
        self.agents = agents # all agents in the session
        self.treatment = treatment # treatment of the session

        for r in range(self.num_rounds):
            # in each round do actions
            is_rented, renter = self.doActions(r)

            if is_rented: # increment o decrement function of the last action
                self.house.rounds_rented.append(1)
                # In case apply the treatment and the price get the limit we continue with the same price, else we
                # increment the price
                if self.treatment:
                    if self.house.price * price_diff > self.high_limit:
                        new_price = self.house.price
                    else:
                        new_price = self.house.price * price_diff
                else:
                    new_price = self.house.price * price_diff

                self.house = self.house.updateRenting(renter, r+1)
                self.houses.append(self.house)

                # Create a new house
                self.house = House(new_price, r+1)

            else:
                self.house.rounds_rented.append(0)
                # In case apply the treatment and the price get the limit we continue with the same price, else we
                # decrease the price
                if self.treatment:
                    if self.house.price / price_diff < self.low_limit:
                        new_price = self.house.price
                    else:
                        new_price = self.house.price / price_diff
                else:
                    new_price = self.house.price / price_diff

                self.house.price = new_price
                self.house.prices.append(new_price)
                self.house.rounds.append(r+1)

        #print 'End dilemma'

    def doActions(self, round):

        self.round = round # current round

        idx_renter = None # index_renter
        is_rented = False

        # print '---- Round %d ----' %(round+1)

        # actions for each agent
        for index, a in enumerate(self.agents):

            # agent want to rent and agent has no house
            if a.decisions[round] == 1 and a.house is None:

                # In case of first round
                if idx_renter is None:
                    idx_renter = index
                # In the other cases get the house the faster
                if self.agents[idx_renter].time_decisions[round] > a.time_decisions[round]:
                    idx_renter = index

        # house rented in this round
        if idx_renter is not None:

            is_rented = True # house is rented

            self.agents[idx_renter].house = self.house
            self.agents[idx_renter].endowment = self.agents[idx_renter].endowment - self.house.price

            self.number_rented_house += 1

            if self.number_rented_house == self.num_houses:
                self.final_round = self.round

            #print '<<<<<<<<<< Round %d >>>>>>>>>>' %(round+1)
            #self.agents[idx_renter].displayAgent()
            return is_rented, self.agents[idx_renter]

        else:
            'Non-agent'
            return is_rented, None


    def displaySession(self):
        print 'Session %d' %(self.id)
        for h in self.houses:
            #h.displayHouse()
            h.displayPriceEvolution()

    def displaySessionById(self, id):
        if self.id == id:
            print 'Session %d' %(self.id)
            for h in self.houses:
                #h.displayHouse()
                h.displayPriceEvolution()

    def priceHousesRented(self):
        prices = []
        for h in self.houses:
            if h.renter is not None:
                prices.append(h.price)
        return prices




