par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}
#your code go here:

def count_letters(text):
    
      text = text.lower().replace(" ", "")
     
      
      for letter in text:
     
        if letter not in counts:
          counts[letter] = 1

        else:
          counts[letter] += 1
      return counts
      
print(count_letters(par))
