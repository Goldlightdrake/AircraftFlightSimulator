from lib.gui.simulation import Simulation

s = Simulation()

while s.running:
    s.curr_menu.display_menu()
    s.simulation_loop()
