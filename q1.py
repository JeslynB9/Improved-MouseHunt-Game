'''
We will use the art by Joan Stark as the logo:
           _____()()
          /      @@
    `~~~~~\_;m__m._>o

Answer for Question 1 - Game Title

Name: 
SID: 
unikey: 

'''

title = 'Mousehunt'

logo = '''
       ____()()
      /      @@
`~~~~~\_;m__m._>o
'''

author = 'An INFO1110/COMP9001 Student'

credits = f'''
Inspired by Mousehunt© Hitgrab
Programmer - {author}
Mice art - Joan Stark'''

splash = title + '\n' + logo + credits


def main():
    print(splash)


if __name__ == '__main__': 
    main()