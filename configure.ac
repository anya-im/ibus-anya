#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.69])
AC_INIT([ibus-egoisticliliy], [0.0.1], [syuta.hashimoto@gmail.com])
AM_INIT_AUTOMAKE

PACKAGE_DIR=`pwd`
AC_SUBST(PACKAGE_DIR)

AC_ARG_WITH(anya-model,
	[AC_HELP_STRING([--with-anya-model=PATH],
			[file path of anya model])],
	[ANYA_MODEL_DIR="$withval"],
	[ANYA_MODEL_DIR="`pwd`/model"])
AC_SUBST(ANYA_MODEL_DIR)	


AC_CONFIG_FILES([
Makefile
src/Makefile
src/main.py
src/engine.py
src/factory.py
config/Makefile
config/anya/Makefile
config/gschema/Makefile
config/ibusengines/Makefile
config/ibusengines/anya.xml
])

AC_CONFIG_FILES(
[src/ibus-engine-anya],
[chmod +x src/ibus-engine-anya])

AC_OUTPUT
