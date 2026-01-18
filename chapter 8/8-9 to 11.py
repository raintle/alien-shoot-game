

messages_1_pack = ['hello', 'one', 'go', 'good']
messages_1 = ['hello', 'one', 'go', 'good']
messages_2 = []
messages_2_pack = []

def show_messages(messages_1st, messages_2nd):
    """处理列表"""
    while messages_1st:
        message = messages_1st.pop()
        #弹出
        messages_2nd.append(message)
        #加入

def show_messages_list(messages_1st, messages_2nd):
    """打印消息"""
    print(messages_1st, '\n', messages_2nd)

show_messages(messages_1, messages_2)
show_messages_list(messages_1, messages_2)
show_messages(messages_1_pack[:], messages_2_pack)
#禁止修改原列表
show_messages_list(messages_1_pack, messages_2_pack)