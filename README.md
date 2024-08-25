## Notes:

- See the Github repo [here](https://github.com/larymak/Python-project-Scripts/tree/main) where Hillary Nyakundi created a repo for programmers to contribute Python projects of all types. Jason will probably find this interesting.

## Jason's game idea:

- See [this](https://stackoverflow.com/questions/39488788/how-to-make-a-menu-in-python-navigable-with-arrow-keys) answer from FocusedWolf. It was the last answer the last I looked.

- In my case the keyboard value for the arrow keys are as follows:

  - arrow up is 450 or curses.KEY_A2
  - arrow left is 452 or curses.KEY_B1
  - arrow down is 456 or curses.KEY_C2
  - arrow right is 454 or curses.KEY_B3
  - the enter key maps correctly

- See [this](https://github.com/microsoft/vscode/issues/112405) discussion which implies it has something to do with VSCode's integrated terminal. That is not true! It is because it is running in a bash terminal. I should try running it in a cmd terminal.
