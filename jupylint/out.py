# ==============================================================================
def fitfunc(xvalues, mu, sigma, R, A, b1, b2):
    pass

# Given
# write the fitfunc function above(!) this since it is being used below.
def fitter(xval, yval, initial):
    ''' function to fit the given data using a 'fitfunc' TBD.
        The curve_fit function is called. Only the best fit values
        are returned to be utilized in a main script.
    '''
    best, _ = curve_fit(fitfunc, xval, yval, p0=initial)
    return best

# Use functions with script below for plotting parts (a) and (b)
# start value parameter definitions, see equations for s(m) and b(m).
# init[0] = mu
# init[1] = sigma
# init[2] = R
# init[3] = A
# init[4] = b1
# init[5] = b2
init = (125.8, 1.4, 470.0, 5000.0, -0.04, -1.5e-4)
xvalues = np.arange(start=105.5, stop=160.5, step=1)
data = np.array([4780, 4440, 4205, 4150, 3920, 3890, 3590, 3460, 3300, 3200, 3000,
                 2950, 2830, 2700, 2620, 2610, 2510, 2280, 2330, 2345, 2300, 2190,
                 2080, 1990, 1840, 1830, 1730, 1680, 1620, 1600, 1540, 1505, 1450,
                 1410, 1380, 1380, 1250, 1230, 1220, 1110, 1110, 1080, 1055, 1050,
                 940, 920, 950, 880, 870, 850, 800, 820, 810, 770, 760])
# YOUR CODE HERE

# ==============================================================================
# Test cell
val = fitfunc(xvalues, init[0], init[1], init[2], init[3], init[4], init[5])
assert (val[1]>4800 and val[1]<4805), 'fitfunc wrong or initial values changed'


# ==============================================================================
# Test cell
bf = fitter(xvalues, data, init)
assert (bf[0]<126.0 and bf[0]>125.9), 'bad fit'
assert (bf[1]<1.55 and bf[1]>1.5), 'bad fit'
