'''
NAME:HARIHARAN P
DATE:31/05/2022
'''
import csv

def write_into_file(info_list):
    with open('student_info.csv','a',newline='') as csv_file:
        write_obj=csv.writer(csv_file,info_list)

        if csv_file.tell()==0:
            write_obj.writerow(["Name","Age","Contact Number","E-Mail ID"])

        write_obj.writerow(info_list)
            
if __name__ == '__main__':
    condition = True
    student_num =1

    while(condition):
        student_info = input("Enter student information for student #{} in the following format(Name Age Contact_Number E-Mail_ID):".format(student_num))

        student_info_list = student_info.split(' ')
        print("\n The entered information is -\nName:{}\nAge:{}\nContact_number:{}\nE-mail_ID:{}"
        .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))

        choice_flag=input("Is the entered information correct? (yes/no):")

        if choice_flag=="yes":
            write_into_file(student_info_list)

            condition_check=input ("Enter (yes/no) if you want to enter info for next student:")
            if condition_check=="yes":
                condition = True
                student_num=student_num+1
            elif condition_check=="no":
                condition=False

        elif choice_flag=="no":
            print("\n Please re-enter the values!")            
