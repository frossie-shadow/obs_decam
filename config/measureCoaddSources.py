from lsst.meas.algorithms import LoadIndexedReferenceObjectsTask
config.match.refObjLoader.retarget(LoadIndexedReferenceObjectsTask)
config.match.refObjLoader.ref_dataset_name = "ps1_pv3_3pi_20170110"
config.match.refObjLoader.filterMap['u'] = 'g'
