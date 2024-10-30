# Copyright 2024 Dong An dong@bu.edu
# Copyright 2024 Shenghan Wu wshwsh@bu.edu
# Copyright 2024 Ziheng Qu heng24@bu.edu


import numpy as np
import plotly.graph_objs as go
import ipywidgets as widgets
from ipywidgets import interact, VBox, HTML, HBox
from IPython.display import display
import cv2
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from scipy.stats import norm


#Our goal is to develop an educational visualization which can help students understand Normal distribution.
#Users can change the mean and the standard deviation of the distribution and get the plot of it.



#The first tool we use is ipywidgets
# Function to plot the normal distribution
def plot_distribution(mean, std_dev, scale_factor):
    # Generate x values, fixed to the range [-10, 10]
    x = np.linspace(-10, 10, 500)
    # Calculate y values using the normal distribution formula, apply the scale factor
    y = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2) * scale_factor

    # Create the plot
    plt.figure(figsize=(8, 5))
    plt.plot(x, y)

    # Add a vertical line for the mean
    plt.axvline(mean, color='r', linestyle='--')

    # Highlight standard deviation areas
    highlight_std_area(x, y, mean, std_dev)

    # Set title and labels
    plt.title(f"Normal Distribution (Mean: {mean}, Std Dev: {std_dev}, Scale: {scale_factor})(ipywidgets)")
    plt.xlabel("x")
    plt.ylabel("Probability Density")

    # Fix both x and y axes ranges so they do not change when sliders are moved
    plt.xlim(-10, 10)  # Fix x-axis range
    plt.ylim(0, 1.5)  # Fix y-axis range

    # Display grid and the plot
    plt.grid(True)
    plt.show()


# Function to highlight the areas within 1 and 2 standard deviations
def highlight_std_area(x, y, mean, std_dev):
    plt.fill_between(x, y, where=((x > mean - std_dev) & (x < mean + std_dev)), color='yellow', alpha=0.3)
    plt.fill_between(x, y, where=((x > mean - 2 * std_dev) & (x < mean + 2 * std_dev)), color='blue', alpha=0.2)


# Function to generate explanatory text for the current plot
def get_explanation(mean, std_dev, scale_factor):
    text = f"""
    <h4>Normal Distribution Details</h4>
    <p><strong>Mean (μ):</strong> The red dashed line marks the mean at x = {mean}.</p>
    <p><strong>Std Dev (σ):</strong> The curve spread is determined by the standard deviation. 
    A smaller σ means a narrower distribution, and a larger one makes it wider.</p>
    <p>About <strong>68%</strong> of the data lies within 1 standard deviation of the mean (yellow area), 
    and <strong>95%</strong> lies within 2 standard deviations (blue area).</p>
    <p><strong>Scale Factor:</strong> The curve has been scaled by a factor of {scale_factor}, adjusting its height accordingly.</p>
    """
    return HTML(value=text)


# Define sliders and reset button
mean_input = widgets.FloatSlider(value=0, min=-5, max=5, step=0.1, description='Mean')
std_input = widgets.FloatSlider(value=1, min=0.1, max=2, step=0.1, description='Std Dev')
scale_input = widgets.FloatSlider(value=1, min=0.1, max=3, step=0.1, description='Scale')  # New scale factor slider
reset_button = widgets.Button(description="Reset")


# Function to reset slider values to defaults
def reset_values(b):
    mean_input.value = 0
    std_input.value = 1
    scale_input.value = 1  # Reset the scale factor


# Link the reset button to the reset function
reset_button.on_click(reset_values)


# Update plot and explanation based on current slider values
def update_plot(mean, std_dev, scale_factor):
    plot_distribution(mean, std_dev, scale_factor)
    display(get_explanation(mean, std_dev, scale_factor))


# Arrange controls in a horizontal box
controls = HBox([mean_input, std_input, scale_input, reset_button])

# Enable interactive updates when sliders are moved
interact(update_plot, mean=mean_input, std_dev=std_input, scale_factor=scale_input)

# Display the controls
display(controls)



#The second tool we use is ploty
# Function to plot the normal distribution with Plotly
def draw_normal_plotly(mean, std_dev):
    # Generate data points for the normal distribution
    x = np.linspace(mean - 4 * std_dev, mean + 4 * std_dev, 500)
    y = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2)

    # Create Plotly figure
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Normal Distribution'))

    # Add a line indicating the mean
    fig.add_vline(x=mean, line=dict(color='red', dash='dash'), name='Mean')

    # Update the layout of the figure
    fig.update_layout(
        title=f"Normal Distribution (Mean: {mean}, Std Dev: {std_dev})(ploty)",
        xaxis_title="x",
        yaxis_title="Probability Density",
        template="plotly_white",
        showlegend=True
    )

    # Display the figure
    fig.show()


