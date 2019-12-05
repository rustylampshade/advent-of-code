#! /bin/bash
function two_adjacent_digits_are_same {
    password=$1
    for digit in {0..4}
    do
        if [ ${password:$digit:1} -eq ${password:$(($digit+1)):1} ]; then
            # Uncomment for part 1
            #return 0
            # Does the third digit also match? 
            if [ $digit -gt 0 ]; then
                if [ ${password:$digit:1} -eq ${password:$(($digit-1)):1} ]; then
                    continue
                fi
            fi
            if [ $digit -lt 4 ]; then
                if [ ${password:$digit:1} -eq ${password:$(($digit+2)):1} ]; then
                    continue
                fi
            fi
            # We had a double that didn't fail triple checks.
            return 0
        fi
    done
    return 1
}
function no_decreasing_digits {
    password=$1
    for digit in {0..4}
    do
        if [ ${password:$digit:1} -gt ${password:$(($digit+1)):1} ]; then
            return 1
        fi
    done
    return 0
}
rm password_options
for password in $(seq $1 $2)
do
    if ! no_decreasing_digits "$password";
    then
        continue
    fi
    if ! two_adjacent_digits_are_same "$password";
    then
        continue
    fi
    # All requirements met.
    echo $password >> password_options
done
wc -l password_options
