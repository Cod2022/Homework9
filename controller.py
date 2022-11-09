import model
import view

def run():
    start = view.show_menu()
    if start == 1:
        show = model.show_all()
        print(show)