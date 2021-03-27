 [![Python application](https://github.com/alexb-dev/django_blog/actions/workflows/python-app.yml/badge.svg)](https://github.com/alexb-dev/django_blog/actions/workflows/python-app.yml)
 
# Polling and Blogging Application on Django

Sample blog on Django with polling 

- have polls
- posts
- unit tests


Your Assignment
You’ll be reversing that relationship so that you can only add categories to posts

Take the following steps:

- Read the documentation again about the Django admin.

- You’ll need to create a customized ModelAdmin class for the Post and Category models.

- And you’ll need to create an InlineModelAdmin to represent Categories on the Post admin view.

- Finally, you’ll need to exclude the ‘posts’ field from the form in your Category admin.
