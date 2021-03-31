#### -- Expert System Test -- ####
Reset="\x1b[0m"
Bright="\x1b[1m"
Red="\x1b[31m"
Green="\x1b[32m"
Clear_screen="\E[H\E[2J"

printf $Clear_screen
printf $Bright
echo "Launching Expert System tests... $Reset\n"

passed=0
count=0
SECONDS=0

#### -- Test Function -- ####
unit_test()
{
	## Initialize
	FILEPATH=$1
	TRUTH=$2
	Filename=$(echo $FILEPATH | cut -d "." -f 1 | rev | cut -d "/" -f 1 | rev)
	cmd="python expert_system.py $FILEPATH -c"

	## Time
	start=$(gdate +%s%N)
	output=$(eval "$cmd") ## Run
	end=$(gdate +%s%N)
	runtime=$( echo "scale=3; (($end - $start) / 1000000000)" | bc -l )

	## Print 
	if [ "$output" == "$TRUTH" ]
	then
		((passed+=1))
		printf "$Green%-25s %-6s %ss$Reset\n" $Filename "OK" $runtime
	else
		printf "$Red%-25s %-6s %ss$Reset\n" $Filename "ERROR" $runtime
		echo "Truth:  $TRUTH"
		echo "Output: $output\n"
	fi
	((count+=1))
}

#### -- AND -- ####
printf "$Bright%-25s %-6s %s$Reset\n" "And tests" "Pass" "Runtime"
unit_test input/correction/and_1.txt "A is True
F is True
K is True
P is True"
unit_test input/correction/and_2.txt "A is True
F is True
K is False
P is True"

#### -- MORE AND -- ####
echo
unit_test input/valid/and_3.txt "C is True
F is False"
unit_test input/valid/and_long.txt "Z is True"
unit_test input/valid/and_long_2.txt "A is False"
unit_test input/valid/and_long_3.txt "Y is True
Z is True"
unit_test input/valid/and_long_4.txt "Y is False
Z is False"
unit_test input/valid/and_conclusion.txt "C is True
D is True
U is True"
unit_test input/valid/and_comments.txt "C is True
D is True
F is True
I is True"
unit_test input/valid/initial_fact_not_in_rules.txt "A is True
F is True
K is True
P is True
Z is True"
unit_test input/valid/no_rules.txt "A is True
Z is True"

#### -- OR -- ####
echo $Bright 
echo "Or tests$Reset"
unit_test input/correction/or_1.txt "A is False"
unit_test input/correction/or_2.txt "A is True"
unit_test input/correction/or_3.txt "A is True"
unit_test input/correction/or_4.txt "A is True"

#### -- MORE OR -- ####
echo
unit_test input/valid/or_5.txt "C is True
F is True"
unit_test input/valid/or_long.txt "Z is True"
unit_test input/valid/or_long_2.txt "A is False"
unit_test input/valid/undetermined_or.txt "B is Undetermined
C is Undetermined"
unit_test input/valid/undetermined_or_2.txt "B is Undetermined
C is Undetermined
D is Undetermined"
unit_test input/valid/undetermined_or_3.txt "B is Undetermined
C is Undetermined
D is Undetermined
E is Undetermined"
unit_test input/valid/undetermined_or_4.txt "B is Undetermined
C is Undetermined
D is Undetermined"
unit_test input/valid/undetermined_or_5.txt "B is Undetermined
C is Undetermined
D is Undetermined
E is Undetermined"
unit_test input/valid/undetermined_long.txt "C is Undetermined
Z is Undetermined"

#### -- OR NOT -- ####
unit_test input/valid/or_not_1.txt "A is True"
unit_test input/valid/or_not_2.txt "A is False"
unit_test input/valid/or_not_3.txt "A is True"
unit_test input/valid/or_not_4.txt "A is True"
unit_test input/valid/or_not_5.txt "A is True"

