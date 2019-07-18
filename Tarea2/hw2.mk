Resultados_hw2.tex: Fourier.py FFT2D.png ODEs.cpp Plots_hw2.py Posicion_Orbital.png Velocidad_Orbital.png Momentum_Angular.png Energia_Euler.png Energia_LeapFrog.png Energia_RK.png Euler1.dat Euler2.dat Euler3.dat LeapFrog1.dat LeapFrog2.dat LeapFrog3.dat RK1.dat RK2.dat RK3.dat
	pdflatex Resultados_hw2.tex

FFT2D.png: Fourier.py
	python Fourier.py

Posicion_Orbital.png Velocidad_Orbital.png Momentum_Angular.png Energia_Euler.png Energia_LeapFrog.png Energia_RK.png: Plots_hw2.py ODEs.cpp Euler1.dat Euler2.dat Euler3.dat LeapFrog1.dat LeapFrog2.dat LeapFrog3.dat RK1.dat RK2.dat RK3.dat
	python Plots_hw2.py

Plots_hw2.py: ODEs.cpp Euler1.dat Euler2.dat Euler3.dat LeapFrog1.dat LeapFrog2.dat LeapFrog3.dat RK1.dat RK2.dat RK3.dat
	python Plots_hw2.py

Euler1.dat Euler2.dat Euler3.dat LeapFrog1.dat LeapFrog2.dat LeapFrog3.dat RK1.dat RK2.dat RK3.dat: ODEs.cpp
	g++ ODEs.cpp
	./a.out
    
