from collections import namedtuple, defaultdict
from faker import Faker
from time import perf_counter
from datetime import date
import random
import re
import string
from matplotlib import pyplot as plt
import pandas as pd
from functools import wraps



def timer(n_iter: int) -> 'Decorator':
    """
    function acts as a decorator factory which takes function repetition count
    as argument returns back a decorator.
    """
    def timed_inner(fn: callable) -> 'closure':
        """
        Decorator which returns a closure , it runs the function that number of times and gives 
        back avergae performance.
        """
        @wraps(fn)
        def inner(*args: 'arguments', **kwargs: 'keyword arguments'):
            '''
            Calculates the Average Time and Run the Funciton
            '''
            start = perf_counter()
            for _ in range(n_iter):
                result = fn(*args, **kwargs)
            end = perf_counter()
            print(f'Average Time to Run the Function is: {(end-start)/n_iter :.3f}')

            return result

        return inner

    return timed_inner



###################### Using Named tuple ############################

@timer(1)
def nt_approach(num_profiles: int):
    '''
    function generates a profile of a person using faker library and
    using namedtuple, calculates the largest blood type, mean_location,
    oldest_person_age and average age using the namedtuple.
    returns namedtuple of the above data.
    '''
    faker = Faker()
    Person = namedtuple('Person', faker.profile().keys())
    Person.__doc__ =  'Fake personal profile of non-existing people using faker library'

    all_persons = []
    '''Reason for using List - Using another Named Tuple to stroe 10000 tuples, will be not feasible,
    as NamedTuple allows maximum 255 variables, and all if we need to add one more,
    we need to create an entire new NamedTuple with 10,001 variables, hihgly Ineffecient.'''
    for _ in range(num_profiles):
        fake_person = faker.profile()
        fake_person = Person(**fake_person)
        all_persons.append(fake_person)

    current_loc_lat = current_loc_long = max_age = total_age = 0
    blood_groups = defaultdict(int)
    today = date.today()

    for person in all_persons:
        current_loc_lat += person.current_location[0]
        current_loc_long += person.current_location[1]
        blood_groups[person.blood_group] += 1
        age = int((today - person.birthdate).days / 365)
        total_age += age
        max_age = age if age > max_age else max_age
    
    average_age = total_age/len(all_persons)
    mean_lat = float(current_loc_lat/len(all_persons))
    mean_long = float(current_loc_long/len(all_persons))
    mean_location = (mean_lat, mean_long)
    
    max_bgroup = 0
    highest_blood = ""
    for group_name, group_num in blood_groups.items():
        highest_blood = group_name if group_num > max_bgroup else highest_blood

    Stat = namedtuple(
        'Stat', 'largest_blood_type,  mean_location, oldest_person,  average_age')
    Stat.__doc__ = '''Statistics of profile data showing the largest present 
    blood type, mean current location, oldest person age and average age using the namedtuple'''
    
    result = Stat(highest_blood, mean_location, max_age, average_age)

    return result


# Dictionary Approach
@timer(1)
def dict_approach(num_profiles: int):
    '''
    This function generates a profile of a person using faker library and
    using dictionary, calculates the largest blood type, mean-current_location,
    oldest_person_age and average age.
    returns dictionary of the above data.
    '''
    all_persons = []
    faker= Faker()

    for _ in range(num_profiles):
        fake_person = faker.profile()
        fake_person = {key:value for key,value in fake_person.items()}
        all_persons.append(fake_person)

    current_loc_lat = current_loc_long = max_age = total_age = 0
    blood_groups = defaultdict(int)
    today = date.today()

    for person in all_persons:
        current_loc_lat += person["current_location"][0]
        current_loc_long += person["current_location"][1]
        blood_groups[person["blood_group"]] += 1
        age = int((today - person["birthdate"]).days / 365)
        total_age += age
        max_age = age if age > max_age else max_age
    
    average_age = total_age/len(all_persons)
    mean_lat = float(current_loc_lat/len(all_persons))
    mean_long = float(current_loc_long/len(all_persons))
    mean_location = (mean_lat, mean_long)
    
    max_bgroup = 0
    highest_blood = ""
    for group_name, group_num in blood_groups.items():
        highest_blood = group_name if group_num > max_bgroup else highest_blood

    return {'largest_blood_type': highest_blood, 'mean_location': mean_location, 'oldest_person': max_age, 'average_age': average_age}

