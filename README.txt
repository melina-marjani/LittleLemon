to enter virtual env: source myenv/bin/activate
to enter mysql: mysql -u root -p

LittleLemon API Endpoints for Testing

1. Menu API
- List and create menu items:
  /restaurant/menu-items/

- Retrieve, update, delete a single menu item by ID:
  /restaurant/menu-items/<id>/

2. Table Booking API
- List and create table bookings:
  /restaurant/booking/tables/

- Retrieve, update, delete a single booking by ID:
  /restaurant/booking/tables/<id>/

3. User Registration and Authentication (via Djoser)
- User registration:
  /auth/users/

- Obtain auth token (login):
  /auth/token/login/

- Logout (invalidate token):
  /auth/token/logout/

4. Protected API Example
- Example of an authenticated-only endpoint:
  /restaurant/message/

Note: Use Bearer token authentication with tokens obtained from the login endpoint when testing protected routes.

