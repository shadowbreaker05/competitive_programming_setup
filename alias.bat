@echo off
::Turn off echo to prevent the contents of this file from getting printed in the CMD

::For Windows users
::Create a new String Value with name "AutoRun" in Regedit in "Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Command Processor"
::For Windows 10 users
::Create a new String Value with name "AutoRun" in Regedit in "Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Command Processor"
::Give the full path of the Alias.cmd or Alias.bat file as the data for the String Value

DOSKEY ls = dir /B
DOSKEY clear = cls
DOSKEY gedit = notepad $*
::$* allows us to give arguments after the command. For eg. notepad helloworld.txt
DOSKEY ifconfig = ipconfig
DOSKEY python = python3 $*
DOSKEY sublime = sublime_text $*
DOSKEY alias = notepad C:\Windows\thsmartkid\hello.bat
::Allows us to add new entries into the alias file for CMD
DOSKEY ~ = cd "%USERPROFILE%\$*"
::Direct access to the Home/CurrentUser Directory
