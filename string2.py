# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
    if len(s)>= 3:
        if s[-3:]!='ing' :
            s= s+'ing'
        elif s[-3:]=='ing':
            s= s +'ly'

    return s

# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
    s1=s.find('not')
    s2=s.find('bad')
    length = len('bad') 
    if s1 < s2:
      s=s.replace(s[s1:(s2+length)],'good');
    return s

# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
  l_a= len(a)
  l_b= len(b)

  if l_a%2 == 0:
      f_a= a[0:(l_a//2)]
      b_a= a[((l_a//2)):]
  if l_a%2 != 0:
      f_a= a[0:(l_a//2)+1]
      b_a= a[(l_a//2)+1:]
  if l_b%2 == 0:
      f_b= b[0:(l_b//2)]
      b_b= b[(l_b//2):]
  if l_b%2 != 0:
      f_b= b[0:(l_b//2)+1]
      b_b= b[(l_b//2)+1:]
  s= f_a + f_b + b_a + b_b
  
  return s


def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

def main():
  print('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')
  print()

  print('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  
  print()
  print('front_back')
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
