# Country Data Scraper and Area Predictor

## Overview

This Python project automates the process of scraping country data (country name, capital, population, and area) from [scrapethissite.com](https://www.scrapethissite.com/pages/simple/), stores it in a SQL Server database, and then uses linear regression to predict a country's area based on its population.

This project demonstrates skills in web scraping, database interaction, data analysis, and basic machine learning.

## Features

*   **Web Scraping:** Extracts country data from [scrapethissite.com](https://www.scrapethissite.com/pages/simple/) using `requests` and `BeautifulSoup`.
*   **Database Storage:** Creates and truncates a table in SQL Server (`UserDB`) to store the scraped data using `pyodbc`.
*   **Data Processing:** Uses `pandas` to clean and prepare the data for analysis, including handling numeric conversions and missing values.
*   **Linear Regression Model:** Trains a linear regression model using `sklearn` to predict a country's area based on its population.
*   **Area Prediction:** Provides a command-line interface to input a population and predict the corresponding area using the trained linear regression model.
*   **Environment Variable Management:** Utilizes `dotenv` and `os` to securely manage database credentials and server information.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/F-Naseri/Area-forecast/blob/main/Area%20forecast.py
    cd [repository-directory]
    ```

    *(Replace `[repository-url]` with your repository URL and `[repository-directory]` with the cloned directory name)*

2.  **Install required Python libraries:**

    ```bash
    pip install -r requirements.txt
    ```

    *(Ensure you have a `requirements.txt` file in your repository with the following content):*

    ```
    requests
    beautifulsoup4
    pyodbc
    python-dotenv
    pandas
    scikit-learn
    ```

3.  **Set up Environment Variables:**

    *   Create a `.env` file in the project's root directory.
    *   Add the following environment variables to the `.env` file, replacing the placeholder values with your actual SQL Server credentials:

        ```
        SERVER=your_server_address
        USERNAME=your_sql_server_username
        PASSWORD=your_sql_server_password
        ```

        *(Make sure to replace `your_server_address`, `your_sql_server_username`, and `your_sql_server_password` with your actual SQL Server details.)*

4.  **Database Setup:**

    *   Ensure you have a SQL Server instance running and accessible.
    *   The script assumes a database named `UserDB` exists. If not, you may need to create it manually or modify the script accordingly.
    *   The script will automatically create or truncate the `scrapethissite` table within the `UserDB` database upon execution.

## Usage

1.  **Run the Python script:**

    ```bash
    python your_script_name.py
    ```

    *(Replace `your_script_name.py` with the actual name of your Python script file.)*

2.  **Data Scraping and Model Training:**

    *   The script will first scrape data from the website and store it in the SQL Server database.
    *   Then, it will train a linear regression model using the scraped data.
    *   Linear Regression results, including Mean Squared Error and R-squared, will be printed to the console.

3.  **Area Prediction:**

    *   After the model training, the script will enter an interactive command-line mode.
    *   You will be prompted to "Enter a population to guess the area (or 'exit' to quit):".
    *   Enter a population value to get the predicted area based on the linear regression model.
    *   Type `exit` to quit the interactive prediction mode.

## Environment Variables

The following environment variables are required for the script to function correctly:

*   `SERVER`:  The address or hostname of your SQL Server.
*   `USERNAME`: The username for connecting to the SQL Server.
*   `PASSWORD`: The password for the SQL Server user.

**Important:** Ensure these environment variables are set securely and are not hardcoded directly into the script, especially if you are sharing your code publicly.

## Dependencies

*   Python 3.x
*   requests
*   beautifulsoup4
*   pyodbc
*   python-dotenv
*   pandas
*   scikit-learn

  These libraries can be installed using `pip install -r requirements.txt`.

## Future Improvements

*   **Graphical User Interface (GUI):** Implement a GUI using libraries like Tkinter or PyQt to make the application more user-friendly.
*   **Enhanced Error Handling:** Improve error handling throughout the script, especially for web scraping and database operations.
*   **Advanced Data Analysis:** Explore more advanced data analysis techniques and machine learning models to improve prediction accuracy.
*   **Data Visualization:**  Incorporate data visualization to better understand the scraped data and model results.
*   **More Data Features:** Scrape and incorporate more features from the website or other sources to enhance the prediction model.
