#! /bin/bash

source 2.solution1.sh

echo "Puzzle part 2"
for noun in $(seq 0 99)
do
    echo "Trying noun = $noun"
    for verb in $(seq 0 99)
    do
        if [ "x$(run_program "$(cat 2.txt)" "$noun" "$verb")" == "x19690720" ];
        then
            echo "Noun = $noun, Verb = $verb"
            echo $((100 * $noun + $verb))
            exit
        fi
    done
done
