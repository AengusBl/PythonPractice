answer = 40
user_input = input("What number am I thinking of?")
print(f"   {user_input}!")
if user_input == answer:
  print("Amazing!")
else:
  print("Better luck next time!")
  new_try = input("Here, have another try:")
  print(f"   {new_try}!")
  if abs(answer-new_try) > abs(answer-user_input):
    print("Getting colder!")
  else:
    print("Getting warmer!")
