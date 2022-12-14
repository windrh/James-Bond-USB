This product has been manufactured for legal and responsible use.

Product Version: 0.1.1 [test stage].[update number].[release version]

WARNING: These files are only usable to the fullest extent if KeyloggerScript.py and Infected_Client.py are
    converted to .exe files. Use the following code to do so:

    import os
    os.system("cd [PyInstaller Location] --noconsole --onefile KeyloggerScript.py")
    os.system("cd [PyInstaller Location] --noconsole --onefile Infected_Client.py")

    Rename the files to something not so obvious for stealth purposes.


Overview
    This project is supposed to mimic something of a James Bond type gadget. This gadget, a USB, when plugged into any computer
    with an internet connection and running Windows, can secretly monitor target machines and even be reverse shell commanded for future hacking.
    One thing to note: I hate impractical code. Video games would have been worthless for me to do as a learning project. I was inspired to do this project because it seemed impossible for
    me to do when I thought of it, and was practical. I love a challenge, and I love shitty James Bond movies. Over the course of 40-50 hours I learned and programmed multiple
    scripts designed to function across three different machines (a USB, host and target computers). It was not easy at all. Everything I did in this project was new to me
    since this was my first semester coding. I had to learn about internet traffic (to make my project universally usable) and how forwarded ports worked, how Windows security
    procedures worked to implement workarounds, and also Malduino scripting.

    In the end, this product works perfectly for one person use. My future aspirations with this project include making it an actual product that can be shipped out to
    other people on a massive scale, and also making it work for more than one operating system.


----------------------------------------------------------------------------------scripts--------------------------------------------------------------------------------------------
Developer Note: There are no arguments except for the host machine insert_commands folder, in which any windows command can be typed into a .txt to be executed on target machine.
    The target machine will return the output of this command, if any.

Server.py

    Description:
        This is the main script to run on a host computer, where you want the final data transmissions and keylogged
        words to be sent to. This scipt can be ran with python.

    Features:
        - Send/Receive Protocol: Always sends a reverse shell command at the start of every five seconds. The script then
            opens up for receiving data transmissions.
        - Can receive keylogged submissions from any computer that Infected_Client.py is plugged in to.
        - Has the other end of a custom decoding protocol for data, this is custom file encryption made by me.
        - Stores the results in one folder: programreports
        - Programreports files are a simple .txt file that all begin with a time, date, and ipaddress of targetmachine, and contains keylogged information.
            Different reports do come into this folder, but this is the generalized format.
        - Sends reverse shell commands through insert_commands folder, which contains a single text file to input commands into. \

    Requirements:
        - Host computer must have the following specifications to use this script.
        - Custom UDP/TCP forwarded open port at port 8080
        - Firewalls deactivated

Infected_Client.py

    Description:
        This is the main script ran on a target's computer. It is best converted into a .exe but can be ran as a python file
            as well. This script is responsible for logging keys and sending them every day to the host running Server.py.

    Features:
        - Stealthy when converted to an .exe with no console and as one file [SEE WARNING]
        - Custom encryption for storage and sending: only host can see the data stored and sent from target computer.
        - Can be installed and then forgot about forever.
        - Sends keylogged data, along with a report of the target machine to include IPCONFIG and machine hardware details to
            host computer with the first time it is ran on a new machine.
        - Stores files in a global folder: windows_system.

    Requirements:
        - If the file is converted according to above specifications: No requirements for installation and use.

KeyloggerScript.py

    Description:
        This file is based off of the python module: pynput. It is responsible for recording the raw keys inputed on
            to the target machine, nothing more. The Infected_Client.py script handles the output of this file.

USB_Script_.txt/.py

    Description:
        This is the custom script used on the Malduino W USB that is used to deliver these files on to a target computer.
            This script is responsible for a lot of the anti-security attributes that are associated with this product.

    Features:
        - no Microsoft Defender Scanning
        - target to host connection (meaning target firewall is irrelevant)
        - installation and placement of product into hidden folders
        - folder settings changed to start the product on every machine startup.

    Requirements:
        - Must have the actual USB. Plug USB into computer and wait for it's script to complete.
            Once the script is completed there is nothing else to do.

----------------------------------------------------------------------------------misc----------------------------------------------------------------------------------------------
Python Modules Needed:
    If .exe on all machines as intended, none.
    If the scripts are tested as a .py, the modules pynput, logging, datetime, time, socket, and os are needed.

Output Files:
    Read Above for more specifics
    TL:DR; Standardized reports of keylogged data in the programreports folder.

----------------------------------------------------------------------------------citations-----------------------------------------------------------------------------------------
David Bombal, https://www.youtube.com/watch?v=XKoTwepEzPI, shows his audience how to
    program a simple keylogging bot that can be used to gather information. I copied this
    code because it is an element that my creative work depends on to function, not an
    element I am claiming to have made myself. In total, he provided 8 lines of code to my
    500-ish code line project.

Godinho, johan, https://www.youtube.com/watch?v=27qfn3Gco00, Godinho shows his audience how to
    create a simple file transfer protocol in order to move information across the web itself using JUST
    python. I took a lot of inspiration from this video and even copied the code at first. However, the code was too simple
    for me to use and I ended up scrapping the copied code and developing my own based on a loose guide from Johan. It was
    my first step in learning about data transfer though.

Sentdex, https://pythonprogramming.net/buffering-streaming-data-sockets-tutori
    al-python-3/?completed=/sockets-tutorial-python-3/, in this video it gives an example of making a real file transfer protocol.
    I retained the main train of thoughts and structures from the code provided in this video but I did not just straight up
    copy the code in the video. The main idea this helped me with was the 'header' in each data transmission, and why they are important.

Zak, Robert, https://www.maketecheasier.com/how-to-set-up-port-forwarding-windows-
    10/#:~:text=Create%20New%20Port%20Rules,ports%20you%20want%20to%20open, this is a simple forwarded port tutorial
    I had to follow in order to make my scripts communicate between two separate computers.

Documentations Used:

    Pynput Documentation:
        https://pynput.readthedocs.io/en/latest/
