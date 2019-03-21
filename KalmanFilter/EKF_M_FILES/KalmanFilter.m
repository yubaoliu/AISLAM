% intial parameters

% define system
%   x_t = A x_t-1 + B u_t-1+w_t-1
%   z_t = H x_t + v_t
%
%   x : state vector           - P : cova. matrix
%   u : control vector
%   n : perturbation vector    - Q : cov. matrix
%   y : measurement vector
%   v : measuremet noise       - R : cov. matrix
%
%   F_x : transition matrix
%   F_u : control amtrix
%   F_n : perturbation matrix
%   H   : measurement matrix



dt = 1;

F_x = 1;
F_u = dt;
F_n = 1;
H = 1;

Q = 1;
R = 1;



