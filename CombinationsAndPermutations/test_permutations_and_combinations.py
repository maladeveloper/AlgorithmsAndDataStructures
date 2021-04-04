from permutations_and_combinations import permutations_w_replacement, permutations_wo_replacement, combinations_w_replacement, combinations_wo_replacement, backtrack_combinations_wo_replacement
from itertools import product, permutations, combinations, combinations_with_replacement
from pprint import pprint, pformat
import logging
import os
import datetime
import shutil
import time

##Variables 
log_fname = "test_permutations_and_combinations_log.txt"

##Setup logging
try:

    os.remove(log_fname)

except:

    pass

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[
        logging.FileHandler(log_fname),
        logging.StreamHandler()
        ]
    )

def log(log_str, prettify=False):

    if prettify:

        log_str = pformat(log_str)
    
    logging.info(log_str)
##

def built_in_perms_w_replace(arr, r):

    return list(product(arr, repeat=r))

test_contestents = {

    "Permutations with Repetitions---":{
        "func": permutations_w_replacement, 
        "built-in": built_in_perms_w_replace
    }, 

    "Permutations without Repetitions":{
        "func": permutations_wo_replacement, 
        "built-in": permutations
    }, 

    "Combinations with Repetitions---":{
        "func": combinations_w_replacement, 
        "built-in": combinations_with_replacement,
    }, 

    "Combinations without Repetitions":{
        "func": combinations_wo_replacement, 
        "built-in": combinations
    }
}

test_samples = [

    {
        "name":"Test-Sample-1",
        "desc": "Large array with large choice selection (r)", 
        "arr": ["a", "b", "x", "y"], 
        "r": 3,
        "very_large": False
    }, 
    {
        "name":"Test-Sample-2",
        "desc":"Large array with small choice selection (r)", 
        "arr": ["a", "b", "x", "y"],
        "r":2, 
        "very_large": False
    },

    {
        "name":"Test-Sample-3",
        "desc": "Small array with large choice selection (r)", 
        "arr": ["a", "b", "x"], 
        "r": 3,
        "very_large": False
    }, 
    {
        "name":"Test-Sample-4",
        "desc":"Small array with small choice selection (r)", 
        "arr": ["a", "b", "x"],
        "r":2,
        "very_large": False
    },
    {
        "name":"Test-Sample-5", 
        "desc": "VERY Large array with VERY large choice selection (r) - to test time.",
        "arr": ["a", "b", "x", "c", "f", "l", "v"],
        "r": 6,
        "very_large": True
    },

    {
        "name":"Test-Sample-6", 
        "desc": "Small array with small choice selection (r) - with repeating values.",
        "arr": ["a", "b", "a"],
        "r": 3,
        "very_large": False
    }
]

##For each of the test samples have the contestents battle it out
log(f'''======================================================================================================\n{datetime.datetime.now()}\nRUNNING...''')

for test in test_samples:

    log(f'''\n\n{test["name"]}+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nDescripton:{test["desc"]}\nArray:{test["arr"]}\nr: {test["r"]}''')

    for name, info in test_contestents.items():
        
        log(f'''\n----------------------{name}------------------------------------''')

        t0 = time.time()

        result_set = info["func"](test["arr"], test["r"])

        t1 = time.time()
        
        verified_set = list(info["built-in"](test["arr"], test["r"]))

        t2 = time.time()

        if  not test["very_large"]:
            
            log(result_set, True)
        
        else:

            log("Resulting array is not shown since too large.")

        status = "FAIL"

        if len(set(verified_set)) == len(result_set):

            status = "PASS"
        
        else:
            log(f'''My Set Len: {len(result_set)}''')

            log(f'''Verified Set Len: {len(verified_set)}''')

            log(set(verified_set),True)

    
        log(f'''Status:{status}\nMy Implementation Time:{t1- t0}(sec)\nBuilt-In Implementation Time:{t2-t1}(sec)''')

log(f'''======================================================================================================\n''')