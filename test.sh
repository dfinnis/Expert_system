#### -- Expert System Test -- ####
echo "\n\x1b[1mLaunching Expert System tests...\x1B[0m\n"

#### -- AND -- ####
cmd="python3 expert_system.py input/correction/and_1.txt"
output=$(eval "$cmd")
desired="A is true
F is true
K is true
P is true"

if [ "$output" == "$desired" ]
then
	echo "\x1b[32mand_1:\t\tOK\x1b[0m"
else
	echo "\x1b[31mand_1:\t\tERROR\x1b[0m"
	echo "$output"
fi

echo "\n\x1b[1mAll Expert System tests finished\x1b[0m\n"