#### -- OR PRECEDENCE-- ####
unit_test input/valid/or_precedence_1.txt "E is False"
unit_test input/valid/or_precedence_2.txt "E is True"
unit_test input/valid/or_precedence_3.txt "E is False"
unit_test input/valid/or_precedence_4.txt "E is False"
unit_test input/valid/or_precedence_5.txt "E is True"
unit_test input/valid/or_precedence_6.txt "E is True"

#### -- XOR -- ####
echo $Bright 
echo "Xor tests$Reset"
unit_test input/correction/xor_1.txt "A is False"
unit_test input/correction/xor_2.txt "A is True"
unit_test input/correction/xor_3.txt "A is True"
unit_test input/correction/xor_4.txt "A is False"

#### -- MORE XOR -- ####
echo
unit_test input/valid/xor_5.txt "C is False
F is True
I is True
L is False"
unit_test input/valid/xor_long.txt "Z is True"
unit_test input/valid/xor_long_2.txt "Z is False"
unit_test input/valid/xor_mix.txt "P is False
N is True
G is True
M is True
T is False
X is False"
unit_test input/valid/xor_mix_2.txt "C is True"
unit_test input/valid/undetermined_xor.txt "B is Undetermined
C is Undetermined"
unit_test input/valid/undetermined_xor_2.txt "B is Undetermined
C is Undetermined
D is Undetermined"
unit_test input/valid/undetermined_xor_3.txt "B is Undetermined
C is Undetermined
D is Undetermined
E is Undetermined"
unit_test input/valid/undetermined_xor_4.txt "B is Undetermined
C is Undetermined
D is Undetermined
E is Undetermined"
unit_test input/valid/undetermined_xor_5.txt "B is Undetermined
C is Undetermined
D is Undetermined
E is Undetermined"
unit_test input/valid/undetermined_xlong.txt "C is Undetermined
Z is Undetermined"

#### -- XOR NOT -- ####
unit_test input/valid/xor_not_1.txt "A is True"
unit_test input/valid/xor_not_2.txt "A is False"
unit_test input/valid/xor_not_3.txt "A is False"
unit_test input/valid/xor_not_4.txt "A is True"
unit_test input/valid/xor_not_5.txt "A is False"
unit_test input/valid/xor_not_6.txt "A is False"
unit_test input/valid/xor_not_7.txt "A is True"

#### -- XOR PRECEDENCE-- ####

unit_test input/valid/xor_precedence_1.txt "E is False"
unit_test input/valid/xor_precedence_2.txt "E is True"
unit_test input/valid/xor_precedence_3.txt "E is False"
unit_test input/valid/xor_precedence_4.txt "E is False"
unit_test input/valid/xor_precedence_5.txt "E is True"
unit_test input/valid/xor_precedence_6.txt "E is True"

#### -- NOT -- ####
echo $Bright 
echo "Not tests$Reset"
unit_test input/correction/not_1.txt "A is False"
unit_test input/correction/not_2.txt "A is True"
unit_test input/correction/not_3.txt "A is False"
unit_test input/correction/not_4.txt "A is False"

#### --	MORE NOT -- ####
echo
unit_test input/valid/not_5.txt "B is False
D is True"

#### -- SAME CONCLUSION -- ####
echo $Bright 
echo "Same conclusion tests$Reset"
unit_test input/correction/same_conclusion_1.txt "A is False"
unit_test input/correction/same_conclusion_2.txt "A is True"
unit_test input/correction/same_conclusion_3.txt "A is True"
unit_test input/correction/same_conclusion_4.txt "A is True"
#### -- PARENTHESIS -- ####
echo $Bright 
echo "Parenthesis tests$Reset"

unit_test input/correction/parenthesis_1.txt "E is False"
unit_test input/correction/parenthesis_2.txt "E is True"
unit_test input/correction/parenthesis_3.txt "E is False"
unit_test input/correction/parenthesis_4.txt "E is False"
unit_test input/correction/parenthesis_5.txt "E is True"
unit_test input/correction/parenthesis_6.txt "E is True"
unit_test input/correction/parenthesis_7.txt "E is False"
unit_test input/correction/parenthesis_8.txt "E is False"
unit_test input/correction/parenthesis_9.txt "E is False"
unit_test input/correction/parenthesis_10.txt "E is True"
unit_test input/correction/parenthesis_11.txt "E is True"

