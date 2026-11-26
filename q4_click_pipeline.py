def select_clicks(raw_clicks, min_clicks=10):
    stripped = map(lambda s: s.strip(), raw_clicks)
    non_empty = filter(None, stripped)
    numbers = list(map(int, non_empty))
    qualified = list(filter(lambda x: x >= min_clicks, numbers))
    return (numbers, qualified)


def main():
    student_id = input("請輸入完整學號：").strip().upper()
    tail = student_id[-3:]
    a = int(student_id[-3])
    b = int(student_id[-2])
    c = int(student_id[-1])
    s = a + b + c

    raw_clicks = [str(10 + a), "0", "", " " + str(5 + b) + " ",
                  "   ", str(15 + c), str(5 + b)]
    min_clicks = 5 + b

    numbers, qualified = select_clicks(raw_clicks, min_clicks=min_clicks)

    print(f"學號：{student_id}")
    print(f"點擊門檻：{min_clicks}")
    print(f"清理結果：{numbers}")
    print(f"合格結果：{qualified}")
    print(f"合格筆數：{len(qualified)}")
    print(f"合格合計：{sum(qualified)}")

    ranked = sorted(qualified, reverse=True)
    for rank, clicks in enumerate(ranked, start=1):
        print(f"第{rank}名：{clicks}次")

    _, high_qualified = select_clicks(raw_clicks, min_clicks=100)
    print(f"門檻100合格結果：{high_qualified}")
    print(f"門檻100合格筆數：{len(high_qualified)}")
    print(f"門檻100合格合計：{sum(high_qualified)}")
    if not high_qualified:
        print("無符合門檻的素材")


if __name__ == "__main__":
    main()