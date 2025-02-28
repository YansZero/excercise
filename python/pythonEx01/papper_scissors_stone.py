# 剪刀石頭布遊戲
import random

# 製作一個剪刀石頭布的遊戲
# 讓電腦跟你玩
# 規則 :
# 剪刀(scissors)贏布(paper)
# 石頭(stone)贏剪刀(scissors)
# 布(paper)贏石頭(stone)
# 玩法:
# 一開始玩家選擇要出的手勢(剪刀,石頭,布),選擇好之後依據規則比出勝負
# 若相同則繼續比出勝負

game_option = {1: "剪刀", 2: "石頭", 3: "布"}
running = True
print("------------歡迎來到剪刀石頭布的遊戲------------")

while running:
    user_choose = int(input("請輸入你要出的手勢(1:剪刀,2:石頭,3:布)"))
    com_choose = random.randint(1, 3)
    if user_choose not in game_option.keys():
        print("輸入錯誤,請重新出手勢")
    else:
        user_option = game_option.get(user_choose)
        com_option = game_option.get(com_choose)
        if user_choose == com_choose:
            print(f"雙方平手,皆為{com_option}")
        elif ((user_choose == 1 and com_choose == 3)
              or (user_choose == 2 and com_choose == 1)
              or (user_choose == 3 and com_choose == 2)):
            print(f"恭喜你獲勝了,你出{user_option},電腦出{com_option}")
        else:
            print(f"抱歉你輸了,你出{user_option},電腦出{com_option}")

    play_again = input("是否在玩一局(y/n)")
    if play_again == 'n':
        running = False
        print("謝謝遊玩")