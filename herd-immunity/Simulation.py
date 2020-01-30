import sys
import random
from Person import Person
from Virus import Virus
from FileWriter import FileWriter


class Simulation:
    def __init__(self, initial_vaccinated, initial_infected, initial_healthy,
                 virus, resultsfilename):
        '''Set up the initial simulation values'''

        self.virus = virus
        self.initial_infected = initial_infected
        self.initial_healthy = initial_healthy
        self.initial_vaccinated = initial_vaccinated

        self.population = []

        self.population_size = (initial_infected
                                + initial_healthy
                                + initial_vaccinated)

        self.total_dead = 0
        self.total_vaccinated = initial_vaccinated

        self.file_writer = FileWriter(resultsfilename)

    def create_population(self):
        '''Creates the population (a list of Person objects) consisting of initial
        infected people, initial healthy non-vaccinated people, and initial
        healthy vaccinated people. Adds them to the population list'''

        for i in range(self.initial_infected):
            person = Person(False, virus)
            self.population.append(person)

        for i in range(self.initial_healthy):
            person = Person(False, None)
            self.population.append(person)

        for i in range(self.initial_vaccinated):
            person = Person(True, None)
            self.population.append(person)

    def print_population(self):
        '''Prints out every person in the population and their
        current attributes'''
        for person in self.population:
            if person.is_vaccinated is True and person.infection is None:
                print("Person: Vaccinated and Uninfected")
            elif person.is_vaccinated is False and person.infection is None:
                print("Person: Unvaccinated and Uninfected")
            else:
                print("Person: Unvaccinated and Infected")

    def get_infected(self):
        '''Gets all the infected people from the population and
        returns them as a list'''
        infected = []

        for person in self.population:
            if person.infection is not None:
                infected.append(person)
                return infected

    def simulation_should_continue(self):
        '''Determines whether the simulation should continue.
        If everyone in the population is dead then return False,
        the simulation should not continue
        If everyone in the population is vaccinated return False
        If there are no more infected people left and everyone is
        either vaccinated or dead return False
        In all other cases return True'''
        for person in self.population:
            if person.is_alive is False or person.is_vaccinated is True:
                return False
            else:
                return True

    def run(self):
        ''' This method should run the simulation until all requirements for ending
        the simulation are met.
        '''

        self.create_population()
        random.shuffle(self.population)

        self.print_population()

        time_step_counter = 0
        should_continue = True

        self.file_writer.init_file(self.virus, self.population_size,
                                   self.initial_vaccinated,
                                   self.initial_healthy, self.initial_infected)

        # keep looping until the simulation ends
        while self.simulation_should_continue():

            # save the current infected
            old_infected = self.get_infected()
            self.time_step(old_infected)
            # time step will create newly infected people, just determine the
            # survival of the previous infected people
            self.determine_survival(old_infected)

            time_step_counter += 1

        print(f'The simulation has ended after {time_step_counter} turns.')
        self.file_writer.write_results(time_step_counter, self.total_dead,
                                       self.total_vaccinated)

    def determine_survival(self, infected):
        '''Check if the current infected people survive their infection
        Call the did_survive_infection() method
        if it returns false then the person is no longer alive, does not have
        an infection and one is added to total dead
        if it returns true then the person no longer has an infection and is
        vaccinated, one is added to total vaccinated'''
        for person in infected:
            if person.did_survive_infection() is False:
                self.total_dead += 1
            else:
                person.is_vaccinated = True
                self.total_vaccinated += 1

    def time_step(self, infected):
        ''' For every infected person interact with a random person from
        the population 10 times'''

        for infected_person in infected:

            for i in range(10):
                index = random.randrange(0, len(self.population) - 1)
                random_person = self.population[index]
                self.interaction(infected_person, random_person)

    def interaction(self, infected, random_person):
        '''If the infected person is the same object as the
        random_person return and do nothing
        if the random person is not alive return and do nothing
        if the random person is vaccinated return and do nothing
        if the random person is not vaccinated:
            generate a random float between 0 and 1
            if the random float is less then the infected person's virus
            reproduction number then the random person is infected
            othersie the random person is vaccinated and one is added to
            the total vaccinated'''
        if (infected is random_person or random_person.is_alive is not True or
                random_person.is_vaccinated is True):
            return
        elif random_person.is_vaccinated is not True:
            rand_float = random.randrange(0.0, 1.0)

            if rand_float < self.virus.reproduction_num:
                random_person.infection = self.virus
                return random_person
            else:
                random_person.is_vaccinated = True
                return random_person


# Set up the initial simulations values
# To give users more control of the program, parameters were added

virus_name = str(sys.argv[1])  # Needs to be a string
reproduction_num = float(sys.argv[2])  # Needs to be a float, 0.0 and 1.0
mortality_num = float(sys.argv[3])  # Needs to be a float, 0.0 and 1.0

initial_healthy = int(input("Initially Healthy (#): "))
initial_vaccinated = int(input("Initially Vaccinated (#): "))

initial_infected = int(input("Initially Infected (#): "))

virus = Virus(virus_name, reproduction_num, mortality_num)

simulation = Simulation(initial_vaccinated, initial_infected, initial_healthy,
                        virus, "results.txt")

# run the simulation
simulation.run()
