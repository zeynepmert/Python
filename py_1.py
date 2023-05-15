#my first application of python

#e.x Calculation of school achievement degree

# We asked the user for behavioral score, grade point average and weekly total course hours.
# We made a str to int conversion to perform mathematical operations in the function.
behavior_score    = int(input('Please enter your behavior score : '))
grade_average     = int(input('Please enter your grade average : '))
total_class_hours = int(input('please enter your weekly total class hours : '))

upper_boundary = 760
lower_boundary = 450

# We calculated the user's success score with this function.
def success_calculation( behavior_score, grade_average, total_class_hours):
    return( behavior_score*grade_average) + total_class_hours

#We compared the calculated success score of the user with the limits we determined.
if success_calculation(behavior_score, grade_average, total_class_hours) > upper_boundary:
    print("Congratulations! Your success grade is: " + str(success_calculation(behavior_score, grade_average, total_class_hours)) + '. So, you have a great degree of achievement.')
    
elif lower_boundary < success_calculation(behavior_score, grade_average, total_class_hours) < upper_boundary:
    print('Your success grade is: ' + str(success_calculation(behavior_score, grade_average, total_class_hours)) + '. You have an intermediate level of achievement.')

else:
    print('Your success grade is: ' + str(success_calculation(behavior_score, grade_average, total_class_hours)) + '. You have a low achievement score. So you can contact the guidance service for support.')


# =============================================================================
# type(behavior_score)
# type(grade_average)
# type(total_class_hours)
# 
# =============================================================================




