# FindHepMC.cmake - Find HepMC2 library
#
# This module defines:
#  HEPMC_FOUND - system has HepMC
#  HEPMC_INCLUDE_DIR - the HepMC include directory
#  HEPMC_LIBRARIES - Link these to use HepMC
#  HEPMC_LIBRARY - HepMC library
#  HEPMC_VERSION - HepMC version

find_path(HEPMC_INCLUDE_DIR
  NAMES HepMC/GenEvent.h
  HINTS ${HEPMC_DIR} $ENV{HEPMC_DIR} ${HEPMC_ROOT} $ENV{HEPMC_ROOT}
  PATH_SUFFIXES include
)

find_library(HEPMC_LIBRARY
  NAMES HepMC
  HINTS ${HEPMC_DIR} $ENV{HEPMC_DIR} ${HEPMC_ROOT} $ENV{HEPMC_ROOT}
  PATH_SUFFIXES lib lib64
)

find_library(HEPMCFIO_LIBRARY
  NAMES HepMCfio
  HINTS ${HEPMC_DIR} $ENV{HEPMC_DIR} ${HEPMC_ROOT} $ENV{HEPMC_ROOT}
  PATH_SUFFIXES lib lib64
)

set(HEPMC_LIBRARIES ${HEPMC_LIBRARY})
if(HEPMCFIO_LIBRARY)
  list(APPEND HEPMC_LIBRARIES ${HEPMCFIO_LIBRARY})
endif()

# Extract version from HepMC/Version.h if available
if(HEPMC_INCLUDE_DIR AND EXISTS "${HEPMC_INCLUDE_DIR}/HepMC/Version.h")
  file(READ "${HEPMC_INCLUDE_DIR}/HepMC/Version.h" HEPMC_VERSION_FILE)
  string(REGEX MATCH "#define HEPMC_VERSION \"([0-9]+\\.[0-9]+\\.[0-9]+)\"" HEPMC_VERSION_MATCH ${HEPMC_VERSION_FILE})
  if(HEPMC_VERSION_MATCH)
    set(HEPMC_VERSION ${CMAKE_MATCH_1})
  endif()
endif()

include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(HepMC
  REQUIRED_VARS HEPMC_LIBRARY HEPMC_INCLUDE_DIR
  VERSION_VAR HEPMC_VERSION
)

mark_as_advanced(HEPMC_INCLUDE_DIR HEPMC_LIBRARY HEPMCFIO_LIBRARY)
