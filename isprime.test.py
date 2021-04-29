import sys

from isprime import isprime

right_answer = (False, True, True, False, True)
if tuple(map(isprime, (1,2,3,4,5))) == right_answer:
    sys.exit(0)
else:
    sys.exit(1)
