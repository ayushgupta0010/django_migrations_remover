# Django Migrations Remover
This code is written to automate the task of removing django migrations and the default database. After removing, it will automatically create new migrations and migrate it. 

**Note: This does not remove the `migrations` folder and the `__init__.py` because it could cause errors.**

## Follow these steps to successfully remove the migrations

 1. Clone the repository and put the `migrations_remover.py` inside the
    root deirectory(*where `manage.py` file is located*). 
 2. Make sure all the applications accessing `db.sqlite3` are closed.
 3. Simply run `python migrations_remover.py` and all your migrations will be removed.
