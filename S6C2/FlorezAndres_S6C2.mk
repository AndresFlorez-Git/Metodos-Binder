FlorezAndres_S6C2_plots.py: datos.dat FlorezAndres_S6C2.cpp
	python FlorezAndres_S6C2_plots.py
	rm datos.dat
datos.dat:
	g++ FlorezAndres_S6C2.cpp
	./a.out> datos.dat
    