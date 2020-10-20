function m_animatePath(xD,yD,x,y)
%
% m_animatePath(xD,yD,x,y)
%
% This function takes the data structures stored from the Simulink model
% and displays an animation of their motion.

% Maximum range
maxRange = 2;

% Extracting time and actual coordinates
t = xD(1).time;
xD = xD(1).data;
yD = yD(1).data;
x = x(1).data;
y = y(1).data;

% Step size
dt = t(2)-t(1);

figure(1)
set(gcf, 'Position',  [100, 100, 1000, 1000])

for i = 1:length(t)
    subplot(2,2,1); plot(t(1:i),x(1:i),'b-','linewidth',2); hold on;
    plot(t(1:i),xD(1:i),'r-','linewidth',2); hold off; grid on;
    xlabel('time'); ylabel('x(t)'); axis([0 t(i)+dt -maxRange maxRange]);
    subplot(2,2,3); plot(t(1:i),y(1:i),'b-','linewidth',2); hold on;
    plot(t(1:i),yD(1:i),'r-','linewidth',2); hold off; grid on;
    xlabel('time'); ylabel('y(t)'); axis([0 t(i)+dt -maxRange maxRange]);
    subplot(1,2,2); m_plotRobot(x(i),y(i)); hold on;
    plot(x(1:i),y(1:i),'b-','linewidth',2);
    plot(xD(1:i),yD(1:i),'r-'); hold off;
    title(sprintf('t = %4.1f',t(i)));
    
    pause(0.1);
end
