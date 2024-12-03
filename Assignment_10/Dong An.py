# Copyright 2024 Dong An dong@bu.edu

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.stats import kstest
from google.colab import files

# File upload function
def upload_files():
    """Upload files in Google Colab"""
    print("Please upload your .npy files...")
    uploaded = files.upload()
    file_names = list(uploaded.keys())
    print(f"Uploaded files: {file_names}")
    return file_names

# Global function definitions
def load_signal(file_name):
    """Load signal data from a .npy file"""
    data = np.load(file_name)
    print(f"Loaded file: {file_name}, Data size: {data.shape}")
    return data

def plot_signal(data, title="Radio Signal Intensity Over Time"):
    """Visualize the time-domain radio signal intensity"""
    plt.figure(figsize=(10, 5))
    plt.plot(data, label='Signal Intensity')
    plt.title(title)
    plt.xlabel("Time (samples)")
    plt.ylabel("Intensity")
    plt.legend()
    plt.grid()
    plt.show()

def analyze_frequency(data, sample_rate=1000):
    """Frequency analysis: Check if there are signal frequencies"""
    spectrum = np.abs(fft(data))
    freqs = np.fft.fftfreq(len(data), 1/sample_rate)

    plt.figure(figsize=(10, 5))
    plt.plot(freqs[:len(freqs)//2], spectrum[:len(spectrum)//2])
    plt.title("Frequency Spectrum")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.show()

def test_for_noise(data):
    """Statistical analysis: Test if the data is noise"""
    mean_val = np.mean(data)
    std_dev = np.std(data)
    stat, p_value = kstest(data, "norm", args=(mean_val, std_dev))
    print(f"K-S Test Results:")
    print(f"  - Mean: {mean_val:.4f}, Standard Deviation: {std_dev:.4f}")
    print(f"  - Test Statistic: {stat:.4f}, p-value: {p_value:.4f}")
    if p_value > 0.05:
        print("  => The data follows a normal distribution and is likely noise.")
    else:
        print("  => The data deviates from a normal distribution and likely contains a signal.")

def check_hidden_patterns(data):
    """Check for hidden patterns, such as potential encodings or images"""
    try:
        reshaped_data = data[:10000].reshape((-1, 100))  # Assume reshaping into 100 columns
        plt.figure(figsize=(8, 6))
        plt.imshow(reshaped_data, cmap='gray')
        plt.title("Potential Hidden Pattern (First 10,000 points)")
        plt.colorbar()
        plt.show()
    except Exception as e:
        print(f"Unable to reshape data into an image: {e}")

# Main program logic
if __name__ == '__main__':
    # Upload files to Colab
    file_names = upload_files()

    # Iterate through each file for analysis
    for file_name in file_names:
        print(f"\nAnalyzing file: {file_name}")
        
        # 1. Load the signal
        signal = load_signal(file_name)

        # 2. Plot the time-domain signal
        plot_signal(signal, title=f"Time Domain Signal: {file_name}")

        # 3. Perform frequency analysis
        analyze_frequency(signal)

        # 4. Test if the data is noise
        test_for_noise(signal)

        # 5. Check for hidden patterns
        check_hidden_patterns(signal)