#### -- MORE PARENTHESIS -- ####
echo
unit_test input/valid/parenthesis_double.txt "D is True
E is False"
unit_test input/valid/parenthesis_double_2.txt "D is True
E is False"
unit_test input/valid/parenthesis_double_3.txt "D is True
E is False"
unit_test input/valid/parenthesis_double_4.txt "D is True
E is False"
unit_test input/valid/parenthesis_double_5.txt "D is True
E is False"
unit_test input/valid/parenthesis_double_6.txt "D is True
E is False"
unit_test input/valid/parenthesis_double_7.txt "D is True
E is False"
unit_test input/valid/parenthesis_double_8.txt "D is True
E is False"
unit_test input/valid/parenthesis_double_9.txt "D is True
E is True"
unit_test input/valid/parenthesis_triple.txt "D is True
E is False"
unit_test input/valid/parenthesis_triple_2.txt "D is True
E is True"
unit_test input/valid/parenthesis_triple_3.txt "D is True
E is True"
unit_test input/valid/parenthesis_triple_4.txt "D is True
E is True"
unit_test input/valid/parenthesis_quad.txt "D is True
E is False"
unit_test input/valid/parenthesis_quad_2.txt "D is True
E is True"
unit_test input/valid/parenthesis_mix.txt "C is True
D is False
W is False
G is True
F is True
Z is True"

#### -- ERROR -- ####
echo $Bright 
echo "Error tests$Reset"
unit_test input/invalid/bullshit_filepath "Error: Invalid filepath"
unit_test input/invalid/bullshit_folder.txt/ "Error: Invalid filepath"
unit_test input/invalid/invalid_symbol.txt "Error: Invalid symbol in file"
unit_test /dev/random "Error: Invalid filepath"
unit_test /dev/null "Error: Invalid filepath"
unit_test input/symbolic_link "Error: Invalid filepath"

touch input/no_permissions.txt
chmod 000 input/no_permissions.txt
unit_test input/no_permissions.txt "Error: file has no read permissions"
chmod 755 input/no_permissions.txt
rm input/no_permissions.txt

unit_test input/invalid/2_initial_fact_lines.txt "Error: Multiple lines of initial facts"
unit_test input/invalid/2_initial_fact_lines_2.txt "Error: Multiple lines of initial facts"
unit_test input/invalid/2_initial_fact_lines_3.txt "Error: Rule given after initial facts"
unit_test input/invalid/2_query_lines.txt "Error: Multiple lines of queries"
unit_test input/invalid/query_not_in_rules.txt "Error: Query not in rules"
unit_test input/invalid/missing_symbol.txt "Error: Bad Syntax, + missing symbol in conclusion"

#### -- ERROR: Combined conditions -- ####
unit_test input/invalid/combined_conditions_1.txt "Error: Bad Syntax, combined conditions"
unit_test input/invalid/combined_conditions_2.txt "Error: Bad Syntax, combined conditions"
unit_test input/invalid/combined_conditions_3.txt "Error: Bad Syntax, combined conditions"
unit_test input/invalid/combined_conditions_4.txt "Error: Bad Syntax, combined conditions"
unit_test input/invalid/combined_conditions_5.txt "Error: Bad Syntax, combined conditions"
unit_test input/invalid/combined_conditions_6.txt "Error: Bad Syntax, combined conditions"
unit_test input/invalid/combined_conditions_7.txt "Error: Bad Syntax, too many combined conditions"
unit_test input/invalid/combined_conditions_8.txt "Error: Bad Syntax, many combined conditions"
unit_test input/invalid/combined_conditions_or.txt "Error: Bad Syntax, 2 combined conditions"

