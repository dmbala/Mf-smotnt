
## Evolutionary dynamics - Collection of jobs with makeflow

## Overview

[Makeflow](http://ccl.cse.nd.edu/software/makeflow/) is a workflow engine that handles a large number
of jobs. The following are characteristics of Makeflow.

*    `Master/Workers paradigm`  The master monitors and controls the workers while the workers complete the tasks.
master monitors and controls the workers.
*    `Parallel job execution` Jobs are executed in parallel as much as possible.
*    `Fault tolerant` In case of failure, the jobs are continued from where they are stopped.
*    `UNIX tool Make` The syntax of Makeflow is similar to the popular UNIX tool Make. The Make rules are
convenient in describing the job dependencies.


## Steps on OSG

Step 0: Keep all the relevant files in the work directory (argarray_1.txt, wrapper.sh, executable, input gene data, etc.)

 
Step 1: Generate the makeflow file
 $ python generate_makeflow_fromlist.py > my-workflow.mf

Step 2: 
  $ module load cctools/5.4.7
 Run a screen session
  $ screen  
  $ makeflow -T condor --max-remote 1000 my-workflow.mf &

 To finally close the screen session after completion of workflow, quit the screen as follows. 
  $ screen -ls 
There is a screen on:
        2883478.pts-1.login02   (Attached)
1 Socket in /var/run/screen/S-dbala.
 
  $ screen -X -S "2883478.pts-1.login02" quit

## Steps on Amarel

Similar to OSG set up except the following changes. 
1) Add SLURM specific details in the header of makeflow file 
2) While submitting the make file, provide slurm option -T slurm and --shared-fs / for filesystem


