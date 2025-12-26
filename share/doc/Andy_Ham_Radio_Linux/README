
Getting Started with Andy's Ham Radio Linux (AHRL)
==================================================

Please don't deviate from the instructions below.
Other Linux distributions which are based on Ubuntu *might* work.


Supported Hardware
==================

* Must be a 64-bit CPU architecture, e.g. x86_64 or aarch64
* Raspberry Pi:  ONLY the RPI 4 and RPI 5 are supported.  Note that
  a RPI 400 contains an RPI 4, and a RPI 500 contains an RPI 5, thus
  they are supported.
* Any machine with less than 2GB of memory is not supported


These are the currently tested configurations.
Software was updated in November 2025 from these base configurations.
====================================================================

  * 64-bit Raspberry Pi OS version 5.5
    * Raspberry Pi 5 (8GB memory)
    * Raspberry Pi 4 (2GB memory but IMHO sluggish performance)
    * Supports the multitiered menu structure preferred by AHRL
	
  * The following configurations were tested on Virtualbox
    with 2 CPUs and either 4GB or 8GB of memory:

    * Xubuntu 24.04.3 (Desktop)
      - XFCE supports the multitiered menu structure preferred by AHRL

    * Kubuntu 24.04 (normal installation)
	
    * Linux Mint 22 (Cinnamon)

    * Debian 12.12 (XFCE)
      - XFCE supports the multitiered menu structure preferred by AHRL
      - cat /etc/debian_version

    * LMDE 6 - Linux Mint Debian Edition 12.1

  * One user reported that it works on Zorin OS (a Debian derivative).
    I have not tested this version, but I wouldn't be surprised if it worked.

* Some of the tested configurations don't have the multitiered menus found
  in XFCE.  Thus, the AHRL menu will be one giant flat menu with many entries
  (not very nice IMHO).  If you have suggestions for improvement, please send
  them to the author.

* Sometimes a program will work on one flavor of Linux but not another.  For
  example, some programs don't work on the Raspberry Pi but work fine on other
  computers.  In these cases, it likely isn't a bug in AHRL, but please report
  this so I can check.


Configurations which are explicitly NOT supported in v26e
=========================================================

* Linux Mint 21.3 (Cinnamon) is EXPLICITLY NOT SUPPORTED
  - dummy output audio issues
  - replace pipewire with pulseaudio helps
  - wsjtx doesn't recognize any audio inputs or outputs
  - don't go here ... just don't ... it is known NOT to work

* Debian 13 - it will be supported during the next release of AHRL

* Ubuntu 25.* - these versions will never be officially supported since
                they are not long term support versions (LTS).


Storage requirements on Raspberry Pi (OS plus AHRL files)
=========================================================

*  8GB - not enough storage
* 16GB - adequate storage
* 32GB - plenty of storage!
* 64GB - plenty of storage!

The installation requires about 10GB of storage and is checked by the
installation script in a function called check_storage().


Memory requirements - all systems
=================================

*  2GB - not enough
*  4GB - this is enough!
*  8GB - this is more than enough!
* 16GB - even more is better :-)

The amount of memory is checked by the installation script in a function called
check_memory().  If 2GB or less of memory are detected, the installation script
will print an error and terminate.


Network requirements - all systems
==================================

The network must be properly configured and up.  A new addition for version 26d
is for the installation to explicitly check that the network is up and running.
If it is not, the script will immediately terminate.  

Many files are installed from a repository, and some files are downloaded from github.
This cannot happen if the network is down or misconfigured.  The network is checked
in the check_network() function, found in the /usr/local/bin/install_ahrl script.


Additional Notes
================

The ability to install the software is only one consideration.  Does your
computer have enough memory and a sufficiently fast CPU to execute the
software to your satisfaction?

In theory, this script SHOULD work on any Ubuntu based Linux distribution.
Some distributions have been tested and are listed above.  If you try something
different, please let me know the result so I can update the list of working
distributions.  If things don't work, please let me know.  It may be possible
for me to fix it to work on your favorite Ubuntu based Linux distribution.

The preference is to run this script on a clean copy of a supported flavor
of Linux.  That said, you can run it on your current setup and it should work fine.
Further, it works if you run the script today, and then again 3 months from now
to get any updated software.


Install Software Faster
=======================

On the author's computer, it takes about 2.5 hours to install the software when
using 1 CPU.  In the /usr/local/bin/install_ahrl script, there's a variable
called NUM_CPUS.  The following setting for NUM_CPUS *should* work for you and
thus speed up the installation time.  NUM_CPUS=1 is very conservative but works
in every case so far.  If you're unsure, leave it alone.  If you change it,
especially on a Raspberry Pi, be VERY sure that your cooling system is sufficient.

Recommended settings which SHOULD work:
  - 4GB memory -> NUM_CPUS=2
  - 8GB memory -> NUM_CPUS=4
  - more than 8GB of memory -> NUM_CPUS=`nproc` (go for it!)


Customizing the programs to be installed
========================================

The user might wish to have more control over the software that is installed.
For example, if one is involved with EMCOMM and uses the NBEMS software, one
might not want AHRL to overwrite the installation of flmsg.

