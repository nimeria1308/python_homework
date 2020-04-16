import sys, time

maze = [ list(row) for row in [
    "####################",
    "#                  #",
    "# ####### # ###### #",
    "#       # # #g## # #",
    "# ####### # # ## # #",
    "# #         # ## # #",
    "# # ### ##### ## # #",
    "# # # # #     ## # #",
    "#   #     #        #",
    "####################",
]]

FREE_PATH = " "
TRACED_PATH = "."
GOAL = "g"

def printMaze(sleep_time=None):
    for row in maze:
        print("".join(row))

    print()
    if sleep_time:
        time.sleep(sleep_time)

def solveMaze(x, y, debug=False):
    # nachalen vuzel
    path_trace = [ (x, y) ]

    while path_trace:
        # vzimame kakvoto ima za obrabotvane
        x, y = path_trace.pop()

        # ako koordinatite sa nevalidni produljavame
        if (x < 0 or x >= len(maze[0])) or (y < 0 or y >= len(maze)):
            continue

        if maze[y][x] == GOAL:
            printMaze()
            return

        if maze[y][x] != FREE_PATH:
            continue

        # ako e izvikana s debug shte printirame stupikite
        if debug:
            printMaze(0.1)

        # zapisvame v labirinta, che tova e obraboteno
        maze[y][x] = TRACED_PATH
        path_trace.append((x - 1, y))
        path_trace.append((x + 1, y))
        path_trace.append((x,     y - 1))
        path_trace.append((x,     y + 1))

    # nakraq printirame labirinta
    printMaze()

# po podrazbirane polzvame tazi startova pozicia
x, y = 1, 1

# vzimame x i y ot argumentite, ako gi nqma polzvame po podrazbirane
if len(sys.argv) > 2:
    x, y = int(sys.argv[1]), int(sys.argv[2])

solveMaze(x, y)

# tova shte pokaje i stupkite
# solveMaze(x, y, True)
