from simulation import Simulation

g = Simulation()

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()