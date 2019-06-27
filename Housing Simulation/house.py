__author__ = 'julian'

class House():

    house_count = 0

    def __init__(self, average_price, current_round):

        self.id = House.house_count + 1
        self.price = average_price
        self.renter = None
        self.round_rented = 0
        self.prices = []
        self.rounds = []
        self.rounds_rented = []
        self.prices.append(average_price)
        self.rounds.append(current_round)

        House.house_count +=1

        #print 'House %d created' %(self.id)

    def countAgents(self):
        print "Total House %d" % House.agent_count

    def updateRenting(self, renter, current_round):
        self.renter = renter
        self.round_rented = current_round

        return self

    def displayHouse(self):
        print 'House %d' % self.id
        print 'Price %d' % self.price
        print 'Round rented %d' % self.round_rented

    def displayPriceEvolution(self):
        for index, price in enumerate(self.prices):
            print 'Round %d (%d): House %d, %d euros' %(self.rounds[index], self.rounds_rented[index], self.id, self.prices[index])





