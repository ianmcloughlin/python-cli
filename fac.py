import sys
import myfunctions

# Get n from the command line.
n = int(sys.argv[1])
# Calculate the factorial of n.
ans = myfunctions.factorial(n)
# Print the answer.
print("The factorial of", n, "is:", ans)

