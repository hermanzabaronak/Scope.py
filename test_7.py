#try/except
try:
  print(a)
except NameError:
  print("Variable a is not defined")
except:
  print("Something else went wrong")

#finally
try:
  print(b)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")