with open("test.txt") as inp_file:
    lines = inp_file.readlines()


# only 12 red cubes, 13 green cubes, and 14 blue cubes?
limit = { 
    "red": 12,
    "green": 13,
    "blue": 14
}
possible = []
for game in lines:
    # Game ID: set1;set2;..
    # set = "6 green, 4 red, 3 blue"

    game_header, sets = game.split(": ")
    game_id = int(game_header[4:])
    sets = sets.split(";")
    valid = True
    for set in sets:
        picked = set.strip().split(', ')
        for pick in picked:
            print(picked, set)
            num, color = pick.split(' ')
            if int(num) > limit[color]:
                valid = False
    if valid:
        possible.append(int(game_id))

print(sum(possible))