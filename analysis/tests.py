from datetime import datetime
import json
import pickle
import os
from math import nan
from urllib.parse import unquote

import pandas as pd
# Create your tests here.
import re
import redis
import urllib

def get_compSize(words: str):
    reg = r'[0-9]*'
    if words is not nan:
        nums = re.findall(reg, words)
        sums = 0
        num = 0
        for j in nums:
            if j.isnumeric():
                sums += float(j)
                num += 1
        if num >= 1:
            sums = sums / num
            return sums
        else:
            return 1
    else:
        return 100


def del_all_key():
    r = redis.Redis()
    keys = r.keys()
    for key in keys:
        res = r.delete(key)
        print(res)


if __name__ == "__main__":
    # del_all_key()

    r = redis.Redis()
    keys = r.keys()
    print(unquote('%E5%A4%A7%E6%95%B0%E6%8D%AE_new'))
    print(unquote('java'))
    # name = 'java_new'
    # jobs = r.hvals(name)
    # keys = r.hkeys(name)
    # for key in keys:
    #     job = r.hget(name, key)
    #     job = pickle.loads(job)
    #     print(job)
