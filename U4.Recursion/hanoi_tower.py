def move_tower(height,from_pole,to_pole,with_pole):
    if height<1:return
    move_tower(height-1,from_pole,with_pole,to_pole)
    move_disk(from_pole,to_pole)
    move_tower(height-1,with_pole,to_pole,from_pole)

def move_disk(from_pole,to_pole):
    pass
    #print("Moving disk from {0} to {1}".format(from_pole,to_pole))

if __name__=="__main__":
    move_tower(30,'#1','#2','#3')