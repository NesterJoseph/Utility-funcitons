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

def Phraze(list_name):
    phraze_0 = ""
    for i in list_name:
        if len(list_name) == 1:
            phraze_0 = str(i)
        elif len(list_name) == 2:
            if list_name.index(i) == 0:
                phraze_0 = "{} ".format(i)
            else:
                phraze_0 += "and {}".format(i)
        else:
            if list_name.index(i) != len(list_name) - 1:
                phrase = "{}, ".format(i)
                phraze_0 += phrase
            elif list_name.index(i) == len(list_name) - 2:
                phrase_0 = "{} ".format(i)
                phraze_0 += phrase_0
            else:
                phraze_0 += "and {}".format(i)
    return phraze_0

#print(Phraze([1,2,4,5,6]))

def dict_subtractor(dict_1,dict_2,demultiplier):
    """Works only when the keys of both the dictionaries are the same."""
    """Format: dict_1 - dict_2"""
    difference_dict = {}
    for keys,values in dict_1.items():
        difference = (values - dict_2[keys])/demultiplier
        difference_element = {keys:difference}
        difference_dict.update(difference_element)
        
    return difference_dict

def dict_percentage_calculator(dict_1,dict_2):
    """Works only when the keys of both the dictionaries are the same."""
    """Format: (dict_1 - dict_2)/dict_2 * 100"""
    percent_difference_dict = {}
    for keys,values in dict_1.items():
        if dict_2[keys] != 0:
            percent_difference = (values - dict_2[keys])/dict_2[keys] * 100
            percent_difference_element = {keys:percent_difference}
        else:
            percent_difference = 0
            percent_difference_element = {keys:percent_difference}
        percent_difference_dict.update(percent_difference_element)
        
    return percent_difference_dict

def number_to_rupees_indian(value):
    round_value = round(value,0)
    
    length_value = len(str(round_value)) - 2
    
    new_value = str(round_value)[:length_value]
    
    rupee_value = 0
    if length_value <= 3:
        rupee_value = 'Rs.' + str(round_value)
    
    if 3 < length_value <= 5:
        rupee_value = 'Rs.' + '{:,.0f}'.format(int(new_value))
        
    if 5 < length_value <= 7:
        rupee_value = 'Rs.' + str(round(int(new_value)/10**5, 2)) + ' lakhs'
        
    if 7 < length_value :
        rupee_value = 'Rs.' + str(round(int(new_value)/10**7, 2)) + ' crores'
    
    return rupee_value

def number_to_dollars(value):
    
    if value >= 0:
        value = value
        sign = 'positive'
    else:
        value = abs(value)
        sign = 'negative'
        
    round_value = round(value,0)
    
    if '.' in str(round_value):
        length_value = len(str(round_value)) - 2
    else:
        length_value = len(str(round_value))
    
    new_value = str(round_value)[:length_value]
    
    dollar_value = 0
    if length_value <= 3:
        dollar_value = '$' + str(new_value)
    
    if 3 < length_value <= 6:
        dollar_value = '$' + '{:,.0f}'.format(int(new_value))
        
    if 6 < length_value <= 9:
        dollar_value = '$' + str(round(int(new_value)/10**6, 2)) + ' million'
        
    if 9 < length_value :
        dollar_value = '$' + str(round(int(new_value)/10**9, 2)) + ' billion'
        
    if sign == 'negative':
        dollar_value_with_sign = '-' + dollar_value
    else:
        dollar_value_with_sign = dollar_value
    
    return dollar_value_with_sign

