# Python 發送郵件用法
# import email.message
#
# msg = email.message.EmailMessage()
# msg["From"]="寄件人"
# msg["To"]="收件人"
# msg["Subject"]="郵件標題"
# 寄送純文字的內容
# msg.set_content("文字的內容")
# 寄送比較多樣式的內容
# msg.add_alternative("<h2>優惠券</h2>滿伍佰送一百",subtype="html")

# import smtplib
# server= smtplib.SMTP_SSL("主機名稱","連接埠號(port)")
# server.login("帳號","密碼")
# #msg 變數存放準備好的訊息物件
# server.send_message(msg)
# server.close()

import email.message
import smtplib
from pythonEx01.env import gmail_env as genv

msg = email.message.EmailMessage()
msg["From"] = genv.gmail_obj.get("sender")
msg["To"] = genv.gmail_obj.get("receiver")
msg["Subject"] = "您好,Python Mail測試From YansZero"
# 寄送純文字的內容 與下面擇一
msg.set_content("測試看看")
# 寄送比較多樣式的內容
msg.add_alternative("<h2>優惠券</h2>滿伍佰送一百", subtype="html")

server = smtplib.SMTP_SSL(genv.gmail_obj.get("smtp_url"), genv.gmail_obj.get("smtp_port"))
server.login(genv.gmail_obj.get("sender"), genv.gmail_obj.get("secret"))
server.send_message(msg)
server.close()
