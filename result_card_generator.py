# ==============================================================================
# TOOL 3: Student Result Card Generator for Coaching Centres
# Business Use-Case: Automates the process of calculating student percentages 
# and assigning grades based on scores in multiple subjects.
# Concepts Covered: Lists, for loop, if-elif-else, basic arithmetic.
# ==============================================================================

# Initialize two lists: one for names, one for marks (a list of lists)
student_names = []
# Each inner list will hold marks of 5 subjects for one student
marks_list = [] 
NUM_SUBJECTS = 5 # Total number of subjects (as per assignment description)
MAX_MARKS_PER_SUBJECT = 100 # Assuming 100 marks per subject for simplicity

# --- Data Input Phase using a while loop ---
print("--- Student Marks Entry (5 Subjects per Student) ---")
print("Enter details for 5-10 students. Type 'DONE' to stop entering students.")
student_count = 0

while True:
    student_name = input(f"\nEnter Name of Student #{student_count + 1} (or type 'DONE'): ")
    
    # Check for the exit condition
    if student_name.upper() == 'DONE' and student_count >= 5: # Enforce minimum 5 students
        break
    elif student_name.upper() == 'DONE' and student_count < 5:
        print(f"Please enter at least 5 students. Currently, you have {student_count}.")
        continue
    
    if student_count >= 10: # Stop after 10 students
        print("Maximum 10 students reached. Moving to results calculation.")
        break
        
    student_names.append(student_name)
    current_student_marks = []
    
    print(f"Entering marks for {student_name}:")
    for i in range(NUM_SUBJECTS):
        # Input validation for marks
        while True:
            try:
                mark = int(input(f"  Enter mark for Subject {i + 1} (out of {MAX_MARKS_PER_SUBJECT}): "))
                if 0 <= mark <= MAX_MARKS_PER_SUBJECT:
                    current_student_marks.append(mark)
                    break
                else:
                    print(f"Mark must be between 0 and {MAX_MARKS_PER_SUBJECT}.")
            except ValueError:
                print("Invalid input. Please enter a whole number.")
                
    marks_list.append(current_student_marks)
    student_count += 1
    
# --- Calculation and Output Phase using a for loop ---
print("\n" + "="*60)
print("                    STUDENT RESULT CARDS")
print("="*60)

# The for loop iterates through the list indices to process each student
for i in range(len(student_names)):
    name = student_names[i]
    marks = marks_list[i]
    
    # Calculate total marks for the 5 subjects
    total_marks = sum(marks) 
    # Calculate percentage (Maximum possible marks = 5 subjects * 100 = 500)
    percentage = (total_marks / (NUM_SUBJECTS * MAX_MARKS_PER_SUBJECT)) * 100
    
    # Use if-elif-else to assign Grade A/B/C/D/F
    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    else:
        grade = "F" # Failing Grade
        
    # Print the result card
    print("-" * 60)
    print(f"Name: {name}")
    print(f"Marks (Total): {total_marks}/{NUM_SUBJECTS * MAX_MARKS_PER_SUBJECT}")
    print(f"Marks (List): {marks}") # Useful for report
    print(f"Calculated Percentage: {percentage:.2f}%")
    print(f"Final Grade: **{grade}**")

print("="*60)