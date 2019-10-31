%% 2.2.1.6 matrix exponentials
R = rotx(0.3)
S=logm(R)
vex(S)'

[th, w] = trlog(R)
expm(S)

R = rotx(0.3)
R = expm(skew([1 0 0])*0.3)

%% 2.2.1.7 Unit Quaternions
% rpy2tr Roll-pitch-yaw angles to homogeneous transform
R = rpy2tr(0.1, 0.2, 0.3)
q = UnitQuaternion(R)
q.inv()
q*q.inv()
q.R
q = q*q
%q.plot()
q*[1 0 0]'
