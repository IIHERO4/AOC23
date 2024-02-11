with open("input.txt") as inp_file:
    lines = inp_file.readlines()


# only 12 red cubes, 13 green cubes, and 14 blue cubes?
limit = { 
    "red": 12,
    "green": 13,
    "blue": 14
}
powers = []
for game in lines:
    # Game ID: set1;set2;..
    # set = "6 green, 4 red, 3 blue"

    game_header, sets = game.split(": ")
    game_id = int(game_header[4:])
    sets = sets.split(";")
    valid = True
    maxes = {k: 0 for k in limit.keys()}
    for set in sets:
        picked = set.strip().split(', ')
        for pick in picked:
            num, color = pick.split(' ')
            maxes[color] = max(maxes[color], int(num))
    
    powers.append(maxes["red"] * maxes["green"] * maxes["blue"])

print(sum(powers))