import viz

import vizfx

import vizconnect

‍

vizconnect.go('vizconnect_config_trackers.py')

‍

tracker = vizconnect.getTracker('steamvr_tracker').getNode3d()

‍

ball = vizfx.addChild('basketball.osgb')

‍

trackerLink = viz.link(tracker,ball)