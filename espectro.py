import sys
sys.path.insert(1, 'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate

import thinkplot

frecuencia1 =  SinSignal(freq= 1588 , amp =0.3, offset=0)
frecuencia2 =  SinSignal(freq= 380 , amp =0.6, offset=0)
frecuencia3 =  SinSignal(freq= 5300 , amp =1.0, offset=0)
frecuencia4 =  SinSignal(freq= 12300 , amp =0.1, offset=0)

resultante1 = frecuencia1 + frecuencia2
resultante2 = frecuencia3 + frecuencia4

waveResultante1 = resultante1.make_wave(duration=1,start=0,framerate=44100)
waveResultante2 = resultante2.make_wave(duration=6,start=1.3,framerate=44100)

waveFinal = waveResultante1 + waveResultante2

waveFinal.plot()
decorate(xlabel="Tiempo (s)")
thinkplot.show()

espectro = waveFinal.make_spectrum()
espectro.plot()
decorate(xlabel="Frecuencia(Hz)")
thinkplot.show()

