#### -- Expert System Test -- ####
echo "\n\x1b[1mLaunching Expert System tests...\x1B[0m\n"

#### -- AND -- ####
echo "\x1b[1mand tests:\x1b[0m"

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
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi

cmd="python3 expert_system.py input/correction/and_2.txt"
output=$(eval "$cmd")
desired="A is true
F is true
K is false
P is true"

if [ "$output" == "$desired" ]
then
	echo "\x1b[32mand_2:\t\tOK\x1b[0m"
else
	echo "\x1b[31mand_2:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi

#### -- OR -- ####
echo "\n\x1b[1mor tests:\x1b[0m"

cmd="python3 expert_system.py input/correction/or_1.txt"
output=$(eval "$cmd")
desired="A is false"

if [ "$output" == "$desired" ]
then
	echo "\x1b[32mor_1:\t\tOK\x1b[0m"
else
	echo "\x1b[31mor_1:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi

cmd="python3 expert_system.py input/correction/or_2.txt"
output=$(eval "$cmd")
desired="A is true"

if [ "$output" == "$desired" ]
then
	echo "\x1b[32mor_2:\t\tOK\x1b[0m"
else
	echo "\x1b[31mor_2:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi

cmd="python3 expert_system.py input/correction/or_3.txt"
output=$(eval "$cmd")
desired="A is true"

if [ "$output" == "$desired" ]
then
	echo "\x1b[32mor_3:\t\tOK\x1b[0m"
else
	echo "\x1b[31mor_3:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi

cmd="python3 expert_system.py input/correction/or_4.txt"
output=$(eval "$cmd")
desired="A is true"

if [ "$output" == "$desired" ]
then
	echo "\x1b[32mor_4:\t\tOK\x1b[0m"
else
	echo "\x1b[31mor_4:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi



echo "\n\x1b[1mAll Expert System tests finished\x1b[0m\n"