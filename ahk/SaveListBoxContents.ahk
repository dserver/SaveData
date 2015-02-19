;
; AutoHotkey Version: 1.x
; Language:       English
; Platform:       Win9x/NT
; Author:         A.N.Other <myemail@nowhere.com>
;
; Script Function:
;	Save the contents of the listbox on the left hand side of the Preferences window in Notepad++
;   to a file

;   Before testing make sure that Notepad++ is open with the Preferences window open as well
;   and the Print menu selected

#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

FileDelete, ComboBox7Contents.txt
FileDelete, ComboBox5Contents.txt

ControlGet, OutputVar, List,,ComboBox7,Preferences,,
FileAppend, %OutputVar%,ComboBox7Contents.txt

ControlGet,OutputVar,List,,ComboBox5,Preferences,,
FileAppend,%OutputVar%,ComboBox5Contents.txt