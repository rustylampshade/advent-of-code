#! /bin/bash

function run_program {

    program=( $(echo "$1" | tr ',' ' ') )
    program[1]=$2
    program[2]=$3

    ip=0
    while :;
    do
        case ${program[$ip]} in
            1)
                param1=${program[$(($ip+1))]}
                param2=${program[$(($ip+2))]}
                tgt=${program[$(($ip+3))]}
                sum=$((${program[$param1]} + ${program[$param2]}))
                program[$tgt]=$sum
                ip=$(($ip + 4))
                ;;
            2)
                param1=${program[$(($ip+1))]}
                param2=${program[$(($ip+2))]}
                tgt=${program[$(($ip+3))]}
                mul=$((${program[$param1]} * ${program[$param2]}))
                program[$tgt]=$mul
                ip=$(($ip + 4))
                ;;
            99)
                break
                ;;
        esac
    done
    echo ${program[0]}
}

echo "Puzzle part 1"
run_program "$(cat 2.txt)" "12" "2"
