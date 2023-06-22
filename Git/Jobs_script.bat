@echo off
REM Run FQDAT Test Cases
color a2
title "FQDAT_TEST_CASE_RUNNER"

REM SET IGOR PATHS HERE *****************************************************************
set IGOR_EXE="C:\Program Files\WaveMetrics\Igor Pro 8 Folder\IgorBinaries_x64\Igor64.exe"

REM GET THE USER TO SET THE BUILD DIR ***************************************************
for /F "usebackq tokens=1,2 delims=:" %%A IN (`id -un`) DO (
    SET "current_user=%%A"
)
set BUILD_DIR=C:\Users\%current_user%\Desktop\builds

REM GET THE RUNNER NAME TO SET THE FQDAT DIR ********************************************
for /F %%A in ('dir /B /AD "%BUILD_DIR%"') do set "runner_name=%%A"
set FQDAT_DIR=%BUILD_DIR%\%runner_name%\0\PHL-FQ\v22_flight_test\FQDAT
set IGOR_PXP=%FQDAT_DIR:"=%\FQDAT_ReleasedCleanVersion.pxp

REM SET TEST CASE PATHS *****************************************************************
set TEST_CASES=%FQDAT_DIR:"=%\\test
set test1=%TEST_CASES:"=%\data\fdcm\DTS
set test2=%TEST_CASES:"=%\data\fdcm\GTR
set test3=%TEST_CASES:"=%\data\IADS
set test4=%TEST_CASES:"=%\data\RVLS\AMC
set test5=%TEST_CASES:"=%\data\RVLS\IAP
set test6=%TEST_CASES:"=%\data\shipboard

REM CHECK IGOR PATHWAYS *****************************************************************
if NOT exist "%FQDAT_DIR%" (
echo "FQDAT folder could not be found.  Save modified files and pull this branch's last stable commit from the repository."
exit 1
)
if NOT exist "%IGOR_PXP%" (
echo "FQDAT pxp could not be found.  Save modified files and pull this branch's last stable commit from the repository."
exit 1
)
if NOT exist "%TEST_CASES%" (
echo "FQDAT test cases could not be found.  Save modified files and pull this branch's last stable commit from the repository."
exit 1
)

REM START FQDAT AND GENERATE PLOTS ******************************************************
START "" %IGOR_EXE% /I %IGOR_PXP%
ping 127.0.0.1 -n 31 > nul

%IGOR_EXE% /X PlotTestCasesFromScript("%current_user%;%runner_name%;%test1%;%test2%;%test3%;%test4%;%test5%;%test6%")

REM KILL TASK IF STILL RUNNING AFTER 3 MIN (ERROR OCCURED TO STOP PROCEDURE)*************
ping 127.0.0.1 -n 180 > nul
tasklist | findstr "Igor64.exe" > nul
if not errorlevel 1 (
taskkill /f /im Igor64.exe
echo Task killed.  Macro error in FQDAT procedure.
exit 1
)

REM Display Error Log *******************************************************************
set ERROR_LOG=%TEST_CASES:"=%\output\ErrorLog.txt
set size=0
for /f %%i in ("%ERROR_LOG%") do set size=%%~zi
if %size% gtr 0 (
type %ERROR_LOG%
exit 1
)

echo Plots completed Successfully!
exit 0
