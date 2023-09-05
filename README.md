**Important concepts:** <br>
Clean function scopes:<br>
For modularity it is important that functions dont access variables outside their own scope. <br>
This means that every variable used in a function must be declared inside the function or through its arguments. <br>
A dependency on global variables makes it harder to copy code snippits between projects and it makes the code harder to read. <br>
In the same manner a function should not create global variables, <br>
and all information coming out of a function scope shoulde ideally through returns or yeild statements. <br>
For methods which belong to class object they can modifi the object outside their scope, but in the same manner are they part of the objects scope. <br>

**Native Python Packages** <br>
Must know  packages: <br>
typing <br>
os <br>
sys <br>
copy <br>

good to know packages: <br>
argparse <br>
re <br>
functools <br>
operator <br>
itertools <br>
dataclass <br>
