Important concepts:
Clean function scopes:
For modularity it is important that functions dont access variables outside their own scope. 
This means that every variable used in a function must be declared inside the function or through its arguments.
A dependency on global variables makes it harder to copy code snippits between projects and it makes the code harder to read
In the same manner a function should not create global variables, 
and all information coming out of a function scope shoulde ideally through returns or yeild statements.
For methods which belong to class object they can modifi the object outside their scope, but in the same manner are they part of the objects scope.

