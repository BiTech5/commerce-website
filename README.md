
# Commerce Website


This repository contains a basic e-commerce website built using Django, a high-level Python web framework. Below you will find details on how to set up and run the project.
## Features

- **User Authentication**: Users can register, sign up, log in, and log out.
- **Product listings**
- **Cart**: Shopping cart functionality.
- **Responsive Design**: The application is designed to be responsive and user-friendly on both desktop and mobile devices.
## Requirements
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Django (version: 5.0.6)
- **Database**: SQLite

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/BiTech5/commerce-website.git

    ```
2.  **Change Directory**
    ```bash
    cd commerce-website
    ```
3. **Navigate to the project directory:**
    ```bash
    python manage.py migrate

    ```
4. **Create SuperUser**
    ```bash
    python manage.py createsuperuser
    ```
5. **Run the program:**
    ```bash
    python manage.py runserver
    ```

6. Open your browser and navigate to http://127.0.0.1:8000/ to view the website.
## Project Structure
- **commerce/** - Main app containing settings and configurations.
- **shop/** - App managing products and orders.
- **media/** - Directory for storing media files.
- **db.sqlite3** - SQLite database file.
- **manage.py** - Command-line utility for administrative tasks.
## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. And here are the steps for Contributing: 


1. Fork the repository.
2. Create a new branch for your feature or bug fix:
    ```bash
    git checkout -b feature-name
    ```
3. Commit your changes:
    ```bash
    git commit -m "Description of your feature or fix"
    ```
4. Push to the branch:
    ```bash
    git push origin feature-name
    ```
5. Create a pull request on GitHub.


## Design Inspiration

The frontend design was inspired by the e-commerce slider design [from Funda of Web IT](https://www.example.com).


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



## Acknowledgements

We welcome contributions to this project. If you have any improvements or suggestions, please fork the repository and submit a pull request.
