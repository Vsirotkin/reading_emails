# Email Retrieval Project

This project is a simplified version of a system designed to retrieve email messages. It is structured to be independent of Google settings, although Google settings are present in the project and can be easily obtained from the Google website and inserted into the project.

## Project Features

- **Simplified Architecture**: The project is designed with a focus on simplifying the process of retrieving and processing email messages.
- **Google Settings**: To work with email messages via Google, you need to obtain the appropriate settings from the Google website and insert them into the project.
- **Testing**: Python scripts for sending and receiving messages, as well as images, have been created for testing the project's functionality. All necessary tests have been conducted.
- **Dockerized**: The entire project is containerized using Docker, making it easy to deploy and run in any environment.

## Installation and Running with Docker

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject
   ```

2. **Build and Run the Docker Containers**:
   ```bash
   docker compose up --build
   ```

3. **Set Up Environment Variables**:
   - Obtain Google settings from the Google website and insert them into the `.env` file in the project root.

4. **Access the Application**:
   - Once the containers are up and running, you can access the application at `http://localhost:8000`.

## Testing with Docker

To run tests within the Docker environment, use the following command:

```bash
docker-compose exec web python manage.py test
```

## Project Structure

- **myapp**: The main application of the project.
- **tests**: Tests to verify the functionality of the project.
- **settings**: Project settings, including Google settings.

## Contributing to the Project

If you wish to contribute to the project, please create a pull request with your changes.

## License

This project is licensed under the [MIT License](LICENSE).

---

Thank you for your interest in our project! If you have any questions or suggestions, please feel free to contact us.
```
