n = -10:0.1:10
x1 = 5*cos(0.5*n+pi/6)
x2 = 5*cos(3*pi*n/20+pi/3)

subplot (2,1,1);
stem(n,x1);
xlabel('n');
ylabel('X1');

subplot (2,1,2);
stem(n,x2);
xlabel('n');
ylabel('X2');