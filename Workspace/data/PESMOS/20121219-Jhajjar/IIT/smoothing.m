### Smooth the vector x[1,...,nx] with an exponentially damped kernel.  The
###  result is a vector "smooth" with indeterminate values at the edges, and
###  smoothed values in between
cutoff = 0.05   ### weights to zero below this value
alpha = 1.8  ### Decay of weight with distance from center
logacutoff = log(cutoff)/log(alpha)   ### log base alpha of cutoff
span = floor(-logacutoff )  ### width to left and right
weights = alpha^(-abs(sequence(left=-span, right=span, step=1)))  ### Overloaded "^"
kernel = weights / sum(weights)  ### Overloaded "/"
nx = length(x)
nk = 2*span+1   ### length(kernel)
assert( nx>nk )
x1 = concatenate( sequence(0,length=ny-1),  x )
k1 = concatenate( kernel, sequence(0,length=nx-1) )
s1 = inverse_fft( fft(x1) * fft(k1) )  ### Overloaded "*"
smooth = sequence(NaN, length=nx)
smooth[1+span:nx-span] = s1[ ny+nk-1 : nx+nk-1 ]  ### using 1 offset notation