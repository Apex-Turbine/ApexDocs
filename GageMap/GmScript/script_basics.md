# Lua Basics

Lua is a very simple programming language, but it differs in some ways from the previous batch system. For example, It is much further away from a C/C++ syntax. This section will cover many of the basic features of the language.

## Comments

Comments are done using two dashes for a single line comment, and matching --[[ and --]] for block comments.

> `number = 3 -- End of line comment`
>
> `-- regular line comment`
>
> `--[[ this`
>
> > `is`
> >
> > `a`
> >
> > `block comment`
>
> `]]--`

> [!NOTE]
> Lua has no restrictions on tabbing. Lines end by carriage return, so there is no requirement for semicolons unless two statements are located on the same line.

## Variables

As shown on the first line of the example above, variables are easy to define. There is no type specifier. Simply supply the desired, unique name of a variable and what it is equal to. When there is nothing stored in a variable, it is a 'nil' value. Variables may be initialized to nil if they are simply being declared.

## Includes

Other scripts may be included from the main script. This allows external tools to be brought in for use in multiple scripts. The syntax for this is simple:

> `require 'tools' -- Where 'tools.lua' is a file that the script is able to find.`

## Functions

Functions are defined using the function identifier and closed using end. For example:

> `function add(value1, value2)`
>
> > `return value1 + value2`
>
> `end`

Any number of parameters may be placed between the parenthesis of a function name, and any data can be passed to those parameters from a calling function. It is up to the programmer not to pass a data type that is compatible with the operation done by the function.

The return keyword allows any value to come back from the function and is optional. Given the above example, x = add(1,1) would now result in 'x' representing the number 2.

> [!NOTE]
> Only one function, main()(no arguments) is required by the scripting engine. Any number of additional functions may be added freely. main() is the function that will be executed by GmScript itself.

## Conditionals

Conditional statements in LUA are done without a main parenthesis, but employ many of the standard equality operators: ==, >=, <=, > and < . Inequalities use a tilde(~), such as ~=, ~< and ~>. The keywords or and and are used to conjoin conditional statements. For example:

> `if (i >= 0) or (i == -100) then`
>
> > `i = i * 10`
>
> `end`

The example above makes use of parenthesis to keep the order of operations obvious and readable. Note the syntax of the if statement. A then is required to start a block of code, concluded by end like a function definition.

> [!NOTE]
> Also shown in the previous example is that basic mathematics like *, /, + and - work as expected. There are many other mathematic capabilities in Lua which can be found online.

## Loops

Loops employ conditional statements to carry out the same logic multiple times until some goal is met. The basic kinds of loops are for and while.

**For Loops** typically work by iterating a specific number of times while incrementing a counter. The Lua syntax is "for <variable>=<value>,<target value> do".

> `-- Print the numbers 1 to 10 to the terminal`
>
> `for i=1,10 do`
>
> > `print(i)`
>
> `end`

**While Loops** will keep running until something ceases to be true. The Lua syntax is "while <condition> do".

> `-- Print the numbers 1 to 10 to the terminal using a while loop`
>
> `i = 1`
>
> `while i <= 10 do`
>
> > `print(i)`
>
> `i = i + 1`
>
> `end`

> [!NOTE]
> Once again we see that any time a block is started by 'then' or 'do', it is concluded by 'end' after all handling is performed. This is consistent among functions, conditionals and loops.
