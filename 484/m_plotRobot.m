function m_plotRobot(xRobot,yRobot)

% Parameters
maxRange = 2;
border = 0.1;
szCenterBlock = 0.1;

% Coordinates of square
x_Square = szCenterBlock*[-1 -1 1 1];
y_Square = szCenterBlock*[1 -1 -1 1];
z_Square = zeros(size(x_Square));

% Plotting the borders
plot([-maxRange-border,-maxRange-border],[-maxRange,maxRange],'k-',...
    [maxRange+border,maxRange+border],[-maxRange,maxRange],'k-',...
    [-maxRange,maxRange],[-maxRange-border,-maxRange-border],'k-',...
    [-maxRange,maxRange],[maxRange+border,maxRange+border],'k-');
hold on;

% Drawing the coordinate lines
plot([xRobot,xRobot],[-maxRange-border,maxRange+border],'k-',...
    [-maxRange-border,maxRange+border],[yRobot,yRobot],'k-',...
    'linewidth',2);

% Drawing squares
patch(x_Square+xRobot,y_Square+yRobot,z_Square,0.5*[1 1 1]);
patch(2*x_Square+xRobot,y_Square+maxRange+border,z_Square,[1 1 1]);
patch(2*x_Square+xRobot,y_Square-maxRange-border,z_Square,[1 1 1]);
patch(x_Square+maxRange+border,2*y_Square+yRobot,z_Square,[1 1 1]);
patch(x_Square-maxRange-border,2*y_Square+yRobot,z_Square,[1 1 1]);

% Setting the axis of the plot
plotRange = maxRange+border+szCenterBlock;
axis equal; axis(plotRange*[-1 1 -1 1]);
hold off;