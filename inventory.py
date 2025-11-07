class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity
        print(f"Tambah {quantity} {item_name}.")

    def edit_item(self, item_name, new_quantity):
        if item_name in self.items:
            self.items[item_name] = new_quantity
            print(f"Perbarui {item_name} menjadi {new_quantity}.")
        else:
            print(f"Item {item_name} tidak ditemukan dalam inventaris.")

    def delete_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Hapus {item_name} dari inventaris.")
        else:
            print(f"Item {item_name} tidak ditemukan dalam inventaris.")

    def view_items(self):
        if not self.items:
            print("Inventaris kosong.")
        else:
            print("Inventaris Saat Ini:")
            for item_name, quantity in self.items.items():
                print(f"{item_name}: {quantity}")

def main():
    inventory = Inventory()
    while True:
        print("\nMenu Inventaris:")
        print("1. Tambah Item")
        print("2. Edit Item")
        print("3. Hapus Item")
        print("4. Lihat Item")
        print("5. Keluar")
        choice = input("Pilih opsi: ")

        if choice == '1':
            item_name = input("Masukkan nama item: ")
            quantity = (input("Masukkan jumlah: "))
            inventory.add_item(item_name, quantity)
        elif choice == '2':
            item_name = input("Masukkan nama item yang ingin diedit: ")
            new_quantity = (input("Masukkan jumlah baru: "))
            inventory.edit_item(item_name, new_quantity)
        elif choice == '3':
            item_name = input("Masukkan nama item yang ingin dihapus: ")
            inventory.delete_item(item_name)
        elif choice == '4':
            inventory.view_items()
        elif choice == '5':
            print("Keluar dari menu inventaris.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
if __name__ == "__main__":
    main()
