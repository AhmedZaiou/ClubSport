# ClubSport
Bureau de suivie Royal Fitnes

openpyxl

styles : https://github.com/danielepantaleone/eddy/blob/master/resources/styles/QSpinBox.qss








 pyinstaller --onefile --windowed --name "RoyalFitnes" \
    --add-data "style/:style/" \
    --add-data "dataset/:dataset/" \
    --add-data "images/logos:images/logos" \
    --add-data "images/profiles:images/profiles" \
    --icon="images/logos/logoa.png" \
    main.py





npm install -g create-dmg



create-dmg dist/RoyalFitnes.app

open dist/RoyalFitnes.app





windows : 


pyinstaller --onefile --windowed --name "RoyalFitnes" ^
    --add-data "style\;style" ^
    --add-data "dataset\;dataset" ^
    --add-data "images\logos\;images\logos" ^
    --add-data "images\profiles\;images\profiles" ^
    --icon="images\logos\logoa.png" ^
    main.py



; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "SetupRoyalFitnes"
#define MyAppVersion "1.0"
#define MyAppPublisher "Mohamed ZAIOU"
#define MyAppURL "https://modeaest.com/"
#define MyAppExeName "RoyalFitnes.exe"
#define MyAppAssocName "My Program File"
#define MyAppAssocExt ".myp"
#define MyAppAssocKey StringChange(MyAppAssocName, " ", "") + MyAppAssocExt

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{3B6044D4-34E2-417B-955A-0B972565BCCA}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\My Program
; "ArchitecturesAllowed=x64compatible" specifies that Setup cannot run
; on anything but x64 and Windows 11 on Arm.
ArchitecturesAllowed=x64compatible
; "ArchitecturesInstallIn64BitMode=x64compatible" requests that the
; install be done in "64-bit mode" on x64 or Windows 11 on Arm,
; meaning it should use the native 64-bit Program Files directory and
; the 64-bit view of the registry.
ArchitecturesInstallIn64BitMode=x64compatible
ChangesAssociations=yes
DisableProgramGroupPage=yes
LicenseFile=C:\Users\mohamed zaiou\Document\projet\ClubSport\license.txt
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
OutputDir=C:\Users\mohamed zaiou\Document\projet
OutputBaseFilename=SetupRoyalFitnes 
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "french"; MessagesFile: "compiler:Languages\French.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\mohamed zaiou\Document\projet\ClubSport\dist\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\mohamed zaiou\Document\projet\ClubSport\style\*"; DestDir: "{app}\style"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\mohamed zaiou\Document\projet\ClubSport\dataset\*"; DestDir: "{app}\dataset"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\mohamed zaiou\Document\projet\ClubSport\images\logos\*"; DestDir: "{app}\images\logos"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\mohamed zaiou\Document\projet\ClubSport\images\profiles\*"; DestDir: "{app}\images\profiles"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\mohamed zaiou\Document\projet\ClubSport\dist\*"; DestDir: "{app}\dist"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Registry]
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocExt}\OpenWithProgids"; ValueType: string; ValueName: "{#MyAppAssocKey}"; ValueData: ""; Flags: uninsdeletevalue
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}"; ValueType: string; ValueName: ""; ValueData: "{#MyAppAssocName}"; Flags: uninsdeletekey
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\{#MyAppExeName},0"
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""
Root: HKA; Subkey: "Software\Classes\Applications\{#MyAppExeName}\SupportedTypes"; ValueType: string; ValueName: ".myp"; ValueData: ""

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent