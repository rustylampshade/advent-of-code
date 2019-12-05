#! /bin/bash

function process_parameters {
    # Reads global variables $ip and $program, don't change them here.

    parameter_count=$1
    write=$2
    if [ ${#program[$ip]} -eq 1 ]; then
        printf -v parameter_modes "%0${parameter_count}d" "${program[$ip]::-1}"
    else
        printf -v parameter_modes "%0${parameter_count}d" "${program[$ip]::-2}"
    fi
    parameter_modes=$(echo "$parameter_modes" | rev)
    for (( parameter_num = 0; parameter_num < parameter_count; parameter_num++ )); do
        parameter_name="p$parameter_num"
        parameter_mode="${parameter_modes:$parameter_num:1}"
        if [ $parameter_num -eq $(($parameter_count - 1)) ]; then 
            if [ $write -eq 0 ]; then
                parameter_mode=1
            fi
        fi
        if [ $parameter_mode -eq 0 ]; then
            # Position Mode
            computed_parameters="$computed_parameters ${program[${program[$(($ip+1+$parameter_num))]}]}"
        elif [ $parameter_mode -eq 1 ]; then
            # Immediate mode
            computed_parameters="$computed_parameters ${program[$(($ip+1+$parameter_num))]}"
        fi
    done
    echo "$computed_parameters"
}

function run_program {
    program=( $(echo "$1" | tr ',' ' ') )
    ip=0
    while :;
    do
        #echo "IP:$ip"
        #echo "Instruction: ${program[$ip]} (plus maybe ${program[$(($ip+1))]})"
        case ${program[$ip]} in
            *1)
                parameter_count=3
                parameters=( $(process_parameters $parameter_count 0) )
                sum=$((${parameters[0]} + ${parameters[1]}))
                program[${parameters[2]}]=$sum
                echo "Instruction 01: Added ${parameters[0]} to ${parameters[1]} ($sum), saved to location ${parameters[2]}"
                ip=$(($ip + 1 + $parameter_count))
                ;;
            *2)
                parameter_count=3
                parameters=( $(process_parameters $parameter_count 0) )
                mul=$((${parameters[0]} * ${parameters[1]}))
                program[${parameters[2]}]=$mul
                echo "Instruction 02: Multiplied ${parameters[0]} by ${parameters[1]} ($mul), saved to location ${parameters[2]}"
                ip=$(($ip + 1 + $parameter_count))
                ;;
            *3)
                parameter_count=1
                parameters=( $(process_parameters $parameter_count 0) )
                echo "Instruction 03: User Input"
                read user_input
                program[${parameters[0]}]=$user_input
                ip=$(($ip + 1 + $parameter_count))
                ;;
            *4)
                parameter_count=1
                parameters=( $(process_parameters $parameter_count 1) )
                echo "Instruction 04: ${parameters[0]}"
                ip=$(($ip + 1 + $parameter_count))
                ;;
            *5)
                parameter_count=2
                parameters=( $(process_parameters $parameter_count 1) )
                if [ ${parameters[0]} -ne 0 ]; then
                    echo "Instruction 05: Jumped to ${parameters[1]} since ${parameters[0]} is non-zero"
                    ip=${parameters[1]}
                else
                    echo "Instruction 05: Considered jump to ${parameters[1]} if ${parameters[0]} were non-zero"
                    ip=$(($ip + 1 + $parameter_count))
                fi
                ;;
            *6)
                parameter_count=2
                parameters=( $(process_parameters $parameter_count 1) )
                if [ ${parameters[0]} -eq 0 ]; then
                    echo "Instruction 06: Jumped to ${parameters[1]} since ${parameters[0]} is zero"
                    ip=${parameters[1]}
                else
                    echo "Instruction 06: Considered jump to ${parameters[1]} if ${parameters[0]} were zero"
                    ip=$(($ip + 1 + $parameter_count))
                fi
                ;;
            *7)
                parameter_count=3
                parameters=( $(process_parameters $parameter_count 0) )
                if [ ${parameters[0]} -lt ${parameters[1]} ]; then
                    echo "Instruction 07: ${parameters[0]} is less than ${parameters[1]}, so writing 1 to ${parameters[2]}"
                    program[${parameters[2]}]=1
                else
                    echo "Instruction 07: ${parameters[0]} is NOT less than ${parameters[1]}, so writing 0 to ${parameters[2]}"
                    program[${parameters[2]}]=0
                fi
                ip=$(($ip + 1 + $parameter_count))
                ;;
            *8)
                parameter_count=3
                parameters=( $(process_parameters $parameter_count 0) )
                if [ ${parameters[0]} -eq ${parameters[1]} ]; then
                    echo "Instruction 08: ${parameters[0]} is equal to ${parameters[1]}, so writing 1 to ${parameters[2]}"
                    program[${parameters[2]}]=1
                else
                    echo "Instruction 08: ${parameters[0]} is NOT equal to ${parameters[1]}, so writing 0 to ${parameters[2]}"
                    program[${parameters[2]}]=0
                fi
                ip=$(($ip + 1 + $parameter_count))
                ;;
            99)
                break
                ;;
        esac
    done
    echo "Overall output: ${program[0]}"
}

run_program "$(cat 5.txt)"
