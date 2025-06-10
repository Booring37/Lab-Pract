t = -10:0.01:10;
x1 = 2*cos(pi*t/3);
x2 = 3*cos(2*pi*t/9);
x3 = x1+x2;

figure;

subplot (3,1,1);
plot(t,x1);
xlabel('Time');
ylabel('X1');

subplot (3,1,2);
plot(t,x2);
xlabel('Time');
ylabel('X2');

subplot (3,1,3);
plot(t,x3);
xlabel('Time');
ylabel('X3');
