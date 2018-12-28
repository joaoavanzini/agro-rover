#!/bin/bash

Menu(){
#collors
green='\e[1;32m';
white='\e[1;37m';
red='\e[1;31m';
yellow='\e[0;33m';
blue='\e[1;34m';
reset='\033[00m';

#starting

echo -e "$red  .d888888                              888888ba                                      $reset";
echo -e "$red d8'    88                              88    \`8b                                     $reset";
echo -e "$red 88aaaaa88a .d8888b. 88d888b. .d8888b. a88aaaa8P' .d8888b. dP   .dP .d8888b. 88d888b. $reset";
echo -e "$red 88     88  88'  \`88 88'  \`88 88'  \`88  88   \`8b. 88'  \`88 88   d8' 88ooood8 88'  \`88 $reset";
echo -e "$red 88     88  88.  .88 88       88.  .88  88     88 88.  .88 88 .88'  88.  ... 88       $reset";
echo -e "$red 88     88  \`8888P88 dP       \`88888P'  dP     dP \`88888P' 8888P'   \`88888P' dP       $reset";
echo -e "$red                 .88                                                                  $reset";
echo -e "$red             d8888P                                                                   $reset";
echo -e "$blue                                                                     [robotecweb.com.br]$reset";

#options
echo -e "";
echo -e "$white -- choose your option: $reset";
echo -e "$blue +--------------------------+ $reset";
echo -e "$blue | $red[ 1 ] about / how to use $blue| $reset";
echo -e "$blue | $red[ 2 ] automatic pilot    $blue| $reset";
echo -e "$blue | $red[ 3 ] pilot programming  $blue| $reset";
echo -e "$blue | $red[ 4 ] photo              $blue| $reset";
echo -e "$blue +--------------------------+ $reset";
read option

#case
 case $option in
	1)About_howuse ;;
	2)Automatic_Pilot ;;
	3)Pilot_Programming ;;
	4)Photo ;;
	5) exit ;;
 esac
}

About_howuse(){

echo -e "$red AgroRover $reset";
echo "";
echo "";
echo -e "$green English $reset";
echo "";
echo -e "$yellow About: $reset";
echo -e "$white AgroRover was created by Mario Avancini and developed by João Victor Barbosa. This robotic device works to water plants on grounds that are not conducive to the routing of hoses, because a plant is planted in scattered places. $reset";
echo -e "$blue Mario Avancini - Campo Di Vita $reset";
echo -e "$blue João VIctor Barbosa - Robotec $reset";
echo -e "$yellow How to use: $reset";
echo -e "$white Simple procedure, choose between - 2 - and - 3 - for the operation of the robotic device. In - automatic pillot - it will make the way checking the path with possibilities of own choice. In - pillot programming -, the user can create the path that the robotic device will do. To do this open the - ControlPillotProgramming.py - and type the necessary commands. $reset";
echo "";
echo "";
echo -e "$green Portuguese - Brazilan $reset";
echo "";
echo -e "$yellow Sobre: $reset";
echo -e "$white o AgroRover foi criado por Mario Avancini e desenvolvido por João Victor Barbosa. Este dispositivo robótico funciona para aguar plantas em terrenos não propicios ao encaminhamento de mangueiras, pelo fato de uma planta estar plantada emlugares disperços. $reset";
echo -e "$blue Mario Avancini - Campo Di Vita $reset";
echo -e "$blue João VIctor Barbosa - Robotec $reset";
echo -e "$yellow Como usar: $reset";
echo -e "$white Procedimento simples, escolha entre - 2 -  e - 3 -  para o funcionamento do dispositivo robótico. Em - automatic pillot - fará o caminho checando com possibilidades de escolha própria. Em - pillot programming -, o usuário poderá criarocaminho que o dispositivo robótico fará. Para isso abrá o - ControlPillotProgramming.py - e escreva os comandos necessários.   $reset";

}

Automatic_Pilot(){

chmod +x Codes/ObstacleAvoid/Backward.py;
chmod +x Codes/ObstacleAvoid/Forward.py;
chmod +x Codes/ObstacleAvoid/Left.py;
chmod +x Codes/ObstacleAvoid/Right.py;
chmod +x Codes/ObstacleAvoid/Stop.py;

chmod +x Codes/ObstacleAvoid/ObstacleAvoid.py;
cd Codes/ObstacleAvoid;
python3 ObstacleAvoid.py;

}

Pilot_Programming(){

chmod +x Codes/ControlPilot/ControlPilotProgramming.py;
python3 Codes/ControlPilot/ControlPilotProgramming.py;

}

Photo(){

DATE=$(date +"%Y-%m-%d_%H%M")

fswebcam -r 1280x720 --no-banner /home/pi/Desktop/AgroRover/Pictures/$DATE.jpg

echo -e "$red Photo ready! $reset";

sudo cp /home/pi/Desktop/AgroRover/Pictures/$DATE.jpg /var/www/html/Pictures

echo -e "$red Photo to localhost! $reset";

}

Menu
