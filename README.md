# NetFix

NetFix is a web application that allows companies to register and create services, while customers can log in to request these services. It is designed to streamline the process of connecting service providers with customers in various fields.

---

## Features

### For Companies
- **Register**: Companies can create an account and provide details such as their field of work, description, and logo.
- **Create Services**: Registered companies can create and manage services, including setting prices and descriptions.
- **View Requests**: Companies can see requests made by customers for their services.

### For Customers
- **Register**: Customers can create an account and provide personal details.
- **Request Services**: Customers can browse available services and request them by providing necessary details.
- **Rate Services**: Customers can rate and review services they have used.

### General Features
- **User Authentication**: Secure login and registration system for both companies and customers.
- **Service Categories**: Services are categorized by field, making it easy for customers to find what they need.
- **Responsive Design**: The application is fully responsive and works on all devices.

---

## Technologies Used

- **Frontend**: HTML, CSS
- **Backend**: Django (Python)
- **Database**: SQLite (default for development)
- **Authentication**: Django's built-in authentication system
- **Styling**: Custom CSS 

---

## Installation

Follow these steps to set up the project locally:

### Prerequisites
- Python 3.x
- Pip (Python package manager)
- Git

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://learn.zone01kisumu.ke/git/clomollo/netfix.git
   cd netfix

2. **Install Dependencies:**
```bash
pip install
```

3. **Run Migrations:**
```bash
Python3 manage.py migrate
```

4. **Run the Development Server:**
```bash
Python manage.py runserver
```
5. **Access the Application:**
Open your browser and go to 
```bash
http://127.0.0.1:8000/
```
# Usage
### For Companies
1. Register as a company.

2. Log in and create services.

3. View and manage customer requests.

### For Customers
1. Register as a customer.

2. Log in and browse available services.

3. Request services and provide necessary details.

4. Rate and review services after use.

# License
This project is licensed under the MIT License.



