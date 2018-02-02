Eka
===

  A declarative language for building modern applications.

Idea
----

  The idea is to write example applications with increasing complexity, along with a compiler to compile those apps.

ToDo
----

* Complete the requirements file.

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

* 180131

  * 0103  Introduced nodes and successfully built the master node (tree).
  * 1219  Added types app.client.element and app.server.resource.
  * 1909  Restructured the processing of nodes.
  * 2005  Introduced ordered parsing of the configs.
  * 2029  Bug fixed: Structures weren't properly updated with providers.
  * 2307  Collected the types under a single file, for convenience.

* 180201

  * 0019  Redid node parsing.

* 180202

  * 0440  Wrote the first builder.
  * 2018  Added a primitive JSON schema.
  * 2340  Improved the master schema.
  * 2345  Started validating the parsed structure.
