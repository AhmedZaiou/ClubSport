# ClubSport
Bureau de suivie Royal Fitnes

openpyxl

styles : https://github.com/danielepantaleone/eddy/blob/master/resources/styles/QSpinBox.qss








 pyinstaller --onefile --windowed --name "ClubSport" \
    --add-data "style/:style/" \
    --add-data "dataset/:dataset/" \
    --add-data "images/logos:images/logos" \
    --add-data "images/profiles:images/profiles" \
    main.py




open dist/ClubSport.app


npm install -g create-dmg



create-dmg dist/MonApplication.app
