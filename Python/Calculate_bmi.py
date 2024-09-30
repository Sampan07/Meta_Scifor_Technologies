from _datetime import datetime
def calculate_bmi(height,weight) ->float:
    bmi = height/(pow(height,2))
    date = datetime.now().strftime("%Y-%m-%d %A %H:%M:%S")
    file = open("bmi.txt","a")
    file.write(f"Date: {date}, Height: {height} cm, Weight: {weight} kg, BMI: {bmi}\n")
    print(f"Date: {date}, Height: {height} cm, Weight: {weight} kg, BMI: {bmi}")
    file.close()

if __name__=="__main__":
    calculate_bmi(1.71,80)