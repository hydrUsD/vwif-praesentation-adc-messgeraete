"""Nachrechnung/Simulation aller Zahlen des DAC-Vortrags (Folien, Q&A, Lernmaterial)."""
import numpy as np, math
def r2r_vout(bits, uref=8.0, R=10e3, dev=None):
    """Spannungsmodus-R-2R per Knotenanalyse. bits: MSB zuerst. dev: dict 'name'->Faktor für Toleranzstudie.
    Struktur: Knoten k=0..n-1 (k=0 = MSB-Knoten = Ausgang). Jeder Knoten hat 2R zum Bit-Schalter,
    zwischen Knoten k und k+1 liegt R, am LSB-Knoten zusätzlich 2R-Abschluss nach Masse."""
    n=len(bits); dev=dev or {}
    G=np.zeros((n,n)); I=np.zeros(n)
    for k in range(n):
        g2=1/(2*R*dev.get(f'2R_{k}',1.0)); G[k,k]+=g2; I[k]+=g2*uref*bits[k]
        if k<n-1:
            g=1/(R*dev.get(f'R_{k}',1.0)); G[k,k]+=g; G[k+1,k+1]+=g; G[k,k+1]-=g; G[k+1,k]-=g
    G[n-1,n-1]+=1/(2*R*dev.get('2R_term',1.0))
    return np.linalg.solve(G,I)[0]
r={}
n=4; uref=8.0
r['LSB_4bit_8V']=uref/2**n
r['Code_1101']=int('1101',2); r['U_1101_formel']=13/16*uref
r['U_1101_sim']=r2r_vout([1,1,0,1])
r['Bitgewichte_V']=[uref/2**(i+1) for i in range(n)]
r['U_max_1111']=r2r_vout([1,1,1,1]); r['U_1000']=r2r_vout([1,0,0,0]); r['U_0001']=r2r_vout([0,0,0,1])
allok=all(abs(r2r_vout([int(b) for b in f'{c:04b}'])-c/16*uref)<1e-9 for c in range(16)); r['alle_16_Codes_ok']=allok
# Innenwiderstand R: Leerlauf vs Last 10R  (Folie: Puffer/OpAmp nötig)
R=10e3
r['Ri_Netzwerk_Ohm']=R
r['U_1101_an_Last_R']=r['U_1101_sim']*R/(R+R)
# Toleranz: MSB-2R 1 % zu klein -> Sprung 0111->1000
# 8-Bit-Fall Monotonie bei 2 % MSB-Fehler
def v8b(c,dev=None): return r2r_vout([int(b) for b in f'{c:08b}'],uref=2.56,dev=dev)
d8={'2R_0':1.02}
r['8bit_LSB_mV']=2.56/256*1e3
r['8bit_Sprung_127_128_mV_bei_MSB+2%']=(v8b(128,d8)-v8b(127,d8))*1e3
# Sinus-Tabelle 16 Punkte, 8 Bit
N=16; tab=[128+round(127*math.sin(2*math.pi*k/N)) for k in range(N)]
r['Sinus16_8bit']=tab
r['Cosinus=Sinus+4']=[tab[(k+4)%N] for k in range(N)]
cosdirekt=[128+round(127*math.cos(2*math.pi*k/N)) for k in range(N)]
r['Cos_check']=r['Cosinus=Sinus+4']==cosdirekt
r['Phasenversatz_Eintraege_90grad']=N//4
fs=16e3; r['f_out_bei_fs16k_kHz']=fs/N/1e3; r['Nyquist_max_kHz']=fs/2/1e3
# Audio
r['CD_Datenrate_Mbit_s']=44100*16*2/1e6
r['CD_Stufen']=2**16
r['CD_MB_pro_min']=44100*2*2*60/1e6
r['24bit_Stufen']=2**24
# ZOH-Abschwaechung bei fs/2: sinc(0.5)
r['ZOH_Daempfung_fs/2']=math.sin(math.pi*0.5)/(math.pi*0.5); r['ZOH_dB']=20*math.log10(r['ZOH_Daempfung_fs/2'])
# Gewichtetes Netzwerk 8 Bit: Verhältnis größter/kleinster Widerstand
r['gewichtet_8bit_Verhaeltnis']=2**7
# ESP32: 8 Bit, Vout=Vref*code/255
r['ESP32_Stufen']=256; r['ESP32_LSB_mV_3V3']=3.3/255*1e3
for k,v in r.items(): print(f'{k:36s} {v}')

# Übungsaufgaben Lernmaterial (andere Zahlen als auf den Folien)
u={}
u['U1_1010_8V']=r2r_vout([1,0,1,0]); u['U2_Code_fuer_3V']=3/(8/16)
u['U3_LSB_8bit_2.56V_mV']=2.56/256*1e3; u['U3b_Code200_V']=200*2.56/256
u['U4_max_10bit_5V']=1023/1024*5
u['U5_32Werte_48kHz_kHz']=48/32; u['U6_Takt_fuer_2kHz_kHz']=2*16
u['U7_cos_offset_32']=32//4; u['U8_max_f_48kHz']=48/2
u['U11_CD_Mbit']=44100*16*2/1e6; u['U10_R2R_8bit_Anzahl']=2*8
u['U9_Last_R_1010']=r2r_vout([1,0,1,0])/2
for k,v in u.items(): print(f'{k:36s} {v}')
