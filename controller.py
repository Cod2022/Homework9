import model
import view

def run():
    start = view.show_menu()
    if start == 1:
        show = model.show_all()
        print(show)
    if start == 2:
        surname = view.find_by_surname()
        model.find_by_surname(surname)
    if start == 3:
        values = view.add_record()
        model.add_record(values)
        
