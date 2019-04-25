# Use the natural-service-base image as a parent image
FROM miketrout/natural-service-base

# Copy the Natural source code into the custom fuser
COPY ./Natural-Libraries/MAIN /fuser/MAIN

# Copy ./service to /service
COPY ./service /service

# Start the buffer pool
# and then run the ftouch utility to build a new FILEDIR.SAG
# and then set up a command file to CATALL library MAIN
# and then start Natural in batch mode and run the command file
# and then remove the command file
# and then check the output of catall and remove the temporary file
RUN natbpsrv bpid=natbp \
    && ftouch lib=main sm -s -d \
    && printf "LOGON MAIN\nCATALL ** ALL TYPES ** CATALOG\nFIN\n" > /tmp/cmd \
    && natural batchmode cmsynin=/tmp/cmd cmobjin=/tmp/cmd cmprint=/tmp/out natlog=err \
    && rm /tmp/cmd \
    && cat /tmp/out && rm /tmp/out
