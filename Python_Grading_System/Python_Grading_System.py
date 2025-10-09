marks = float(input('Enter Your Marks : '))       # Take The User Input From User And Convert It Into Float.


if marks > 100 or marks < 0:       # It will print invalid marks if the marks are above 100 or below 0.
    result = f'inavalid marks {marks}'

elif 80 <= marks <=100 :       # It will print A1 if the marks are between 80 and 100.
    result = 'A1'

elif 70 <= marks <80 :       # It will print A if the marks are between 70 and 80.
    result = 'A'    

elif 60 <= marks <70 :       # It will print B if the marks are between 60 and 70.
    result = 'B'

elif 50 <= marks <60 :       # It will print C if the marks are between 50 and 60.
    result = 'C'

elif 40 <= marks <50 :       # It will print D if the marks are between 40 and 50.
    result = 'D'

else :       # It will print Better Luck Next Time if the marks are below 40.
    result = 'Better Luck Next Time'

print(result)