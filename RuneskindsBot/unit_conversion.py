import random

def length_to_length(length_key, length_val, result_key, old=False):
    
    length_dict = length_dict_gammel if old else length_dict_ny
    
    return (length_val * length_dict[length_key]) / length_dict[result_key], result_key

def length_to_random(length_key, length_val, old=False):
    length_dict = length_dict_gammel if old else length_dict_ny
    (result_key, result_val) = random.choice(list(length_dict.items()))
    return (length_val * length_dict[length_key]) / float(result_val), result_key


length_dict_ny = {
    "alen" : 0.6281,
    "bygkorn" : 0.0049,
    "favn" : 1.8844,
    "fjerdingvej" : 1884.3,
    "fod" : 0.3141,
    "håndsbred": 0.0785,
    "kabellængde": 188.44,
    "linie": 0.00218,
    "mil" : 7537.2,
    "rode" : 3.1405,
    "skrupel" : 0.00018,
    "skår" : 1.8844,
    "tomme" : 0.0262,
    "nautisk mil" : 1852,
    "sømil" : 1852,
    "m" : 1,
    "cm" : 0.01,
    "km" : 1000,
    "mm" : 0.001,
    "mikkel" : 1.75,
    "nes" : 1.78,
    "py" : 1.85,
    "jens" : 1.86,
    "victor": 1.87
}

length_dict_gammel = {
    "alen" : 0.6277,
    "bygkorn" : 0.0049,
    "favn" : 1.8831,
    "fjerdingvej" : 1883.1,
    "fod" : 0.3139,
    "håndsbred": 0.0785,
    "kabellængde": 188.31,
    "linie": 0.00218,
    "mil" : 7532.4,
    "rode" : 3.1385,
    "skrupel" : 0.00018,
    "skår" : 1.8831,
    "tomme" : 0.0262,
    "nautisk mil" : 1852,
    "sømil" : 1852,
    "m" : 1,
    "cm" : 0.01,
    "km" : 1000,
    "mm" : 0.001,
    "mikkel" : 1.75,
    "nes" : 1.78,
    "py" : 1.85,
    "jens" : 1.86,
    "victor" : 1.87
}