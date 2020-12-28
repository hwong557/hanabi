import hanabi
import pandas as pd
import numpy as np
import re
from hand import Hand

np.set_printoptions(precision=3, suppress=True)

seen = pd.DataFrame(
        np.array( [0]*25 ).reshape(5, 5),
        index=hanabi.colors,
        columns=hanabi.numbers,
        )

def add_new_sighting(info:str, seen):
    ''' info should be two characters, and contain a digit and a letter, in any order.'''
    assert len(info) == 2

    color = re.search(r"[a-zA-Z]", info).group().lower()
    color = [ bool(re.search(f"^{color}", col)) for col in hanabi.colors ].index(True)

    number = int(re.search(r"\d", info).group())-1
    assert 0<=number<=4
    seen.iloc[color, number]+=1
