from math import ceil

# Global variables for input values
price_a = 0
price_b = 0
price_c = 0
price_s = 0
weight_a = 0
weight_b = 0
weight_c = 0
weight_o = 0  # Added variable for weight of cargo to O
distance_oa = 0
distance_ab = 0
distance_bc = 0
distance_co = 0

def read_input():
    """read input and store in global variables"""
    global price_a, price_b, price_c, price_s
    global weight_a, weight_b, weight_c, weight_o
    global distance_oa, distance_ab, distance_bc, distance_co
    weight_a = float(input("Weight of cargo to A: "))
    weight_b = float(input("Weight of cargo to B: "))
    weight_c = float(input("Weight of cargo to C: "))
    weight_o = float(input("Weight of cargo to O: "))  # Added input for weight to O
    price_a = float(input("Price of cargo to A: "))
    price_b = float(input("Price of cargo to B: "))
    price_c = float(input("Price of cargo to C: "))
    price_s = float(input("Price of supply: "))
    distance_oa = float(input("Distance O to A: "))
    distance_ab = float(input("Distance A to B: "))
    distance_bc = float(input("Distance B to C: "))
    distance_co = float(input("Distance C to O: "))

def calculate_profit():
    """calculate and return result profit from input data"""
    global price_a, price_b, price_c, price_s
    global weight_a, weight_b, weight_c, weight_o
    global distance_oa, distance_ab, distance_bc, distance_co
    
    # Step 1: from O to A
    w_net = weight_a + weight_b + weight_c + weight_o
    profit = cal_sub_profit(distance_oa, w_net, weight_a, price_a, price_s)
    
    # Step 2: from A to B
    w_net = weight_b + weight_c + weight_o
    profit += cal_sub_profit(distance_ab, w_net, weight_b, price_b, price_s)
    
    # Step 3: from B to C
    w_net = weight_c + weight_o
    profit += cal_sub_profit(distance_bc, w_net, weight_c, price_c, price_s)
    
    # Step 4: from C to O
    w_net = weight_o
    profit += cal_sub_profit(distance_co, w_net, 0, 0, price_s)
    
    return profit

def travel_speed(w):
    """calculate traveling speed using a formula given in the problem"""
    return 90 / (30 + w) + 5

def travel_time(s, d):
    """calculate total days to travel distance d using speed s.
       A fraction of day is roundup to full day """
    hours = d / s
    days = ceil(hours / 24)
    return days

def cal_sub_profit(distance, net_weight, sell_weight, cargo_price_per_ton, supply_price_per_day):
    """calculate profit received when traveling from one town to the next"""
    speed = travel_speed(net_weight)
    cargo_price = sell_weight * cargo_price_per_ton
    supply_price = travel_time(speed, distance) * supply_price_per_day
    return cargo_price - supply_price

# Main program
read_input()
profit = calculate_profit()
print("Result profit is %.3f" % profit)
