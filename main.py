#Session algorithm
# Step 1. Display welcome
# Step 2. Introduction to game
# Step 3. Choose if it's single player or multiplayer
# Step 4. Choose number of rounds
# Step 5. Player one chooses gesture
# Step 6. Player two chooses gesture
# Step 7. Compare the gestures against one another
# Step 8. Determine which gesture wins
# Step 9. Play until someone wins twice
# Step 10. Display winner who ends up winning the best of three

# Classes: 
# player(parent)
#   - computer(child)
#   - human(child)
# game 


from game import Game

game1 = Game()
game1.run_game()


