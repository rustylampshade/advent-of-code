#! /bin/bash

rm wire.*
rm overlaps
wirenum=1
for wire in $(cat $1)
do
    x=0
    y=0
    for movement in ${wire//,/ }
    do
        direction=${movement:0:1}
        distance=${movement:1}
        case $direction in
            U)
                for y in $(seq $((y + 1)) $(($y + $distance)) )
                do
                    echo "$x,$y" >> wire.$wirenum
                done
                ;;
            D)
                for y in $(seq $(($y - 1)) -1 $(($y - $distance)) )
                do
                    echo "$x,$y" >> wire.$wirenum
                done
                ;;
            R)
                for x in $(seq $((x + 1)) $(($x + $distance)) )
                do
                    echo "$x,$y" >> wire.$wirenum
                done
                ;;
            L)
                for x in $(seq $(($x - 1)) -1 $(($x - $distance)) )
                do
                    echo "$x,$y" >> wire.$wirenum
                done
                ;;
        esac
    done
    wirenum=$(($wirenum + 1))
done
for overlap in $(cat wire.* | sort | uniq -c | grep -v '^[ ]*1 ' | awk '{print $2}')
do
    # Make sure this wasn't a self-cross only
    if ! grep "^$overlap$" wire.1 > /dev/null 2>&1 ; then
        #echo "Point $overlap was only present in wire2"
        continue
    elif ! grep "^$overlap$" wire.2 > /dev/null 2>&1 ; then
        #echo "Point $overlap was only present in wire1"
        continue
    fi
    
    x=$(echo $overlap | awk -F, '{print $1}')
    y=$(echo $overlap | awk -F, '{print $2}')
    manhattan=$((${x#-} + ${y#-}))
    time1=$(grep -n -- "^$x,$y$" wire.1 | head -n1 | awk -F: '{print $1}')
    time2=$(grep -n -- "^$x,$y$" wire.2 | head -n1 | awk -F: '{print $1}')
    signal_time=$(($time1 + $time2))
    echo "$manhattan,$signal_time,$x,$y" >> overlaps
done
echo "Shortest Manhattan"
sort -g overlaps | head -n1
echo "Shortest Signal Time"
cat overlaps | tr ',' ' ' | sort -k2 -n | head -n1
