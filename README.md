# AI Assignment 01 - Kids in the Yard

See assignment details on Canvas.
Answer the following questions:

Which tool(s) did you use?
Claude code

If you used an LLM, what was your prompt to the LLM?

Hi I am working on a project that requires an AI      
creates the project and implementation without        
looking at my code. I am going to share the           
assignment information with you. I want you to use    
python and code in intellij and name in ClaudePerson  
or ClaudeFamilyTree what ever makes sense for you.    
Please do not look at or touch my code. I am going to
share the files with you now. please comb through the    
instructions with a fine tooth comb and be sure to    
use the style guidelines.

Additional prompt because the last_name.csv was not correct
I updated the last names CSV file - this may have     
caused an issue with your code - please revisit and make
necessary changes to only your files. This will      
change things so you do need to update things

What differences are there between your implementation and the LLM?

The LLM has a main file which initially made me nervous because mine does not - 
however my program runs without it. I am not sure if it is a better practice
to have a main method, which I will ask during a code review 

The LLM has some really long comments on things that are obvious, unnecessarily 
crowding the code. They almost write a whole comment with pseudo code prior to
the real code making it hard to get through the file

It has some extra variables like "is_direct_descendant"

It calls @property for every getter and setter which I have never seen before 
The also initialize a few with "value"

There is a doc line comment for every getter and setter, which I had initially 
but I confirmed with the professor that they were unnecessary

It seems to have done more work when reading in files, It reads in the first line
while my code skips the first line and reads in the rest. It also seems to create
both a dictionary and array to store the information. I just set up a dictionary 
for each file and determined the appropriate key by examining what was in the 
other files and thinking about what we would need from the dictionary to continue
the code.

Some of the variables names are the same, but some are not 

It adds a catch in gender inc ase there is no decade 

The code they wrote is somewhat unclear at times and very crowded, when I look 
at my code it is pretty clear what it is doing without the need for over commenting 

It has unnecessary import statements at the top of the page 

it hard coded in the first two people in the tree, rather than calling on a 
person object to create them

It includes a check in partner to ensure the person is not their direct descendant
this is strange to me as we specify partners would need to be born with in 10
years (either way) of the person, so there really isn't a chance for their partner
to be a direct descendant 

Their family tree file is much bigger then mine because they did a lot of unnecessary
things like hard coding in the first two people, rather than utilizing the 
PersonFactory to make them, which is kinda the point. They have methods in the 
family tree that belong in the PersonFactory 

What changes would you make to your implementation in general based on suggestions from the
LLM?
For this assignment it's fine but I noted the claude code has some extra lines of
code in the event information is missing, like randomly selecting male or female 
for the gender if the decade is missing. I think that's a good practice 


What changes would you refuse to make?
Addition of too many unnecessary comments 

unnecessary lines of code. I understand why they are there, but they aren't specifically
needed here

Overall, I like my code much better, it is cleaner and clearer to understand.
Claude's code isn't organized well, includes a lot of unnecessary comments and code 
that make it almost impossible to look at. In my prompt, I specifically told it 
to follow pep8 and I don't think it did based on the comments alone.

While it is good to know how to use AI as a tool to help you learn and work more 
efficiently, it actually gives me some comfort to know that if I asked claude to 
do my whole assignment, I would be heavily graded down due to me not following the rules.
I would be embarrassed to turn in this code, there are way too many redundant methods
and it seems to be generally inefficient. This is why we need to have strong
foundations as coders because we need to know when AI does something silly so we
can fix it. 

