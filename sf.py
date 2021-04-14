APIKEY='API_KEY'

A0='black'
z='2009-01-01'
y='sf1y'
x='flow1y'
w='flow'
v=dict
u=range
g='center'
f='log'
e='ds_bfr_hlvng'
d='Date'
c=None
b='2010-09-01'
R='#fff3ea'
K='sf'
I='cap'
H='Value'
G='%Y-%m-%d'
import quandl as S,numpy as T,pandas as h,matplotlib as U
from datetime import datetime as J,timedelta as i,date as F
import matplotlib.pyplot as A
from matplotlib.pyplot import figure as j
def N(df):A=df;B=A[A.sum(axis=1)==0].index;A=A.drop(B);return A
def O(quandl_id):S.ApiConfig.api_key=APIKEY;A=S.get(quandl_id,returns='pandas');A=N(A);return A
def V(d1,d2):d1=J.strptime(d1,G);d2=J.strptime(d2,G);return abs((d2-d1).days)
def k(b):
	if b>=33*210000:return 20999999.9769
	else:
		A=5000000000.0;B=0;C=210000
		while b>C-1:B=B+C*A;A=int(A/2.0);b=b-C
		B=B+b*A;return(B+A)/100000000.0,A/100000000.0
B=O('BCHAIN/TOTBC')[b:]
l=O('BCHAIN/MKTCP')[b:]
A1=O('BCHARTS/KRAKENUSD')[b:]
A.style.use('seaborn')
U.rcParams['font.family']='serif'
j(num=c,figsize=(16,16),dpi=200)
B[w]=B[H].diff(periods=14)
B[x]=B[H].diff(periods=365)
B=N(B)
B[K]=B[H]/B[w]
B[y]=B[H]/B[x]
B[I]=l[H]
L,m=A.subplots()
P=[z,'2012-11-28','2016-07-09','2020-05-11','2024-05-01','2028-05-01','2032-05-01']
E=h.DataFrame(columns=[d,e,K,I])
for W in u(1,len(P)):
	F=P[W]
	for (M,X) in B[:F].iterrows():
		if M<J.strptime(F,G)and M>J.strptime(P[W-1],G):n=V(str(M.date()),F);E=E.append({d:M.strftime(G),e:n,K:X[K],I:X[I]},ignore_index=True)
E=N(E)
L=A.figure(num=c,figsize=(16,16),dpi=200)
C=18
D=A.gca()
D.tick_params(labelsize=C)
o=D.scatter(E[K],E[I],c=E[e],alpha=0.9,cmap='gist_rainbow',s=15,zorder=1)
D.plot(E[K],E[I],c='#474747',alpha=0.6,zorder=2,linewidth=0.2)
D.set_title('Stock-to-Flow & Market Value',fontsize=C)
D.set_xlabel('log(Stock-to-Flow)',fontsize=C)
D.set_ylabel('log(Market Value)',fontsize=C)
D.set_yscale(f)
D.set_xscale(f)
A2=U.ticker.MaxNLocator(nbins=6)
Q=A.colorbar(o)
Q.ax.get_yaxis().labelpad=15
Q.ax.tick_params(labelsize=C)
Q.ax.set_ylabel('Days before halving',fontsize=C)
D.text(0.1,0.95,'$SF = \\frac{S}{F_p}$\np = 14d',ha=g,va=g,style='italic',fontsize=C,transform=D.transAxes,bbox=v(facecolor='none',edgecolor=A0,pad=10.0))
L.tight_layout()
A.savefig('BTC-SF-MV-2.png',facecolor=R,edgecolor=R)
A.savefig('BTC-SF-MV.png')
A.show()
A.clf()
Y=[]
Z=[]
p=z
q=J.strptime('2011-09-01',G)
for F in (q+i(A)for A in u(9000)):r=V(p,F.strftime(G))*24*6;a,s=k(r);Y.append(F);t=a/(365*24*6*s);Z.append(T.exp(12.7598)*t**4.1167/a)
L=A.figure(num=c,figsize=(16,16),dpi=200)
A.title('Stock-to-flow Estimated & Real Price',fontsize=C)
A.xlabel(d,fontsize=C)
A.ylabel('ln(Price, USD)',fontsize=C)
A.yscale(f)
A.plot(B.index,B[I]/B[H],color='royalblue',label='BTCUSD')
A.plot(B.index,T.exp(12.7598)*B[y]**4.1167/B[H],color='red',label='Expected price based on real stock and flow')
A.plot(Y,Z,color='cornflowerblue',label='Expected price based on calculated stock and flow')
D.text(0.5,0.5,'Stock-to-Flow',horizontalalignment='right',verticalalignment=g,transform=m.transAxes,fontsize=20,bbox=v(facecolor='#e1e1e1',alpha=0.4,edgecolor=A0,pad=10.0))
A.legend(fontsize=C)
A.tick_params(labelsize=C)
A.grid(True,which='both')
L.tight_layout()
A.savefig('BTC-SF-Exp_Price-Price-2.png',facecolor=R,edgecolor=R)
A.savefig('BTC-SF-Exp_Price-Price.png')
A.show()
