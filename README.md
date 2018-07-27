
# Car Dealer Managment System

- To try it out:
  1. clone master branch
  2. type: git checkout Develop
  3. go to /car_dealer_project
  4. in console type:
```
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata test_data.json
python manage.py runserver
```
after loaddata your superuser will be:
- name: Admin
- pass: adminadmin
