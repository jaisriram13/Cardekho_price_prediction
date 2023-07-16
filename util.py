import pickle
import json
import numpy as np

__fuels = None
__data_columns = None
__model = None

def get_estimated_price(fuel,km_driven,mileage,engine,seats,no_years):
    try:
        _loc_index = __data_columns.index(fuel.upper())
    except:
        _loc_index = -1

        x = np.zeros(len(__data_columns))
        x[0] = km_driven
        x[1] = mileage
        x[2] = engine
        x[3] = seats
        x[4] = no_years
        if _loc_index >= 0:
            x[_loc_index] = 1

        return round(__model.predict([x])[0])


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __fuels

    with open("./artifacts/car_columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __fuels = __data_columns[5:]  # first 5 columns are km,milage, engine, seats, No_years.

    global __model
    if __model is None:
        with open('./artifacts/Cardekho_price_prediction.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_fuel_names():
    return __fuels

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_fuel_names())
    print(get_estimated_price('Petrol', 145500, 23, 1248, 5, 9))
    print(get_estimated_price('Petrol', 120000, 23, 1248, 6, 1))
    print(get_estimated_price('CNG', 10000, 23, 1248, 6, 1)) # other fuel
    #print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location