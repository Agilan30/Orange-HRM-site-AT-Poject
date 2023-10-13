# Web Automation on OrangeHRM Website with Python, Selenium, PyTest

## PFA the Test cases scenarios 

https://github.com/Agilan30/AT-Project---Orange-HRM-3.0/blob/main/AT%20Project%201.xlsx

## Scenerios:

- Login to orange hrm demo site: https://opensource-demo.orangehrmlive.com/
- Create 2 new employees and save it to a JSON list
- Now go to PIM dashboard and search by 1st user name. Assert that the user is found.
- Now click on the user from the search table and update id by random userid / delete user id
- Now again search the user by new user id from the PIM dashboard menu and assert that the user is found
- Now logout from admin and login with the 2nd user from your JSON list
- Now click on My Info menu
- Select Gender and Blood Type and save it
- Click on contact details and input address and email
- Logout the user

## Test case check list based on the Scenerio:

- Admin Login with Invalid credential. 
- Admin Login with valid credential.
- Create employee without username.
- Create first employee.
- create second employee.
- Search existing employee with invalid name.
- Search employee with valid name.
- Update employee Id by random Id.
- Search employee again with updated employee id.
- Delete Employee
- Logout Admin.
- Login second user with valid credential. 
- Insert the second user's Gender, Blood, Address and email. 
- Logout second user. 









