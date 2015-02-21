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

IfWinExist, Preferences
{
	WinActivate
	WinWaitActive, Preferences
	IfWinActive, Preferences
	{
		; get preferences windo position and listbox control position
		WinGetPos, X_PREF, Y_PREF, W_PREF, H_PREF, Preferences
		ControlGetPos, X_CTRL, Y_CTRL, W_CTRL, H_CTRL, ListBox1, Preferences
		
		SP = " "
		; get position of "Tab Settings" from the listbox
		SaveFolder := "Tab Settings"
		; Call LB_SELECTSTRING
		SendMessage, 396,-1, &SaveFolder, ListBox1 , Preferences
		ItemIndex := ErrorLevel
		
		VarSetCapacity(Rect, 16)
		SendMessage, 408, %ItemIndex%, &Rect, ListBox1, Preferences
		x_upper_left := NumGet(Rect,0,true)
		y_upper_left := NumGet(Rect,4,true)
		x_lower_right := NumGet(Rect,8,true)
		y_lower_right := NumGet(Rect,12,true)
		
		FileAppend, "X_PREF | Y_PREF | W_PREF | H_PREF | X_CTRL | Y_CTRL | W_CTRL | H_CTRL | x_upper_left | y_upper_left | x_lower_right | y_lower_right ", PrefTest.txt
		FileAppend, %X_PREF%%SP%%Y_PREF%%SP%%W_PREF%%SP%%H_PREF%%SP%%X_CTRL%%SP%%Y_CTRL%%SP%%W_CTRL%%SP%%H_CTRL%%SP%%x_upper_left%%SP%%y_upper_left%%SP%%x_lower_right%%SP%%y_lower_right%, PrefTest.txt
	}
}