# Function to update the plot based on slider values
def update(mean, std_dev):
    draw_normal_plotly(mean, std_dev)


# Create sliders for interactive control of mean and standard deviation
mean_slider = widgets.FloatSlider(value=0, min=-5, max=5, step=0.1, description='Mean')
std_slider = widgets.FloatSlider(value=1, min=0.1, max=2, step=0.1, description='Std Dev')
reset_button = widgets.Button(description="Reset")


# Reset sliders and update plot
def reset_values(b):
    mean_slider.value = 0
    std_slider.value = 1
    update(mean_slider.value, std_slider.value)  # Update the plot after resetting


reset_button.on_click(reset_values)

# Set up interactive controls
interact(update, mean=mean_slider, std_dev=std_slider)

# Display the sliders and reset button in a vertical box
display(VBox([mean_slider, std_slider, reset_button]))



#The third tool we used is opencv
# Define global variables for storing mean, standard deviation, and axis scaling range
mu = 0
sigma = 1
x_scale = 6  # Control for the horizontal axis range in the interactive interface
y_scale = 8  # Control for the vertical axis range in the interactive interface

# Set initial window size
width, height = 600, 400

# Define the callback function for mouse click events
def mouse_click(event, x, y, flags, param):
    global mu, sigma
    if event == cv2.EVENT_LBUTTONDOWN:
        # Convert click coordinates to mean and standard deviation
        mu = (x - width // 2) / (width // 2) * x_scale  # Map based on scaling factor
        sigma = max(0.1, (height - y) / height * y_scale)  # Prevent sigma from being zero
        print(f"Selected mu: {mu}, sigma: {sigma}")
        update_normal_distribution(mu, sigma)

# Function to draw the coordinate plane with ticks, labels, and title
def draw_plane():
    img = np.ones((height, width, 3), np.uint8) * 255

    # Draw x and y axes
    cv2.line(img, (0, height // 2), (width, height // 2), (0, 0, 0), 2)  # x-axis
    cv2.line(img, (width // 2, 0), (width // 2, height), (0, 0, 0), 2)  # y-axis

    # Add title at the top of the image
    cv2.putText(img, 'Set Mean and Standard Deviation', (width // 4, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)

    # Label horizontal and vertical axes
    cv2.putText(img, 'Mean (mu)', (width - 100, height // 2 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 1)
    cv2.putText(img, 'Std Dev (sigma)', (width // 2 + 10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 1)

    # Draw ticks and labels for x-axis based on scaling
    for i in range(-x_scale, x_scale + 1):
        x_pos = int(width // 2 + (i / x_scale) * (width // 2))
        cv2.line(img, (x_pos, height // 2 - 5), (x_pos, height // 2 + 5), (0, 0, 0), 2)  # Tick
        cv2.putText(img, f'{i}', (x_pos - 10, height // 2 + 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)  # Label

    # Draw ticks and labels for y-axis based on scaling
    for i in range(0, y_scale + 1):
        y_pos = int(height - (i / y_scale) * height)
        cv2.line(img, (width // 2 - 5, y_pos), (width // 2 + 5, y_pos), (0, 0, 0), 2)  # Tick
        cv2.putText(img, f'{i}', (width // 2 + 10, y_pos + 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)  # Label

    return img

# Remaining functions remain unchanged


# Initialize Matplotlib plot with Sliders for axis scaling
def init_plot():
    global line, x_slider, y_slider
    x = np.linspace(-10, 10, 500)
    y = norm.pdf(x, mu, sigma)

    # Set initial x-axis and y-axis range
    fig, ax = plt.subplots()
    plt.subplots_adjust(left=0.1, bottom=0.25)  # Leave space for sliders
    ax.set_xlim(-x_scale, x_scale)  # Initialize x-axis range
    ax.set_ylim(0, 0.5)  # Initialize y-axis range
    ax.set_title("Normal Distribution")
    ax.set_xlabel("x")
    ax.set_ylabel("Probability Density")

    # Draw initial normal distribution curve
    line, = ax.plot(x, y, lw=2)
    plt.grid(True)
    plt.ion()  # Enable interactive mode

    # Add Sliders for dynamic adjustment of x and y axis ranges
    axcolor = 'lightgoldenrodyellow'
    ax_xscale = plt.axes([0.1, 0.1, 0.65, 0.03], facecolor=axcolor)
    ax_yscale = plt.axes([0.1, 0.05, 0.65, 0.03], facecolor=axcolor)

    x_slider = Slider(ax_xscale, 'X Scale', 1, 20, valinit=x_scale, valstep=1)
    y_slider = Slider(ax_yscale, 'Y Scale', 0.1, 1, valinit=0.5, valstep=0.1)

    # Update axis range when sliders change
    x_slider.on_changed(update_plot_scale)
    y_slider.on_changed(update_plot_scale)

    plt.show(block=False)  # Ensure main program is not blocked

# Function to update the normal distribution plot
def update_normal_distribution(mu, sigma):
    global line
    x = np.linspace(-10, 10, 500)
    y = norm.pdf(x, mu, sigma)

    # Update curve data
    line.set_data(x, y)
    plt.draw()  # Redraw plot
    plt.pause(0.01)  # Enable dynamic updates for animation effect

# Update plot's x and y axis range when slider values change
def update_plot_scale(val):
    global x_slider, y_slider
    x_scale_val = x_slider.val
    y_scale_val = y_slider.val
    plt.gca().set_xlim(-x_scale_val, x_scale_val)
    plt.gca().set_ylim(0, y_scale_val)
    plt.draw()

# OpenCV slider callback for adjusting axis scaling in the interactive interface
def on_xscale_change(val):
    global x_scale
    x_scale = val

def on_yscale_change(val):
    global y_scale
    y_scale = val

# plot function
def plot_opencv_distribution():
    global mu, sigma, x_scale, y_scale

    # Initialize OpenCV window
    cv2.namedWindow('Select Mean and Std Dev')
    cv2.setMouseCallback('Select Mean and Std Dev', mouse_click)

    # Create OpenCV sliders for x and y axis scaling
    cv2.createTrackbar('X Scale', 'Select Mean and Std Dev', x_scale, 20, on_xscale_change)
    cv2.createTrackbar('Y Scale', 'Select Mean and Std Dev', y_scale, 20, on_yscale_change)

    # Initialize Matplotlib plot
    init_plot()

    while True:
        img = draw_plane()  # Draw coordinate plane
        cv2.imshow('Select Mean and Std Dev', img)

        # Wait for user input
        key = cv2.waitKey(10)
        if key == 27:  # Press Esc to exit
            break

    cv2.destroyAllWindows()

plot_opencv_distribution()

#For this task, ploty and ipywidgets seems to be the better tools to visualize normal distribution with the use of sliders.

/*In this Project, we examine the performance and limitations of three popular Python-based visualization tools—ipywidgets, Plotly, and OpenCV—when deployed in the Google Colab environment. 
Google Colab presents unique constraints due to its browser-based nature and limited support for certain interactive functionalities, which influences the suitability of each tool for educational and analytical purposes.

ipywidgets: In a standard Jupyter Notebook environment, ipywidgets provides a straightforward and efficient means to create interactive controls (e.g., sliders, buttons) that can dynamically update visualizations in real time. 
However, in the Google Colab environment, ipywidgets encounters limitations in rendering real-time interactions due to Colab's lack of native support for direct widget interactivity. Although some basic widget functionalities 
can be enabled with additional setup, the overall responsiveness and interactivity are generally compromised compared to traditional Jupyter Notebooks. Consequently, ipywidgets in Colab is best suited for displaying static controls 
or configurations that do not rely on frequent updates, making it less ideal for high-frequency real-time data manipulation tasks.

Plotly: Plotly operates effectively in Google Colab, as Colab's built-in HTML rendering capabilities allow full utilization of Plotly's interactive features. Plotly supports a wide range of interactive elements, 
including zooming, panning, and tooltip displays, which are preserved in Colab with minimal configuration. This makes Plotly an optimal choice for presenting high-quality, interactive visualizations directly within Colab notebooks. 
For applications requiring complex data visualizations or interactive exploration of mathematical and statistical models, Plotly in Colab offers an efficient and user-friendly solution, providing robust functionality for educational 
and data analysis applications.

OpenCV: OpenCV, while powerful for image processing and custom graphical manipulations, faces substantial limitations within Colab. Colab lacks support for the interactive OpenCV windows used to capture mouse events, 
manage dynamic sliders, or execute real-time updates within a dedicated OpenCV GUI window. As a result, only static images processed by OpenCV can be displayed, typically through secondary visualization libraries such as matplotlib. 
This restricts OpenCV's application in Colab to non-interactive image processing tasks. OpenCV is therefore limited to scenarios where static images can adequately demonstrate the intended results, making it less suitable for applications 
requiring continuous user interaction or real-time parameter adjustments.

#Conclusion
In summary, within the Google Colab environment, Plotly emerges as the most suitable tool for generating high-quality, interactive visualizations, effectively supporting a broad range of data analysis and educational tasks. ipywidgets, 
while constrained, can still be used effectively for displaying static controls or configuring non-dynamic elements, though it is suboptimal for real-time updates. OpenCV, limited to static image processing in Colab, 
is not recommended for interactive applications in this environment. For visualizations such as normal distribution models that benefit from user interactivity, Plotly is recommended as the primary tool in Google Colab to achieve the desired functionality and user experience.*/

