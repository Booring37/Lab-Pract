t = -50:0.01:50;
x = sawtooth(t,0.5);



subplot(3,1,1);
plot(t,x);
title('Plot of sawtooth');
xlabel('t');
ylabel('X');
xlim([-10, 10]); 
ylim([-1.5, 1.5]);


subplot(3,1,2);
[xs,ts]=tshift(x,t,4,0.01);
title('Shifting of sawtooth');
xlabel('t-4');
ylabel('X');
xlim([-10, 10]); 
ylim([-1.5, 1.5]);

subplot(3,1,3);
tscale(xs,ts,2,0.01);
title('Scaling of sawtooth');
xlabel('2t-4');
ylabel('X');
xlim([-10, 10]); 
ylim([-1.5, 1.5]);


