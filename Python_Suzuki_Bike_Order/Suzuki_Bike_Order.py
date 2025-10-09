### THIS PROGRAM WILL BOOK A SUZUKI BIKE IF ALL THE CONDITIONS ARE MET OTHERWISE IT WILL PRINT THE REASON WHY IT CANT BOOK THE BIKE ###

company = input('Enter Your Desired Company').title().strip() # It will take input and convert first letter to capital and remove any extra spaces

if company == 'Suzuki' : # it will check if company is suzuki or not . If yes so it will proceed Further if not so it will print company is not suzuki.
    engine_capacity = input('Enter Engine Capacity') # It will take input of engine capacity

    if engine_capacity == '150' : # It will check if engine capacity is 150 or not . If yes so it will proceed Further if not so it will print engine capacity is not 150
        year = int(input('Enter Year'))# It will take input of year and convert it to integer

        if year in (2023 , 2024 , 2025 ): # It will check if year is 2023 , 2024 , 2025 or not . If yes so it will proceed Further if not so it will print year is not 2023 , 2024 , 2025
            color = input('Enter Desired Color').title().strip() # It will take input of color and convert first letter to capital and remove any extra spaces

            if color == 'Black' : #It will check if color is black or not . If yes so it will print yes pack the bike if not so it will print dont want this color
                print('Yes Pack The Bike ') #It will print yes pack the bike

            else : # It will print dont want this color
                print ("Don't Want This Color")

        else : # It will print year is not 2023 , 2024 , 2025
            print(f'Year is not 2023 , 2024 , 2025 . You Entered  {year}')

    else : # It will print engine capacity is not 150
        print(f'Engine capacity is not 150. You Entered {engine_capacity}.')

else : # It will print company is not suzuki
    print('Company is not Suzuki')