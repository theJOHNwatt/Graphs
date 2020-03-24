from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


from util import Stack 
from util import Queue

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = [] # once you make the function that spits out traversal_path - test on line 52 should be done 

# ADDING REVERSE 
# reversed_traversal_path = []



opposite_direction = {"n":"s", "s":"n", "e":"w", "w":"e"}



def find_exits(current_room, visited):
    valid_exits = []
    for exit in current_room.get_exits():
        if exit in room_graph[current_room.id][1]:
            if room_graph[current_room.id][1][exit] not in visited:
                valid_exits.append(exit)
    return valid_exits



def traverse_maze():
    visited = set()
    visited.add(player.current_room.id)
    reversed_traversal_path = [] 

    while len(visited) < len(room_graph.keys()):
        current_room = player.current_room.id
        valid_exits = find_exits(player.current_room, visited)
        print(valid_exits)

        if len(valid_exits) > 0:
            for direction in valid_exits:
                visited.add(room_graph[current_room][1][direction])
                traversal_path.append(direction)
                reversed_traversal_path.append(opposite_direction[direction])
                player.travel(direction)

                break
        else: 
            print(reversed_traversal_path)
            direction = reversed_traversal_path.pop()
            player.travel(direction)
            traversal_path.append(direction)
traverse_maze()







# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)




for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")