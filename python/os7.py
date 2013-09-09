#!/usr/bin/env python

import os
import stat


existing_permissions=stat.S_IMODE(os.stat(__file__).st_mode)


if not os.access(__file__,os.X_OK):
    print 'Adding execute permssion'
    new_permissions = existing_permissions | stat.S_IXUSR
else:
    print 'Removing execute permssion'
    new_permissions = existing_permissions ^ stat.S_IXUSR

os.chmod(__file__,new_permissions)

