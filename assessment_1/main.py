import menu
import kiosk

while not menu.should_close:
    menu.draw_menu(
        kiosk.get_options()
    )