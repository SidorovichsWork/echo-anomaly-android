"""Rebuild Echo's own audio. Development only; NOT needed to install the mod.

Requires numpy and soundfile. Creates short rising/falling electronic chirps
without sampling Bullet Time Enhanced or any other game/mod audio.
"""
from pathlib import Path
import numpy as np
import soundfile as sf

def main():
    out=Path(__file__).resolve().parents[1]/'payload/echo/gamedata/sounds/echo'
    out.mkdir(parents=True,exist_ok=True)
    rate=44100;duration=0.42;t=np.arange(int(rate*duration))/rate
    for name,start,end in [('slowmo_on',280,940),('slowmo_off',940,240)]:
        phase=2*np.pi*(start*t+(end-start)*t*t/(2*duration))
        signal=(np.sin(phase)+0.2*np.sin(phase*2))*np.sin(np.pi*t/duration)**2*0.22
        sf.write(out/(name+'.ogg'),signal,rate,format='OGG',subtype='VORBIS')
if __name__=='__main__':main()
