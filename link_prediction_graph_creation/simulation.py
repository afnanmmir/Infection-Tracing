#########################################
#         Problem 1 Skeleton Code
#########################################
 
#     A) plot the SIR vs time for the seed being highest degree
#     B) plot SIR vs time for  random
#     C) propose and implement your own mitigation technique
#     Note: you can change the function arguments, however 
#     keep the Simulation Parameters the same for parts A and B.

#########################################
import networkx as nx 
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import operator
import time
import random

#########################################
#         Simulation Parameters
#########################################

DELTA_RECOVER = 7
DELTA_INFECT = 5
# p_transmit_virus = .015
p_transmit_virus = .3
SEED = .04

#########################################
#         Node and Infection Data
#########################################
node_data = dict()
# node_data = {node_id: [status, recovery_time]}

infection_data_random = []
suscipetible_data_random = []
recovered_data_random = []

total_infected = set()

#########################################
#         Utility Functions
#########################################

#converts a list of tuples into dictionary 
#(use this for G.degrees() if useful)
def convert_tuple_to_dict(list_of_tuples):
    my_dict = dict()
    for i,j in list_of_tuples:
        my_dict[i] = j
    return my_dict


#build scale free networks
def build_networks():
    networks = list()
    # iterate through all files in contact_graphs and create a networkx graph
    for i in range(1, 32):
        # read in the csv file
        date = '2020-07-' + str(i).zfill(2)
        target_file_location = f"contact_graphs/{date}.gexf"
        G = nx.read_gexf(target_file_location)
        networks.append(G)
    for i in range(1, 32):
        # read in the csv file
        date = '2020-08-' + str(i).zfill(2)
        target_file_location = f"contact_graphs/{date}.gexf"
        G = nx.read_gexf(target_file_location)
        networks.append(G)
    return networks

###########################################
#      Initialize the Population 
###########################################

def init_population(m, networks):
    
    #TODO: initialize a population of N nodes 
    global node_data
    node_data = dict()

    # nodes = networks[0].nodes()
    # not_vaccinated_people = []
    # # randomly vaccinate 20% of the population
    # for node in nodes:
    #     not_vaccinated_people.append(node)
    
    # m = int(len(not_vaccinated_people) * m)

    # set all nodes to be susceptible
    for network in networks:
        nodes = network.nodes()
        for node in nodes:
            node_data[node] = ['S', 0]
    # print("Total Nodes: ", len(node_data))
    init_infection_size = int(len(node_data) * m)

    # get 5 randomly chosen nodes
    nodes_random = random.sample(list(node_data.keys()), init_infection_size)
    # infect those nodes
    for node in nodes_random:
        # set node data 
        node_data[node] = ['I', DELTA_RECOVER]
        # add to total infected
        total_infected.add(node)

###########################################
#              SIR Simulation  
###########################################
 
def run_experiment(days,networks):
    
    for day in range(days):
        G = networks[day]

        #susceptible to infected
        # if day == time_to_recover, then recover the person
        infected = list()
        for node in node_data:
            if node_data[node][0] == 'I':
                infected.append(node)
        
        for person in infected:
            if person not in G.nodes():
                continue
            #get neighbors
            neighbors = list(G.neighbors(person))
            #for each neighbor: 
                #apply chance of infection
                #if chance <= p_transmit_virus:
                    #this node is now infected 
                    #set recovery time to day + DELTA_RECOVER
            for neighbor in neighbors:
                if node_data[neighbor][0] == 'S':
                    chance = random.random()
                    if chance <= p_transmit_virus:
                        node_data[neighbor] = ['I', DELTA_RECOVER + day]
                        total_infected.add(neighbor)

        #infected to recovered 
        #Transition infected people to recovered after DELTA_RECOVER days.

        for node in node_data:
            if node_data[node][0] == 'I':
                if node_data[node][1] == day:
                    node_data[node][0] = 'R'
        
        #count number of infected people
        countI = 0
        countR = 0
        countS = 0
        for node in node_data:
            if node_data[node][0] == 'I':
                countI += 1
            elif node_data[node][0] == 'R':
                countR += 1
            elif node_data[node][0] == 'S':
                countS += 1
        infection_data_random.append(countI)
        recovered_data_random.append(countR)
        suscipetible_data_random.append(countS)

###########################################
#              Plot Results  
###########################################

def plot_SIR():
    plt.figure()

    #plot infection vs day from part B
    plt.plot(infection_data_random, label='Infected')
    plt.plot(suscipetible_data_random, label='Susceptible')
    plt.plot(recovered_data_random, label='Recovered')

    #label your plot lines 
    plt.legend()
    plt.grid()
    plt.title("SIR vs Day")
    plt.xlabel("Day")
    plt.ylabel("Count")
    plt.show()
    
    return 


def main():
    
    #init experiment based on these parameters:
    days = 62
    m = 0.2

    networks = build_networks()
   
    #initialize population for random 5 nodes 
    init_population(m, networks)

    run_experiment(days, networks)

    print("Total Infected: ", len(total_infected))
    print("Max Infected on a single day: ", max(infection_data_random))
    print("Total People: ", len(node_data))

    #plot all infections vs time 
    plot_SIR()




if __name__ == '__main__':
    main()
