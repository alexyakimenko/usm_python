import menu
import xfunds

while not menu.should_close:
    menu.draw_menu(
        xfunds.get_options()
    )