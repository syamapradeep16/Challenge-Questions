#Calculate the grade of a student with given marks in 5 subjects

sub1 = 92
sub2 = 73
sub3 = 95
sub4 = 81
sub5 = 88
Total_Marks = 500
Marks_Scored = sub1 + sub2 + sub3 + sub4 + sub5
Percentage = (Marks_Scored * 100) / Total_Marks

print ('Total Marks = 500')
print ('Percentage =', Percentage)
if Percentage >= 90:
    print ('Grade = A+')
elif Percentage <= 89 and Percentage >= 80:
    print ('Grade = A')
elif Percentage <= 79 and Percentage >= 70:
    print ('Grade = B')
elif Percentage <= 69 and Percentage >= 60:
    print ('Grade = C')
elif Percentage <= 59 and Percentage >= 50:
    print ('Grade = D')
else:
    print ('Grade = F')