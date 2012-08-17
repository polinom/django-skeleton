#!/usr/bin/env python
#
# This script is designed to  rename the default skeleton project name (myproject) and app (myfirstapp) to names you choose
#
import os, sys

CURRENT_DIRECTORY    = os.getcwd()
CURRENT_PROJECT_NAME = 'myproject'
CURRENT_APP_NAME     = 'myfirstapp'
GITHUB_CLONE_CMD     = 'git clone https://github.com/mschettler/django-skeleton.git'

BAR80 = '-'*80

################################################################################
# Helper functions
################################################################################

def get_user_feedback():
    """ get user feedback, failing nicely if they kill it during input """
    try:
        return raw_input().strip()
    except KeyboardInterrupt:
        print 'The script was killed. Goodbye!'
        sys.exit(0)


def validate_name(name):
    """ 
    returns None on success, otherwise an error message is returned describing
    why the name failed to validate
    """

    if ' ' in name:
        return 'Error: Name cannot contain spaces'
    
    # name passed validation
    return None


def get_folder_list_for_directory(path, ignorehidden=True):
    """ returns a list of dirs found at the given path """

    if not os.path.isdir(path):
        raise Exception('Invalid path "%s" passed to get_folder_list_for_directory(), does not appear to be a directory.') % path

    ret = [d for d in os.listdir(path) if os.path.isdir(d)]

    if ignorehidden:
        ret = [d for d in ret if not d.startswith('.')]

    return ret


def rename(oldpath, newpath):
    if not (oldpath and newpath):
        raise Exception('Failed to supply a paramter to rename()')
    if os.path.exists(newpath):
        raise Exception('Cannot rename, newpath [%s] already exists' % newpath)
    if not os.path.exists(oldpath):
        raise Exception('Cannot rename, oldpath [%s] does not exist' % old)

    print '%s: Renamed %s to %s' % (__file__, oldpath, newpath)
    os.rename(oldpath, newpath)


################################################################################
# Some sanity checks
################################################################################

# make sure we were executed from the proper directory
if not CURRENT_DIRECTORY.endswith('django-skeleton'):
    print 'Error: Script cannot continue'
    print '    * We seem to be in directory "%s", but we need to be in the django-skeleton/ directory. Please navigate there and run this script again.' % CURRENT_DIRECTORY
    print '    * If you need to re-download a fresh copy of this repo, please execute the command "%s"' % GITHUB_CLONE_CMD
    sys.exit(1)


# lets see if we can find myproject
if not CURRENT_PROJECT_NAME in get_folder_list_for_directory(CURRENT_DIRECTORY):
    print 'Error: Script cannot continue'
    print '    * We failed to find "%s" in directory "%s". This might have happened because you already renamed the project.' % (CURRENT_PROJECT_NAME, CURRENT_DIRECTORY)
    print '    * This script depends on an exact file structure to work properly.'
    print '    * If you need to re-download a fresh copy of this repo, please execute the command "%s"' % GITHUB_CLONE_CMD
    sys.exit(1)


################################################################################
# Main script routine - get a new name for the project
################################################################################

inputerror = True

while inputerror:

    print BAR80
    print 'Your current project name is "%s". Please enter a new outer project name (blank to skip): ' % CURRENT_PROJECT_NAME
    new_project_name = get_user_feedback()

    inputerror = validate_name(new_project_name)
    if inputerror:
        print inputerror

# they entered a valid name
if new_project_name:
    print 'You entered "%s" as your new project name.' % new_project_name
else:
    print 'You skipped renaming your default project. The current name of "%s" still stands.' % CURRENT_PROJECT_NAME


################################################################################
# Main script routine - get a new name for the app
################################################################################

inputerror = True

while inputerror:

    print BAR80

    print 'Your current default app name is "%s". Please enter a new app name (blank to skip): ' % CURRENT_APP_NAME
    new_app_name = get_user_feedback()

    inputerror = validate_name(new_app_name)
    if inputerror:
        print inputerror

# they entered a valid name
if new_app_name:
    print 'You entered "%s" as your new default app name.' % new_app_name
else:
    print 'You skipped renaming your default app. The current name of "%s" still stands.' % CURRENT_APP_NAME


################################################################################
# Main script routine - actually rename projects
################################################################################

print BAR80

if not new_app_name and not new_project_name:
    print 'You decided not to rename your project or app. This script has nothing to do. Goodbye!'


# walk the directory and perform renames
for root, dirs, files in os.walk(CURRENT_DIRECTORY):
    # print 'root: ', root
    # print 'dirs: ', dirs
    # print 'files: ', files
    if CURRENT_PROJECT_NAME in dirs or CURRENT_PROJECT_NAME in files:
        rename(os.path.join(root, CURRENT_PROJECT_NAME), os.path.join(root, new_project_name))








