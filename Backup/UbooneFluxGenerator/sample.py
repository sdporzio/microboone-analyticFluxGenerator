import pandas as pd
import numpy as np

glob = pd.read_json('Constants/constants.json')

g_f = glob['physics']['constants']['Gf']
c = glob['physics']['constants']['c']
m_lep = glob['physics']['mass']['mu']
detW = glob['experiment']['detector']['width']
detH = glob['experiment']['detector']['height']
detL = glob['experiment']['detector']['length']
detD = glob['experiment']['detector']['distance']
pipeL = glob['experiment']['decay_pipe']['length']
detD = detD - detL/2.
area = detH*detW
radius = np.sqrt(area/(2*np.pi))

def MesonEnergy(p_mes,m_mes):
    '''
    Energy of the meson given the mometum
    '''
    return np.sqrt(p_mes**2 + m_mes**2)

def MesonSpectrum(p_mes,spectrum_mes,l,m_mes,t_mes):
    '''
    Meson momentum spectrum as a function of position in the decay pipe.
    '''
    lambda_mes = (t_mes*c)*(p_mes/float(m_mes))
    spectrum_mes *= np.exp(-1*np.divide(l,lambda_mes))
    return spectrum_mes

def ThetaMax(l):
    '''
    Maximum angle with respect to the beam line that a neutrino
    can have in order to go through the detector.
    '''
    thetaMax = np.arccos( (detD-l) / np.sqrt((detD-l)**2 + (radius)**2) )
    return thetaMax

def ProjectionFunction(l,theta):
    '''
    Projection function. Returns 1 if neutrino trajectory is inside
    the detector. Return 0 otherwise.
    '''
    proj = np.where(abs(theta) >= ThetaMax(l), 0, 1)
    return proj

def LIPS(p_mes1,p_mes2,e_nu,theta,m_mes):
    '''
    Lorentz invariant phase space factor.
    '''
    psFactor1 = m_mes**2. - m_lep**2. - 2*e_nu*MesonEnergy(p_mes1,m_mes) + 2.*p_mes1*e_nu*np.cos(theta)
    psFactor2 = m_mes**2. - m_lep**2. - 2*e_nu*MesonEnergy(p_mes2,m_mes) + 2.*p_mes2*e_nu*np.cos(theta)
    if psFactor1*psFactor2 < 0:
        return 1
    else:
        return 0

def MatrixElement2(m_mes,f_mes,v_mes):
    '''
    Matrix element for meson 2-body decay.
    '''
    matrixElement2 = 2*(g_f**2.)*(f_mes**2.)*(m_mes**4.)*(v_mes**2.)*((m_lep/float(m_mes))**2. - (m_lep/float(m_mes))**4.)
    return matrixElement2

def DiffDecayWidth(p_mes1,p_mes2,e_nu,theta,m_mes,f_mes,v_mes):
    '''
    Differential decay width.
    '''
    diffDecayWidth = MatrixElement2(m_mes,f_mes,v_mes)/(2.*MesonEnergy(p_mes1,m_mes)) * e_nu/float(8.*np.pi**2) * LIPS(p_mes1,p_mes2,e_nu,theta,m_mes)
    return diffDecayWidth

def SourceTerm(p_mes,spectrum_mes,e_nu,theta,l,m_mes,t_mes,f_mes,v_mes):
    '''
    Source term for the neutrino flux.
    '''
    source = 0
    for i in np.arange(len(p_mes)-1):
        source += MesonSpectrum(p_mes[i],spectrum_mes[i],l,m_mes,t_mes)*(p_mes[i]/float(m_mes))*DiffDecayWidth(p_mes[i],p_mes[i+1],e_nu,theta,m_mes,f_mes,v_mes)
        print p_mes[i], MesonSpectrum(p_mes[i],spectrum_mes[i],l,m_mes,t_mes)*(p_mes[i]/float(m_mes))*DiffDecayWidth(p_mes[i],p_mes[i+1],e_nu,theta,m_mes,f_mes,v_mes)
    return source

def CalculateFlux(p_mes,spectrum_mes,pdg_code,e_nu,n_steps=20):
    '''
    Integrate the source term for different values of angle and production point and apply
    projection function to determine number of neutrinos in the detector.
    '''

    if pdg_code == 321:
        m_mes = glob['physics']['mass']['k+']
        t_mes = glob['physics']['mean_life']['k+']
        f_mes = glob['physics']['decay_const']['k+']
        v_mes = glob['physics']['ckm']['us']
    elif pdg_code == 211:
        m_mes = glob['physics']['mass']['pi+']
        t_mes = glob['physics']['mean_life']['pi+']
        f_mes = glob['physics']['decay_const']['pi+']
        v_mes = glob['physics']['ckm']['ud']
    else:
        raise Exception("Flux generation is available only for K+ (pdg: 321) and Pi+ (pdg: 211) components.")

    # cosThetaRange = np.linspace(-1,1,n_steps)
    logCosThetaRange = np.logspace(0,3,50)
    cosThetaRange = logCosThetaRange[::-1]*(-2/999.) + 2/999. + 1 # Get a "log style" binning for small degrees
    distanceRange = np.linspace(0,50,n_steps)
    lStep = distanceRange[1]-distanceRange[0]

    lInt = 0
    for l in distanceRange:
        tInt = 0
        for i,cosTheta in enumerate(cosThetaRange[1:]):
            tStep = cosThetaRange[i+1]-cosThetaRange[i]
            theta = np.arccos(cosTheta)
            tInt += SourceTerm(p_mes,spectrum_mes,e_nu,theta,l,m_mes,t_mes,f_mes,v_mes)*ProjectionFunction(l,theta)*tStep
        lInt += tInt*lStep

    return lInt
