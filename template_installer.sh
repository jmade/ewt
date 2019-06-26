#!/bin/sh

# COLORS
_reset=$(tput sgr0)
_green=$(tput setaf 76)
_purple=$(tput setaf 171)
_red=$(tput setaf 1)
_tan=$(tput setaf 3)
_blue=$(tput setaf 38)
_bold=$(tput bold)
_underline=$(tput sgr 0 1)


function _success()
{
    printf "${_green}✔ %s${_reset}\n" "$@"
}

function _bolded()
{
	printf "${_bold}%s${_reset}\n" "$@"
}

function _error()
{
	printf "${_red}%s${_reset}\n" "$@"
}


_bolded 'Installing Template Maker'
clear
cd 
wget https://raw.githubusercontent.com/jmade/ewt/master/make_template.py
clear
_bolded 'Installing Bash Profile Alias'
echo '' >> ~/.bash_profile
echo '# Template Helper alias' >> ~/.bash_profile
echo 'alias start="python3 ~/make_template.py"' >> ~/.bash_profile
_success 'Instalation Complete'
clear
echo '. ~/.bash_profile' | pbcopy
echo "To use: type 'start' in the terminal."

_bolded "Press COMMAND + V to finish."
