# CassiePy
A command line tool for managing and running python scripts

## Requirements
Needs a terminal that supports ansii text  - Windows Terminal should work great, tested on Kali Linux and Parrot OS. Untested on Mac or other linux distros, but should work fine.

## Installation
##### *For now just download the code, might get published somewhere later*
Clone this repository:

  `$git clone https://github.com/SaberSwordBoy/CassiePy`  
  `$cd CassiePy`

Install Requirements:

  `$pip install -r requirements.txt`
  
  
## Usage
After installing, simply run the script

`$python main.py`

This will start the program!
After it loads, it will prompt you to enter a command. Don't know what to type?  
Try the `help` command!
It prints out all the commands and a short description.

Still not getting a command?  
Do `help <command>` to get more detailed info

## Adding Modules
If you want to add your own modules, you can!

NOTE: *modules currently do not support command line arguments from CassiePy, but that may be coming soon*  
*if you want your module to use arguments, ask for them with the `input()` function built into python*

All you need to do is have a .py file with some specific variables and functions.  
To get started, follow the below instructions!  
After you put your module in, CassiePy should load it!

First make your module: 
To see what a module should look like, check out `CassiePy/modules/example1.py`

Modules should have a short but descriptive name, like 'netscraper' or 'texttospeech'

Each module needs a `NAME` and `DESCRIPTION` variable.

It also needs a `run()` function, for executing the code from the CassiePy CLI

Place this file in the `CassiePy/modules/` directory 

And done! Your modules should show up when running the `modules` command in CassiePy

### Want to publish your module?
Start a pull request on this repository! The only change you should need to make is adding your module to the modules directory.  
I will review the module, test it, and if it works, it will get added!

## Contributing

Feel free to make edits to my code! (it's probably bad anyway)

I'm always open to criticism as well. Let us know if you think we should do something different!


# Thanks for contributing!


###### *this file is now exactly 69 lines*
