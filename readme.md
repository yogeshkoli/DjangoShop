# DjangoShop

# Notes To Remember:

## MyUser Model

### BaseUserManager & AbstractBaseUser

`BaseUserManager` and `AbstractBaseUser` are both classes provided by Django that are used to create custom user models. However, they serve different purposes:

    - `BaseUserManager` is a base class for creating custom user managers. A user manager is responsible for creating, updating, and deleting user accounts, as well as performing authentication and authorization tasks. It provides a set of methods that can be customized to fit your application's requirements.

    - `AbstractBaseUser` is a base class for creating custom user models. A user model is responsible for storing user information, such as the user's username, email, password, and other attributes. It provides a set of methods and fields that can be customized to fit your application's requirements.

In other words, `BaseUserManager` provides the methods to manage users, while `AbstractBaseUser` provides the fields and methods to define the user model.

When creating a custom user model in Django, you typically subclass both `BaseUserManager` and `AbstractBaseUser`. The `BaseUserManager` is used to define methods for creating, updating, and deleting user accounts, and the `AbstractBaseUser` is used to define the fields and methods for the user model itself.

### def has_perm(self, perm, obj=None):

The `has_perm` method is a built-in method provided by the Django `AbstractBaseUser` class, which is a base class for creating custom user models in Django. This method is used to check if the user has a specific permission.

The method takes two parameters:
    - `perm`: A string representing the permission that needs to be checked.
    - `obj`: An optional parameter that represents the object for which the permission needs to be checked. If the permission is not related to any specific object, this parameter can be omitted.

The `has_perm` method should return `True` if the user has the specified permission, and `False` otherwise. The logic for checking whether the user has the permission should be implemented in this method.

For example, let's say you have a custom user model called `MyUser`, and you want to check whether a user has a permission called can_view_dashboard. You could implement the has_perm method in the `MyUser` model as follows:

```
class MyUser(AbstractBaseUser):
    # ... other fields and methods ...

    def has_perm(self, perm, obj=None):
        if perm == "can_view_dashboard":
            # check if the user has the required permissions to view the dashboard
            return self.is_staff
        return False
```

In this example, the `has_perm` method checks if the perm parameter is equal to `"can_view_dashboard"`, and if so, it checks if the user is a staff member (i.e., `self.is_staff` is `True`). If the user is a staff member, it returns `True`, indicating that the user has the `can_view_dashboard` permission. If the `perm` parameter is not equal to `"can_view_dashboard"`, or if the user is not a staff member, it returns `False`.

### def has_module_perms(self, add_label):

The `has_module_perms` method is another built-in method provided by the Django `AbstractBaseUser` class, which is a base class for creating custom user models in Django. This method is used to check if the user has permissions to access the entire module (or app).

The method takes one parameter:

    - `add_label`: A string representing the label (or name) of the module that needs to be checked.

The `has_module_perms` method should return `True` if the user has permissions to access the entire module, and `False` otherwise. The logic for checking whether the user has module permissions should be implemented in this method.

For example, let's say you have a custom user model called `MyUser`, and you want to check whether a user has permissions to access the `myapp` module. You could implement the `has_module_perms` method in the MyUser model as follows:

```
class MyUser(AbstractBaseUser):
    # ... other fields and methods ...

    def has_module_perms(self, add_label):
        if add_label == "myapp":
            # check if the user has the required permissions to access the 'myapp' module
            return self.is_staff
        return False

```
In this example, the `has_module_perms` method checks if the `add_label` parameter is equal to `"myapp"`, and if so, it checks if the user is a staff member (i.e., `self.is_staff` is `True`). If the user is a staff member, it returns `True`, indicating that the user has permissions to access the myapp module. If the `add_label` parameter is not equal to `"myapp"`, or if the user is not a staff member, it returns `False`.