import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

df = pd.read_csv(out_file, parse_dates=True, index_col = 0)
