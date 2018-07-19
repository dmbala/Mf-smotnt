#!/bin/bash
source /cvmfs/oasis.opensciencegrid.org/osg/modules/lmod/current/init/bash
module load gsl/2.3
./SMOTNT_working_osg_static "$@"
