#! /bin/bash

image=$(cat 8.txt)
rm 8.results

idx=0
layer=0
line_width=25
while [ $idx -lt ${#image} ];
do
    # Because there's six lines per layer.
    layer_zeros=0
    layer_ones=0
    layer_twos=0
    for line in {0..5};
    do
        layer_line="${image:$idx:$line_width}"

        zeros=${layer_line//[^0]/}
        layer_zeros=$(($layer_zeros + ${#zeros}))

        ones=${layer_line//[^1]/}
        layer_ones=$(($layer_ones + ${#ones}))

        twos=${layer_line//[^2]/}
        layer_twos=$(($layer_twos + ${#twos}))

        idx=$(($idx+$line_width))
    done
    echo "$layer $layer_zeros $layer_ones $layer_twos $(($layer_ones*$layer_twos))" >> 8.results
    layer=$(($layer+1))
done

echo "PART 1: "$(sort -n -k2 8.results | head -n1)


# Why bother reusing.
idx=0
layer=0
declare -a line0
declare -a line1
declare -a line2
declare -a line3
declare -a line4
declare -a line5
while [ $idx -lt ${#image} ];
do
    for x in {0..24}
    do
        line0[$x]="${line0[$x]}${image:$idx:1}"
        idx=$(($idx+1))
    done
    for x in {0..24}
    do
        line1[$x]="${line1[$x]}${image:$idx:1}"
        idx=$(($idx+1))
    done
    for x in {0..24}
    do
        line2[$x]="${line2[$x]}${image:$idx:1}"
        idx=$(($idx+1))
    done
    for x in {0..24}
    do
        line3[$x]="${line3[$x]}${image:$idx:1}"
        idx=$(($idx+1))
    done
    for x in {0..24}
    do
        line4[$x]="${line4[$x]}${image:$idx:1}"
        idx=$(($idx+1))
    done
    for x in {0..24}
    do
        line5[$x]="${line5[$x]}${image:$idx:1}"
        idx=$(($idx+1))
    done
    layer=$(($layer+1))
done

for pixel in ${line0[@]}
do
    no_transparent=${pixel//2/}
    character=${no_transparent:0:1}
    if [ $character == '1' ]; then
        echo -n '#'
    else
        echo -n ' '
    fi
done
echo ""
for pixel in ${line1[@]}
do
    no_transparent=${pixel//2/}
    character=${no_transparent:0:1}
    if [ $character == '1' ]; then
        echo -n '#'
    else
        echo -n ' '
    fi
done
echo ""
for pixel in ${line2[@]}
do
    no_transparent=${pixel//2/}
    character=${no_transparent:0:1}
    if [ $character == '1' ]; then
        echo -n '#'
    else
        echo -n ' '
    fi
done
echo ""
for pixel in ${line3[@]}
do
    no_transparent=${pixel//2/}
    character=${no_transparent:0:1}
    if [ $character == '1' ]; then
        echo -n '#'
    else
        echo -n ' '
    fi
done
echo ""
for pixel in ${line4[@]}
do
    no_transparent=${pixel//2/}
    character=${no_transparent:0:1}
    if [ $character == '1' ]; then
        echo -n '#'
    else
        echo -n ' '
    fi
done
echo ""
for pixel in ${line5[@]}
do
    no_transparent=${pixel//2/}
    character=${no_transparent:0:1}
    if [ $character == '1' ]; then
        echo -n '#'
    else
        echo -n ' '
    fi
done
echo ""
