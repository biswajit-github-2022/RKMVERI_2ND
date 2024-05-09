function ss_draw_line(p1, p2, colr)

if nargin < 3
    colr = 'b';
end
%DRAWLINE Draws a line from point p1 to point p2
%   DRAWLINE(p1, p2) Draws a line from point p1 to point p2 and holds the
%   current figure
plot([p1(1) p2(1)], [p1(2) p2(2)], 'Color', colr);
end