#Break and continue 
 # Break : used to terminate the loop when encountered

  # Continue : terminates excuetion in the current iteration and contiues execution of the loop with the next iteration.

i = 1
while i <= 5:
    print(i)
    if(i == 3) : 
      break
    i += 1
print ("end of loop")    