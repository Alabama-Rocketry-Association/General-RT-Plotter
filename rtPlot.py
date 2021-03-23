import asyncio
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib import pyplot as plt1
import matplotlib.animation as anim

data = list()
fig = plt1.figure()
ax = Axes3D(fig)

async def gen():
    for i in range(10):
        yield (i, i*i, i*i*i)

async def main():
    async for i in gen():
        data.append(i)
        e, n, u = map(list, zip(*data))
        #ax.scatter(e, n, u)
        print(e, n, u)
        #plt.show()


loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.run_until_complete(loop.shutdown_asyncgens())
    loop.close()