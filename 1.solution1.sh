function fuel_me {
    awk '{print $1/3-2}' $1 | grep -v '^-' | cut -d. -f1
}

echo "Puzzle part 1"
fuel_me 1.txt | paste -sd+ | bc