#### -- ERROR: Rules -- ####
unit_test input/invalid/bad_rule_1.txt "Error: Bad Syntax, combined conditions"
unit_test input/invalid/bad_rule_2.txt "Error: Bad Syntax, combined conditions"
unit_test input/invalid/bad_rule_3.txt "Error: Non-alphabet character in initial facts"
unit_test input/invalid/bad_rule_4.txt "Error: Non-alphabet character in initial facts"

#### -- ERROR: And -- ####
unit_test input/invalid/bad_and_1.txt "Error: Bad Syntax, + missing symbol"
unit_test input/invalid/bad_and_2.txt "Error: Bad Syntax, + missing symbol"
unit_test input/invalid/bad_and_3.txt "Error: Bad Syntax, + missing symbol"

#### -- ERROR: Or -- ####
unit_test input/invalid/bad_or_1.txt "Error: Bad Syntax, | missing symbol"
unit_test input/invalid/bad_or_2.txt "Error: Bad Syntax, | missing symbol"
unit_test input/invalid/bad_or_3.txt "Error: Bad Syntax, | missing symbol"
unit_test input/invalid/bad_or_4.txt "Error: Bad Syntax, combined conditions"

#### -- ERROR: Xor -- ####
unit_test input/invalid/bad_xor_1.txt "Error: Bad Syntax, ^ missing symbol"
unit_test input/invalid/bad_xor_2.txt "Error: Bad Syntax, ^ missing symbol"
unit_test input/invalid/bad_xor_3.txt "Error: Bad Syntax, ^ missing symbol"

#### -- ERROR: Not -- ####
unit_test input/invalid/bad_not_1.txt "Error: Bad Syntax, too many combined conditions"
unit_test input/invalid/bad_not_2.txt "Error: Bad Syntax, too many combined conditions"
unit_test input/invalid/bad_not_3.txt "Error: Bad Syntax, too many combined conditions"

#### -- ERROR: Non-alphabet -- ####
unit_test input/invalid/non-alphabet.txt "Error: Bad Syntax, non-alphabet symbol"
unit_test input/invalid/non-alphabet_or.txt "Error: Bad Syntax, non-alphabet symbol with |"

#### -- ERROR: Initial facts -- ####
unit_test input/invalid/bad_initial_facts1.txt "Error: Non-alphabet character in initial facts"
unit_test input/invalid/bad_initial_facts2.txt "Error: Bad Syntax, missing =>"
unit_test input/invalid/bad_initial_facts3.txt "Error: Invalid symbol in file"
unit_test input/invalid/bad_initial_facts4.txt "Error: Invalid symbol in file"

#### -- ERROR: Queries -- ####
unit_test input/invalid/bad_query1.txt "Error: Non-alphabet character in query"
unit_test input/invalid/bad_query2.txt "Error: Non-alphabet character in query"
unit_test input/invalid/bad_query3.txt "Error: Invalid symbol in file"

#### -- ERROR: Implies -- ####
unit_test input/invalid/bad_implies1.txt "Error: Bad Syntax, missing =>"
unit_test input/invalid/bad_implies2.txt "Error: Bad Syntax, missing =>"
unit_test input/invalid/bad_implies3.txt "Error: Bad Syntax, missing =>"
unit_test input/invalid/bad_implies4.txt "Error: Bad Syntax, parenthesis unbalanced"
unit_test input/invalid/2_implies.txt "Error: Bad Syntax, two implies in one rule"
unit_test input/invalid/2_implies_2.txt "Error: Bad Syntax, two implies in one rule"
unit_test input/invalid/2_implies_3.txt "Error: Bad Syntax, two implies in one rule"

