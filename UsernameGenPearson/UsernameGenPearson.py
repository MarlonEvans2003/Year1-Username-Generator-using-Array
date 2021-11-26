rows, cols = (4, 5) 
array = [[0 for i in range(cols)] for j in range(rows)]

array[0][0] = ' '
array[0][1] = 'Jones'
array[0][2] = 'Helen'
array[0][3] = '2001'
array[0][4] = '06'

array[1][0] = ' '
array[1][1] = 'Rees'
array[1][2] = 'Ceryl'
array[1][3] = '1990'
array[1][4] = '10'

array[2][0] = ' '
array[2][1] = 'Phillips'
array[2][2] = 'Ann'
array[2][3] = '2002'
array[2][4] = '01'

array[3][0] = ' '
array[3][1] = 'Leech'
array[3][2] = 'Fred'
array[3][3] = '2005'
array[3][4] = '05'

for row in array: 
    print(row ) 


for i in range(0,rows): #read each row in table/array 
  Surname = array[i][1]
  
  
  S_part = Surname[:2]

  
  Forename = array[i][2]

  
  F_part = Forename[:1]

  BirthYear = array[i][3]


  BY_part = BirthYear[2:4]

  BirthMonth = array[i][4]


  BM_part = BirthMonth[1]
  
  #now populate userid
  array[i][0] = S_part + F_part + BY_part + BM_part
  print("")
  print("")

  for row in array: 
    print(row )  