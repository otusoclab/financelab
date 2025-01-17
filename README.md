This project is a web sign-in form created using Python, SQLite, HTML, CSS, and JavaScript. It is designed for the Financed Lab to allow visitors such as professors, students, and teaching assistants to sign in and use the software available on the PCs in the lab.

Features
User Authentication: Secure sign-in process for authorized users.
Database Integration: Uses SQLite to store user information.
Responsive Design: Works well on both desktop and mobile devices.
Easy to Use: Simple and intuitive interface for users.

Technologies Used
Frontend: HTML, CSS, JavaScript
Backend: Python (Flask framework)
Database: SQLite

Docker Deployment: 
 - clone and cd into repository
 - run `docker compose build`, this will build the container hosting the flask webserver
 - run `docker run -d -p 5000:5000 financelab-web` to deploy the container, optionally bind mount student sign in database with `--mount type=bind,src=<DATABASE_LOCATION>,dst=/app/instance`

Contributing
We welcome contributions! If you have any suggestions or improvements, please feel free to open an issue or submit a pull request.
