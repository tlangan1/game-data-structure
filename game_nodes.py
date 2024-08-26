game_nodes = {
    "beginning": {"Do you want to go into the cave?": [{"answer": "yes", "node": "enter the cave"}, {"answer": "no", "node": "exit the game"}]},
    "enter the cave": {"You are in the cave. Do you want to go deeper, dig into the wall or hyper jump to phobos?": [{"answer": "go deeper into the cave", "node": "go deeper"}, {"answer": "dig into the wall", "node": "start mining"}, {"answer": "hyper jump to phobos", "node": "your on phobos"}]},    
    "go deeper": {"You are at the end of the cave. Do you want to go back or dig into the wall?": [{"answer": "go back", "node": "enter the cave"}, {"answer": "dig into the wall", "node": "start mining"}]},
    "start mining": {"You found a treasure chest! Do you want to open it or leave it?": [{"answer": "open it", "node": "win the game"}, {"answer": "leave it", "node": "lose the game"}]},
    "your on phobos": {"You are on phobos. Do you want to explore phobos, go back to the beginning, back to the cave or exit the game?": [{"answer": "explore phobos", "node": "explore phobos"}, {"answer": "go back to the beginning", "node": "beginning"}, {"answer": "go back to the cave", "node": "enter the cave"}, {"answer": "exit the game", "node": "exit the game"}]},
    "explore phobos": {"It's raining diamonds, Do you want to pick some up or not?": [{"answer": "pick some diamonds up", "node": "win the game"}, {"answer": "don't pick up some diamonds", "node": "lose the game"}]},
    "win the game": {"You won the game!": []},
    "lose the game": {"You lost the game!": []},
    "exit the game": {"Goodbye!": []}
}
