# antitype-solver
[Antitype](https://apps.apple.com/us/app/antitype/id1117100543) is an interesitng word puzzle game. It is so attrative to me that I decide to write a Python script to solve it. This scripts simply tries all possibilities and relies on PyEnchant to filter the results. Written and tested on Ubuntu 18.04. 

Install PyEnchant: 
  ```pip install -U pyenchant```

Then run: 
  ```python antitype-game-solver.py```
and follow the instructions

Tips: I heard installing Enchant on 64bit Windows is very difficult. It is possible to use this script without Enchant. They you have to give at least two initial hints to make the script work. 

Warning: this script may ruin the fun of the game!
