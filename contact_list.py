friends = [{'name': 'Alice', 'number': '867-5309'},
    {'name': 'Bob', 'number': '555-5555'}]
work_buddies = [{'name': 'Alice', 'number': '867-5309'},
                {'name': 'Carlos', 'number': '555-5555'}]
class ContactList:
    def __init__(self, category, contacts):
        self.category = category
        self.contact_list = {category: contacts}

    def add_contact(self, new_contact):
        self.contact_list[self.category].append(new_contact)

    def remove_contact(self, contact_name):
        for contact in self.contact_list[self.category]:
            if contact['name'] == contact_name:
                self.contact_list[self.category].remove(contact)

    # def find_shared_contacts(self, new_list):# 2 for loops
    #     shared_contacts = []
    #     for contact in new_list.list[new_list.category]:
    #         for other_contact in self.list[self.category]:
    #             if contact['name']==other_contact['name'] and contact['number']==other_contact['number']:
    #                 shared_contacts.append(contact)
    #     return shared_contacts

    def find_shared_contacts(self, other_list):
        self_set=set(contact['name'] for contact in self.contact_list[self.category])
        other_set=set(contact['name'] for contact in other_list.contact_list[other_list.category])
        shared_set=self_set.intersection(other_set)
        return [contact for contact in self.contact_list[self.category] if contact['name'] in shared_set ]
        


        # contacts_set = set(contact['name'] for contact in self.list[self.category])
        # other_set = set(contact['name'] for contact in other_list.list[other_list.category])
        # shared_set = contacts_set.intersection(other_set)
        # shared_contacts = [contact for contact in self.list[self.category] if contact['name'] in shared_set]
        # return shared_contacts
 
        # for our_contact in self.list[self.category]:
        #     for their_contact in new_list:
        #         if their_contact == our_contact:
        #             shared_contacts.append(our_contact)
        # return shared_contacts


my_friends_list = ContactList('My Friends', friends)
my_work_buddies = ContactList('Work Buddies', work_buddies)
print(my_friends_list.contact_list)
# my_friends_list.add_contact({'name': 'Dan', 'number': '123-123-1234'})
# print(my_friends_list.list)
# my_friends_list.remove_contact('Dan')
# print(my_friends_list.list)
friends_i_work_with = my_friends_list.find_shared_contacts(my_work_buddies)
print(friends_i_work_with)











