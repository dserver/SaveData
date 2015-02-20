;
; AutoHotkey Version: 1.x
; Language:       English
; Platform:       Win9x/NT
; Author:         A.N.Other <myemail@nowhere.com>
;
; Script Function:
;   Takes in one command line parameter that is the string of the folder to select to save in
;	Assumes the "Save Current Report" window is visible and will select the correct folder to save in.
;   This will be C:\DataPage\Vxxx. The item needs to be selected
;	and double clicked in order to save inside the folder. To do this follow these steps:
;		1. Call LB_SELSTRING. The function will select the string it is passed and scroll to make it visible.
;			It will also return the index of the selected item, which will be used next.
;		2. Call LB_GETITEMRECT. The function takes the index from above and a pointer to a RECT
;			structure. The RECT structure will contain the LONG integers for each of these values:
				;1. left = x-coordinate of upper-left corner of the item
				;2. top = y-coordinate of upper-left corner of the item
				;3. right = x-coordinate of lower-right corner of the item
				;4. bottom = y-coordinate of the lower-right corner of the item
			; ** See http://www.autohotkey.com/docs/commands/DllCall.htm#types
			;    	 http://www.autohotkey.com/docs/commands/DllCall.htm#ExStruct
			;    General doc in first link, Example with RECT structure in second link
;		3. Call ahk MouseMove on the midpoint of the rectangle of the item
;		4. Call ahk Click 2 to double click the mouse

#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

;SaveFolder := %1% ; SaveFolder contains the string name of the folder to save in
SaveFolder := "c:\DATAPAGE\Dim'l  Shortcuts"
; Call LB_SELSTRING
SendMessage, 396,-1, &SaveFolder, ListBox2 , "Save As" 
ItemIndex := ErrorLevel

VarSetCapacity(Rect, 16) ; rect structure is held in Rect variable

; Call LB_GETITEMRECT
SendMessage, 408, %ItemIndex%, &Rect, ListBox2, "Save As"
x_upper_left := NumGet(Rect,0,true)
y_upper_left := NumGet(Rect,4,true)
x_lower_right := NumGet(Rect,8,true)
y_lower_right := NumGet(Rect,12,true)

; Calculate point to click
x_mid := x_lower_right - x_upper_left
y_mid := y_lower_right - y_upper_left

MouseMove, x_mid, y_mid
Click 2


