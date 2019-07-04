plotsS5C1.py: data.dat S5C1Deriv.cpp
	python plotsS5C1.py
    
data.dat:
	g++ S5C1Deriv.cpp
	./a.out >data.dat