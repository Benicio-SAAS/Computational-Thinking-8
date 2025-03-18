###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("winter")

q1 = codesters.Square (100, 100, 200, 'orange')
q2 = codesters.Square (-100, 100, 200, 'black')
q3 = codesters.Square (-100, -100, 200, 'green')
q4 = codesters.Square (100, -100, 200, 'gray')

s1 = codesters.Sprite ("Flag_of_Brazil", 100, 100,)
s1.set_size(0.3)
s2 = codesters.Sprite ("basketball", -100, -100)
s2.set_size(4.0)
s3 = codesters.Sprite ("images", 100, -100)
s3.set_size(0.6)
s4 = codesters.Sprite ("711AZZ6TT3L", -100, 100)
s4.set_size (0.1)

message1 = codesters.Text ("Benicio",0,220,"orange")
message2 = codesters.Text ("This is my coat of arms",0,-220,"orange")