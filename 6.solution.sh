#! /bin/bash

orbit_file="6.txt"

function recurse_orbits {
    local celestial_body=$1
    local depth=$2
    local string_so_far="$3-${celestial_body}"
    for next_level_body in $(grep "^${celestial_body})" $orbit_file | awk -F\) '{print $2}')
    do
        direct_orbits=$(($direct_orbits + 1))
        indirect_orbits=$(($indirect_orbits + $depth - 1))
        recurse_orbits "$next_level_body" $(($depth + 1)) "${string_so_far}"
    done
    if [ $celestial_body == "SAN" ]; then
        echo "$string_so_far" >> 6.santa_substring
    elif [ $celestial_body == "YOU" ]; then
        echo "$string_so_far" >> 6.you_substring
    fi
}

direct_orbits=0
indirect_orbits=0
recurse_orbits "COM" 1 "-"

echo "$(($direct_orbits + $indirect_orbits))"

diff -y <(cat 6.you_substring | tr '-' '\n' ) <(cat 6.santa_substring | tr '-' '\n') > 6.diff
echo "Santa Hops: "$(($(grep -c '|' 6.diff)*2 + $(grep -c '[<>]' 6.diff)))
