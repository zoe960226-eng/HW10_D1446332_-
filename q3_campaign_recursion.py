def cumulative_spend(daily_spend, n):
    if n == 0:
        return 0
    return cumulative_spend(daily_spend, n - 1) + daily_spend[n - 1]


def main():
    student_id = input("請輸入完整學號：").strip().upper()
    tail = student_id[-3:]
    a = int(student_id[-3])
    b = int(student_id[-2])
    c = int(student_id[-1])
    s = a + b + c

    daily_spend = [100 + 10 * a, 150 + 10 * b, 0,
                   200 + 10 * c, 50 + 10 * s]
    n = 3 + c % 3

    print(f"學號：{student_id}")
    print(f"每日費用：{daily_spend}")
    print(f"指定n：{n}")
    print(f"指定前{n}天累計：{cumulative_spend(daily_spend, n)}元")

    for day in range(6):
        print(f"前{day}天：{cumulative_spend(daily_spend, day)}元")

    print(f"空資料：{cumulative_spend([], 0)}元")


if __name__ == "__main__":
    main()