.. _sqlite-mapper:

=============
Sqlite mapper
=============

Scipion objects can be composed of several attributes and when an object
is stored in the database it is necessary to store every attribute of
the object. The attributes of an object can be single python objects
(such integer or float) or other objects that are also composed of
several attributes (that is, objects can be nested). This mapper is
meant to store objects that can be thought of as structures with fields
or other structures inside it.

Every subclass (set, list, pointer, etc...) of the class object has its
own attributes, and also new attributes can be added dynamically to any
instance of a subclass. If a new attribute is added to the subclass it
is treated as it was declared in the subclass definition. When an object
is stored in the database, all its attributes are “discovered” from the
object instance and stored one per row in the database.

The image shown below describes the object structure:

All object attributes are stored in the same database and every object
attribute is stored in a single row. For every row a set of fields are
stored for every attribute:

-  *id*: unique identifier of the attribute.
-  *parent\_id*: parent identifier of the attribute.
-  *name*: name of the attribute in the object. If the attribute is a
   child then this field is built concatenating the ancestors of the
   attribute and ending with its name (see figure below). If the
   attribute is the root (first row in the image) then the name of the
   object is stored.
-  *classname*: class type of the attribute.
-  *value*: value of the attribute.
-  *label:free* text to tag the attribute.
-  *comment*: free text to describe the attribute.
-  *creation*: creation date of the object.

When storing the object, the value of the column “name” of a child
attribute is built dynamically to keep trace of the child-parent
relationship.

.. todo: The image depicted below shows the structure of the table and an object stored in it: