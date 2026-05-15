import logging

# 1. 配置：告诉机器，日记长什么样，记到什么程度
# 这里的 format 就是你提到的“四要素”中的：等级 (Level) + 内容 (Payload)
logging.basicConfig(level=logging.ERROR, format='%(levelname)s: %(message)s')

def save_money(amount):
    # 【DEBUG】—— 细碎记录（导演要求的“废话”，开发时看）
    logging.debug(f"正在尝试存入金额: {amount}") 
    
    if amount <= 0:
        # 【ERROR】—— 严重错误（这个必须记，程序出大事了）
        logging.error(f"存钱失败！金额 {amount} 是非法输入。")
    elif amount < 10:
        # 【WARNING】—— 提醒（虽然没崩，但有点不对劲）
        logging.warning(f"存得有点少啊，只有 {amount} 元。")
    else:
        # 【INFO】—— 正常汇报（每天的例行公事）
        logging.info(f"存钱成功！当前存入: {amount} 元。")

# 运行看看效果
save_money(100)  # 触发 INFO
save_money(5)    # 触发 WARNING
save_money(-1)   # 触发 ERROR