#### -- ERROR: Conclusion -- ####
unit_test input/invalid/bad_conclusion1.txt "Error: Bad Syntax, + missing symbol in conclusion"
unit_test input/invalid/bad_conclusion2.txt "Error: Bad Syntax, + missing symbol in conclusion"
unit_test input/invalid/bad_conclusion3.txt "Error: Bad Syntax, parenthesis in conclusion"
unit_test input/invalid/bad_conclusion4.txt "Error: Bad Syntax, parenthesis in conclusion"
unit_test input/invalid/bad_conclusion5.txt "Error: Bad Syntax, parenthesis in conclusion"
unit_test input/invalid/bad_conclusion6.txt "Error: Bad Syntax, parenthesis in conclusion"
unit_test input/invalid/bad_conclusion7.txt "Error: Bad Syntax, + missing symbol in conclusion"
unit_test input/invalid/bad_conclusion8.txt "Error: Bad Syntax, + missing symbol in conclusion"
unit_test input/invalid/bad_conclusion9.txt "Error: Bad Syntax, combined conditions"
unit_test input/invalid/bad_conclusion10.txt "Error: Bad Syntax, | missing symbol"
unit_test input/invalid/bad_conclusion11.txt "Error: Bad Syntax, ^ missing symbol"
unit_test input/invalid/bad_conclusion12.txt "Error: Bad Syntax, parenthesis in conclusion"
unit_test input/invalid/bad_conclusion13.txt "Error: Bad Syntax, parenthesis in conclusion"
unit_test input/invalid/bad_conclusion14.txt "Error: Bad Syntax, parenthesis in conclusion"
unit_test input/invalid/bad_conclusion15.txt "Error: Bad Syntax, parenthesis in conclusion"
unit_test input/invalid/bad_conclusion16.txt "Error: Bad Syntax, parenthesis in conclusion"
unit_test input/invalid/bad_conclusion17.txt "Error: Bad Syntax, parenthesis in conclusion"
unit_test input/invalid/bad_conclusion18.txt "Error: Bad Syntax, parenthesis in conclusion"
unit_test input/invalid/bad_conclusion19.txt "Error: Bad Syntax, + missing symbol in conclusion"
unit_test input/invalid/bad_conclusion20.txt "Error: Bad Syntax, + missing symbol in conclusion"
unit_test input/invalid/bad_conclusion21.txt "Error: Bad Syntax, parenthesis in conclusion"
unit_test input/invalid/bad_conclusion22.txt "Error: Bad Syntax, parenthesis in conclusion"
unit_test input/invalid/bad_conclusion23.txt "Error: Bad Syntax, parenthesis in conclusion"

#### -- ERROR: Empty -- ####
unit_test input/invalid/empty.txt "Error: No initial facts"
unit_test input/invalid/empty_facts.txt "Error: Queries given before initial facts"
unit_test input/invalid/empty_facts_2.txt "Error: Queries given before initial facts"
unit_test input/invalid/empty_query.txt "Error: No queries"
unit_test input/invalid/empty_rules.txt "Error: No queries"

#### -- ERROR: max line -- ####
unit_test input/invalid/max_line.txt "Error: Rule too long"
unit_test input/invalid/max_line_2.txt "Error: Initial facts too long"
unit_test input/invalid/max_line_3.txt "Error: Queries too long"
unit_test input/invalid/max_lines.txt "Error: File too long"
unit_test input/invalid/random_alphabet.txt "Error: Bad Syntax, missing =>"

#### -- ERROR: Binary -- ####
unit_test input/invalid/random_binary0.txt "Error: Invalid symbol in file"
unit_test input/invalid/random_binary1.txt "Error: Invalid symbol in file"
unit_test input/invalid/random_binary2.txt "Error: Invalid symbol in file"
unit_test input/invalid/random_binary3.txt "Error: Invalid symbol in file"
unit_test input/invalid/random_binary4.txt "Error: Invalid symbol in file"
unit_test input/invalid/random_binary5.txt "Error: Invalid symbol in file"

