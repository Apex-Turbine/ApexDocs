# Getting Started

## Creating a Script File

A script file may have any name, but the standard is to use the .lua format. Scripts are plain text and may be edited in the any program of choice. There are many tools that will color-code the text according to Lua syntax, but this is not required.

In order for GageMap to call a script, it must define a main function. A basic script file looks like this:

> `def main()`
>
> > `print("Hello World!")`
>
> `end`

Custom functions may be defined outside of main and called freely. Returning from anywhere in main (thus exiting the script) is done using the following syntax:

> `def main()`
>
> > `do return end`
> >
> > `print("Hello World!")`
>
> `end`

Nothing in this example is printed. "return" by itself can unfortunately not be called if it does not precede and "end", so use this syntax in cases where the script needs to exit abruptly.

## Developing the Script

Anything within main() will be executed in a step by step order by GageMap. Only when executed by GmScript (as opposed to a separate Lua runtime) does the script have access to GageMap functionality. To use these functionalities, refer to [Function Groups for Scripting](script_funcGroups.md).

For a better look at the features that are built into Lua apart from GageMap, refer to this guide on [Lua Basics](script_basics.md).
