#In this code, you will learn how to remove special characters.

#1 == make the function

      def remove_special_char(txt):
      
#2 == define the special characters

      special = set("!@#$%^&\'*().[]{}<>+=~,`|?")
      
#3 == define the output

      output = ' '
      
#4 == make the for loop
      
       for char in txt:
            if char not in special:
                  output += char
 
 #5 == return the output
 
      return output
 
 #6 == You are done!!!




# HERE IS THE SAMPLE CODE FOR THE TASK
def remove_special_characters(txt):
  special = set("!@#$%^&\'*().[]{}<>+=~,`|?")
  output = ''
  for char in txt:
    if char not in special:
      output += char
  return output
