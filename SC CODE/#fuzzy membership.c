#fuzzy membership 
#triangular
x = 0:10; 
y = trimf(x,[3 6 10]); 
plot(x, y); 
xlabel('triangular MF, p= x,[3,4,10]') 
ylabel('Fuzziness') 
ylim([-0.05 1.05]); 

#trapazoidal

x = 0:10; 
y = trapmf(x,[1 4 6 9]); 
plot(x,y); 
xlabel('trapezoidal MF,p = (x,[1 4 6 9])'); 
ylabel('Fuzziness'); 
ylim([-0.05,1.05]); 

# 6. sigmoidal MF 
x = 0:0.1:10; 
y = sigmf(x,[1,4]); 
plot(x,y); 
xlabel('Sigmoidal MF, p = (x,[1,4])'); 
ylabel('Fuzziness'); 
ylim([-0.05,1.05]);

#8. PI MF 
x = 0:0.1:10; 
y = pimf(x,[1,4, 5,7]); 
plot(x,y); 
xlabel('PI MF, p = (x,[1,4,5,7])'); 
ylabel('Fuzziness');
ylim([-0.05,1.05]);

#9. Gaussian MF 
x = 0:0.1:10;   
y = gaussmf(x,[1,5]);
plot(x,y); 
xlabel('Gaussian MF, p = (x,[1,5])');
ylabel('Fuzziness');
ylim([-0.05,1.05]);


#% 4. Gaussian 2 MF 
x = 0:0.1:10; 
y = gauss2mf(x, [1,4,5,7]); 
plot(x,y); 
xlabel('Gaussian 2 MF, p = (x,[1,4,5,7])'); 
ylabel('Fuzziness'); 
ylim([-0.05 1.05]); 


# 10. Generalized bell MF
x = 0:0.1:10; 
y = gbellmf(x,[1 4 7]); 
plot(x,y); 
xlabel('Bell MF,p = (x,[1 4 7])'); 
ylabel('Fuzziness'); 
ylim([-0.05 1.05]);

