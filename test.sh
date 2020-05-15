#### -- Expert System Test -- ####
echo "\n\x1b[1mLaunching Expert System tests...\x1B[0m\n"

passed=0
count=0

#### -- AND -- ####
echo "\x1b[1mand tests:\x1b[0m"

cmd="python3 expert_system.py input/correction/and_1.txt"
output=$(eval "$cmd")
desired="A is True
F is True
K is True
P is True"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mand_1:\t\t\tOK\x1b[0m"
else
	echo "\x1b[31mand_1:\t\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/correction/and_2.txt"
output=$(eval "$cmd")
desired="A is True
F is True
K is False
P is True"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mand_2:\t\t\tOK\x1b[0m"
else
	echo "\x1b[31mand_2:\t\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

#### -- MORE AND -- ####
echo

cmd="python3 expert_system.py input/valid/and_long.txt"
output=$(eval "$cmd")
desired="Z is True"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mand_long:\t\tOK\x1b[0m"
else
	echo "\x1b[31mand_long:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/valid/and_long_2.txt"
output=$(eval "$cmd")
desired="A is False"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mand_long_2:\t\tOK\x1b[0m"
else
	echo "\x1b[31mand_long_2:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

#### -- OR -- ####
echo "\n\x1b[1mor tests:\x1b[0m"

cmd="python3 expert_system.py input/correction/or_1.txt"
output=$(eval "$cmd")
desired="A is False"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mor_1:\t\t\tOK\x1b[0m"
else
	echo "\x1b[31mor_1:\t\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/correction/or_2.txt"
output=$(eval "$cmd")
desired="A is True"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mor_2:\t\t\tOK\x1b[0m"
else
	echo "\x1b[31mor_2:\t\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/correction/or_3.txt"
output=$(eval "$cmd")
desired="A is True"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mor_3:\t\t\tOK\x1b[0m"
else
	echo "\x1b[31mor_3:\t\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/correction/or_4.txt"
output=$(eval "$cmd")
desired="A is True"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mor_4:\t\t\tOK\x1b[0m"
else
	echo "\x1b[31mor_4:\t\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

#### -- MORE OR -- ####
echo

cmd="python3 expert_system.py input/valid/or_long.txt"
output=$(eval "$cmd")
desired="Z is True"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mor_long:\t\tOK\x1b[0m"
else
	echo "\x1b[31mor_long:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/valid/or_long_2.txt"
output=$(eval "$cmd")
desired="A is False"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mor_long_2:\t\tOK\x1b[0m"
else
	echo "\x1b[31mor_long_2:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/valid/undetermined_or.txt"
output=$(eval "$cmd")
desired="B is Undetermined
C is Undetermined"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mor_undetermined:\tOK\x1b[0m"
else
	echo "\x1b[31mor_undetermined:\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/valid/undetermined_or_2.txt"
output=$(eval "$cmd")
desired="B is Undetermined
C is Undetermined
D is Undetermined"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mor_undetermined_2:\tOK\x1b[0m"
else
	echo "\x1b[31mor_undetermined_2:\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

#### -- OR NOT -- ####

cmd="python3 expert_system.py input/valid/or_not_1.txt"
output=$(eval "$cmd")
desired="A is True"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mor_not_1:\t\tOK\x1b[0m"
else
	echo "\x1b[31mor_not_1:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/valid/or_not_2.txt"
output=$(eval "$cmd")
desired="A is False"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mor_not_2:\t\tOK\x1b[0m"
else
	echo "\x1b[31mor_not_2:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/valid/or_not_3.txt"
output=$(eval "$cmd")
desired="A is True"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mor_not_3:\t\tOK\x1b[0m"
else
	echo "\x1b[31mor_not_3:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/valid/or_not_4.txt"
output=$(eval "$cmd")
desired="A is True"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mor_not_4:\t\tOK\x1b[0m"
else
	echo "\x1b[31mor_not_4:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/valid/or_not_5.txt"
output=$(eval "$cmd")
desired="A is True"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mor_not_5:\t\tOK\x1b[0m"
else
	echo "\x1b[31mor_not_5:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

#### -- XOR -- ####
echo "\n\x1b[1mxor tests:\x1b[0m"

cmd="python3 expert_system.py input/correction/xor_1.txt"
output=$(eval "$cmd")
desired="A is False"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mxor_1:\t\t\tOK\x1b[0m"
else
	echo "\x1b[31mxor_1:\t\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/correction/xor_2.txt"
output=$(eval "$cmd")
desired="A is True"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mxor_2:\t\t\tOK\x1b[0m"
else
	echo "\x1b[31mxor_2:\t\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/correction/xor_3.txt"
output=$(eval "$cmd")
desired="A is True"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mxor_3:\t\t\tOK\x1b[0m"
else
	echo "\x1b[31mxor_3:\t\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/correction/xor_4.txt"
output=$(eval "$cmd")
desired="A is False"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mxor_4:\t\t\tOK\x1b[0m"
else
	echo "\x1b[31mxor_4:\t\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

#### -- MORE OR -- ####
echo

cmd="python3 expert_system.py input/valid/xor_long.txt"
output=$(eval "$cmd")
desired="Z is True"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mxor_long:\t\tOK\x1b[0m"
else
	echo "\x1b[31mxor_long:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/valid/xor_long_2.txt"
output=$(eval "$cmd")
desired="Z is False"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mxor_long_2:\t\tOK\x1b[0m"
else
	echo "\x1b[31mxor_long_2:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/valid/undetermined_xor.txt"
output=$(eval "$cmd")
desired="B is Undetermined
C is Undetermined"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mxor_undetermined:\tOK\x1b[0m"
else
	echo "\x1b[31mxor_undetermined:\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/valid/undetermined_xor_2.txt"
output=$(eval "$cmd")
desired="B is Undetermined
C is Undetermined
D is Undetermined"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mxor_undetermined_2:\tOK\x1b[0m"
else
	echo "\x1b[31mxor_undetermined_2:\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

#### -- XOR NOT -- ####

cmd="python3 expert_system.py input/valid/xor_not_1.txt"
output=$(eval "$cmd")
desired="A is True"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mxor_not_1:\t\tOK\x1b[0m"
else
	echo "\x1b[31mxor_not_1:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/valid/xor_not_2.txt"
output=$(eval "$cmd")
desired="A is False"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mxor_not_2:\t\tOK\x1b[0m"
else
	echo "\x1b[31mxor_not_2:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/valid/xor_not_3.txt"
output=$(eval "$cmd")
desired="A is False"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mxor_not_3:\t\tOK\x1b[0m"
else
	echo "\x1b[31mxor_not_3:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/valid/xor_not_4.txt"
output=$(eval "$cmd")
desired="A is True"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mxor_not_4:\t\tOK\x1b[0m"
else
	echo "\x1b[31mxor_not_4:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/valid/xor_not_5.txt"
output=$(eval "$cmd")
desired="A is False"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mxor_not_5:\t\tOK\x1b[0m"
else
	echo "\x1b[31mxor_not_5:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/valid/xor_not_6.txt"
output=$(eval "$cmd")
desired="A is False"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mxor_not_6:\t\tOK\x1b[0m"
else
	echo "\x1b[31mxor_not_6:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/valid/xor_not_7.txt"
output=$(eval "$cmd")
desired="A is True"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mxor_not_7:\t\tOK\x1b[0m"
else
	echo "\x1b[31mxor_not_7:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

#### -- NOT -- ####
echo "\n\x1b[1mnot tests:\x1b[0m"

cmd="python3 expert_system.py input/correction/not_1.txt"
output=$(eval "$cmd")
desired="A is False"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mnot_1:\t\t\tOK\x1b[0m"
else
	echo "\x1b[31mnot_1:\t\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/correction/not_2.txt"
output=$(eval "$cmd")
desired="A is True"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mnot_2:\t\t\tOK\x1b[0m"
else
	echo "\x1b[31mnot_2:\t\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/correction/not_3.txt"
output=$(eval "$cmd")
desired="A is False"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mnot_3:\t\t\tOK\x1b[0m"
else
	echo "\x1b[31mnot_3:\t\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/correction/not_4.txt"
output=$(eval "$cmd")
desired="A is False"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mnot_4:\t\t\tOK\x1b[0m"
else
	echo "\x1b[31mnot_4:\t\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

#### -- SAME CONCLUSION -- ####
echo "\n\x1b[1msame conclusion tests:\x1b[0m"

cmd="python3 expert_system.py input/correction/same_conclusion_1.txt"
output=$(eval "$cmd")
desired="A is False"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32msame_conclusion_1:\tOK\x1b[0m"
else
	echo "\x1b[31msame_conclusion_1:\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/correction/same_conclusion_2.txt"
output=$(eval "$cmd")
desired="A is True"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32msame_conclusion_2:\tOK\x1b[0m"
else
	echo "\x1b[31msame_conclusion_2:\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/correction/same_conclusion_3.txt"
output=$(eval "$cmd")
desired="A is True"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32msame_conclusion_3:\tOK\x1b[0m"
else
	echo "\x1b[31msame_conclusion_3:\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/correction/same_conclusion_4.txt"
output=$(eval "$cmd")
desired="A is True"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32msame_conclusion_4:\tOK\x1b[0m"
else
	echo "\x1b[31msame_conclusion_4:\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

#### -- PARENTHESIS -- ####
echo "\n\x1b[1mparenthesis tests:\x1b[0m"

cmd="python3 expert_system.py input/correction/parenthesis_1.txt"
output=$(eval "$cmd")
desired="E is False"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mparenthesis_1:\t\tOK\x1b[0m"
else
	echo "\x1b[31mparenthesis_1:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/correction/parenthesis_2.txt"
output=$(eval "$cmd")
desired="E is True"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mparenthesis_2:\t\tOK\x1b[0m"
else
	echo "\x1b[31mparenthesis_2:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/correction/parenthesis_3.txt"
output=$(eval "$cmd")
desired="E is False"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mparenthesis_3:\t\tOK\x1b[0m"
else
	echo "\x1b[31mparenthesis_3:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/correction/parenthesis_4.txt"
output=$(eval "$cmd")
desired="E is False"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mparenthesis_4:\t\tOK\x1b[0m"
else
	echo "\x1b[31mparenthesis_4:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/correction/parenthesis_5.txt"
output=$(eval "$cmd")
desired="E is False"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mparenthesis_5:\t\tOK\x1b[0m"
else
	echo "\x1b[31mparenthesis_5:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/correction/parenthesis_6.txt"
output=$(eval "$cmd")
desired="E is True"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mparenthesis_6:\t\tOK\x1b[0m"
else
	echo "\x1b[31mparenthesis_6:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/correction/parenthesis_7.txt"
output=$(eval "$cmd")
desired="E is False"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mparenthesis_7:\t\tOK\x1b[0m"
else
	echo "\x1b[31mparenthesis_7:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/correction/parenthesis_8.txt"
output=$(eval "$cmd")
desired="E is False"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mparenthesis_8:\t\tOK\x1b[0m"
else
	echo "\x1b[31mparenthesis_8:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/correction/parenthesis_9.txt"
output=$(eval "$cmd")
desired="E is False"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mparenthesis_9:\t\tOK\x1b[0m"
else
	echo "\x1b[31mparenthesis_9:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/correction/parenthesis_10.txt"
output=$(eval "$cmd")
desired="E is True"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mparenthesis_10:\t\tOK\x1b[0m"
else
	echo "\x1b[31mparenthesis_10:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/correction/parenthesis_11.txt"
output=$(eval "$cmd")
desired="E is True"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mparenthesis_11:\t\tOK\x1b[0m"
else
	echo "\x1b[31mparenthesis_11:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

#### -- ERROR -- ####
echo "\n\x1b[1merror tests:\x1b[0m"

cmd="python3 expert_system.py input/invalid/bullshit_filepath"
output=$(eval "$cmd")
desired="Error: Invalid filepath"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32minvalid filepath:\tOK\x1b[0m"
else
	echo "\x1b[31minvalid filepath:\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/invalid/invalid_symbol.txt"
output=$(eval "$cmd")
desired="Error: Invalid symbol in file"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32minvalid symbol:\t\tOK\x1b[0m"
else
	echo "\x1b[31minvalid symbol:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/invalid/2_initial_fact_lines.txt"
output=$(eval "$cmd")
desired="Error: Multiple lines of initial facts"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32m2 initial fact lines:\tOK\x1b[0m"
else
	echo "\x1b[31m2 initial fact lines:\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/invalid/2_query_lines.txt"
output=$(eval "$cmd")
desired="Error: Multiple lines of queries"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32m2 query lines:\t\tOK\x1b[0m"
else
	echo "\x1b[31m2 query lines:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/invalid/inital_fact_not_in_rules.txt"
output=$(eval "$cmd")
desired="Error: Inital fact not in rules"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32minital fact !in rules:\tOK\x1b[0m"
else
	echo "\x1b[31minital fact !in rules:\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/invalid/query_not_in_rules.txt"
output=$(eval "$cmd")
desired="Error: Query not in rules"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mquery !in rules:\tOK\x1b[0m"
else
	echo "\x1b[31mquery !in rules:\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/invalid/missing_symbol.txt"
output=$(eval "$cmd")
desired="Error: Bad Syntax, + missing symbol"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32m+ missing symbol:\tOK\x1b[0m"
else
	echo "\x1b[31m+ missing symbol:\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/invalid/combined_conditions_1.txt"
output=$(eval "$cmd")
desired="Error: Bad Syntax, combined conditions"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mcombined conditions_1:\tOK\x1b[0m"
else
	echo "\x1b[31mcombined conditions_1:\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/invalid/combined_conditions_2.txt"
output=$(eval "$cmd")
desired="Error: Bad Syntax, combined conditions"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mcombined conditions_2:\tOK\x1b[0m"
else
	echo "\x1b[31mcombined conditions_2:\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/invalid/combined_conditions_3.txt"
output=$(eval "$cmd")
desired="Error: Bad Syntax, combined conditions"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mcombined conditions_3:\tOK\x1b[0m"
else
	echo "\x1b[31mcombined conditions_3:\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/invalid/combined_conditions_4.txt"
output=$(eval "$cmd")
desired="Error: Bad Syntax, combined conditions"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mcombined conditions_4:\tOK\x1b[0m"
else
	echo "\x1b[31mcombined conditions_4:\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/invalid/combined_conditions_5.txt"
output=$(eval "$cmd")
desired="Error: Bad Syntax, combined conditions"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mcombined conditions_5:\tOK\x1b[0m"
else
	echo "\x1b[31mcombined conditions_5:\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/invalid/combined_conditions_6.txt"
output=$(eval "$cmd")
desired="Error: Bad Syntax, combined conditions"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mcombined conditions_6:\tOK\x1b[0m"
else
	echo "\x1b[31mcombined conditions_6:\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/invalid/combined_conditions_or.txt"
output=$(eval "$cmd")
desired="Error: Bad Syntax, 2 combined conditions"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mcombined conditions_or:\tOK\x1b[0m"
else
	echo "\x1b[31mcombined conditions_or:\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/invalid/non-alphabet.txt"
output=$(eval "$cmd")
desired="Error: Bad Syntax, non-alphabet symbol"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mnon-alphabet symbol:\tOK\x1b[0m"
else
	echo "\x1b[31mnon-alphabet symbol:\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/invalid/non-alphabet_or.txt"
output=$(eval "$cmd")
desired="Error: Bad Syntax, non-alphabet symbol with |"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mnon-alphabet symbol_or:\tOK\x1b[0m"
else
	echo "\x1b[31mnon-alphabet symbol_or:\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/invalid/contradiction.txt"
output=$(eval "$cmd")
desired="Error: Bad Logic, contradiction"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mcontradiction:\t\tOK\x1b[0m"
else
	echo "\x1b[31mcontradiction:\t\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/invalid/contradiction_2.txt"
output=$(eval "$cmd")
desired="Error: Bad Logic, contradiction"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32mcontradiction_2:\tOK\x1b[0m"
else
	echo "\x1b[31mcontradiction_2:\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/invalid/infinite_loop.txt"
output=$(eval "$cmd")
desired="Error: circular Logic, infinite loop"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32minfinite loop:\tOK\x1b[0m"
else
	echo "\x1b[31minfinite loop:\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

cmd="python3 expert_system.py input/invalid/infinite_loop_2.txt"
output=$(eval "$cmd")
desired="Error: circular Logic, infinite loop"
if [ "$output" == "$desired" ]
then
	((passed+=1))
	echo "\x1b[32minfinite loop:\tOK\x1b[0m"
else
	echo "\x1b[31minfinite loop:\tERROR\x1b[0m"
	echo "desired output: $desired"
	echo "actual output:  $output\n"
fi
((count+=1))

#### -- TOTAL -- ####
echo "\n\n\x1b[1mAll Expert System tests finished\x1b[0m"

if [ "$passed" == "$count" ]
then
	echo "\n\x1b[32mPassed $passed of $count total tests\x1b[0m\n"
else
	echo "\n\x1b[31mPassed $passed of $count total tests\x1b[0m\n"
fi