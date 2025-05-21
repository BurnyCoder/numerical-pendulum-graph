Web VPython 3.2

g1 = graph(title="Pendulum",xtitle="t [s]",ytitle="theta [deg]",
width=400, height=200)
f1 = gcurve(color=color.blue,dot=True)
f2 = gcurve(color=color.red,dot=True)

t = 0
dt = 0.01
L = 0.3
g = 9.8
theta = 10*pi/180
thetadot  = 0
w = sqrt(g/L)
A = 10

while t<4:
  rate(100)
  thetaddot = -g*sin(theta)/L
  thetadot = thetadot + thetaddot*dt
  theta = theta + thetadot*dt
  t = t + dt
  ttheta = A*cos(w*t)
  f1.plot(t,theta*180/pi)
  f2.plot(t,ttheta)
