## Introduction to PowerShell
- Types of commands: native executables, cmdlets, functions, scripts, or aliases
- Cmdlets (compiles commands) follow a verb-noun syntax; helps programmers understand the command intention
- Using Get-Command will return thousands of commands, must filter to make response useful
  - Flags applied to either the noun or verb will accomplish this, using pattern matching for example
    - Flags expect a string value
  - Output of this looks like a table in the shell console, but is actually an object
- 


- Cmds:
  - Get-Verb: list of approved PowerShell verbs (with descriptions)
  - Get-Command: lists all available cmdlets in your system
    - Get-Command -Verb Get -Noun a-noun*
      - "-Noun" targets part of command thats a noun
      - "a-noun*" targets all commands whose Noun starts with "a-noun"
      - likewise the first part targets commands whose verb is "Get"
  - Get-Help: invoke built-in help system; can also use alias of "help"
  - Get-Member: response of a command is an object with many properties; use this command to drill down into object and get more details
