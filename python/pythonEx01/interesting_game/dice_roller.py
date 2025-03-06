# Python骰骰子遊戲

# 骰出骰子後顯示總和圖案
# 使用unicode 字元才製作骰子圖案

import random

dice_art = {
    1: (
        "┌───────┐",
        "│       │",
        "│   ●   │",
        "│       │",
        "└───────┘",
    ),
    2: (
        "┌───────┐",
        "│ ●     │",
        "│       │",
        "│     ● │",
        "└───────┘",
    ),
    3: (
        "┌───────┐",
        "│ ●     │",
        "│   ●   │",
        "│     ● │",
        "└───────┘",
    ),
    4: (
        "┌───────┐",
        "│ ●   ● │",
        "│       │",
        "│ ●   ● │",
        "└───────┘",
    ),
    5: (
        "┌───────┐",
        "│ ●   ● │",
        "│   ●   │",
        "│ ●   ● │",
        "└───────┘",
    ),
    6: (
        "┌───────┐",  # 0
        "│ ●   ● │",  # 1
        "│ ●   ● │",  # 2
        "│ ●   ● │",  # 3
        "└───────┘",  # 4
    ),
}
# print(dice_art.get(6))
dice_number = 0
dice_list = []


def get_dice_number(number):
    for x in range(5):
        print(dice_art.get(number)[i])


# get_dice_number(3)

num_dices = int(input("請輸入要骰幾顆骰子(最多5個):"))
if num_dices < 1 or num_dices > 5:
    print("無效的骰子個數")
else:
    for i in range(num_dices):
        dice_number = random.randint(1, 6)
        dice_list.append(dice_number)

print(f"你總共骰了{num_dices}個骰子,結果如下")
for item in dice_list:
    get_dice_number(item)

print(f"骰子總和為{sum(dice_list)}")
