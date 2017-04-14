#!/usr/bin/env python3

"""The rolloing subs calculator calculates the amount of time each
player on a team will have on the pitch, times substitutions should
be made and which players are subbed on / off at each substitution.
"""

# Capture match variables. These vary week to week and will be set from the web app in future.
MATCH_DURATION = int(input(' Enter match duration in minutes '))
NUMBER_PLAYERS = int(input(' Enter total number of available players '))
NUMBER_GOALKEEPERS = 1

# Set game variables. These do not change from week to week
OUTFIELD_PLAYERS = (NUMBER_PLAYERS - NUMBER_GOALKEEPERS)
PLAYERS_ON_PITCH = 7
NUMBER_OUTFIELD_PLAYERS = (NUMBER_PLAYERS - NUMBER_GOALKEEPERS)
AVAILABLE_OUTFIELD_MINUTES = (MATCH_DURATION * (PLAYERS_ON_PITCH - 1))
MINUTES_PER_OUTFIELD = (AVAILABLE_OUTFIELD_MINUTES / OUTFIELD_PLAYERS)
SUB_FREQUENCY = (MATCH_DURATION / OUTFIELD_PLAYERS)
NUMBER_SUBS = NUMBER_PLAYERS - PLAYERS_ON_PITCH

# Capture outfield players names
OUTFIELD_PLAYERS_NAMES = []
i = 0
while len(OUTFIELD_PLAYERS_NAMES) < OUTFIELD_PLAYERS:
    i += 1
    PLAYER = input('Outfield player name %d: '%i)
    OUTFIELD_PLAYERS_NAMES.append(PLAYER)
print(OUTFIELD_PLAYERS_NAMES)
print("\n")

# Print summary instructions
INSTRUCTIONS = "Substitute " + str(NUMBER_SUBS) + " players every " + str(SUB_FREQUENCY) + " mins"
print(INSTRUCTIONS)
print(" Every outfield player will get " + str(MINUTES_PER_OUTFIELD) + " minutes")

# Decide starting team - by first entered at the player input stage.
STARTING_TEAM = (OUTFIELD_PLAYERS_NAMES[0:PLAYERS_ON_PITCH - NUMBER_GOALKEEPERS])
STARTING_TEAM.sort()
print("\n")
print("Starting team " + str(STARTING_TEAM))


# Print substitutions plan details
SUB_COUNT = 1 # Sets the number of the first substitution to 1
NEXT_SUB = SUB_FREQUENCY #Sets initial time for NEXT_SUB variable

# Loop through sub times and print subs on, subs off and current team after each set of subs
while NEXT_SUB < (MATCH_DURATION):
    print("\n") # Adds line breaks for legibility
    print("@ " + str(round(NEXT_SUB, 2)) + " minutes")
    print("Sub off " + str(STARTING_TEAM[0:NUMBER_SUBS]))
    SUB_COUNT = SUB_COUNT + 1
    NEXT_SUB = NEXT_SUB + SUB_FREQUENCY
    BENCH = (set(OUTFIELD_PLAYERS_NAMES) - set(STARTING_TEAM))
    del STARTING_TEAM[0:NUMBER_SUBS]
    STARTING_TEAM.extend(BENCH)
    print("Sub on" + str(BENCH))
    print("Current team" + str(STARTING_TEAM))
