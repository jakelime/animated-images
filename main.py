from PIL import Image, ImageSequence
im = Image.open('project_management.webp')
im.info.pop('background', None)
print(f'{im=}')
print(im.mode)
frames = []
for frame in ImageSequence.Iterator(im):
    print(frame)
    frames.append(frame)
# im.save('saved.gif', 'gif', save_all=True)

im_out = Image.new(im.mode, im.size)
# im_out.save("test.gif", save_all=True, append_images=frames, duration=100, loop=0)