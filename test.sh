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

#### -- XOR -- ####
echo "\n\x1b[1mxor tests:\x1b[0m"

cmd="python3 expert_system.py input/correction/xor_1.txt"
output=$(eval "$cmd")
desired="A is false"
if [ "$output" == "$desired" ]
then
	echo "\x1b[32mxor_1:\t\tOK\x1b[0m"
else
	echo "\x1b[31mxor_1:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi

cmd="python3 expert_system.py input/correction/xor_2.txt"
output=$(eval "$cmd")
desired="A is true"
if [ "$output" == "$desired" ]
then
	echo "\x1b[32mxor_2:\t\tOK\x1b[0m"
else
	echo "\x1b[31mxor_2:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi

cmd="python3 expert_system.py input/correction/xor_3.txt"
output=$(eval "$cmd")
desired="A is true"
if [ "$output" == "$desired" ]
then
	echo "\x1b[32mxor_3:\t\tOK\x1b[0m"
else
	echo "\x1b[31mxor_3:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi

cmd="python3 expert_system.py input/correction/xor_4.txt"
output=$(eval "$cmd")
desired="A is false"
if [ "$output" == "$desired" ]
then
	echo "\x1b[32mxor_4:\t\tOK\x1b[0m"
else
	echo "\x1b[31mxor_4:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi

#### -- NOT -- ####
echo "\n\x1b[1mnot tests:\x1b[0m"

cmd="python3 expert_system.py input/correction/not_1.txt"
output=$(eval "$cmd")
desired="A is false"
if [ "$output" == "$desired" ]
then
	echo "\x1b[32mnot_1:\t\tOK\x1b[0m"
else
	echo "\x1b[31mnot_1:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi

cmd="python3 expert_system.py input/correction/not_2.txt"
output=$(eval "$cmd")
desired="A is true"
if [ "$output" == "$desired" ]
then
	echo "\x1b[32mnot_2:\t\tOK\x1b[0m"
else
	echo "\x1b[31mnot_2:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi

cmd="python3 expert_system.py input/correction/not_3.txt"
output=$(eval "$cmd")
desired="A is false"
if [ "$output" == "$desired" ]
then
	echo "\x1b[32mnot_3:\t\tOK\x1b[0m"
else
	echo "\x1b[31mnot_3:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi

cmd="python3 expert_system.py input/correction/not_4.txt"
output=$(eval "$cmd")
desired="A is false"
if [ "$output" == "$desired" ]
then
	echo "\x1b[32mnot_4:\t\tOK\x1b[0m"
else
	echo "\x1b[31mnot_4:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi

#### -- SAME CONCLUSION -- ####
echo "\n\x1b[1msame conclusion tests:\x1b[0m"

cmd="python3 expert_system.py input/correction/same_conclusion_1.txt"
output=$(eval "$cmd")
desired="A is false"
if [ "$output" == "$desired" ]
then
	echo "\x1b[32msame_conclusion_1:\t\tOK\x1b[0m"
else
	echo "\x1b[31msame_conclusion_1:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi

cmd="python3 expert_system.py input/correction/same_conclusion_2.txt"
output=$(eval "$cmd")
desired="A is true"
if [ "$output" == "$desired" ]
then
	echo "\x1b[32msame_conclusion_2:\t\tOK\x1b[0m"
else
	echo "\x1b[31msame_conclusion_2:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi

cmd="python3 expert_system.py input/correction/same_conclusion_3.txt"
output=$(eval "$cmd")
desired="A is true"
if [ "$output" == "$desired" ]
then
	echo "\x1b[32msame_conclusion_3:\t\tOK\x1b[0m"
else
	echo "\x1b[31msame_conclusion_3:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi

cmd="python3 expert_system.py input/correction/same_conclusion_4.txt"
output=$(eval "$cmd")
desired="A is true"
if [ "$output" == "$desired" ]
then
	echo "\x1b[32msame_conclusion_4:\t\tOK\x1b[0m"
else
	echo "\x1b[31msame_conclusion_4:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi

#### -- PARENTHESIS -- ####
echo "\n\x1b[1mparenthesis tests:\x1b[0m"

cmd="python3 expert_system.py input/correction/parenthesis_1.txt"
output=$(eval "$cmd")
desired="E is false"
if [ "$output" == "$desired" ]
then
	echo "\x1b[32mparenthesis_1:\t\tOK\x1b[0m"
else
	echo "\x1b[31mparenthesis_1:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi

cmd="python3 expert_system.py input/correction/parenthesis_2.txt"
output=$(eval "$cmd")
desired="E is true"
if [ "$output" == "$desired" ]
then
	echo "\x1b[32mparenthesis_2:\t\tOK\x1b[0m"
