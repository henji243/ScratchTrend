import sys
from os.path import dirname, abspath
sys.path.append(dirname(dirname(abspath(__file__))))

import scratchtrend as sct
from scratchtrend.select import Lang, Sort


data = sct.connect(Lang.ENGLISH, Sort.POPULAR)
res = data.get_by_num(1, 100)

print(res)
