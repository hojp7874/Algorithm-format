# https://programmers.co.kr/learn/courses/30/lessons/42888?language=python3

class User:
    def __init__(self, user_id):
        self.user_id = user_id
    
    def rename(self, new_name):
        self.nickname = new_name
        

class ChatRoom:
    def __init__(self):
        self.logs = []
    
    def enter(self, user):
        log = [user, 'enter']
        self.logs.append(log)
    
    def leave(self, user):
        log = [user, 'leave']
        self.logs.append(log)
    
    def get_logs(self):
        logs = []
        for user, state in self.logs:
            if state == 'enter':
                logs.append(f'{user.nickname}님이 들어왔습니다.')
            else:
                logs.append(f'{user.nickname}님이 나갔습니다.')
        return logs
        

def solution(record):
    chat_room = ChatRoom()
    user_dict = {}
    for rec in record:
        command, user_id, *nickname = rec.split()
        nickname = nickname[0] if nickname else None
        if command == 'Enter':
            if user_dict.get(user_id) is None:
                user_dict.setdefault(user_id, User(user_id))
            user_dict[user_id].rename(nickname)
            chat_room.enter(user_dict[user_id])
        elif command == 'Leave':
            chat_room.leave(user_dict[user_id])
        elif command == 'Change':
            user_dict[user_id].rename(nickname)
    return chat_room.get_logs()


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
result = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
print(solution(record) == result)