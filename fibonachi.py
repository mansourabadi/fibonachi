def fibonacci(n):
    fib_list = [0, 1]  # دو عدد ابتدایی در دنباله فیبوناچی
    total_sum = 1  # مجموع تا اینجا
    for i in range(2, n):
        next_num = fib_list[i - 1] + fib_list[i - 2]  # محاسبه عدد بعدی در دنباله
        fib_list.append(next_num)  # اضافه کردن عدد بعدی به لیست
        total_sum += next_num  # اضافه کردن عدد بعدی به مجموع
    return fib_list, total_sum

n = int(input("ta jomle chandm namayesh bedm? "))
fib_sequence, sum_of_sequence = fibonacci(n)
print(fib_sequence)
print("sum of fibonachi list: ", sum_of_sequence)
