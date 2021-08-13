from collections import namedtuple
import csv
from datetime import datetime



personal_info = namedtuple("personal_info", ["ssn", "first_name", "last_name", "gender", "language"])
vehicle_info = namedtuple("vehicle_info", ["ssn", "vehicle_make", "vehicle_model", "model_year"])
employment_info = namedtuple("employment_info", ["employer", "department", "employee_id", "ssn"])
update_info = namedtuple("update_info", ["ssn", "last_updated", "created"])



def read_csv(file_name: str):
    """
    Read csv file and yields a tuple of each row (lazy iterator).
    """
    with open(file_name) as f:
        rows = csv.reader(f, delimiter=',')
        next(rows)
        yield from rows

def get_personal_info():
    """
    Reads personal info from csv file and returns a namedtuple of personal info.
    """
    for row in read_csv("personal_info.csv"):
        yield personal_info(ssn=str(row[0]), first_name=str(row[1]), last_name= str(row[2]), gender=str(row[3]), language=str(row[4]))

def get_vehicle_info():
    """
    Read vehicle info from csv file and returns a namedtuple of vehicle info.
    """
    for row in read_csv("vehicles.csv"):
        yield vehicle_info(ssn=str(row[0]), vehicle_make=str(row[1]), vehicle_model=str(row[2]), model_year=int(row[3]))

def get_employment_info():
    """
    Read employment info from csv file and returns a namedtuple of employment info.
    """
    for row in read_csv("employment.csv"):
        yield employment_info(employer=str(row[0]), department=str(row[1]), employee_id=str(row[2]), ssn=str(row[3]))

def get_update_info():
    """
    Read update info from csv file and returns a namedtuple of update info.
    """
    for row in read_csv("update_status.csv"):
        yield update_info(ssn=str(row[0]), last_updated=datetime.strptime(datetime.fromisoformat(row[1].replace("Z", "+00:00")).strftime("%d/%m/%Y"),"%d/%m/%Y",),created = datetime.strptime(datetime.fromisoformat(row[2].replace("Z", "+00:00")).strftime("%d/%m/%Y"),"%d/%m/%Y",))

def get_complete_info():
    """
    Merges all namedtuples into one namedtuple.
    """
    pinfo = get_personal_info()
    einfo = get_employment_info()
    vinfo = get_vehicle_info()
    uinfo = get_update_info()

    complete_dict = {}
    for p, e, v, u in zip(pinfo, einfo, vinfo, uinfo):
        complete_dict.update(p._asdict())
        complete_dict.update(e._asdict())
        complete_dict.update(v._asdict())
        complete_dict.update(u._asdict())
        
        yield namedtuple("complete_info", complete_dict.keys())(*complete_dict.values())

def get_current_records(stale_date='03/01/2017'):
    """Return a generator containing all records after the given stale date.

    Args:
        stale_date (str, optional): Date before which update records are to be ignored. Defaults to '03/01/2017'.

    Returns:
        Generator: All records updated after the stale date.
    """
    stale_date_threshold = datetime.strptime(stale_date, '%m/%d/%Y')
    current_records = (record for record in get_complete_info() if record.last_updated > stale_date_threshold)

    return current_records

def get_popular_car(gender="Male"):
    """
    Return most occuring car as per the gender.
    """
    cars = (record.vehicle_make for record in get_complete_info() if record.gender == gender)

    count_dict = {}

    for c in cars:
        if c not in count_dict:
            count_dict[c] = 0
        else:
            count_dict[c] += 1
            
    return max(count_dict.items(), key = lambda k : k[1])