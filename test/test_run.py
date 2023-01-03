import scratchtrend as sct
from scratchtrend.select import Lang, Sort


data = sct.connect(Lang.ENGLISH, Sort.POPULAR, False)
res = data.get_by_rank(1, 1000)

print(res)