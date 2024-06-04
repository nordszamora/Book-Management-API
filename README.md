# Book Management RESTful API

## Overview

This API allows you to manage a collection of books. You can perform CRUD operations including creating, retrieving, updating, and deleting book records.

## API Endpoints

### Register Account
**Endpoint:** `POST /api/v1/token/register`

**Description:** Create new account.

### Login User Account Token
**Endpoint:** `POST /api/v1/token/login`

**Description:** Login account to get an access token.

### Destroy Account Token
**Endpoint:** `POST /api/v1/token/logout`

**Description:** Log-out account by revoking the token.

### Get All Books
**Endpoint:** `GET /api/v1/books`

**Description:** Retrieve a list of all books.

### Create a New Book
**Endpoint:** `POST /api/v1/books`

**Description:** Add a new book to the collection.

### Get a Book by ISBN
**Endpoint:** `GET /api/v1/books/{isbn}`

**Description:** Retrieve a specific book by its ISBN.

### Update a Book by ISBN
**Endpoint:** `PUT /api/v1/books/{isbn}`

**Description:** Update the details of a specific book by its ISBN.

### Delete a Book by ISBN
**Endpoint:** `DELETE /api/v1/books/{isbn}`

**Description:** Delete a specific book by its ISBN.

## Request Body Fields

- **username**: The account user
- **password**: The account password
- **isbn**: The International Standard Book Number (ISBN) of the book.
- **title**: The title of the book.
- **author**: The author of the book.
- **genre**: The genre of the book.
- **year**: The year the book was published.
- **publisher**: The publisher of the book.
- **quantity**: The quantity of the book in stock.
- **price**: The price of the book.

## Installation

To run this API locally, follow these steps:

1. Clone the repository:
    ```
    $ git clone https://github.com/nordszamora/Book-Management-API.git
    ```

2. Navigate to the project directory:
    ```
    $ cd Book-Management-API
    ```

3. Install the required packages:
    ```
    $ pip install -r requirements.txt
    ```

4. Initialize the database:
    ```
    $ flask db init
    ```

5. Apply the database migrations:
    ```
    $ flask db migrate -m 'books'
    ```

6. Upgrade the database:
    ```
    $ flask db upgrade
    ```

7. Run the application:
    ```
    $ python app.py
    ```

8. Navigate into localhost:
    ```
    http://127.0.0.1:5000/api/v1/<route>
    ```

## Usage

1. Auth:
    ```
    $ curl -X POST http://127.0.0.1:5000/api/v1/token/register -H "Content-Type: application/json" -d '{"username": "<user>", "password": "<pass>"}'

    $ curl -X POST http://127.0.0.1:5000/api/v1/token/login -H "Content-Type: application/json" -d '{"username": "<user>", "password": "<pass>"}'

    $ curl -X POST http://127.0.0.1:5000/api/v1/token/logout -H "Content-Type: application/json" -H "Authorization: Bearer <token>"

    ```

2. Read, Add, Edit & Delete Book:
    ```
    $ curl http://127.0.0.1:5000/api/v1/books

    $ curl http://127.0.0.1:5000/api/v1/books/<ISBN>

    $ curl -X POST http://127.0.0.1:5000/api/v1/books -H "Content-Type: application/json" -H "Authorization: Bearer <token>" -d '{"isbn": <isbn>, "title": "<title>", "author": "<author>", "genre": "<genre>", "year": <year>, "publisher": "<publisher>", "quantity": <quantity>, "price": <price>
    }'

    $ curl -X PUT http://127.0.0.1:5000/api/v1/books/<ISBN> -H "Content-Type: application/json" -H "Authorization: Bearer <token>" -d '{"isbn": <isbn>, "title": "<title>", "author": "<author>", "genre": "<genre>", "year": <year>, "publisher": "<publisher>", "quantity": <quantity>, "price": <price>
    }'

    $ curl -X DELETE http://127.0.0.1:5000/api/v1/books/<ISBN> -H "Content-Type: application/json" -H "Authorization: Bearer <token>"
    ```
    
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
