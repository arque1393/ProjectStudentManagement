#! /usr/bin/bash 
# sudo apt update 
# sudo apt install python-pip 
home="home"
student="student"
my_app_path=$( dirname $(readlink -f "$0"))
echo $my_app_path
source "$my_app_path/../pyenv/bin/activate"
uiforms=($( ls $home | grep "\.ui" ))

uiforms2=($( ls $student | grep "\.ui" ))

for i in ${uiforms[@]}; do
    pyside6-uic "$home/$i" -o "$home/${i::-3}.py"
done
for i in ${uiforms2[@]}; do
    pyside6-uic "$student/$i" -o "$student/${i::-3}.py"
done
python "$my_app_path/main.py"
