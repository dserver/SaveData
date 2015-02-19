;
; AutoHotkey Version: 1.x
; Language:       English
; Platform:       Win9x/NT
; Author:         A.N.Other <myemail@nowhere.com>
;
; Script Function:
;	Template script (you can customize this template by editing "ShellNew\Template.ahk" in your Windows folder)
;

#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

IfWinExist, DataPage
{
	WinActivate
	WinWaitActive, DataPage
	IfWinActive, DataPage
	{
		WinMaximize
		Sleep 50
		
		; Click spreadsheet report button
		MouseMove, 229, 63 
		Click
		
		; Save Parts combobox into Parts.txt
		ControlGet, OutputVar, List,,ComboBox1
		FileAppend, %OutputVar%,Parts.txt

		; Save Transactions listbox into Transactions.txt
		ControlGet, OutputVar, List,,ListBox3
		FileAppend, %OutputVar%,Transactions.txt

	}
}

