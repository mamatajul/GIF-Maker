import imageio
import os

        # To find the absolute path 
clip = os.path.abspath("your_file_name.mp4")

def gifMaker(inputPath, targetFormat):
        # It takes the file name and divides into two, then takes the first part and adds the desired extention
    outputPath = os.path.splitext(inputPath)[0] + targetFormat

        # imageio reads the file
    reader = imageio.get_reader(inputPath)
        # get the fps
    fps = reader.get_meta_data()["fps"]

    writer = imageio.get_writer(outputPath, fps=fps)

    for frames in reader:
        writer.append_data(frames)
        print(f'Frames {frames}')
    print("Done!")
    writer.close()


gifMaker(clip, '.gif')