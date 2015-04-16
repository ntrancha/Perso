#/bin/sh

if [ $1 -eq 0 ]
then
	if [ $2 -eq 0 ]
	then
		rand=`tr -cd 0-9 </dev/urandom | head -c 1`
		rand=`expr $rand + $3`
		./pause $rand

		if [ $4 -eq 4 ]
		then
			xdotool click 1
			xdotool click 1
			exit
		fi

		xdotool click $4
		exit
	fi
fi

rand=`tr -cd 0-5 </dev/urandom | head -c 1`
rand=`expr $rand - 3`
x1=`expr $rand + $1`
x2=`expr $rand + $2`
xdotool mousemove $x1 $x2

if [ $4 -eq 0 ]
then
	exit
fi

rand=`tr -cd 0-9 </dev/urandom | head -c 1`
rand=`expr $rand + $3`
./pause $rand

if [ $4 -eq 4 ]
then
	xdotool click 1
	xdotool click 1
	exit
fi

xdotool click $4
