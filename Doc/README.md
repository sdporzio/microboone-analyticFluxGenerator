#Generating active flux at MicroBooNE

* Kaon flux:
$$
\Phi_K(p_K,l) = \Phi_K(p_K) \ e^{- \frac{l}{\Lambda_K}}
$$
where $\Phi_K(p_K)$ is the spectrum at the beginning of the decay pipe ($l=0$) and $\Lambda_K$ is the total decay length of the kaon $\Lambda_K = 3.7 (p_K / m_K)$ with the kaon mass $m_K = 493$ MeV.




* Source term:
$$
S_{\nu}(E_{\nu},\theta,\phi,l) = \int_0^{\infty} dp_K \left( - \frac{d  \Phi_K(p_k,l)}{dl} \right) \frac{dn^3}{dE_{\nu} \ d \Omega} 
$$
$$
= \int_0^{\infty} dp_K \frac{\Phi_K(p_K,l)}{\Lambda_K} \frac{1}{\Gamma} \frac{d^3 \Gamma}{dE_{\nu} \ d \cos \theta \ d \phi}
$$
$$
= \int_0^{\infty} dp_K \frac{\Phi_K(p_K,l)}{\gamma \beta c (1/\Gamma)} \frac{1}{\Gamma} \frac{d^3 \Gamma}{dE_{\nu} \ d \cos \theta \ d \phi}
$$
$$
= \int_0^{\infty} dp_K \ \Phi_K(p_K,l) \left( \frac{p_K}{m_K} \right) \frac{d^3 \Gamma}{dE_{\nu} \ d \cos \theta \ d \phi}
$$



* Neutrino flux at MicroBoone:
$$
\Phi_{\nu}(E_{\nu}) = \int_{0}^{l_f} dl \int_{-1}^{1} d \cos \theta \int_{0}^{2 \pi} d \phi \ \frac{1}{A} \ S_{\nu} (E_{\nu},\theta,\phi,l) \ P(\theta)
$$
$$
= \frac{2 \pi}{A} \int_{0}^{l_f} dl \int_{-1}^{1} d \cos \theta \ S_{\nu}(E_{\nu},\theta,\phi,l) \ P(\theta)
$$

* Differential decay width:
$$
\frac{d^3 \Gamma}{dE_{\nu} \ d \cos \theta \ d \phi} = \frac{\left| \cal{M} \right|^2}{2 E_K} \frac{E_{\nu}}{8 \pi^2} \delta \left[ f(p_K) \right]
$$
where:
$$
\left| \cal{M} \right|^2 = 2 G_F^2 \ f_K^2 \ m^4_K \ \left| V_{us} \right|^2 \left[ \left( \frac{m_{\mu}}{m_{K}} \right)^2 - \left( \frac{m_{\mu}}{m_K} \right)^4 \right]
$$
$$
f(p_{k}) = m^2_K - m^2_{\mu} - 2E_{\nu} \sqrt{p^2_K + m^2_K} + 2 p_K E_{\nu} \cos \theta
$$


* Full form:
$$
\Phi_{\nu}(E_{\nu}) = \int_{0}^{l_f} dl \int_{-1}^{1} d \cos \theta \ \int_{0}^{2 \pi} d \phi\int_0^{\infty} dp_K \ \Phi_K(p_K) \ e^{- \frac{l}{\Lambda_K}} \left( \frac{p_K}{m_K} \right) \ P(\theta) \\
 \frac{2 G_F^2 \ f_K^2 \ m^4_K \ \left| V_{us} \right|^2 \left[ \left( \frac{m_{\mu}}{m_{K}} \right)^2 - \left( \frac{m_{\mu}}{m_K} \right)^4 \right]}{2 E_K} \frac{E_{\nu}}{8 \pi^2} \\
 \delta \left[ m^2_K - m^2_{\mu} - 2E_{\nu} \sqrt{p^2_K + m^2_K} + 2 p_K E_{\nu} \cos \theta \right]
$$