%Project 3 Code

%Use root locus to find poles and jw-intercept using damping ratio
clc
clear all
s = tf('s');
Gs =(1)/((1.2*s^2+2*s));
rlocus(Gs);
sgrid(.5,0);
axis([-10 10 -8 8])

%Find K for jw-intercept
s = -.833+.8735i; % Desired pole location
disp(['Pole = ' num2str(s)]);
Gs =(1)/((1.2*s^2+2*s)); % Plug in value for Gs
K = 1./abs(Gs); % Gain formula
disp(['K = ' num2str(K)]);

OS=.05;
H=1;
BigR=1000;
zeta = -log(OS)/sqrt(pi^2 + log(OS)^2);
G0 = tf(1,[1.2 2 0]); %Open Loop Gain
GH = G0*1;

newpole=20*s; %Reduces the settling time by a factor of 20 [top, bottom] = tfdata(GH,'v');
zerosGH = roots(top);
polesGH = roots(bottom);
zeroAngle = pi;

    for i = 1:length(zerosGH) %Finding Angle
        zeroAngle = zeroAngle - unwrap(angle(newpole-zerosGH(i)));
    end
    for i = 1:length(polesGH) %Finding Angle
        zeroAngle = zeroAngle + unwrap(angle(newpole-polesGH(i)));
    end
    
zeroAngle = mod(zeroAngle,2*pi);
finalZeroAngle = zeroAngle * 180/pi; %Angle of Zero
disp(['Zero Angle = ' num2str(finalZeroAngle)]);
zerolocation = real(newpole) - imag(newpole)/tan(zeroAngle); %Location of Zero
disp(['Zero Location = ' num2str(zerolocation)]);
G1 = tf([1 -zerolocation],1); %PD Compensator
G2 = tf([1 0.01],[1 0]); %PI Compensator with a zero at -0.01
[G1poles,G1K] = fnc_rootLocusCrossing(G0*G1*H,zeta,BigR); %Poles and K of G1
disp(['G1 Poles = ' num2str(G1poles)]);
disp(['G1 K = ' num2str(G1K)]);
[G2poles,G2K] = fnc_rootLocusCrossing(G0*G1*G2*H,zeta,BigR); %Poles and K of G2
disp(['G2 Poles = ' num2str(G2poles)]);
disp(['G2 K = ' num2str(G2K)]);
Ge1 = feedback(G2K*G0*G1,H);
Ge2 = feedback(G2K*G0*G1*G2,H);

figure(1)
rlocus(G0*G1*H); %Root Locus Plot
sgrid(zeta,0);
figure(2)
step(Ge1,1); %Step Response Plot of Ge1
figure(3)
step(Ge2,1); %Step Response Plot of Ge2