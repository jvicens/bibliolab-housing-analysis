__author__ = 'julian'

class House():

    house_count = 0

    def __init__(self, average_price):

        self.id = House.house_count + 1
        self.price = average_price
        self.renter = None
        self.round_rented = 0

        House.house_count +=1

        #print 'House %d created' %(self.id)

    def countAgents(self):
        print "Total House %d" % House.agent_count

    def updateRenting(self, renter, round):
        self.renter = renter
        self.round_rented = round

        print "Renter" %(self.id_renter)
        print "Round" %(self.round_rented)




