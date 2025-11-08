import datetime
import json
import os
from typing import List, Dict

class FoodItem:
    def __init__(self, name: str, expiry_date: datetime.date, quantity: str = "1 unit"):
        self.name = name
        self.expiry_date = expiry_date
        self.quantity = quantity
        self.added_date = datetime.date.today()
    
    def days_until_expiry(self) -> int:
        today = datetime.date.today()
        return (self.expiry_date - today).days
    
    def is_expired(self) -> bool:
        return self.days_until_expiry() < 0
    
    def to_dict(self) -> Dict:
        return {
            'name': self.name,
            'expiry_date': self.expiry_date.isoformat(),
            'quantity': self.quantity,
            'added_date': self.added_date.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict):
        item = cls(
            name=data['name'],
            expiry_date=datetime.date.fromisoformat(data['expiry_date']),
            quantity=data['quantity']
        )
        item.added_date = datetime.date.fromisoformat(data['added_date'])
        return item

class FoodWasteManager:
    def __init__(self, data_file: str = "food_items.json"):
        self.data_file = data_file
        self.food_items: List[FoodItem] = []
        self.load_data()
    
    def add_food_item(self, name: str, expiry_date: datetime.date, quantity: str = "1 unit"):
        """Add a new food item to track"""
        item = FoodItem(name, expiry_date, quantity)
        self.food_items.append(item)
        self.save_data()
        print(f"Added {quantity} of {name} (expires: {expiry_date})")
    
    def remove_food_item(self, index: int):
        """Remove a food item by index"""
        if 0 <= index < len(self.food_items):
            removed_item = self.food_items.pop(index)
            self.save_data()
            print(f"Removed {removed_item.name}")
        else:
            print("Invalid index!")
    
    def check_expiry_reminders(self, days_before: int = 3) -> List[FoodItem]:
        """Get items that are expiring soon or have expired"""
        reminders = []
        for item in self.food_items:
            days_until = item.days_until_expiry()
            if days_until <= days_before:
                reminders.append((item, days_until))
        
        # Sort by days until expiry (soonest first)
        reminders.sort(key=lambda x: x[1])
        return reminders
    
    def display_reminders(self, days_before: int = 3):
        """Display expiry reminders to the user"""
        reminders = self.check_expiry_reminders(days_before)
        
        if not reminders:
            print("\nNo expiry reminders! All items are fresh.")
            return
        
        print(f"\nEXPIRY REMINDERS (next {days_before} days):")
        print("-" * 50)
        
        for item, days_until in reminders:
            if days_until < 0:
                status = "EXPIRED!"
            elif days_until == 0:
                status = "Expires TODAY!"
            else:
                status = f"Expires in {days_until} day(s)"
            print(f"- {item.name} ({item.quantity}) - {status}")
    
    def list_all_items(self):
        """Display all tracked food items"""
        if not self.food_items:
            print("\nNo food items being tracked.")
            return
        
        print("\nALL TRACKED FOOD ITEMS:")
        print("-" * 50)
        
        for i, item in enumerate(self.food_items):
            days_until = item.days_until_expiry()
            if days_until < 0:
                status = "EXPIRED"
            else:
                status = f"{days_until} days left"
            print(f"{i+1}. {item.name} ({item.quantity}) - Expires: {item.expiry_date} [{status}]")
    
    def save_data(self):
        """Save food items to JSON file"""
        data = [item.to_dict() for item in self.food_items]
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_data(self):
        """Load food items from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                self.food_items = [FoodItem.from_dict(item_data) for item_data in data]
            except (json.JSONDecodeError, KeyError):
                print("Warning: Data file corrupted, starting fresh.")
                self.food_items = []

def main():
    manager = FoodWasteManager()
    
    while True:
        print("\nFOOD WASTE MANAGEMENT APP")
        print("1. Add food item")
        print("2. View expiry reminders")
        print("3. List all items")
        print("4. Remove food item")
        print("5. Exit")
        
        choice = input("\nChoose an option (1-5): ").strip()
        
        if choice == '1':
            name = input("Food item name: ").strip()
            quantity = input("Quantity (e.g., '2 bottles', '500g'): ").strip() or "1 unit"
            
            try:
                expiry_str = input("Expiry date (YYYY-MM-DD): ").strip()
                expiry_date = datetime.date.fromisoformat(expiry_str)
                
                if expiry_date < datetime.date.today():
                    print("Warning: This expiry date has already passed!")
                
                manager.add_food_item(name, expiry_date, quantity)
            except ValueError:
                print("Invalid date format! Please use YYYY-MM-DD")
        
        elif choice == '2':
            try:
                days_input = input("Show reminders for how many days before expiry? (default 3): ").strip()
                days = int(days_input) if days_input else 3
                manager.display_reminders(days)
            except ValueError:
                print("Invalid number! Using default of 3 days.")
                manager.display_reminders(3)
        
        elif choice == '3':
            manager.list_all_items()
        
        elif choice == '4':
            manager.list_all_items()
            if manager.food_items:
                try:
                    index = int(input("Enter item number to remove: ")) - 1
                    manager.remove_food_item(index)
                except ValueError:
                    print("Invalid number!")
        
        elif choice == '5':
            print("Goodbye! Don't forget to check your food items regularly.")
            break
        
        else:
            print("Invalid option! Please choose 1-5.")

if __name__ == "__main__":
    main()