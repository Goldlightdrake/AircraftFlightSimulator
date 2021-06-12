from lib.classes.MapHolder import MapHolder
from lib.gui.simulation import Simulation

s = Simulation()
m = MapHolder()

while s.running:
    print(m.list_of_airports)
    s.curr_menu.display_menu()
    s.simulation_loop()
