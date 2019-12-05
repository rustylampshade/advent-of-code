#! /bin/bash
source 1.solution1.sh

echo "Puzzle part 2"

i=0
fuel_me 1.txt > iter$i
running_total=$(paste -sd+ iter$i | bc)
while :;
do
    old=$i
    i=$(($i + 1))
    fuel_me iter$old > iter$i
    if [ $(wc -c "iter$i" | cut -f1 -d' ') -eq 0 ]; then
        break
    fi
    running_total=$(($running_total + $(paste -sd+ iter$i | bc)))
done
rm iter*
echo $running_total
