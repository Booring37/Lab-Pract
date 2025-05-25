%impulse, step ,ramp
t=(-10:10);
range = 5
impulse = t==0;
unitstep = t>=0;
ramp = t
rectangle = t<range & t>-range

subplot(2,4,1)
plot(t,impulse)
title('Impulse')
xlabel('Time')
ylabel('Amp')

subplot(2,4,2)
plot(t,unitstep)
title('Unitstep')
xlabel('Time')
ylabel('Amp')

subplot(2,4,5)
stem(t,impulse)
title('Impulse')
xlabel('Number')
ylabel('Amp')

subplot(2,4,6)
stem(t,unitstep)
title('Unitstep')
xlabel('Number')
ylabel('Amp')

subplot(2,4,3)
plot(t,ramp)
title('Ramp')
xlabel('Time')
ylabel('Amp')

subplot(2,4,7)
stem(t,ramp)
title('Ramp')
xlabel('Number')
ylabel('Amp')


subplot(2,4,4)
plot(t,rectangle)
title('Rectangle')
xlabel('Time')
ylabel('Amp')

subplot(2,4,8)
stem(t,rectangle)
title('Rectangle')
xlabel('Number')
ylabel('Amp')

%figure()
%hold on:
%plot(a,c)