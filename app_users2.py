class User:
    total_user=0
    user_list={}
    def __init__(self,name,email_address,driverlincense_num):
        self._name=name
        self._email_address=email_address
        self._driverlicense_num=driverlincense_num
        User.total_user+=1
        User.user_list[self._name]=[]
        
        #User._post_list[self.name]=[]
    
    def create_post(self,content):
        User.user_list[self._name].append(content)

    def delete_post(self,post_content):
        for content in User.user_list[self._name]:
            if content==post_content:
                User.user_list[self._name].remove(post_content)
    
    def get_total_user():
        return User.total_user
    
    def get_user_list():
        return User.user_list

        
    
yen = User('Yen','jina@gmail.com','D12242')
mark =User('Mark','mak@gmail.com','D12342')

print(User.total_user)
print(User.user_list)
yen.create_post('Week2 day1 post')
mark.create_post('Week1 day2')
yen.create_post('Week2 day1 post2')
print(User.user_list)

yen.delete_post('Week2 day1 post2')
print(User.user_list)
