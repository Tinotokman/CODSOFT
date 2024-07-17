import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactManager:
    def __init__(self, root):
        self.contacts = {}
        
        self.root = root
        self.root.title("Contact Manager")
        
        self.name_label = tk.Label(root, text="Name")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)
        
        self.phone_label = tk.Label(root, text="Phone")
        self.phone_label.grid(row=1, column=0)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1)
        
        self.email_label = tk.Label(root, text="Email")
        self.email_label.grid(row=2, column=0)
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=2, column=1)
        
        self.address_label = tk.Label(root, text="Address")
        self.address_label.grid(row=3, column=0)
        self.address_entry = tk.Entry(root)
        self.address_entry.grid(row=3, column=1)
        
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2)
        
        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=5, column=0, columnspan=2)
        
        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=6, column=0, columnspan=2)
        
        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=7, column=0, columnspan=2)
        
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=8, column=0, columnspan=2)
    
    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        
        if name and phone:
            self.contacts[phone] = {"name": name, "email": email, "address": address}
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Name and Phone are required fields.")
    
    def view_contacts(self):
        contacts_list = "\n".join([f"{info['name']} - {phone}" for phone, info in self.contacts.items()])
        messagebox.showinfo("Contact List", contacts_list if contacts_list else "No contacts found.")
    
    def search_contact(self):
        query = simpledialog.askstring("Search Contact", "Enter name or phone number")
        if query:
            results = [f"{info['name']} - {phone}" for phone, info in self.contacts.items() if query in phone or query.lower() in info['name'].lower()]
            messagebox.showinfo("Search Results", "\n".join(results) if results else "No contacts found.")
    
    def update_contact(self):
        query = simpledialog.askstring("Update Contact", "Enter phone number of the contact to update")
        if query and query in self.contacts:
            name = self.name_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()
            
            if name:
                self.contacts[query]["name"] = name
            if email:
                self.contacts[query]["email"] = email
            if address:
                self.contacts[query]["address"] = address
            
            messagebox.showinfo("Success", "Contact updated successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Contact not found.")
    
    def delete_contact(self):
        query = simpledialog.askstring("Delete Contact", "Enter phone number of the contact to delete")
        if query and query in self.contacts:
            del self.contacts[query]
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showwarning("Input Error", "Contact not found.")
    
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()