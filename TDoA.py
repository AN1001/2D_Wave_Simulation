from scipy.optimize import minimize

def extract_peak(data, dt):
    peak = 0
    i_peak = 0
    for index in range(len(data)):
        if peak < abs(data[index]):
            peak = abs(data[index])
            i_peak = index
    return i_peak*dt

def find_center(imu1, imu2, imu3, c):
    x0, y0, t0 = imu1
    positions = [imu2[:2], imu3[:2]]  # Extract just x,y
    t_diff = [imu2[2]-t0, imu3[2]-t0]  # Time differences
    
    # Error function to minimize
    def error(pos):
        x, y = pos
        d0 = ((x-x0)**2 + (y-y0)**2)**0.5
        error_sum = 0
        for (xi, yi), dt in zip(positions, t_diff):
            di = ((x-xi)**2 + (y-yi)**2)**0.5
            error_sum += ((di - d0) - c*dt)**2
        return error_sum
    
    # Initial guess (centroid of IMUs)
    x_init = (x0 + imu2[0] + imu3[0]) / 3
    y_init = (y0 + imu2[1] + imu3[1]) / 3
    
    # Optimize using L-BFGS-B method
    result = minimize(error, [x_init, y_init], method='L-BFGS-B')
    
    return result.x.tolist()
