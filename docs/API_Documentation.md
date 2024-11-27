# Organization Profile Service API Documentation

## Base URL

- **Local Development**: `http://127.0.0.1:8000`

## Endpoints

### 1. GET `/`

- **Description**: Returns a welcome message.
- **Response**:
  - **Status Code**: `200 OK`
  - **Body**:
    ```json
    {
      "message": "Welcome to the Organization Profile Service!"
    }
    ```

---

### 2. POST `/organizations/`

- **Description**: Creates a new organization.
- **Request Body** (JSON):

  ```json
  {
    "name": "string",            // Required
    "description": "string",     // Optional
    "contact_email": "string",   // Optional
    "website_url": "string",     // Optional
    "profile_picture": "string"  // Optional
  }
  ```

- **Response**:
  - **Status Code**: `201 Created`
  - **Body**: The created organization object.

    ```json
    {
      "id": 6,
      "name": "Starlight Astronomy Club",
      "description": "A club dedicated to exploring the wonders of the night sky, organizing stargazing events, and educating members about astronomy.",
      "contact_email": "contact@starlightastronomy.org",
      "website_url": "https://www.starlightastronomy.org",
      "profile_picture": "https://www.starlightastronomy.org/logo.png"
    }
    ```

---

### 3. GET `/organizations/`

- **Description**: Retrieves a list of organizations.
- **Query Parameters**:
  - `skip` (integer, optional): Number of records to skip. Default is `0`.
  - `limit` (integer, optional): Maximum number of records to return. Default is `100`.
- **Response**:
  - **Status Code**: `200 OK`
  - **Body**: An array of organization objects.

    ```json
    [
      {
        "id": 6,
        "name": "Starlight Astronomy Club",
        "description": "A club dedicated to exploring the wonders of the night sky, organizing stargazing events, and educating members about astronomy.",
        "contact_email": "contact@starlightastronomy.org",
        "website_url": "https://www.starlightastronomy.org",
        "profile_picture": "https://www.starlightastronomy.org/logo.png"
      },
      {
        "id": 7,
        "name": "Eco Warriors Environmental Group",
        "description": "Focused on promoting sustainability, organizing clean-up drives, and advocating for environmental policies.",
        "contact_email": "info@ecowarriors.org",
        "website_url": "https://www.ecowarriors.org",
        "profile_picture": "https://www.ecowarriors.org/logo.png"
      },
      {
        "id": 8,
        "name": "Tech Innovators Society",
        "description": "A hub for tech enthusiasts to collaborate on projects, attend workshops, and stay updated with the latest in technology.",
        "contact_email": "hello@techinnovators.org",
        "website_url": "https://www.techinnovators.org",
        "profile_picture": "https://www.techinnovators.org/logo.png"
      }
    ]
    ```

---

### 4. GET `/organizations/{organization_id}`

- **Description**: Retrieves an organization by ID.
- **Path Parameters**:
  - `organization_id` (integer): The ID of the organization.
- **Response**:
  - **Status Code**: `200 OK` if found.
  - **Status Code**: `404 Not Found` if the organization does not exist.
  - **Body**: The organization object.

    **Example (Found):**

    ```json
    {
      "id": 6,
      "name": "Starlight Astronomy Club",
      "description": "A club dedicated to exploring the wonders of the night sky, organizing stargazing events, and educating members about astronomy.",
      "contact_email": "contact@starlightastronomy.org",
      "website_url": "https://www.starlightastronomy.org",
      "profile_picture": "https://www.starlightastronomy.org/logo.png"
    }
    ```

    **Example (Not Found):**

    ```json
    {
      "detail": "Organization not found"
    }
    ```

---

### 5. PUT `/organizations/{organization_id}`

- **Description**: Updates an existing organization.
- **Path Parameters**:
  - `organization_id` (integer): The ID of the organization to update.
- **Request Body** (JSON):

  ```json
  {
    "name": "string",            // Optional
    "description": "string",     // Optional
    "contact_email": "string",   // Optional
    "website_url": "string",     // Optional
    "profile_picture": "string"  // Optional
  }
  ```

- **Response**:
  - **Status Code**: `200 OK` if updated.
  - **Status Code**: `404 Not Found` if the organization does not exist.
  - **Body**: The updated organization object.

    **Example (Updated):**

    ```json
    {
      "id": 1,
      "name": "Starlight Astronomy Club",
      "description": "An updated description for the astronomy club.",
      "contact_email": "newcontact@starlightastronomy.org",
      "website_url": "https://www.newstarlightastronomy.org",
      "profile_picture": "https://www.newstarlightastronomy.org/logo.png"
    }
    ```

    **Example (Not Found):**

    ```json
    {
      "detail": "Organization not found"
    }
    ```

---

### 6. DELETE `/organizations/{organization_id}`

- **Description**: Deletes an organization.
- **Path Parameters**:
  - `organization_id` (integer): The ID of the organization to delete.
- **Response**:
  - **Status Code**: `200 OK` if deleted.
  - **Status Code**: `404 Not Found` if the organization does not exist.
  - **Body**: The deleted organization object.

    **Example (Deleted):**

    ```json
    {
      "id": 1,
      "name": "Starlight Astronomy Club",
      "description": "A club dedicated to exploring the wonders of the night sky, organizing stargazing events, and educating members about astronomy.",
      "contact_email": "contact@starlightastronomy.org",
      "website_url": "https://www.starlightastronomy.org",
      "profile_picture": "https://www.starlightastronomy.org/logo.png"
    }
    ```

    **Example (Not Found):**

    ```json
    {
      "detail": "Organization not found"
    }
    ```

---

## Models

### Organization

- **Fields**:
  - `id` (integer): The unique identifier of the organization.
  - `name` (string): The name of the organization.
  - `description` (string, optional): A description of the organization.
  - `contact_email` (string, optional): The contact email address.
  - `website_url` (string, optional): The website URL.
  - `profile_picture` (string, optional): The URL or path to the profile picture.

---

## Error Responses

- **400 Bad Request**: The request was invalid or cannot be served.
- **404 Not Found**: The requested resource could not be found.
- **500 Internal Server Error**: An error occurred on the server.

---

## Notes

- All data is sent and received in JSON format.
- Ensure that the `Content-Type: application/json` header is included in requests with a body.
- The `id` field is auto-generated by the server and cannot be specified during creation.
