"""Empirische Nachrechnung der Rechenwerte in lernen/07–10 und im Messwert-Trainer (Übungen R1–R13, Präsentationszahlen P1–P3/Stichwortkarte, Rückfragen-Extras).
Toleranzen der App-Eingabe werden separat in check_app_tolerances() geprüft."""
import math
par=lambda a,b:a*b/(a+b)
def sar(uin,uref,n):
    code=0;steps=[]
    for b in range(n-1,-1,-1):
        trial=code|(1<<b); v=trial*uref/2**n
        ok=v<=uin; steps.append((b,round(v,4),ok))
        if ok: code=trial
    return code,steps
r={}
r['R1_U2']=12*par(100e3,10e6)/(100e3+par(100e3,10e6))
r['R1_err%']=(r['R1_U2']/6-1)*100
r['R2_I_mA']=3/10.5*1e3; r['R2_err%']=(3/10.5/0.3-1)*100; r['R2_burden_V']=3/10.5*0.5
r['R3_Rv_kOhm']=(30/(50e-6*2e3)-1)*2   # n=300
n4=1e-3/50e-6; r['R4_n']=n4; r['R4_RN_Ohm']=2000/(n4-1); r['R4_falsch_Ri_durch_n']=2000/n4
r['R4_Probe_mA']=(50e-6+0.1/r['R4_RN_Ohm'])*1e3
r['R5_LSB_mV']=3.3/4096*1e3; r['R5_code']=math.floor(1.65*4096/3.3); r['R5_halfLSB_mV']=r['R5_LSB_mV']/2
r['R6_U']=820*5/1024; r['R6_code3.3']=math.floor(3.3*1024/5)
r['R7_Uadc']=12*10/25; r['R7_code']=math.floor(4.8*1024/5); r['R7_back']=r['R7_code']*5/1024*25/10
r['R8_alias']=10-7
r['R9a']=sar(6.7,16,4); r['R9b']=sar(1.003,2.56,8)
r['R10']=(5-0.025-0.003, 5+0.025+0.003)
r['R12']=(2**6-1,2**10-1); r['R13_SNR']=6.02*12+1.76
r['Q_shunt_mOhm']=0.1/10*1e3; r['Q_shunt_P']=10**2*0.01
r['Q_bits_2000counts']=math.log2(2000); r['Q_formfaktor']=(1/math.sqrt(2))/(2/math.pi)
for k,v in r.items(): print(k, v)

# Präsentationszahlen (Folien 4, 5, 10, 11, 13, 14)
p={}
p['P1_DMM_4.76V']=10*par(1e6,10e6)/(1e6+par(1e6,10e6))
p['Zeiger_1.43V']=10*par(1e6,200e3)/(1e6+par(1e6,200e3))
p['Amp_192mA']=5/(25+1)*1e3
p['P2_LSB_mV']=5/1024*1e3; p['Code_2.5V']=math.floor(2.5*1024/5)
p['P3_alias_kHz']=15-10; p['SAR_11.3V']=sar(11.3,16,4)[0]
p['Tol_100V']=(100-1-0.2,100+1+0.2); p['F2_Ref1pct_mV']=5*0.01*1e3
p['N13_R9a_Fehler_LSB']=6.7-6
for k,v in p.items(): print(f"{k:24s} {v}")

def check_app_tolerances(path):
    """Jede numerische App-Aufgabe: Sollwert liegt im Toleranzband der nachgerechneten Lösung; typische Fehlrechnungen fallen heraus."""
    import re
    h=open(path,encoding='utf8').read()
    tasks=re.findall(r'\{id:"(\w+)"[^\n]*?ans:([\d.]+),tol:([\d.]+)',h)
    for tid,a,t in tasks: print(f"APP {tid:5s} ans={a:8s} tol=±{t}")
    d={x[0]:(float(x[1]),float(x[2])) for x in tasks}
    assert abs(d['R4'][0]-r['R4_RN_Ohm'])<=d['R4'][1] and abs(100-d['R4'][0])>d['R4'][1], 'R4: Fehlformel Ri/n darf nicht akzeptiert werden'
    assert abs(d['P2'][0]-4.9)<=d['P2'][1] and abs(d['R5'][0]-0.81)<=d['R5'][1] and abs(d['R2'][0]-285)<=d['R2'][1]
    print('APP-Toleranzen OK')
import sys
if len(sys.argv)>1: check_app_tolerances(sys.argv[1])
