import os
for Story in range(0,52):
  Story = "{0:02d}".format(Story)
  if os.path.exists(f'Story/{Story}.jpeg'):
   os.rename(f'/workspace/volume1/Story/{Story}.jpeg',f'/workspace/volume1/Story/{Story}.png')
   print(os.path.exists('/workspace/volume1/Story/{Story}.png'))