else
	echo "\x1b[31mparenthesis_2:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi

cmd="python3 expert_system.py input/correction/parenthesis_3.txt"
output=$(eval "$cmd")
desired="E is false"
if [ "$output" == "$desired" ]
then
	echo "\x1b[32mparenthesis_3:\t\tOK\x1b[0m"
else
	echo "\x1b[31mparenthesis_3:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi

cmd="python3 expert_system.py input/correction/parenthesis_4.txt"
output=$(eval "$cmd")
desired="E is false"
if [ "$output" == "$desired" ]
then
	echo "\x1b[32mparenthesis_4:\t\tOK\x1b[0m"
else
	echo "\x1b[31mparenthesis_4:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi

cmd="python3 expert_system.py input/correction/parenthesis_5.txt"
output=$(eval "$cmd")
desired="E is false"
if [ "$output" == "$desired" ]
then
	echo "\x1b[32mparenthesis_5:\t\tOK\x1b[0m"
else
	echo "\x1b[31mparenthesis_5:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi

cmd="python3 expert_system.py input/correction/parenthesis_6.txt"
output=$(eval "$cmd")
desired="E is true"
if [ "$output" == "$desired" ]
then
	echo "\x1b[32mparenthesis_6:\t\tOK\x1b[0m"
else
	echo "\x1b[31mparenthesis_6:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi

cmd="python3 expert_system.py input/correction/parenthesis_7.txt"
output=$(eval "$cmd")
desired="E is false"
if [ "$output" == "$desired" ]
then
	echo "\x1b[32mparenthesis_7:\t\tOK\x1b[0m"
else
	echo "\x1b[31mparenthesis_7:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi

cmd="python3 expert_system.py input/correction/parenthesis_8.txt"
output=$(eval "$cmd")
desired="E is false"
if [ "$output" == "$desired" ]
then
	echo "\x1b[32mparenthesis_8:\t\tOK\x1b[0m"
else
	echo "\x1b[31mparenthesis_8:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi

cmd="python3 expert_system.py input/correction/parenthesis_9.txt"
output=$(eval "$cmd")
desired="E is false"
if [ "$output" == "$desired" ]
then
	echo "\x1b[32mparenthesis_9:\t\tOK\x1b[0m"
else
	echo "\x1b[31mparenthesis_9:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi

cmd="python3 expert_system.py input/correction/parenthesis_10.txt"
output=$(eval "$cmd")
desired="E is true"
if [ "$output" == "$desired" ]
then
	echo "\x1b[32mparenthesis_10:\t\tOK\x1b[0m"
else
	echo "\x1b[31mparenthesis_10:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi

cmd="python3 expert_system.py input/correction/parenthesis_11.txt"
output=$(eval "$cmd")
desired="E is true"
if [ "$output" == "$desired" ]
then
	echo "\x1b[32mparenthesis_11:\t\tOK\x1b[0m"
else
	echo "\x1b[31mparenthesis_11:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi

#### -- ERROR -- ####
echo "\n\x1b[1merror tests:\x1b[0m"

cmd="python3 expert_system.py input/invalid/bullshit_filepath"
output=$(eval "$cmd")
desired="Error: Invalid filepath"
if [ "$output" == "$desired" ]
then
	echo "\x1b[32minvalid filepath:\tOK\x1b[0m"
else
	echo "\x1b[31minvalid filepath:\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi

cmd="python3 expert_system.py input/invalid/invalid_symbol.txt"
output=$(eval "$cmd")
desired="Error: Invalid symbol in file"
if [ "$output" == "$desired" ]
then
	echo "\x1b[32minvalid symbol:\t\tOK\x1b[0m"
else
	echo "\x1b[31minvalid symbol:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi

cmd="python3 expert_system.py input/invalid/2_initial_fact_lines.txt"
output=$(eval "$cmd")
desired="Error: Multiple lines of initial facts"
if [ "$output" == "$desired" ]
then
	echo "\x1b[32m2 initial fact lines:\tOK\x1b[0m"
else
	echo "\x1b[31m2 initial fact lines:\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi

cmd="python3 expert_system.py input/invalid/2_query_lines.txt"
output=$(eval "$cmd")
desired="Error: Multiple lines of queries"
if [ "$output" == "$desired" ]
then
	echo "\x1b[32m2 query lines:\t\tOK\x1b[0m"
else
	echo "\x1b[31m2 query lines:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi

echo "\n\x1b[1mAll Expert System tests finished\x1b[0m\n"