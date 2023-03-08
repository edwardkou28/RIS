@echo on
set hh=%time:~-11,2%
set /a hh=%hh%+100
set hh=%hh:~1%
Set mydir=%date:~10,4%-%date:~4,2%-%date:~7,2%-%hh%-%time:~3,2%-%time:~6,2%
copy C:\PROJECT\RIS\RIS\RIS.xlsx \\pluto02\RnD\Hardware\RIS\Data\RIS_%mydir%.xlsx

attrib +r \\pluto02\RnD\Hardware\RIS\Data\RIS_%mydir%.xlsx

forFiles /p "\\pluto02\RnD\Hardware\RIS\Data\RIS_%mydir%.xlsx" /s /d -7 /c "cmd /c del /q @RIS_%mydir%.xlsx"


::start excel /r "\\pluto02\RnD\Hardware\RIS\Temp\RIS.xlsx"