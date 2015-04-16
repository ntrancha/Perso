#/bin/sh

testa=`wmctrl -l | grep "Battle.net" | wc -l`
if [ $testa -eq 0 ]
then
	echo "lancement de battle.net"
	./lanch_p1.sh 2> /dev/null
	sleep 5
fi

testb=`wmctrl -l | grep "Heroes of the Storm" | wc -l`
testa=`wmctrl -l | grep "Battle.net" | wc -l`
if [ $testa -eq 1 ]
then
	if [ $testb -eq 0 ]
	then
		echo "lancement de Heroes"
		wmctrl -r Battle.net -e 0,0,0,1980,1080
		xdotool mousemove 300 1000
		./pause 20
		xdotool click 1
		xdotool click 1
		sleep 10
	fi
fi

testa=`wmctrl -l | grep "Heroes of the Storm" | wc -l`
if [ $testa -eq 1 ]
then
	echo "Heroes est lance"
	python server.py
fi
