;
; AutoHotkey Version: 1.x
; Language:       English
; Platform:       Win9x/NT
; Author:         A.N.Other <myemail@nowhere.com>
;
; Script Function:
;   Takes in one command line parameter that is the string of the folder to select
;   to save in. This will be something like "V3011". 

#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

IfWinExist, DataPage
{
	WinActivate
	WinWaitActive, DataPage
	IfWinActive, DataPage
	{
		WinMenuSelectItem, DataPage,,File, Save to File, Save Current Report
	}
}

Sleep, 60

IfWinExist, Save As
{
	WinActivate
	WinWaitActive, Save As
	IfWinActive, Save As
	{
		SaveFolder := "V3075"
		;SaveFolder := %1% ; SaveFolder contains the string name of the folder to save in
		; Call LB_SELECTSTRING
		SendMessage, 396,-1, &SaveFolder, ListBox2 , Save As
		ItemIndex := ErrorLevel

		if (%ItemIndex% == -1){
			return
		}
		VarSetCapacity(Rect, 16) ; rect structure is held in Rect variable

		; Get ListBox2's position relative to the Save As windo
		ControlGetPos, X_LB, Y_LB, ListBox2, "Save As"
		; Call LB_GETITEMRECT
		SendMessage, 408, %ItemIndex%, &Rect, ListBox2, Save As
		x_upper_left := NumGet(Rect,0,true)
		y_upper_left := NumGet(Rect,4,true)
		x_lower_right := NumGet(Rect,8,true)
		y_lower_right := NumGet(Rect,12,true)

		; Calculate point to click
		x_mid := x_lower_right - x_upper_left + %X_LB%
		y_mid := y_lower_right - y_upper_left + %Y_LB%

		MouseMove, x_mid, y_mid
		;Click 2


	}
}