To accomplish this task, open the /usr/local/bin/install_ahrl script with a
text editor and notice the following lines:

INSTALL_FLMOXGEN=1
INSTALL_FLMSG=1
INSTALL_FLNET=1

These lines are of the general format:  INSTALL_<name_of_software>={0,1}

For every program that is understood by the AHRL installation script, there is
one such line.  If it is set to 1 (one), the software will be installed.  If
the user edits the file and sets it to 0 (zero), the software will NOT be
installed.

For example:

INSTALL_FLMSG=1 means that AHRL will install the FLMSG software.
INSTALL_FLMSG=0 means that AHRL will NOT install the FLMSG software.


Installation Instructions
=========================

The network (wired or wireless) MUST be working properly or the installation
will fail.

Download the files from Sourceforge:
  * Replace "v26d" with the most recent version available
  * andy_VER.tar.gz, e.g. andy_v26d.tar.gz
  * md5sum_vVER.txt, e.g. md5sum_v26d.txt
  * move the file to /root (e.g. sudo mv andy_VER.tar.gz /root)
  
Verify the md5sum to ensure the download was good:
  * md5sum andy_VER.tar.gz
  * cat md5sum_vVER.txt
  * be sure that the md5sums match

Unpack the andy_VER.tar.gz file thus:
  * sudo -i
  * cd /usr/local
  * tar xzvf /root/andy_VER.tar.gz (again, replacing VER with the actual
    version information)

Optional: edit install_ahrl to change NUM_CPUS for faster installation (see above).
Optional: customize the list of installed software to match your preferences (see above).

Run the installation script:
  * cd /usr/local/bin
  * ./install_ahrl 2>&1 | tee out.txt
  
  * While it is running, in another terminal, you can optionally do the
    following to watch the progress of the installation:

	* sudo -i
	* cd /usr/local/bin
	* tail -f out.txt | grep AHRL:
	
Useful debug info will be in the file "out.txt".

Some questions will be asked during the installation.

  - When asked "What is the username of the default user?",
    enter the name of the account where ham radio software will be run.
      For example, if your user name is "andy", enter "andy" (without the
      double quotes).

  - Use the TAB key to select the desired answer (if multiple choice) and then
    hit enter when asked the following questions:
    - For dump1099, the recommended answer is "no"
    - For xastir, the recommended answer is "yes" or "OK"

  - You may see a message similar to this one:
      - Archive:  /usr/local/tarballs/js8spotter-115_src.zip
      - replace js8spotter-115_src/1.wav?  [y]es, [n]o, [A]ll, [N]one, [r]ename

      - type the capital letter A and hit enter, which will cause all files in
        the directory to be replaced.


Post Installation Steps
=======================

At the end of the installation, there will be a few things for the user to
note.  This will be shown in the terminal window where the install_ahrl
script was executed.

Once the installation completes, reboot the computer.

After the reboot, log in to the "default user" account specified during the
installation.

Check the menus and see if there is an entry called "Andy_Ham_Radio_Linux"
with several ham radio related submenus.

On some systems, there won't be a menu called "Andy_Ham_Radio_Linux", but each
program will have its own menu.


Filing a bug report
===================

If you need to file a bug report, certain information must be supplied.  I will
try to duplicate the issue in VirtualBox.

* the name and version of your Linux distribution
* the version of AHRL (either from the tar file or the version command)
* the out.txt file
* a screenshot showing the error or issue
* Please post the info on Sourceforge in the bugs module


Changing the background
=======================

Background files live here:  /usr/local/share/ahrl/backdrops

  - Right-click on the background and select "Desktop Settings".
  - Folder -> Other and select the aforementioned directory.
  - Pick the desired background.


Upgrading from one AHRL version to the next
===========================================

Instructions:

  - In a terminal window, type the "version" command and note which version
    you are currently using.

  - Make sure that the newer version has been tested on your desired version
    of Linux (see GETTING_STARTED).

  - If your version of Linux is OLD, this may not work.

  - Download the newer version of AHRL.

  - Read the GETTING_STARTED document and just install it on top of the old
    AHRL version.

  - If this fails, reinstall the version that you noted in the first
    instruction.

  - Naturally, all permutations cannot be supported.


Workarounds
===========

No audio, only the Dummy Output:

  - /usr/local/bin/fix_sound
      OR
  - In the AHRL Menu -> Workarounds -> Fix Sound

  - Unfortunately, this usually must be done after EVERY reboot, but once is
    enough.

  - It has been recently discovered that this workaround only has a chance
    to succeed on systems running ALSA.  Some systems are running pulseaudio.
    I don't have a workaround for that case.  This issue comes and goes and
    is not a bug in AHRL.  I've seen internet posts about this issue from
    many years ago.


Error updating HamClock
=======================

If HamClock asks you to upgrade to a newer version, and you click Yes, but an error occurs,
try typing this at the command line:

sudo hamclock

That will allow HamClock to upgrade to the new version.  Subsequently, HamClock will work
as expected from the menu without the additional privileges.


AMS 29-Nov-2025
