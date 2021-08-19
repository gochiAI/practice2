import os

findDir = "/workspace/volume1/Story"
files = os.listdir(findDir)
jpegFiles = [file for file in files if file.endswith(".jpeg")]

for jpegFile in jpegFiles:
    os.rename(
        f'{findDir}/{jpegFile}',
        f'{findDir}/{jpegFile.replace(".jpeg",".png")}'
    )
