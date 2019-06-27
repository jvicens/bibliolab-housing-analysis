__author__ = 'julian'

from agent import Agent
from house import House
from dilemma import Dilemma

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def showFinalSession(dilemmas):
    for d in dilemmas:
        d.displaySession()
        #d.displaySessionById(2)

def calculateAveragePrice(dilemmas):
    prices = []
    ids_dilemma = []
    prices_average = []
    for d in dilemmas:
        prices.append(d.priceHousesRented())
        ids_dilemma.append(d.id)
        prices_average.append(np.mean(d.priceHousesRented()))

    df_prices_dilemma = pd.DataFrame({'id_dilemma': ids_dilemma,
                                      'prices': prices,
                                      'prices_average': prices_average})

    return df_prices_dilemma['prices_average'].mean(), df_prices_dilemma['prices_average'].std()

def plot_evolution_average_price_simulation(x,y,error,limits):

    plt.clf()
    plt.figure(figsize=(5,5))

    # example data
    # example error bar values that vary with x-position
    # error bar values w/ different -/+ errors
    #lower_error = [e/2 for e in error]
    #upper_error = [e/2 for e in error]
    #asymmetric_error = [lower_error, upper_error]
    #plt.errorbar(x, y, asymmetric_error, fmt='o', markersize=6, capsize=3, capthick=1, elinewidth=1, ecolor='black', color='black', markeredgecolor = 'none')

    plt.ylim(limits[1], limits[0])

    plt.plot(x, y, markersize=6, color="black", markeredgecolor = 'none')
    plt.title('')

    plt.savefig('plots/evolution_average_price_simulation.png')

if __name__ == '__main__':

    print '---- Running Housing Dilemma Simulation ----'

    num_agents = 6
    num_houses = 6
    num_rounds = 12
    prob = .5 # probability of do not rent a house (zero decisions)
    price_diff = 1.05 # increment of 5%
    treatment = True

    num_sim = 2000 # number of simulation

    endowments = 1000
    house_price_average = 500
    high_limit = house_price_average * 1.15 # upper limitation 15%
    low_limit = house_price_average * 0.85 # lower limitation 15%


    ##### Fort Pienc #####
    # house_price_average = 873
    # endowments = 1943
    # high_limit = 1004
    # low_limit = 742

    ##### Granollers #####
    # house_price_average = 560
    # endowments = 1933
    # high_limit = 645
    # low_limit = 477

    ##### Olesa #####
    house_price_average = 570
    endowments = 1643
    high_limit = 655
    low_limit = 485

    '''
    Results
    -------
    dilemmas: all the information for each dilemma / session of game
    avg_rent_prices_accumulated and std_rent_prices_accumulated: average price accumulated in each simulation
    '''
    dilemmas = []
    avg_rent_prices_accumulated = []
    std_rent_prices_accumulated = []

    for i in range(num_sim):
        '''
        Creation of 'num_agents' agents
        '''
        agents = []

        for a in range(num_agents):

            agent = Agent(endowments)
            agent.doRandomDecisions(num_rounds, prob) # Agents with random selections
            agents.append(agent)

        '''
        Creation of 'first house'
        '''
        house = House(house_price_average, 0) # first house

        '''
        Create and run dilemma
        '''
        dilemma = Dilemma(num_rounds, num_houses)
        if treatment:
            dilemma.runDilemma(agents, house, price_diff, treatment, high_limit=high_limit, low_limit=low_limit)
        else:
            dilemma.runDilemma(agents, house, price_diff, treatment)
        dilemmas.append(dilemma)

        # Show evolution of price in each dilemma
        # dilemma.displaySession()

        # Average price and standard deviation in all the simulations (len=num_sim)
        avg, std = calculateAveragePrice(dilemmas)
        avg_rent_prices_accumulated.append(avg)
        std_rent_prices_accumulated.append(std)

        if i % 100 == 0:
            print 'n=%d -> mean= %.2f, std= %.2f' %(i, avg, std)

    # Show evolution all dilemmas
    # showFinalSession(dilemmas)

    # Evolution of average price in each simulation/session
    plot_evolution_average_price_simulation(range(0, num_sim), avg_rent_prices_accumulated, std_rent_prices_accumulated, [high_limit, low_limit])


