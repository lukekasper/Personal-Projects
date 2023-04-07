## Introduction to PowerShell
- Types of commands: native executables, cmdlets, functions, scripts, or aliases
- Cmdlets (compiles commands) follow a verb-noun syntax; helps programmers understand the command intention
- Using Get-Command will return thousands of commands, must filter to make response useful
  - Flags applied to either the noun or verb will accomplish this, using pattern matching for example
    - Flags expect a string value
  - Output of this looks like a table in the shell console, but is actually an object
  

## Discover Commands in PowerShell
- The help cmdlet returns a page with multiple sections:
  - NAME: Provides the name of the command
  - SYNTAX: Shows ways to call the command by using a combination of flags, and sometimes, allowed parameters
  - ALIASES: Lists any aliases for a command. An alias is a different name for a command, and it can be used to invoke the command
  - REMARKS: Provides information about what commands to run to get more help for this command
  - PARAMETERS: Provides details about the parameter. It lists its type, a longer description, and acceptable values, if applicable
- Some flags to reduce the number of pages reutrned from the help cmdlet
  - Full: Returns a detailed help page. It specifies information like parameters, inputs, and outputs that you don't get in the standard response
  - Detailed: Returns a response that looks like the standard response, but it includes a section for parameters
  - Examples: Returns only examples, if any exist
  - Online: Opens a web page for your command
  - Parameter: Requires a parameter name as an argument. It lists a specific parameter's properties
- "help" alias pipes Get-Help into a funtcion which makes response readable line-by-line and page-by-page
  - view results line-by-line with arrow key and page-by-page with space bar
- Get-Member: is piped on top of another command to filter output (know more about what is returned and how you can alter it)
  - when you know the tpye of returned object, you can search for other commands that operate on this
  - response is verbose, meaning it returns many columns
  - use Select-Object to filter on what columns to return
    - use either a comma-seperated list of columns or "*" to display all

## Connecting Commands into a Pipeline
- Creating a pipeline requires the output of one cmdlet to match the required input to the next cmdlet
  - must have parameters with property "Accept Pipeline Input?" set to "True"
  - input can be considered valid:
    - By Value: input matches an array to a specific type
    - By Property Name: object that is passed in must have a property with a specific name
- To format output of cmdlet, use Get-Member to get the real property names for a process in order to use Select-Object to filter
- Use Sort-Object in a pipeline to sort by default properties first, or provide property names to sort by specific column names
- Filtering left: filter results as early as possible (make data processing as efficient as possible)
- Formatting right: format is the last thing you do; formatting changes the oject you are dealing with, making Select-Object calls invalid
  - most common formatting calls are Format-Table or Format-List


## Cmdlets:
- Get-Verb: list of approved PowerShell verbs (with descriptions)
- Get-Command: lists all available cmdlets in your system
  - Get-Command -Verb Get -Noun a-noun*
    - "-Noun" targets part of command thats a noun
    - "a-noun*" targets all commands whose Noun starts with "a-noun"
    - likewise the first part targets commands whose verb is "Get"
- Get-Help: invoke built-in help system; can also use alias of "help"
- Get-Member: response of a command is an object with many properties; use this command to drill down into object and get more details
- Get-Help -Name Get-Help: invoke "Get-Help" and then specify the name of the cmdlet after "-Name" (in this case the Get-Help cmdlet)
- Get-Help Get-FileHash -Examples: only return examples of the cmdlet
  - Get-FileHash returns the hashing function output for a file using the specified hashing algorithm
  - Hashing functions produce an output based on the content of the file, they help ensure file contents have not been altered
- Get-Process -Name 'name-of-process' | Get-Member:
  - Result of Get-Process is passed as an input to Get-Member by using pipe "|"
  - This returns the Name, MemberType, and Definition columns, along with the type of returned object
  - Get-Process returns a list of processes running on your machine
- Get-Command -ParameterType Process: to search cmdlets that use the type "Process"
  - use if returned object type is "TypeName: System.Diagnostics.Process" for example
- Get-Process -Name 'name-of-process' | Get-Member | Select-Object Name, MemberType
  - specifies you only want the Name and MemberType columns returned
  - can add -MemberType Method flag to specify you only want to return MemberTypes that are a method
- Get-Process zsh | Format-List -Property \*: get full list of properties for zsh process and return in a Format-List
- Get-Process zsh | Get-Member -Name C*: return the real property names for zsh processes that start with "C"
- Get-Process | Sort-Object -Descending -Property Name, CPU: sort proceses in descending order by Name and then CPU 
- Get-Process | Where-Object CPU -gt 2 | Sort-Object CPU -Descending | Select-Object -First 3
  - returns first 3 processes (-First 3), where CPU value > 2 (-gt 2), in descending order
- Get-Process | Select-Object Name | Where-Object Name -eq 'name-of-process' vs Get-Process | Where-Object Name -eq 'name-of-process' | Select-Object Name
  - filter processes by name prior in the pipeline to selecting object columns to improve efficiency
  - Get-Process -Name 'name-of-process' | Select-Object Name: more efficient version of prior statement, -Name does filtering for you
- "a string" | Get-Member | Format-List: overrides default formatting to return list
