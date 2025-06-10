t = -10:0.01:10
x = exp(j*4*pi*t/3)

rx = real(x);
ix = imag(x);

figure;
subplot (2,1,1);
plot(t,rx);
xlabel('Time');
ylabel('Real');

subplot (2,1,2);
plot(t,ix);
xlabel('Time');
ylabel('Imaginary');