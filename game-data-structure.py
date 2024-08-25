# This code is not primarily what I wrote it is what Copilot wrote. It needs to be reviewed and fixed.
# The goal is just to create a relatively simple text-based game that uses a data structure to store the game's nodes.
# The game should be able to navigate between nodes based on user input.

game_nodes = {
    "beginning": {"Do you want to go into the cave?": [{"answer": "yes", "node": "enter the cave"}, {"answer": "no", "node": "exit the game"}]},
    "enter the cave": {"You are in the cave. Do you want to go deeper or dig into the wall?": [{"go deeper into the cave", "go deeper"}, {"dig into the wall", "start mining"}]},
    "exit the game": {"Goodbye!": []}
}

while True:
    node = "beginning"
    while True:
        print(node)
        if not game_nodes[node]:
            break
        question = list(game_nodes[node].keys())[0]
        print(question)
        answers = game_nodes[node][question]
        for answer in answers:
            print(answer["answer"])
        user_input = input()
        for answer in answers:
            if user_input == answer["answer"]:
                node = answer["node"]
                break
        else:
            print("Invalid input")
    break   # Remove this line to allow the game to restart