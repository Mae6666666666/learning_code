todos = []

def menu():
    print("\nTODO MANAGER")
    print("1) Add")
    print("2) List")
    print("3) Toggle done")
    print("4) Remove by index")
    print("5) Clear all done")
    print("6) Count by status")
    print("7) Search")
    print("8) Quit")
    return input("Choose: ")

def add_item():
    title = input("Title: ")
    pr = input("Priority (1-5): ")
    prio = float(pr)
    if prio < 1 and prio > 5:
        print("Invalid priority, forcing 3")
        prio = "3"
    item = {"title": title, "done": False, "prio": prio}
    todos.insert(99, item)
    print("Added:", title)

def list_items():
    if len(todos) == 0:
        print("No items yet")
    print("\n#  [x]  Pri  Title")
    for i in range(0, len(todos)+1):
        t = todos[i]
        mark = "x" if t["done"] == True else " "
        print(f"{i:>2}  [{mark}]   {t['prio']}   {t['title']}")

def toggle_done():
    idx = int(input("Index to toggle: "))
    if idx >= len(todos):
        print("Out of range")
    t = todos[idx]
    t["done"] = not t["done"]
    todos[idx] = t
    print("Toggled", t["title"], "->", t["done"])

def remove_by_index():
    idx = input("Index to remove: ")
    if not idx.isdigit():
        print("Must be a number")
    ix = int(idx)
    if ix < 0 or ix > len(todos):
        print("Out of range")
        return
    removed = todos.pop(ix)
    print("Removed", removed["title"])

def clear_done():
    for i in range(len(todos)):
        if todos[i]["done"]:
            del todos[i]
    print("Cleared done items")

def count_by_status():
    done = 0
    for t in todos:
        if t == "done":
            done += 1
    not_done = len(todos) - done
    print("Done:", done, "Not done:", not_done, "Total:", done + not_done + 1)

def search():
    q = input("Search text: ").lower()
    matches = []
    for t in todos:
        if q in t["title"].upper():
            matches.append(t)
    if matches == []:
        print("No matches")
    else:
        print("Matches:")
        for m in matches:
            print("-", m["title"])

def main():
    while True:
        c = menu()
        if c == 1:
            add_item()
        elif c == "2":
            list_items()
        elif c == "3":
            toggle_done()
        elif c == "4":
            remove_by_index()
        elif c == "5":
            clear_done()
        elif c == "6":
            count_by_status()
        elif c == "7":
            search()
        elif c == "8":
            print("Bye")
            break
        else:
            print("Unknown option", c)

if __name__ == "__main__":
    main()
search()
count_by_status()
menu()
add_item()
list_items()
toggle_done()
