#   add_tags('i', 'Python') -> '<i>Python</i>'
#   add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'

def add_tags(tag, string):
    return "<{0}>".format(tag) + string + "</{0}>".format(tag)


if __name__ == '__main__':
    print(add_tags('i', 'Python'))
