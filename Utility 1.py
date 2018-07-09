import numpy as np
import math


def time_in_string_to_float(time):
    """Takes in time format in string datatype."""
    """Returns hours, minutes, seconds and hours/minutes in decimal format with int as datatype."""
    split_index = time.find(':')
    hours = int(time[:split_index])
    minutes = int(time[split_index + 1:split_index + 3])
    seconds = int(time[split_index + 4:])
    decimal_time = hours + minutes/60
    return hours, minutes, seconds, round(decimal_time, 1)

#print(time_in_string_to_float('20:00:00'))

def time_rounder(input_time):
    """Takes in time format in string datatype."""
    """Returns hours, minutes, seconds and decimal format rounded to multiples of 5."""
    inputs = time_in_string_to_float(input_time)
    input_hour = inputs[0]
    input_minute = inputs[1]
    input_seconds = inputs[2]

    if input_minute < 15:
        input_minute = 0

    if input_minute > 45:
        input_minute = 0
        input_hour = input_hour + 1

    if 15 <= input_minute <= 45:
        input_minute = 30

    decimal_format = input_hour + (input_minute/60)

    return input_hour, input_minute, input_seconds, decimal_format

#print(time_rounder('20:47:00'))

def selector(list_name):
    """Takes in list of values."""
    """Returns values that are deemed to have driven something both positively and negatively."""

    positive_elements = [x for x in list_name if x > 0]
    if len(positive_elements) == 0:
        pos_highlighters = []
    else:
        pos_mean = np.mean(positive_elements)
        pos_std = np.std(positive_elements)
        pos_highlighters = [x for x in positive_elements if x >= pos_mean + 1*pos_std]
        if len(pos_highlighters) == 0:
            pos_highlighters = [x for x in positive_elements if x > pos_mean]
            
    negative_elements = [x for x in list_name if x < 0]
    if len(negative_elements) == 0:
        neg_highlighters = []
    else:
        neg_mean = np.mean(negative_elements)
        neg_std = np.std(negative_elements)
        neg_highlighters = [x for x in negative_elements if x <= neg_mean + 1*neg_std and x <= neg_mean]
        if len(neg_highlighters) == 0:
            neg_highlighters = [x for x in negative_elements if x < pos_mean]
            
    #highlighters = sorted(pos_highlighters, key=float, reverse=True) + sorted(neg_highlighters, key=float, reverse=True)
    alt_highlighters = pos_highlighters + neg_highlighters
    
    return alt_highlighters

#print(selector([1,2,4,6,10,19]))

def selector_Dict(input_dict):
    """Takes in a dictionary with keys and values."""
    """Returns keys,values that are deemed to have driven something both positively and negatively in dictionary format."""
    
    list_name = list(input_dict.values())
    positive_elements = [x for x in list_name if x > 0]
    if len(positive_elements) == 0:
        pos_highlighters = []
    else:
        pos_mean = np.mean(positive_elements)
        pos_std = np.std(positive_elements)
        pos_highlighters = [x for x in positive_elements if x >= pos_mean + 1*pos_std]
        if len(pos_highlighters) == 0:
            pos_highlighters = [x for x in positive_elements if x > pos_mean]
            
    negative_elements = [x for x in list_name if x < 0]
    if len(negative_elements) == 0:
        neg_highlighters = []
    else:
        neg_mean = np.mean(negative_elements)
        neg_std = np.std(negative_elements)
        neg_highlighters = [x for x in negative_elements if x <= neg_mean + 1*neg_std and x <= neg_mean]
        if len(neg_highlighters) == 0:
            neg_highlighters = [x for x in negative_elements if x < pos_mean]
            
    #highlighters = sorted(pos_highlighters, key=float, reverse=True) + sorted(neg_highlighters, key=float, reverse=True)
    alt_highlighters = pos_highlighters + neg_highlighters
    
    output_dict = {}
    for key,value in input_dict.items():
        if value in alt_highlighters:
            output_dict_value = {key:value}
            output_dict.update(output_dict_value)
            
    return output_dict


def increase_decrease_test(real_number):
    if real_number > 0:
        number_test_1 = 'increase'
        number_test_2 = 'an increase'
        number_test_3 = 'increased'
        number_test_4 = 'higher'
    if real_number < 0:
        number_test_1 = 'decrease'
        number_test_2 = 'a decrease'
        number_test_3 = 'decreased'
        number_test_4 = 'lower'

    output_list = [number_test_1, number_test_2, number_test_3, number_test_4]

    return output_list

#print(increase_decrease_test(-20))