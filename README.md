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
