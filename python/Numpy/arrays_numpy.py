import numpy as np
from pathlib import Path

path = Path(__file__).parent;
path = str(path.joinpath("data\carros-km.txt"));

km = np.loadtxt(path);
print(km);