from game_nodes import game_nodes
print("\n\n**********************************")
print("Welcome to the game! Let's start:")
print("**********************************\n")
for node in game_nodes:
    print(node)
    for question in game_nodes[node]:
        print(question)
        for answer in game_nodes[node][question]:
            # print(answer)
            print(answer["answer"])
            print(answer["node"])