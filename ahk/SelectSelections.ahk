;
; AutoHotkey Version: 1.x
; Language:       English
; Platform:       Win9x/NT
; Author:         A.N.Other <myemail@nowhere.com>
;
; Script Function:
;	To read the Selections.txt file and set the value of ComboBox5 from the notepad++ preferences window
;   to the first line of Selections.txt and ComboBox7 to the second line
;

#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


FileReadLine, OutputVar, Selections.txt, 1
SendMessage,0x014D,-1,&OutputVar,ComboBox5,Preferences,,,

FileReadLine, OutputVar, Selections.txt, 2
SendMessage,0x014D,-1,&OutputVar,ComboBox7,Preferences,,,