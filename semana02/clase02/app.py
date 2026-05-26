from users import users, flag
from datetime import datetime
from pprint import pprint
import operations

def main():
    if flag == True:
        for user in users:
            user['now'] = str(datetime.now())
        
        pprint(users)

    print(operations.flag_2)

if __name__ == '__main__':
    main()