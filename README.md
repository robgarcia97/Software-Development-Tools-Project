# Software-Development-Tools-Project

This project involves building and deploying a web application dashboard using Python and Streamlit. The application visualizes a dataset of car sales advertisements, performing Exploratory Data Analysis (EDA) and displaying the results in an interactive dashboard.


## Project Structure

Software-Development-Tools-Project
│
├── myenv
│ └── (virtual environment files and folders)
│
├── notebooks
│ └── EDA.ipynb
│
├── .gitignore
├── README.md
├── app.py
├── vehicles_us.csv (or your dataset file)
└── .streamlit
└── config.toml


## Requirements

- Python 3.8 or higher
- `pandas`
- `streamlit`
- `plotly.express`
- `altair`

## Installation

1. **Clone the repository:**

   git clone https://github.com/robgarcia97/Software-Development-Tools-Project.git
   cd Software-Development-Tools-Project

Create a virtual environment:
python -m venv myenv
Activate the virtual environment:

On Windows (PowerShell):
.\myenv\Scripts\Activate.ps1

On Windows (Command Prompt):
myenv\Scripts\activate

On macOS/Linux:
source myenv/bin/activate

Install the required packages:
pip install -r requirements.txt

Running the Application
Navigate to the project directory:
cd Software-Development-Tools-Project

Run the Streamlit app:
streamlit run app.py

Open the application in your web browser:
The Streamlit application will be available at http://localhost:8501.

Project Details:
Exploratory Data Analysis (EDA)
The EDA is performed in the notebooks/EDA.ipynb Jupyter notebook. This notebook contains various plots and visualizations of the car sales advertisements dataset.

Streamlit Dashboard
The dashboard is implemented in app.py and includes:

At least one header with text
At least one Plotly Express histogram
At least one Plotly Express scatter plot
At least one checkbox that changes the behavior of the components
Deployment
The application is deployed using Render. Configuration files for deployment are included in the repository:
requirements.txt: Lists the required packages.
.streamlit/config.toml: Configuration for the Streamlit server.


How to Contribute:
Fork the repository
Create a new branch: git checkout -b feature/your-feature-name
Commit your changes: git commit -m 'Add some feature'
Push to the branch: git push origin feature/your-feature-name

Create a pull request:
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
If you have any questions or suggestions, feel free to open an issue or contact me directly at [robgarcia97@yahoo.com].