#### -- ERROR: Parenthesis -- ####
unit_test input/invalid/parenthesis_balance.txt "Error: Bad Syntax, parenthesis unbalanced"
unit_test input/invalid/parenthesis_balance_2.txt "Error: Bad Syntax, parenthesis unbalanced"
unit_test input/invalid/parenthesis_balance_3.txt "Error: Bad Syntax, parenthesis unbalanced"
unit_test input/invalid/parenthesis_balance_4.txt "Error: Bad Syntax, parenthesis unbalanced"
unit_test input/invalid/parenthesis_balance_5.txt "Error: Bad Syntax, parenthesis unbalanced"
unit_test input/invalid/parenthesis_balance_6.txt "Error: Bad Syntax, parenthesis unbalanced"
unit_test input/invalid/parenthesis_balance_7.txt "Error: Bad Syntax, parenthesis"
unit_test input/invalid/parenthesis_balance_8.txt "Error: Bad Syntax, parenthesis"
unit_test input/invalid/parenthesis_balance_9.txt "Error: Bad Syntax, parenthesis"
unit_test input/invalid/parenthesis_empty.txt "Error: Bad Syntax, parenthesis empty ()"

#### -- ERROR: More parenthesis -- ####
unit_test input/invalid/bad_parenthesis_1.txt "Error: Bad Syntax, parenthesis with non-alphabet symbol"
unit_test input/invalid/bad_parenthesis_2.txt "Error: Bad Syntax, parenthesis empty ()"
unit_test input/invalid/bad_parenthesis_3.txt "Error: Bad Syntax, parenthesis with non-alphabet symbol"
unit_test input/invalid/bad_parenthesis_4.txt "Error: Bad Syntax, parenthesis with non-alphabet symbol"
unit_test input/invalid/bad_parenthesis_5.txt "Error: Bad Syntax, parenthesis with non-alphabet symbol"
unit_test input/invalid/bad_parenthesis_6.txt "Error: Bad Syntax, parenthesis empty ()"
unit_test input/invalid/bad_parenthesis_7.txt "Error: Bad Syntax, parenthesis unbalanced"
unit_test input/invalid/bad_parenthesis_8.txt "Error: Bad Syntax, parenthesis unbalanced"
unit_test input/invalid/bad_parenthesis_9.txt "Error: Bad Syntax, parenthesis unbalanced"
unit_test input/invalid/bad_parenthesis_10.txt "Error: Bad Syntax, parenthesis unbalanced"
unit_test input/invalid/bad_parenthesis_11.txt "Error: Bad Syntax, parenthesis unbalanced"
unit_test input/invalid/bad_parenthesis_12.txt "Error: Bad Syntax, parenthesis unbalanced"
unit_test input/invalid/bad_parenthesis_13.txt "Error: Bad Syntax, parenthesis with non-alphabet symbol"

#### -- ERROR: Contradiction -- ####
unit_test input/invalid/contradiction.txt "Error: Bad Logic, contradiction"
unit_test input/invalid/contradiction_2.txt "Error: Bad Logic, infinite loop"
unit_test input/invalid/contradiction_3.txt "Error: Bad Logic, contradiction"
unit_test input/invalid/contradiction_4.txt "Error: circular Logic, infinite loop"
unit_test input/invalid/contradiction_5.txt "Error: circular Logic, infinite loop"

unit_test input/invalid/contradiction_6.txt "Error: Bad Logic, contradiction"
unit_test input/invalid/contradiction_7.txt "Error: Bad Logic, contradiction"
unit_test input/invalid/contradiction_8.txt "Error: Bad Logic, contradiction"
unit_test input/invalid/contradiction_long.txt "Error: circular Logic, infinite loop"
unit_test input/invalid/infinite_loop.txt "Error: circular Logic, infinite loop"
unit_test input/invalid/infinite_loop_2.txt "Error: circular Logic, infinite loop"
unit_test input/invalid/infinite_loop_3.txt "Error: circular Logic, infinite loop"


#### -- TOTAL -- ####
echo
echo $Bright
echo "All Expert System tests finished\nTotal runtime $SECONDS seconds$Reset"

if [ "$passed" == "$count" ]
then
	echo "\n\x1b[32mPassed $passed of $count total tests$Reset\n"
elif [ "$passed" == "0" ]
then
	echo "\n\x1b[31mPassed $passed of $count total tests$Reset\n"	
else
	echo "\n\x1b[33mPassed $passed of $count total tests$Reset\n"
fi
