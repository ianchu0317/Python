
def check_word(my_list, number):
  new_list = list()
  for word in my_list:
    if len(word) >= number:
      new_list.append(word)
  return new_list


def main():
  my_list = input("Input sentence: ").split(" ")
  limit = int(input("Input word char limit: "))
  print("List is {0}".format(my_list))
  print("Words In list is {0}".format(check_word(my_list, limit)))

main()
