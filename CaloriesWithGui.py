from tkinter import Tk, Label, Entry, Button, Toplevel

# ============================== الكلاسات ==============================
class Person:
    def __init__(self, name, age, gender, height, weight, activity_level):
        self.name = name
        self.age = int(age)
        self.gender = gender.lower()
        self.height = float(height)
        self.weight = float(weight)
        self.activity_level = activity_level

    def display_info(self):
        return (f"--- Data saved ---\nName: {self.name}\nWeight: {self.weight} kg\n"
                f"Height: {self.height} cm\nAge: {self.age}\nGender: {self.gender}\n"
                f"Activity Level: {self.activity_level}\n")


class DailyCalories(Person):
    def calculate_bmr(self):
        if self.gender == "m":
            return 88.362 + (13.397 * self.weight) + (4.799 * self.height) - (5.677 * self.age)
        return 447.593 + (9.247 * self.weight) + (3.098 * self.height) - (4.330 * self.age)

    def calculate_daily_calories(self):
        activity_multipliers = {"1": 1.2, "2": 1.375, "3": 1.55, "4": 1.725, "5": 1.9}
        return round(self.calculate_bmr() * activity_multipliers.get(self.activity_level, 1.2), 1)

    def save_data(self):
        with open("data.txt", "a") as f:
            f.write(f"{self.display_info()}Daily Calories: {self.calculate_daily_calories()} kcal\n\n")


class FoodCalories:
    def __init__(self, calories_per_grams, grams, grams_to_eat):
        self.calories_per_grams = float(calories_per_grams)
        self.grams = float(grams)
        self.grams_to_eat = float(grams_to_eat)

    def calculate_food_calories(self):
        return round((self.calories_per_grams / self.grams) * self.grams_to_eat, 1)


# ============================== الواجهة الرسومية ==============================
root = Tk()
root.title("Calories Calculator")
root.geometry("600x900")
root.config(bg="black")

def create_daily_calories():
    inputs = [name_entry.get(), age_entry.get(), gender_entry.get(), height_entry.get(), weight_entry.get(), activity_level_entry.get()]
    if "" in inputs:
        display_error("Please fill in all fields.")
        return
    
    user = DailyCalories(*inputs)
    user.save_data()
    display_message(f"{user.name}, daily calories needed: {user.calculate_daily_calories()} kcal")

def get_data():
    try:
        with open("data.txt", "r") as f:
            display_message(f.read())
    except FileNotFoundError:
        display_message("No saved data found.")

def display_message(message):
    message_label.config(text=message)

def display_error(error_message):
    error_label.config(text=error_message)

# واجهة المدخلات
Label(root, text="Welcome to Calories Calculator", font=("Arial", 20), fg="white", bg="black").pack(pady=15)
name_entry, age_entry, gender_entry, height_entry, weight_entry, activity_level_entry = [Entry(root, bg="gray", fg="white") for _ in range(6)]

labels = ["Enter your name:", "Enter your age:", "Enter your gender (m/f):", "Enter your height (cm):", "Enter your weight (kg):", "Enter your activity level (1-5):"]
for label, entry in zip(labels, [name_entry, age_entry, gender_entry, height_entry, weight_entry, activity_level_entry]):
    Label(root, text=label, fg="white", bg="black").pack()
    entry.pack(pady=5)

Button(root, text="Calculate", command=create_daily_calories, bg="green", fg="white").pack(pady=15)
Button(root, text="Get Data", command=get_data, bg="green", fg="white").pack(pady=5)
message_label = Label(root, text="", font=("Arial", 12), fg="white", bg="black")
message_label.pack()
error_label = Label(root, text="", font=("Arial", 12), fg="red", bg="black")
error_label.pack()

def open_food_calculator():
    window2 = Toplevel(root)
    window2.title("Food Calories Calculator")
    window2.geometry("600x600")
    window2.config(bg="black")
    
    def calculate_food():
        inputs = [cal_per_grams_entry.get(), grams_entry.get(), grams_to_eat_entry.get()]
        if "" in inputs:
            food_error_label.config(text="Please fill in all fields.")
            return
        
        food = FoodCalories(*inputs)
        food_result_label.config(text=f"Food Calories: {food.calculate_food_calories()} kcal")
    
    Label(window2, text="Welcome to Food Calories Calculator", font=("Arial", 20), fg="white", bg="black").pack(pady=20)
    cal_per_grams_entry, grams_entry, grams_to_eat_entry = [Entry(window2, bg="gray", fg="white") for _ in range(3)]
    labels = ["How much calories:", "How much grams:", "How much grams you want to eat:"]
    
    for label, entry in zip(labels, [cal_per_grams_entry, grams_entry, grams_to_eat_entry]):
        Label(window2, text=label, fg="white", bg="black").pack()
        entry.pack(pady=5)
    
    Button(window2, text="Calculate", command=calculate_food, bg="green", fg="white").pack(pady=15)
    food_result_label = Label(window2, text="", font=("Arial", 12), fg="white", bg="black")
    food_result_label.pack()
    food_error_label = Label(window2, text="", font=("Arial", 12), fg="red", bg="black")
    food_error_label.pack()

Button(root, text="Food Calories", command=open_food_calculator, bg="green", fg="white").pack(pady=5)
root.mainloop()