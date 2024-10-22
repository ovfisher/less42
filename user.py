class User:
    def __init__(self, uid, uname):
        self._uid = uid
        self._uname = uname
        self._uacces = 0

    def get_user_info(self):
        return f" user : {self._uid},{self._uname},{self._uacces}."
    def set_user_name(self,name):
        self._uname = name

# staff - user's list
staff = []

class Admin(User):
    def __init__(self, uid, uname):
        super().__init__(uid,uname)
        self._uacces = 1

    def get_admin_info(self):
        return f" admin : {self._uid},{self._uname},{self._uacces}"

    def add_user(self,usr,staff):
        staff.append(usr)
        add_user = f'{self.get_user_info()}'
        return add_user

    def remove_user(self,usr,staff):
        staff.remove(usr)
        remove_user = f'{self.get_user_info()}'
        return remove_user

adm = Admin(len(staff),'root')
usr = User(len(staff),'usr')

print(usr.get_user_info(),' count = ',len(staff))
adm.add_user(adm,staff)
adm.add_user(usr,staff)

for user in staff:
    #if i.status == 'active':
        print(user.get_user_info())
