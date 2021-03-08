with open('nginx_logs.txt', 'r', encoding='UTF-8') as f:
    ip_gen = (line.split()[0] for line in f)
    user_activity = {}
    for ip in ip_gen:
        if ip in user_activity:
            user_activity[ip] += 1
        else:
            user_activity[ip] = 1
    sorted_user_activity = {}
    sorted_user_activity = sorted(user_activity, key=user_activity.get)
    print(
        f'Пользователь с IP - {sorted_user_activity[-1]} сгенерировал максималное количество запросов.\nКоличество запросов равно {user_activity[sorted_user_activity[-1]]}')
