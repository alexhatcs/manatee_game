# Manatee Game
A fun project to practice game development with Python.

## Description
Help Manny the Manatee eat his way to escape the lagoon through the grate!

## How it works

On the printed grid, Manny the Manatee is denoted as 'M'. The objective of the game is to eat all of the flowers while avoiding objects. Eating every flower on the map will open the Grate obstacle, changing it from G to O, where you can help Manny pass through and conclude the game, showing your final score.

### Key:
| M = Manny |
\* = Boat |
\\\ = Flower |
. = Seaweed |
G = Closed Grate |
O = Open Grate |

### Movement:
| L = Left |
R = Right |
U = Up |
D = Down |
A = Abort/Quit |

## Rules
Use L, R, U, D to move Manny across the board. Try to get all of the flowers and then help Manny safely arrive at the opened grate. If a boat, denoted by \*, is unobstructed downwards, then the boat will move into the open space below. If Manny moves into an open space that has a boat two spaces above it, Manny will be injured, and the user will lose the game.

## Scoring
Every move will subtract 1 from the overall score. Every flower acquired is worth 25 points, and succesfully arriving at the open grate will increase the user's score by 50. Aborting prior to reaching the opened grate will be calculated as | score = move_count * -1 + flower_count * 25 | If Manny becomes injured at any point in time, then the user's score will simply be based on | move_count * -1 |
