# BPX_code_test
Exercise 1: Created by Colton Anderson

Brief Methodology Explanation:
------------------------------
- I implemented a recursive algorithm that finds max "place descriptor" (e.g. thousands) and recursively calls generate_words on the number at that descriptor, and then remainder below that descriptor. 
	- ex: 1234
		- first iteration call 1234
		- next begin building string with generate_words(1) + " thousand " + generate_words(234)
		- next interation "one" (returned from ^ in recursion tree) + " thousand " + generate_words(2) + " hundred " + generate_words(34) (+ etc ...)


Files and Interactions:
-----------------------
- ex_1.py: 
	- file that contains "generate_words" method that will generate the word representations of numerical value
	- can be executed in multiple ways:
		python3 ex_1.py 
		- will execute main and prompt user for a number or "test" to run the unittests

		python3 ex_1.py [ARG]
		- [ARG] can be a number or "test" to run unittests

- test_ex_1.py:
	- file contains TestEx1 unittest class
	- is called from main of ex_1.py
	- runs simple edge case tests, as well as 20 psuedo-random number generated tests
	- simple tests assertEquals, random tests require validation

- Dockerfile
	- containerized docker file that will run ex_1.py main method
	- build (in directoy with src code from repo):
		docker build -t python-ca-bpx .
	- run (in interactive mode (i), without it, EOFerror will be raised)
		docker run -ti python-ca-bpx

