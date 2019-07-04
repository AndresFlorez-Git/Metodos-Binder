plotDatos.py: datos.dat FlorezAndresS5C2.cpp
	python plotDatos.py
	rm datos.dat

datos.dat:
	g++ FlorezAndresS5C2.cpp
	./a.out > datos.dat