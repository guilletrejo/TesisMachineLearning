import numpy as np

matriz500 = np.load("z500_uint8.npy")
matriz700 = np.load("z700_uint8.npy")
matriz1000 = np.load("z1000_uint8.npy")
rain = np.load("rain.npy")
matriz1 = matriz500[:5000][:][:]
matriz2 = matriz700[:5000][:][:]
matriz3 = matriz1000[:5000][:][:]
r1      = rain[:5000][:][:]
matriz_short_500 = matriz500[10000:10100][:][:]
matriz_short_700 = matriz700[10000:10100][:][:]
matriz_short_1000 = matriz1000[10000:10100][:][:]
print(rain.shape)
r = rain[10000:10100][:]
print(r.shape)
np.save("z500_shorter_uint8.npy", matriz_short_500)
np.save("z700_shorter_uint8.npy", matriz_short_700)
np.save("z1000_shorter_uint8.npy", matriz_short_1000)
np.save("rain_shorter.npy", r)
np.save("z500_5000_uint8.npy", matriz1)
np.save("z700_5000_uint8.npy", matriz2)
np.save("z1000_5000_uint8.npy", matriz3)
np.save("rain_5000.npy", r1)