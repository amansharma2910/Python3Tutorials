class FullName:
    name = "Aman Sharma"

    def name_change(self):
        get_name = input("Enter the new name: ")
        self.name = get_name

name = FullName()
name.name_change()
print("Name :",name.name)