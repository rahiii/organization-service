# Organization Profile Service

This is a simple Organization Profile Service built using FastAPI. The service allows users to create, read, update, and delete organization profiles.

## Features

- Create organization profiles
- Read organization profiles
- Update existing organization profiles
- Delete organization profiles

## Requirements

- Python 3.7 or higher
- FastAPI
- Uvicorn
- SQLAlchemy
- PyMySQL (for MySQL database connection)
- python-dotenv (for loading environment variables)

## Installation

1. **Clone the repository:**

   ```bash
   git clone git@github.com:rahiii/organization-service.git
   cd organization-service
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```

4. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Create a `.env` file in the `app` directory with the following content:**

   ```env
   DB_USER=root
   DB_PASSWORD=dbuserdbuser
   DB_HOST=organization-profile-service.cyswkjclynii.us-east-1.rds.amazonaws.com
   DB_PORT=3306
   DB_NAME=organization_db
   ```

## Running the Application

1. **Ensure your database is set up and accessible.**

2. **Run the FastAPI application using Uvicorn:**

   - Locally:
      ```bash
      uvicorn app.main:app --reload
      ```
   - On ec2 instance:
      ```bash
      uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
      ```

3. **Open your browser and go to** `http://127.0.0.1:8000` **or** `http://<ORGANIZATION-PUBLIC-IP>:8000` **to see the application running.**

4. **Access the interactive API documentation at** `http://127.0.0.1:8000/docs` **or** `http://<ORGANIZATION-PUBLIC-IP>:8000/docs`.

## API Endpoints

- **GET /**: Returns a welcome message.
- **POST /organizations/**: Create a new organization profile.
- **GET /organizations/**: Retrieve a list of organization profiles.
- **GET /organizations/{organization_id}**: Retrieve a specific organization profile by ID.
- **PUT /organizations/{organization_id}**: Update an existing organization profile by ID.
- **DELETE /organizations/{organization_id}**: Delete an organization profile by ID.

## Accessing the Database

To access and manage your MySQL database via the terminal, follow these steps:

1. **Open Your Terminal:**

2. **Connect to Your MySQL Database:**

   ```bash
   mysql -h organization-profile-service.cyswkjclynii.us-east-1.rds.amazonaws.com -P 3306 -u root -p
   ```

3. **Enter Your Password:**

   When prompted, enter the password:
   
   ```
   Enter password: dbuserdbuser
   ```

4. **Select Your Database:**

   ```sql
   USE organization_db;
   ```

5. **To See Database:**

   ```sql
   SELECT * FROM organizations;
   ```

   - **Expected Output:**
     ```
     +----+--------------------------+------------------------------------------------------------------------------------------------+---------------------------+-------------------------------+----------------------------------------+
     | id | name                     | description                                                                                    | contact_email             | website_url                   | profile_picture                        |
     +----+--------------------------+------------------------------------------------------------------------------------------------+---------------------------+-------------------------------+----------------------------------------+
     |  1 | Starlight Astronomy Club | A club dedicated to exploring the wonders of the night sky, organizing stargazing events, and educating members about astronomy. | contact@starlightastronomy.org | https://www.starlightastronomy.org | https://www.starlightastronomy.org/logo.png |
     |  2 | Eco Warriors Environmental Group | Focused on promoting sustainability, organizing clean-up drives, and advocating for environmental policies. | info@ecowarriors.org      | https://www.ecowarriors.org    | https://www.ecowarriors.org/logo.png    |
     |  3 | Tech Innovators Society  | A hub for tech enthusiasts to collaborate on projects, attend workshops, and stay updated with the latest in technology. | hello@techinnovators.org   | https://www.techinnovators.org | https://www.techinnovators.org/logo.png  |
     +----+--------------------------+------------------------------------------------------------------------------------------------+---------------------------+-------------------------------+----------------------------------------+
     3 rows in set (0.00 sec)
     ```

8. **Exit MySQL:**

   ```sql
   EXIT;
   ```

   - **Expected Response:**
     ```
     Bye
     ```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- FastAPI documentation: https://fastapi.tiangolo.com/

