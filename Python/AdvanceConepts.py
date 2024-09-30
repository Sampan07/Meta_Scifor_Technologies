import tkinter as tk
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def filter_numbers():
    return filter(lambda x: x % 2 == 0, numbers)

def iterate_numbers():
    return iter(numbers)

def map_numbers():
    return map(lambda x: x ** 2, numbers)

def on_filter_click():
    filtered_list = list(filter_numbers())
    listbox.delete(0, tk.END)
    for num in filtered_list:
        listbox.insert(tk.END, num)
def on_iterator_click():
    iterator = iterate_numbers()
    listbox.delete(0, tk.END)
    for num in iterator:
        listbox.insert(tk.END, num)
def on_map_click():
    mapped_list = list(map_numbers())
    listbox.delete(0, tk.END)
    for num in mapped_list:
        listbox.insert(tk.END, num)

root = tk.Tk()
root.title("Number Operations")

label = tk.Label(root, text="Click a button to perform an operation on the numbers:")
label.pack(pady=10)

filter_button = tk.Button(root, text="Filter(Gives Even Numbers)", command=on_filter_click)
filter_button.pack(pady=5)

iterator_button = tk.Button(root, text="Iterator(Iterate through numbers)", command=on_iterator_click)
iterator_button.pack(pady=5)

map_button = tk.Button(root, text="Map(Square each number)", command=on_map_click)
map_button.pack(pady=5)

listbox = tk.Listbox(root, width=30)
listbox.pack(pady=10)

root.mainloop()