admin = ['A', 'D']
user = ['A', 'B', 'C', 'D', 'E', 'F']
premium = ['C', 'F']
while True:
    print('ユーザーを検索します。名前を入力してください。')
    print('ユーザーを削除する場合は、削除 と入力してください。')
    name = input('処理を終了するにはENDと入力してください。')
    if name == 'END':
        print('プログラムを終了します。')
        break
    elif name in user:
        if name in admin:
            print(f'{name} さんは管理者です。')
            continue
        elif name in premium:
            print(f'{name} さんは有料会員です。')
            continue
        print(f'{name} さんは一般ユーザーです。')
    elif name not in user:
        print(f'{name} さんはユーザー登録されていません。新規登録します。')
        user.append(name)
        print(f'UserList: {user}')