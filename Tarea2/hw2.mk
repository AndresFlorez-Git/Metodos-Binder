Resultados_hw2.pdf: Resultados_hw2.tex FFT2D.png Posicion_Orbital.png Velocidad_Orbital.png Momentum_Angular.png Energia_Euler.png Energia_LeapFrog.png Energia_RK.png 
	pdflatex Resultados_hw2.tex

FFT2D.png: Fourier.py
	python Fourier.py

Posicion_Orbital.png Velocidad_Orbital.png Momentum_Angular.png Energia_Euler.png Energia_LeapFrog.png Energia_RK.png: Plots_hw2.py Euler1.dat Euler2.dat Euler3.dat LeapFrog1.dat LeapFrog2.dat LeapFrog3.dat RK1.dat RK2.dat RK3.dat
	python Plots_hw2.py

Euler1.dat Euler2.dat Euler3.dat LeapFrog1.dat LeapFrog2.dat LeapFrog3.dat RK1.dat RK2.dat RK3.dat: a.out
	./a.out
    
a.out: ODEs.cpp
	g++ ODEs.cpp