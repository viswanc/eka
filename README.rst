Eka
===

  A declarative language for building modern applications.

Idea
----

  The idea is to write example applications with increasing complexity, along with a compiler to compile those apps.

ToDo
----

* Write an MVP.

Notes
-----

* Though the compiler is written in python, the goal is to allow for the builders to be written in any language. The plan is to build a master structure and pass it to builders. From then on the control is transferred to builders.

Decisions
---------

* 180129

  * 1950  Decided not to write tests, till the structure is stable or when it's an absolute necessity.

Log
---

* 180115

  * 2040  Scaffolded.
  * 2130  Wrote the first test.

* 180116

  * 0021  Added linting.
  * 0044  Parsed the config from a file.
  * 0055  Wrote the MVP.
  * 1254  Added debugging.
  * 1813  Basic parsing done.

* 180117

  * 2234  Redid the imports.

* 180127

  * 0224  Bug fixed: Importing children wasn't working.
  * 0337  Bug fixed: File paths to the YAML parser was passed incorrectly.

* 180129

  * 1950  Streamlined the tests.
