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
            bmr = 88.362 + (13.397 * self.weight) + (4.799 * self.height) - (5.677 * self.age)#حساب معدل الحرق للرجل
        else:
            bmr = 447.593 + (9.247 * self.weight) + (3.098 * self.height) - (4.330 * self.age)#حساب معدل الحرق للانثى
        return bmr

    #دالة لحساب السعرات اليومية حسب نشاطك اليومي
    def calculate_daily_calories(self):#تعريف الدالة
        bmr = self.calculate_bmr() #تخزين معلومات معدل الحرق بناء على الجنس
        activity_multipliers = { # قاموس لمعدل الحركة في اليوم
            "1": 1.2, #sedentary
            "2": 1.375, #light
            "3": 1.55, #moderate
            "4": 1.725, #active
            "5": 1.9 #very_active
        }
        activity_multiplier = activity_multipliers.get(self.activity_level.lower(), 1.2)#الحصول على معلومات معدل الحرق 
        daily_calories = bmr * activity_multiplier #ضرب ناتج معلومات الحرق في معدل الحركة اليومية
        return daily_calories #ارجاع القيمة
    
    #دالة لحفظ المعلومات الخاصه ي السعرات اليومية
    def save_data(self):#تعريف الدالة
        with open("caloie.txt","a") as f:#فتح الملف في حال كان متواجد او انشاء الملف في حال كان غير موجود
            f.write("daily calorie is: "+str(self.calculate_daily_calories()) + "\n") #كتابة المعلومات في داخل الملف

    def get_data(self):
        with open("caloie.txt","r") as f:
           print("calorie saved is: \n"+f.read()) 

class calories:
    #حساب السعرات الحراريه للطعام

    #دالة لتعريف السعرات لكل 100قرام و كم قرام تبي تاكل
    def __init__(self,calories_per_100g,weight_reference,grams_eat):
        self.weight_reference = weight_reference  # القيمة المرجعيه الي نقسم عليها عدد السعرات
        self.calories_per_100g = calories_per_100g  #السعرات حسب القيمة المرجعية
        self.grams_eat= grams_eat #القرامات المراد اكلها


    #دالة لحساب السعرات الحراري للطعام
    def calculate_calories(self):# تعريف الدالة 
      cal = (self.calories_per_100g/weight_reference)*self.grams_eat #العملة الحسابة لحساب سعرات الطعام
      return cal #ارجاع مخرجات العملة الحسابة
    
    #دالة لطباعة النتائج لسعرات الطعام
    def display_calories(self):#تعريف الدالة
        print(f"\t--Calories: {self.calculate_calories():} (for {self.weight_reference}g)\n")#طباعة السعرات الحرارية
        


print("Welcome to the calories calculator (daily calories or food calories)") #رسالة ترحيبية
print("================================")

#====================منطق البرنامج بالكامل==========================

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
            print(f"\t--Daily Calories: {user.calculate_daily_calories()}\n-------------\n\nif you want to (lose or add) some weight around 1kg every two weks (-500 or +500) calores") #طباعة النتيجه 
            print("--------------\n")

            
            
            while True:
                save = input("do you want to save your calories? (y/n)  or get the data? (get) or remove data? (del): ") #سوال لو حاب تحفظ المعلومات في ملف txt
                if save == "y":# في حال وافقت عل خفظ المعلومات
                    print("data saved")
                    user.save_data()
                    break

                elif save == "n":#في حال عدم الرغبة في حفظ المعلومات
                    print("no saved data")
                    break

                elif save == "get":
                    user.get_data()
                    break
                else: 
                    print("Denied, plz enter to save your calories? (y/n)  or get the data? (get) or remove data? (del):")
            print("--------------\n")
            

            print("================================")

        elif fd_calores == "f":# لو في حال كان لحساب سعرات الطعام
            print("Food Calories Calculator\nEnter the calories per 100g and weight in grams")
            print("================================")
            weight_reference = float(input("\t--cla p er (g)?: ")) #قرامات الي يدخلها المستخدم
            print("--------------\n")

            calories_per_100g = float(input(f"\t--Calories per {weight_reference} (g): ")) #السعرات لكل قرام ادخله المستخدم
            print("--------------\n")

            grams_eat = float(input("\t--grams you want to eat (g): ")) #عدد القرامت المتناولة
            print("\t--------------")

            food = calories(calories_per_100g,weight_reference,grams_eat)# انشاء عنصر من كلاس حساب سعرات الطعام و ارسال القيم المدخله له
            food.display_calories()# طباعة النتيجة
    else:
        break 
       