
default:
	echo
	python3 encode.py > encoded.py
	wc -cm emirp.py encoded.py
	python3 emirp.py > output.txt

	diff answer.txt output.txt
