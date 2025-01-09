from map import Map

map_ = Map()
while True:
    if map_.game_start_screen() == "2":
        break
    map_.initialize()
    map_.play()
    map_.statistics()
