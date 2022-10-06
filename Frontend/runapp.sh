#! /usr/bin/bash 
# sudo apt update 
# sudo apt install python-pip 
my_app_path=$( dirname $(readlink -f "$0"))
echo $my_app_path
source "$my_app_path/../pyenv/bin/activate"
uiforms=($( ls | grep "\.ui" ))


for i in ${uiforms[@]}; do
    pyside6-uic "$i" -o "${i::-3}.py"
done

python "$my_app_path/main.py"
