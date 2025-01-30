class CalorieCalculator:
    # حساب السعرات الحرارية

    #دالة لتعريف القيم الطول الوزن العمر الخ
    def __init__(self, weight, height, age, gender, activity_level):
        self.weight = weight  # الوزن بالكيلوغرام
        self.height = height  # الطول بالسنتيمتر
        self.age = age  # العمر
        self.gender = gender  # الجنس (ذكر أو أنثى)
        self.activity_level = activity_level  # مستوى النشاط البدني

    #دالة لحساب معدل الايض بناء على جنسك
    def calculate_bmr(self):
        if self.gender.lower() == "m":
            bmr = 88.362 + (13.397 * self.weight) + (4.799 * self.height) - (5.677 * self.age)
        else:
            bmr = 447.593 + (9.247 * self.weight) + (3.098 * self.height) - (4.330 * self.age)
        return bmr

    #دالة لحساب السعرات اليومية حسب نشاطك اليومي
    def calculate_daily_calories(self):
        bmr = self.calculate_bmr()
        activity_multipliers = {
            "1": 1.2, #sedentary
            "2": 1.375, #light
            "3": 1.55, #moderate
            "4": 1.725, #active
            "5": 1.9 #very_active
        }
        activity_multiplier = activity_multipliers.get(self.activity_level.lower(), 1.2)
        daily_calories = bmr * activity_multiplier
        return daily_calories
    

class calories:
    #حساب السعرات الحراريه للطعام
    weight_reference = 100 # القيمه المرجعيه الي نقسم عليها عدد السعرات

    #دالة لتعريف السعرات لكل 100قرام و كم قرام تبي تاكل
    def __init__(self,calories_per_100g,weight_in_grams):
        self.calories_per_100g = calories_per_100g  
        self.weight_in_grams = weight_in_grams  


    #دالة لحساب السعرات الحراري للطعام
    def calculate_calories(self):
      cal = (self.calories_per_100g/self.weight_reference)*self.weight_in_grams
      return cal
    #دالة لطباعة النتائج لسعرات الطعام
    def display_calories(self):
        print(f"\t--Calories: {self.calculate_calories():} (for {self.weight_in_grams}g)\n")


print("Welcome to the calories calculator (daily calories or food calories)") #رسالة ترحيبية
print("================================")
#منطق البرنامج بالكامل

while True: #تكرار العملية حتى يطلب العميل التوقف
    fd_calores = input('--what calores you want to calc ("D" for daily "F" for food ) "q" to close the app ').lower()# يطلب من المستخدم اذا كان يبي يحسب السعرات الحرارية لليوم او الاكل
    print("================================")
    if fd_calores != "q": #في حال لم تكن القيمه في الادخال السابق لاغلاق التطبيق

        if fd_calores == "d":#لو كان المدخل ذكر
            print("Daily Calories Calculator\nEnter your weight, height, age, gender, and active level")

            weight = float(input("\t--Weight (kg): ")) #يسال عن الوزن
            print("--------------\n")
            height = float(input("\t--Height (cm): "))# يسال عن الطول
            print("--------------\n")
            age = int(input("\t--Age: "))#يسال عن العمر
            print("--------------\n")
            gender = input('\t--Gender ("m" for male and "f" for female): ')#يسال عن الجنس ذكر او انثى
            print("--------------\n")
            activity_level = input("\t--Activity level ((1)sedentary, (2)light, (3)moderate, (4)active, (5)very_active): ")#يسال عن مستى النشاط خلال اليوم
            print("--------------\n")
            user = CalorieCalculator(weight, height, age, gender, activity_level)#انشاء عنصر من كلاس حساب السعرات اليومية

            print(f"\t--Daily Calories: {user.calculate_daily_calories()}\n-----------\n\nif you want to (lose or add) some weight around 1kg every two weks (-500 or +500) calores\n================================ ") #طباعة النتيجه 

        elif fd_calores == "f":# لو في حال كان لحساب سعرات الطعام
            print("Food Calories Calculator\nEnter the calories per 100g and weight in grams")
            print("================================")
            calories_per_100g = float(input("\t--Calories per 100g : ")) #السعرات لكل 100 قرام
            print("--------------\n")
            weight_in_grams = float(input("\t--Weight (g): ")) #عدد القرامت المتناولة
            print("\t--------------")
            food = calories(calories_per_100g, weight_in_grams)# انشاء عنصر من كلاس حساب سعرات الطعام و ارسال القيم المدخله له
            food.display_calories()# طباعة النتيجة
    else:
        break 
       