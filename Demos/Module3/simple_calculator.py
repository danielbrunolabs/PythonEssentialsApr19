import math

print("Simple Calculator")
print('------------------------')
print('Enter "quit" to leave the program')

while(1) :
  op = input('Provide operation (add,sub,mul,div,circ): ')
  
  if(op.lower() == 'quit'):
      break
  elif(op in ('add','sub','mul','div','circ')):
      data1 = input('Provide first value: ')
      if(data1.isnumeric() != True):
        print("Please provide a numeric value")
        continue
      data2 = input('Provide second value: ')
      if(data1.isnumeric() != True):
        print("Please provide a numeric value")
        continue
    
      try:
        d1 = float(data1)
      except:
        d1 = 0.0
        print("Data1 did not convert well") 
      try: 
        d2 = float(data2)
      except:
        d2 = 0.0
        print("Data2 did not convert well") 

      if(op == 'add'):
          result = d1 + d2
      elif(op == 'sub'):
          result = d1 - d2
      elif(op == 'mul'):
          result = d1 * d2
      elif(op == 'div'):
          try:
              result = d1/d2
          except ZeroDivisionError:
              result = 0
              print("Error: Can not divide by 0!")
          except ZeroDivisionError:
              result = 0
              print("Something worse happened with division")
      elif(op == 'circ'):
          result = math.pi * 2 * d1
      else:
           print ('Please provide valid operation')
      print(f'The result of {data1} {op} {data2} is {round(result,2)}')     

  else :
      print ('Please provide valid operation')  