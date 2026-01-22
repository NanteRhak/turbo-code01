#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import clear_output


# In[12]:


# Génération des bits sources

def generate_bits(N=30):
    return np.random.randint(0, 2, N)


# In[13]:


# code convolutifs

def conv_encoder(bits):
    memory = 0
    encoded = []

    for b in bits:
        encoded.append(b)           # bit systématique
        encoded.append(b ^ memory)  # redondance
        memory = b

    return np.array(encoded)


# In[14]:


# Entrelanceur

def interleaver(bits):
    idx = np.random.permutation(len(bits))
    return bits[idx], idx


# In[15]:


# Turbo encodeur

def turbo_encoder(bits):
    enc1 = conv_encoder(bits)
    inter_bits, idx = interleaver(bits)
    enc2 = conv_encoder(inter_bits)
    return enc1, enc2, idx


# In[16]:


# Modulation QPSK

def qpsk_mod(bits):
    bits = bits.reshape(-1, 2)
    mapping = {
        (0,0):  1+1j,
        (0,1): -1+1j,
        (1,0):  1-1j,
        (1,1): -1-1j
    }
    return np.array([mapping[tuple(b)] for b in bits])


# In[17]:


# Canal AWGN

def awgn(signal, snr_db):
    snr = 10**(snr_db/10)
    sigma = np.sqrt(1/(2*snr))
    noise = sigma*(np.random.randn(len(signal)) + 1j*np.random.randn(len(signal)))
    return signal + noise


# In[18]:


# Démodulation soft

def soft_demod_qpsk(signal):
    return np.real(signal)


# In[19]:


# Décodage itératif intuitif

def turbo_decode_soft(soft_values, iterations):
    estimate = soft_values.copy()
    history = []

    for _ in range(iterations):
        estimate = 0.6*estimate + 0.4*np.sign(estimate)
        history.append(estimate.copy())

    decoded_bits = (estimate < 0).astype(int)
    return decoded_bits, history


# In[20]:


# Simulation Turbo complète

def turbo_simulator(snr, iterations):
    clear_output(wait=True)

    # 1. Bits source
    bits = generate_bits(30)

    # 2. Turbo codage
    enc1, enc2, _ = turbo_encoder(bits)

    # 3. Sélection simplifiée
    coded_bits = np.hstack([enc1[:30], enc2[:30]])

    # 4. Modulation QPSK
    mod_signal = qpsk_mod(np.repeat(coded_bits, 2))

    # 5. Canal
    rx_signal = awgn(mod_signal, snr)

    # 6. Démodulation soft
    soft = soft_demod_qpsk(rx_signal)

    # 7. Décodage Turbo
    decoded, history = turbo_decode_soft(soft, iterations)

    # 8. Calcul BER
    ber = np.mean(bits != decoded[:len(bits)])

    # === AFFICHAGES ===
    fig, axs = plt.subplots(1, 3, figsize=(15,4))

    # Constellation
    axs[0].scatter(rx_signal.real, rx_signal.imag, alpha=0.6)
    axs[0].set_title("Constellation QPSK reçue")
    axs[0].grid(True)

    # Itérations
    axs[1].plot(
        [np.mean(np.abs(h)) for h in history],
        marker='o'
    )
    axs[1].set_title("Amélioration par itération")
    axs[1].set_xlabel("Itération")
    axs[1].set_ylabel("Confiance moyenne")
    axs[1].grid(True)

    # Bits
    axs[2].stem(bits[:15], linefmt='g-', markerfmt='go', basefmt='k-')
    axs[2].stem(decoded[:15], linefmt='r--', markerfmt='ro')
    axs[2].set_title(f"Bits (vert) vs Décodés (rouge)\nBER ≈ {ber:.3f}")
    axs[2].set_ylim(-0.5, 1.5)

    plt.tight_layout()
    plt.show()


# In[21]:


# Intérface intéractive

snr_slider = widgets.FloatSlider(
    value=2.0,
    min=0.0,
    max=10.0,
    step=0.5,
    description='SNR (dB)',
    continuous_update=True
)

iter_slider = widgets.IntSlider(
    value=4,
    min=1,
    max=10,
    step=1,
    description='Itérations',
    continuous_update=True
)

widgets.interact(
    turbo_simulator,
    snr=snr_slider,
    iterations=iter_slider
)


# In[ ]:




