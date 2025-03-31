def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)

    return the_mean

monday_temperatures = [9.1, 8.2, 7.5] #lista
student_grades = {"marry": 9.1, "Sim": 8.8, "Jon": 9.9}
print(mean(monday_temperatures))