# TSAI Stock Exchange


def simulate_stock(days: 'Number of Days to Run Simulation') -> 'Decorator':
    '''
    function acts as a decorator factory which takes number of days to
    simulate the stock exchange.
    returns the decorator
    '''
    def simulate_inner(fn: 'Funciton') -> 'closure':
        '''
        function acts as a decorator which runs the given function for
        specified number of days using closure.
        returns the closure
        '''
        def inner(*args: 'arguments', **kwargs: 'keyword arguments') -> 'History':
            '''
            Simulates the Index Fund for given days, and append to
            corresponding lists
            '''
            open_, close, high, low = [], [], [], []
            for _ in range(days):
                index = fn(*args, **kwargs)
                open_.append(index.open)
                close.append(index.close)
                high.append(index.high)
                low.append(index.low)
            History = namedtuple('History', 'open high low close')
            history = History(open_, high, low, close)

            return history

        return inner

    return simulate_inner


def stock(count: 'number of companies') -> 'tuple':
    '''
    function generates a company stock profile for market value using faker
    library and simulates instantaneous market trend.
    returns list of comapanies stock profiles and contribution to stock_market.
    '''
    exc = []  # Parent Stock Exchange List which will contain all the Companies Named Tuples.
    Stock = namedtuple(
        'Stock', 'index, name, open_, high, low, close, contribution')
    Stock.__doc__ = "Company stock profile with current market trend values"
    weights = [random.uniform(0.2, 0.8) for _ in range(100)]
    norm_wts = [x/sum(weights) for x in weights]
    index_l = []  # List to store index and maintain all unique indexes.
    for i in range(count):
        comp_name = Faker().company()
        comp_index = ''.join(i[:3] for i in re.split(
            '[ -]+', comp_name.replace('and', ' ').upper(), 1))[:5]
        while True:
            if comp_index not in index_l:
                index_l.append(comp_index)
                break
            comp_index = comp_index[:4] + random.choice(string.ascii_uppercase)
        open_ = random.randint(80, 950)
        close = round(open_ * random.uniform(0.8, 1.2))
        high = round(open_ * random.uniform(1, 1.6))
        high = close if close > high else high
        low = round(open_ * random.uniform(0.6, 1))
        low = close if close < low else low
        comp = Stock(comp_index, comp_name, open_,
                    high, low, close, norm_wts[i])
        exc.append(comp)

    return exc


df = pd.DataFrame(stock(100), columns=[
    'Index', 'Name', 'Open', 'High', 'Low', "Close", "Contribution to Index"])


@simulate_stock(50)
def tsai_index(num_comp: 'Number of Companies') -> 'The Index Fund':
    """
    Generates and gives the Index open, high and close of a 
    small stock exchange simulation of listed stocks.
    input: num_comp, number of companies in the exchange
    output: namedtuple('TSAIEX', 'Open High Low Close')
    """
    TSAI = namedtuple('TSAI', 'open high low close')
    TSAI.__doc__ = 'Shows the market trend as whole.'
    open_, high, low, close = 0, 0, 0, 0
    companies = stock(num_comp)
    for i in companies:
        open_ += round(i.open_ * i.contribution)
        high += round(i.high * i.contribution)
        low += round(i.low * i.contribution)
        close += round(i.close * i.contribution)
    # Index Checks:
    high = close if close > high else high
    low = close if close < low else low
    tsai_index = TSAI(open_, high, low, close)

    return tsai_index
