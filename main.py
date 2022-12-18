from PIL import Image

im = Image.open('original.jpg')

tile_size = 16
x_tiles = im.width // tile_size
y_tiles = im.height // tile_size
tiles = []
for x in range(x_tiles):
    for y in range(y_tiles):
        left = x * tile_size
        top = y * tile_size
        right = (x + 1) * tile_size
        bottom = (y + 1) * tile_size
        tile = im.crop((left, top, right, bottom))
        tiles.append(tile)

colors = []
for tile in tiles:
    pixels = tile.getdata()
    r_sum = 0
    g_sum = 0
    b_sum = 0
    count = 0
    for pixel in pixels:
        r, g, b = pixel
        r_sum += r
        g_sum += g
        b_sum += b
        count += 1
    r_avg = r_sum // count
    g_avg = g_sum // count
    b_avg = b_sum // count
    color = (r_avg, g_avg, b_avg)
    colors.append(color)

mosaic_im = Image.new('RGB', (im.width - tile_size + 1, im.height - tile_size + 1))
for x in range(x_tiles):
    for y in range(y_tiles):
        color = colors[x * y_tiles + y]
        mosaic_im.paste((color), (x * tile_size, y * tile_size, (x + 1) * tile_size, (y + 1) * tile_size))


mosaic_im.save('mosaic.jpg')