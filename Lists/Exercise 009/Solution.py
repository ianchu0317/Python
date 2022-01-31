def copy_list(my_list):
  new_list = [element.capitalize() for element in my_list]
  return new_list

def main():
  my_list = ["Red", "Green", "BLUE", "Yellow", "Brown"]
  print("List is {0}".format(my_list))

  new_list = copy_list(my_list)
  print("New list is {0}".format(new_list))

if __name__ == '__main__':
  main()
