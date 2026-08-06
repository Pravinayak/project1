std_marks={ 
    "pravi":91,
    "manasa":98,
    "jaan":89,
    "hari":79,
    "kumari":69
}
print(std_marks)
std_grades={}

for students in std_marks:
    grades=std_marks[students]
    if grades>90:
        std_grades[students]="A+"
    elif grades>80:
        std_grades[students]="b+" 
    elif grades>70:
        std_grades[students]="C+" 
    elif grades>60:
        std_grades[students]="D+"  
    elif grades<40:
        std_grades[students]="F"   
print(std_grades)         
      
       
       
