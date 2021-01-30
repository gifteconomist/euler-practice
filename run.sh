TIMEFORMAT=$'Exec Time: %R | %S | %U'

echo "Problem #$1"
echo "---"
printf "Python -> Result: " && time python ./python/$1.py 
printf "Go -> Result: " && time ./go/$1 
printf "Rust -> Result: " && time ./rust/$1 