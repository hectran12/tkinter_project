#AUTHOR: HEXTRAN2008
#12/05/2023




# import tkinter
from tkinter import *

# import mongo
import mongo
# import messagebox
from tkinter import messagebox
mongo.url = 'mongodb://localhost:27017' # url
mongo.conn() # connect to database



# render list nhansu
def renderListNhanSu(listbox: Listbox, data):
    # sort 
    data = sorted(data, key=lambda x: x['id'])
    # clear dataa in listbox
    listbox.delete(0, END)
    for item in data:
        infomation = 'ID: ' + str(item["id"]) + ' Name: ' + item['name'] + ' - Age: ' + str(item['age']) + ' - Address: ' + item['address'] + '\n'
        listbox.insert(END, infomation)


# on listbox 
def onListboxSelect(event):
    currentSelect = listbox.curselection()

    if currentSelect:
        item = listbox.get(currentSelect[0])
    
        name = item.split('Name: ')[1].split(' - Age: ')[0]
        # create menu 
        menu = Menu(root, tearoff=0)
        menu.add_command(label="Xoa {0}".format(name), command=delete_item)
        menu.add_command(label="Sua {0}".format(name), command=edit_item)
        menu.post(event.x_root, event.y_root)


def add_item():


    root = Tk()
    root.geometry("400x200")

    # create label with name "Them nhan vien"
    lb = Label(root, text="Them nhan vien")

    name_label = Label(root, text='Họ tên')
    name_label.grid(column=0, row=0, padx=5, pady=5, sticky=W)
    name_entry = Entry(root, width=30)
    name_entry.grid(column=1, row=0, padx=5, pady=5)

    address_label = Label(root, text='Địa chỉ')
    address_label.grid(column=0, row=1, padx=5, pady=5, sticky=W)
    address_entry = Entry(root, width=30)
    address_entry.grid(column=1, row=1, padx=5, pady=5)

    age_label = Label(root, text='Tuổi')
    age_label.grid(column=0, row=2, padx=5, pady=5, sticky=W)
    age_entry = Entry(root, width=30)
    age_entry.grid(column=1, row=2, padx=5, pady=5)
    # Tạo nút "Lưu"
    save_button = Button(root, text='Lưu', command=lambda: [mongo.add(name_entry.get(), age_entry.get(), address_entry.get()), 
                                                            messagebox.showinfo("Thong bao", "Them thanh cong"), renderListNhanSu(listbox, mongo.getAll()), 
                                                            root.destroy()])
    save_button.grid(column=1, row=3, padx=5, pady=5)

    root.mainloop()
    
   

# on delete
def delete_item():
    currentSelect = listbox.curselection()

    if currentSelect:
        item = listbox.get(currentSelect[0])
        
        id = item.split('ID: ')[1].split(' ')[0]
        mongo.delete(int(id))
        renderListNhanSu(listbox, mongo.getAll())
        messagebox.showinfo("Thong bao", "Xoa thanh cong")
    else:
        messagebox.showinfo("Thong bao", "Vui long chon nhan vien muon xoa")

def edit_item():
    currentSelect = listbox.curselection()

    if currentSelect:
        item = listbox.get(currentSelect[0])
        
        id = item.split('ID: ')[1].split(' ')[0]
        root = Tk()
        root.geometry("400x200")

        # create label with name "Them nhan vien"
        lb = Label(root, text="Sua nhan vien")

        name_label = Label(root, text='Họ tên')
        name_label.grid(column=0, row=0, padx=5, pady=5, sticky=W)
        name_entry = Entry(root, width=30)
        name_entry.grid(column=1, row=0, padx=5, pady=5)
        name_entry.insert(0, item.split('Name: ')[1].split(' - Age: ')[0])
        address_label = Label(root, text='Địa chỉ')
        address_label.grid(column=0, row=1, padx=5, pady=5, sticky=W)
        address_entry = Entry(root, width=30)
        address_entry.grid(column=1, row=1, padx=5, pady=5)
        address_entry.insert(0, item.split(' - Address: ')[1].split('\n')[0])
        age_label = Label(root, text='Tuổi')
        age_label.grid(column=0, row=2, padx=5, pady=5, sticky=W)
        age_entry = Entry(root, width=30)
        age_entry.insert(0, item.split(' - Age: ')[1].split(' - Address: ')[0])
        age_entry.grid(column=1, row=2, padx=5, pady=5)
        # Tạo nút "Lưu"
        save_button = Button(root, text='Lưu', command=lambda: [mongo.update(int(id), name_entry.get(), age_entry.get(), address_entry.get()), 
                             messagebox.showinfo("Thong bao", "Sua thanh cong"),
                               renderListNhanSu(listbox, mongo.getAll()), root.destroy()
            ])
        save_button.grid(column=1, row=3, padx=5, pady=5)

        root.mainloop()

# create form with name "Quan ly nhan su"
root = Tk()
root.title("Quan ly nhan su")
root.geometry("500x500")

# create label with name "Quan ly nhan su"
label = Label(root, text="Quan ly nhan su")
label.pack()

# create button with name "Them nhan vien"
button = Button(root, text="Them nhan vien", command=add_item)
button.pack()



# create listbox width and height fill all form
data = mongo.getAll()
listbox = Listbox(root, width=500, height=500)
listbox.pack()
renderListNhanSu(listbox, data)





listbox.bind('<Button-3>', onListboxSelect)
# loop
root.mainloop()
