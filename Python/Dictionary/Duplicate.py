dict_student = {'id1':
                {'Name': ['Tom'],
                 'Class': [11],
                  'subjects': ['English','Math','Computers'] },
                'id2':
                {'Name': ['Harry'],
                 'Class': [12],
                  'subjects': ['English','Math','Computers'] },
                'id3':
                {'Name': ['Tom'],
                 'Class': [11],
                  'subjects': ['English','Math','Computers'] }
}

new_dict = {}
for key, value in dict_student.items():
    if value not in new_dict.values():
        new_dict[key]= value

print(new_dict)


                  
                   
                    
                  
