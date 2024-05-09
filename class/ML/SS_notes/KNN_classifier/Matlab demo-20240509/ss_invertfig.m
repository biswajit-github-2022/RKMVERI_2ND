function ss_invertfig(varargin)
  if (nargin==1), a=varargin{1}; else a=gca; end

  set(gcf,'Color',[0 0 0]);
  set(a,'Color',[1 1 1]);
  set(a,'XColor',[1 1 1]);
  set(a,'YColor',[1 1 1]);  
  set(a,'ZColor',[1 1 1]);
  set(get(a,'Title'),'Color',[1 1 1]);
  
%   h=legend;
%   if (~isempty(h)),
%     set(h,'Color',[0 0 0]);
%     set(h,'TextColor',[1 1 1]);
%   end
end