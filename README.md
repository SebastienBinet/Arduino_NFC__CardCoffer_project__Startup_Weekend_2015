# CardCoffer-Startup-Weekend
Code that I have created during the Montreal 2015 march startup weekend to read and write NFC cards

During the startup weekend, I joined a team that wanted to create a startup aroud NFC business card (replacing paper business cards by one NFC business card and the associated app).

I learned:
    - Arduino IDE
    - Arduino Libraries
    - NFC types (Near Field Communication)
    - NFC format
    - NFC protections
    - Adafruit NFC libraries
    - Python
    - pySerial
    - git CLI
    - chrome app packaging

------------------------------------------------------------------------------------------------------------
---- Here are the steps that I have past through during the weekend: ---------------------------------------

- I have worked with Adafruit-PN532 NFC card that Alireza Saberi have brought.

- My first time with Arduino, so I had to install the arduino IDE and figure out (with help from Ali) its philosophy (tabs that can only be created empty, all code in a .pde file, libraries locations,...)

- My first time with NFC, so I had to figure out that NFC cards (Ali has brought a MiFareClassic1K and a STM bus ticket of type Ultralight) have different data formats.
- With the Adafruit HW and library, I was able to read and write the MiFare Classic card, but not the STM card.
- I have put my email address on the MiFare Classic.
- With an Android, Ali was able to read the stm card, but not the data inside the MiFare Classic.
- Finally I was able to find a library that permits to read a the STM card on adafruit. But when writing, it was possible ony to write correctly 4 memory locations. So I was not able to write my email address on the STM card.

- It was possible to get the arduino send characters (the card memory dump) over the USB port.

- From my previous toaster project, I knew that we can use the unix console to display these character by using /dev/tty.usbmodem1421


- I then tried to find a way to get serial character stream to a web page.
- Tested a few plugins and other things that did not work.
- Figured out that chrome had javascript functions for that.
- Found that these commands were not available to plain HTML page.
- Tried to get acces to these fucntions by writing a chrome extension.
- Figured-out that it was available only to chrome apps.
- Learned how to package a chorme app.
- Then realized that if data is received by the app, it will not be available to web page that Ali was writting for the site demo! 
- Had to find another way.

- Ali had told me that it was possible to get access to the serial port with python.
- I have installed python (first contact with that language).
- I found on internet that PySerial could help me, so installed it.
- Wrote my first python script to capture the serial port and print it.
- Coded to extract the interesting characters from the memory dump (the position of the email address I had written to the card)

- Then I stopped developping because we decided that we would not display the arduino HW during the presentation, so it did not care anymore if we were able to complete the loop about it (the only part missing was a way for the python script to give a string a caracter to the html of the web site demo).


- During that week-end, I also learned that the arduino IDE is a very very basic environment, because I did not see any way to debug the remote code, nor to modify it when it is running.

- Also, I got initiated to the git CLI.

In summary, a great opportunity to learn technical stuff and other stuff (search market price for NFC cards, startup management stuff, ...).
