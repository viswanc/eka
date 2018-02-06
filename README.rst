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

Later
-----

* Allow for web imports. They should be cacheable for ever.

Decisions
---------

* 180129

  * 1950  Decided not to write tests, till the structure is stable or when it's an absolute necessity.

* 180205

  * 1930  Decided to replace custom properties, per type to collect children (ex: app.server.resources), with a standard property, named - *props*. This essentially is to reduce the learning curve and to eliminate the need for choosing, a name per type (while writing extensions). Hence, custom properties had been removed, duck typing couldn't be done. Instead, types are to be set, through the property, *type*.

* 180206

  * 1122  Decided not to use groups. As providers could be used, instead and as it complicates the structure.
  * 1428  Decided to rename the attribute, *type* as *class*, so that the syntax can be a superset of JSON Schema.
  * 1552  Decided not to use slashes, instead of dots as class separators. The idea was to allow for importing modules, from global packages, even when the local has some with the same name. ie: /package would mean a global import, where as package would mean a local import, when available. The decision is to avoid name possible confusions, which could lead to bug hunting.

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
  * 2200  Decided to use JSON Schema Draft 4, across the project, as it's the latest version, that's supported by multiple languages.
  * 2340  Improved the master schema.
  * 2345  Started validating the parsed structure.

* 180203

  * 0002  Decided to have case-sensitive values, as it simplifies the flow.

* 180205

  * 1840  Introduced commands (parse and build, instead of build as default), to ease development.
  * 2125  Started using the masterSchema, to modify the structure (for setting default values).
