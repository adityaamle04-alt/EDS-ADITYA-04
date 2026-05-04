n = int(input())

marks = list(map(int, input().split()))


if any(m < 40 for m in marks):
    print("Fail")
else:
    total_marks = sum(marks)
    aggregate = total_marks / n
    
  
    if aggregate > 75:
        grade = "Grade: Distinction"
    elif aggregate >= 60:
        grade = "Grade: First Division"
    elif aggregate >= 50:
        grade = "Grade: Second Division"
    elif aggregate >= 40:
        grade = "Grade: Third Division"
    
    print(f"Aggregate Percentage: {aggregate:.2f}")
    print(grade)
