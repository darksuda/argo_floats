import imageio

frames = []
time = range(30) #  <- n+1    imagen n creada...
for t in time:
    image = imageio.v2.imread(f'IMGS/PSAL/PSAL_COP_{t}_PERU_2024_ENE.png')
    frames.append(image)

imageio.mimsave('./GIFS/PSAL_PERU_2024_ENE.gif', # output gif
                frames,          # array of input frames
                fps = 3)         # optional: frames per second
