game_nodes = {
    "beginning": {"Do you want to go into the cave?": [{"answer": "yes", "node": "enter the cave"}, {"answer": "no", "node": "exit the game"}]},
    "enter the cave": {"You are in the cave. Do you want to go deeper or dig into the wall?": [{"answer": "go deeper into the cave", "node": "go deeper"}, {"answer": "dig into the wall", "node": "start mining"}]},
    "go deeper": {"You are at the end of the cave. Do you want to go back or dig into the wall?": [{"answer": "go back", "node": "enter the cave"}, {"answer": "dig into the wall", "node": "start mining"}]},
    "start mining": {"You found a treasure chest! Do you want to open it or leave it?": [{"answer": "open it", "node": "open the chest"}, {"answer": "leave it", "node": "don't open the chest"}]},
    "open the chest": {"You won the game!": []},
    "don't open the chest": {"You lost the game!": []},
    "exit the game": {"Goodbye!": []}
}
