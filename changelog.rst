Changelog
=========

%%version%% (unreleased)
------------------------

Fix
~~~

- Bugfix: changed reference from composites.cfg to
  composites/generic.cfg. [Martin Raspaud]

- Bugfix: works now for file auto discovery. [Martin Raspaud]

- Bugfix: get_filename wants a reader_instance and cleanup. [Martin
  Raspaud]

Other
~~~~~

- Update changelog. [Martin Raspaud]

- Bump version: 1.1.0 → 2.0.0-alpha.1. [Martin Raspaud]

- Add config files for release utilities. [Martin Raspaud]

  We add the .bumpversion.cfg and .gitchangelog.rc for easy version bumping
  and changelog updates.

- Remove v from version string. [Martin Raspaud]

- Add str and repr methods for composites. [Martin Raspaud]

  This add simple repl and str methods for compositors.

- Restructure the documentation for satpy2. [Martin Raspaud]

  This is an attempt to reorganize the documentation to prepare for satpy2.
  Old stuff has been take away, and a fresh quickstart and api are now
  provided.

- Improve the ReaderFinder ImportError message to include original
  error. [Martin Raspaud]

  To make the ImportError more useful in ReaderFinder, the original error
  string is now provided.

- Fix save_dataset to allow both empty filename and writer. [Martin
  Raspaud]

  When saving a dataset without a filename and writer, save_dataset would
  crash. Instead, we are now putting writer to "simple_image" in that case.

- Rename projectable when assigning it through setitem. [Martin Raspaud]

  When a new dataset is added to a scene, it's name should match the string
  key provided by the user.

- Remove references to deprecated satpy.projector. [Martin Raspaud]

- Allow resample to receive strings as area identifiers. [Martin
  Raspaud]

  In resample, the interactive user would most likely use pre-defined areas
  from a custom area file. In this case, it's much easier to refer to the
  area by name, than to get the area definition object from the file. This
  patch allows the `resample` projectable method to work with string ids
  also.

- Add a dataset to whishlish when added with setitem. [Martin Raspaud]

  When adding a dataset to a scene via the datasetdict.__setitem__ method,
  it is likely that the user case about this dataset. As such, it should be
  added to the wishlist in order not to get removed accidently.

- Move composite loading out of Scene to satpy.composites. [Martin
  Raspaud]

  The loading of compositors was a part of the Scene object. However, it does
  not belong there, so we decided to move it out of Scene. The next logical
  place to have it is the satpy.composites modules.
  As a conterpart, we now provide the `available_composites` method to the
  Scene to be able to figure out what we have possibility to generate.

- Fix the travis file to allow python 2.6 to fail. [Martin Raspaud]

- Allow travis to fail on python 2.6. [Martin Raspaud]

- Install importlib for travis tests on python 2.6. [Martin Raspaud]

- Add `behave` to the pip installations in travis. [Martin Raspaud]

- Add behaviour testing to travis and coveralls. [Martin Raspaud]

- Add behaviour tests for showing and saving datasets. [Martin Raspaud]

  Three scenarios were added, testing showing a dataset, saving a dataset,
  and bulk saving datasets (`save_datasets`).

- Fix loading behaviour tests. [Martin Raspaud]

  A little cleanup, and using builtin functions for getting the dataset_names

- Fix DatasetDict's setitem to allow empty md in value. [Martin Raspaud]

  Sometimes a dataset/projectable doesn't have any info attached to it, eg
  because the dataset is synthetic. In these cases, setitem would crash.
  This is now fixed, and if a string is provided as a key in setitem it is
  used as a name if no better name is already there.

- Simplify dataset saving to disk. [Martin Raspaud]

  saving datasets can now be done one by one. If a writer is not provided,
  it is guessed from the filename extension.

- Add a show method to the Scene class. [Martin Raspaud]

  That allows the user to interactively vizualize the data

- Add a default areas.def file. [Martin Raspaud]

- Fix the manifest file to include the config files. [Martin Raspaud]

- Add missing config files to setup.py. [Martin Raspaud]

- Fix setup.py to add cfg files. [Martin Raspaud]

  This is in order to make satpy work out of the box after a pip install.

- Add a behaviour test to find out the available dataset. [Martin
  Raspaud]

- Prevent crashing when a load requirement is not available. [Martin
  Raspaud]

  When requiring a band which isn't available, satpy would crash. This is now
  fixed and replaced by a warning in the log.

- Use behave to do higher level tests. [Martin Raspaud]

  Two small scenarios for testing the loading of the data are implemented now.

- Fix import error in scene. [davidh-ssec]

  A small refactor was done and then undone to move DatasetDict and DatasetID. This little import change wasn't properly cleaned up.


- Fix scene to work with "2 part" compositors and added pan sharpened
  true color composite as an example. [davidh-ssec]

- Added log message to pillow writer to say what filename it was saving
  to. [davidh-ssec]

- Handle optional dependencies for composites (not tested) [davidh-ssec]

- Activate the remaining viirs_sdr reader test cases. [Martin Raspaud]

- Remove the overview_sun TODO item. [Martin Raspaud]

- Fix the multiple load issue for composites. [Martin Raspaud]

  The composite loading would crash when several composites would be loaded
  one after the other. This was because composite config files where loaded
  partially but were considered loaded entirely. In order to fix this
  problem and make things simpler, we removed the composite config mechanism
  entirely, so that the composites are reloaded everytime. That allows both
  config changing on the fly, but also more resilience for multiple sensor
  cases, like one sensor is loaded after another, and the composites wouldn't
  get updated.

- Fix the name issue in sensor-specific composite requests. [Martin
  Raspaud]

  The read_composite_config was requiring wrongly that the provided names
  should be empty or None, making it not read the sensor config file at all.
  In turn that meant that generic composites were used instead of sensor-
  specific ones.

- Got metadata requests working for composites. [davidh-ssec]

- Use DatasetID in composite requirements instead of names and
  wavelengths only. [davidh-ssec]

- Adds ERF DNB composite and updates compositor base to allow for
  metadata and optional requirements although they are not completely
  used yet. [davidh-ssec]

- Added adaptive DNB product. [davidh-ssec]

- Fixed bug in scene when getting writer instance in save_images.
  [davidh-ssec]

- Fix the dataset str function to allow missing name and sensor keys.
  [Martin Raspaud]

- Add quickstart seviri to the documentation. [Martin Raspaud]

- Update the documentation. [Martin Raspaud]

- Add a get_writer function to the scene object. [Martin Raspaud]

- Updating dataset displaying. [Martin Raspaud]

- Add a fixme comment. [Martin Raspaud]

- Added histogram_dnb composite as a stepping stone for getting more
  complex composites added (ex. adaptive_dnb) [davidh-ssec]

- Can now retrieve channel with incomplete DatasetID instance. [Martin
  Raspaud]

- First try at loading metadata. [davidh-ssec]

- Added python 3.5 to travis tests and removed 3.x as allowed failures.
  [davidh-ssec]

- Added basic test for DatasetDict. [davidh-ssec]

- Refactored some file reader methods to properties to be more pythonic.
  [davidh-ssec]

- Viirs test case now works with python3 hopefully. [Martin Raspaud]

- Fixed file units for eps l1b reflectances. [davidh-ssec]

- Corrected frame indicator for eps l1b band 3a. [davidh-ssec]

- Updated eps l1b config with temporary calibration information.
  [davidh-ssec]

- First attempt at rewriting eps l1b reader to be more configurable
  (overkill?) [davidh-ssec]

- Renamed Scene projectables to datasets. [davidh-ssec]

- Updated eps l1b file reader to match base class. [davidh-ssec]

- Made generic single file reader abstract base class and cleaned up
  viirs sdr tests. [davidh-ssec]

- Added a fixme comment. [Martin Raspaud]

- Enable python 3 and osx builds in travis. [Martin Raspaud]

- Config treatment for enhancements. [davidh-ssec]

- Update config handling for finding composites. [davidh-ssec]

- Small fix for dumb environment variable clear on tests. [davidh-ssec]

- First attempt at getting readers and writers using PPP_CONFIG_DIR as a
  supplement to builtin configs. [davidh-ssec]

- Fixed scene tests so they pass. [davidh-ssec]

- Added base_dir for finding input files and a separate base_dir kwargs
  on save_images. [davidh-ssec]

- Makes wishlist a set and should fix problems with multiple loads.
  [davidh-ssec]

- Fixed calibration and other DatasetID access in reader, hopefully.
  [davidh-ssec]

- Fix the xrit reader. [Martin Raspaud]

- Cleanup to prepare for handling calibration better. [davidh-ssec]

- Updated filtering based on resolution, calibration, and polarization.
  [davidh-ssec]

- Updated how readers create dataset info and dataset ids. [davidh-ssec]

- Added calibration to DatasetID (not used yet) and added helper method
  on DatasetDict for filtering retrieved items and keys. [davidh-ssec]

- Renamed BandID to DatasetID. [davidh-ssec]

- Better handling of loading composite dependencies...i think. [davidh-
  ssec]

- Got EPS L1B reader working again with readers being given BandID
  objects. [davidh-ssec]

- Fixed small bug with extra empty string being listed as reader file
  pattern. [davidh-ssec]

- Made DatasetDict accept non-BandID keys during setitem. [davidh-ssec]

- Fixed default file reader for the eps l1b reader. [davidh-ssec]

- A little more cleanup of unused code in viirs sdr. [davidh-ssec]

- More work on viirs sdr using base reader class. [davidh-ssec]

- Started using ConfigBasedReader as base class for VIIRS SDR reader.
  [davidh-ssec]

- Fixed failing scene tests. [davidh-ssec]

- Got viirs sdr reader working with namedtuple dataset keys. [davidh-
  ssec]

- Continue on python3 compatibility. [Martin Raspaud]

- Cleanup. [Martin Raspaud]

- WIP: Start python 3 support. [Martin Raspaud]

- Smoother transition in the sun zenith correct imagery. [Martin
  Raspaud]

- Move reader discovery out of the scene and into satpy.readers. [Martin
  Raspaud]

  The class ReaderFinder was created for this purpose.

- Cleanup. [Martin Raspaud]

- Fix overview and natural composites. [Martin Raspaud]

- Make read and load argument lists consistent. [Martin Raspaud]

- Fix the M01 dataset definition in viirs_sdr.cfg. [Martin Raspaud]

- Fix some viirs composites. [Martin Raspaud]

- Fix viirs_sdr loading using start and end times. [Martin Raspaud]

- Introduce BandIDs to allow for more complex referencing of datasets.
  [Martin Raspaud]

  - Add the BandID namedtuple (name, wl, resolution, polarization)
  - Fix querying for compatibility with BandIDs
  - Fix existing readers for BandIDs

  Example usage from the user side:
  scn.load([BandID(wavelength=0.67, resolution=742),
            BandID(wavelength=0.67, resolution=371),
            "natural", "true_color"])

  BandIDs are now used internally as key for the scene's projectables dict.

- Add file keys to metop's getitem. [Martin Raspaud]

- Rename metop calibration functions. [Martin Raspaud]

- Add file keys for start and end times for metop. [Martin Raspaud]

- Merge the old eps l1b reader with the new one. [Martin Raspaud]

- More work on EPS l1b reader. [Martin Raspaud]

- Initial commit for the metop eps l1b reader. [Martin Raspaud]

- New attempt at calibration keyword in viirs sdr reader. [davidh-ssec]

- Renamed 'channel' to 'dataset' [davidh-ssec]

- Added more tests for VIIRS SDR readers before making calibration or
  file discovery changes. [davidh-ssec]

- Use "super" in the readers. [Martin Raspaud]

- Hopefully fixed py2.6 incompatibility in string formatting. [davidh-
  ssec]

- Added viirs sdr tests for MultiFileReader and HDF5MetaData. [davidh-
  ssec]

- More viirs sdr file reader tests. [davidh-ssec]

- Simple proof of concept for calibration level in viirs sdr reader.
  [davidh-ssec]

- Fixed getting end orbit from last file reader in viirs sdr reader.
  [davidh-ssec]

- Use unittest2 in viirs sdr tests so we can use new features. [davidh-
  ssec]

- Added unittest2 to py26 travis build to hopefully fix h5py
  importerror. [davidh-ssec]

- Added h5py and hdf5 library to travis. [davidh-ssec]

- Started adding basic VIIRS SDR reader tests. [davidh-ssec]

- Changed scene to accept sequence instead of *args. [davidh-ssec]

- Merge branch 'feature-simplify-newreader' into feature-simplify.
  [davidh-ssec]

- Added simple method for finding geolocation files based on header
  values. [davidh-ssec]

- Added rows per scan to viirs sdr metadata. [davidh-ssec]

- Got units and file units working for VIIRS SDR reader. [davidh-ssec]

- Cleaner code for viirs sdr scaling factor check and made sure to OR
  any previous masks. [davidh-ssec]

- Better memory usage in new style viirs sdr reader. [davidh-ssec]

- First step in proof of concept with new reader design. Mostly working
  VIIRS SDR frontend. [davidh-ssec]

- Fixed get_area_file in the resample.py module. [davidh-ssec]

- Allowed sensor to be specified in the reader section. [davidh-ssec]

- Added method to base plugin to determine type of a section. [davidh-
  ssec]

- Make sunzenithnormalize a modern class. [Martin Raspaud]

- Add sunz correction feature. [Martin Raspaud]

- Avoid an infinite loop. [Martin Raspaud]

- Add travis notifications to slack. [Martin Raspaud]

- Remove unneeded code for composites. [Martin Raspaud]

- Add a few composites. [Martin Raspaud]

- Cleanup. [Martin Raspaud]

- Allow json in enhancement config files. [Martin Raspaud]

- Switch on test for writers. [Martin Raspaud]

- Move tests for image stuff to corresponding test file. [Martin
  Raspaud]

- Move image stuff out of projectable into writers/__init__.py. [Martin
  Raspaud]

- Forgot to change reader/writer base class imports. [davidh-ssec]

- Moved reader and writer base classes to subpackages. [davidh-ssec]

- Reworked configuration reading in plugins for less redundancy.
  [davidh-ssec]

- Small fixes to make VIIRS SDR reader work with new resampling.
  [davidh-ssec]

- Fix the wishlist names and removing uneeded info when building RGB
  composites. [Martin Raspaud]

- Dataset is now a subclass of np.ma.MaskedArray. [Martin Raspaud]

- Move determine_mode to projectable. [Martin Raspaud]

- Add helper function to read config files and get the area def file.
  [Martin Raspaud]

- Rename precompute kwarg to cache_dir. [Martin Raspaud]

- Convenience enhancements for resample. [Martin Raspaud]

  - we can now provide "nearest" or "kdtree" instead of a resampler class.
  - The precompute/dump kwarg is now a directory where to save the proj info,
    defaulting to '.' if precompute=True.

- Switch to containers in travis. [Martin Raspaud]

- Fix repo in .travis. [Martin Raspaud]

- Add OrderedDict for python < 2.7. [Martin Raspaud]

- Resample is now feature complete. [Martin Raspaud]

  - Dump kd_tree info to disk when asked
  - Cache the kd_tree info for later use, but cache is cleaned up.
  - OO architecture allowing other resampling methods to be implemented.
  - resampling is divided between pre- and actual computation.
  - hashing of areas is implemented, resampler-specific.

- Fixed bad patch on new scene test. [davidh-ssec]

- First try at more scene tests. [davidh-ssec]

- Move image generation methods to Dataset and move enh. application to
  enhancer. [Martin Raspaud]

- Sensor is now either None, a string, or a non-empty set. [Martin
  Raspaud]

- Forgot to actually use default writer config filename. [davidh-ssec]

- Fixed simple scene test for checking ppp_config_dir. [davidh-ssec]

- Slightly better handling of default writer configs and writer
  arguments. [davidh-ssec]

- Add a writer for png images, and move enhancer to satpy.writers.
  [Martin Raspaud]

- Detached the enhancements handling into an Enhancer class. [Martin
  Raspaud]

- Pass ppp_config_dir to writer, still needs work. [davidh-ssec]

- First attempt at configured writers and all the stuff that goes along
  with it. Renamed 'format' in configs to more logical name. [davidh-
  ssec]

- Remove the add_product method. [Martin Raspaud]

- Cleanup scene unittest. [Martin Raspaud]

- Finish testing scene.get_filenames. [Martin Raspaud]

- Testing scene.get_filenames. [Martin Raspaud]

- Updated tests to test new string messages. 100%! [davidh-ssec]

- Merge branch 'pre-master' into feature-simplify. [Martin Raspaud]

  Conflicts:
  	satpy/satellites/__init__.py
  	satpy/satin/helper_functions.py
  	satpy/satin/mipp_xrit.py

- Cleanup. [Martin Raspaud]

- Change printing of projectables and cleanup. [Martin Raspaud]

- Start testing satpy.scene. [Martin Raspaud]

- Fixed assertIn for python 2.6. [davidh-ssec]

- Added more tests for projectables and updated projectable 3d resample
  test. 100% coverage of projectable! [davidh-ssec]

- Renamed .products to .compositors and fixed unknown names bug.
  [davidh-ssec]

- Added check to see what composite configs were read already. [davidh-
  ssec]

- Do not reread already loaded projectables. [Martin Raspaud]

- Complete .gitignore. [Martin Raspaud]

- Fix unittests for python 2.6. [Martin Raspaud]

- Unittesting again... [Martin Raspaud]

- More unittesting. [Martin Raspaud]

- Fix projectables str to look better. [Martin Raspaud]

- More unittesting. [Martin Raspaud]

- Fix unittests for python 2.6. [Martin Raspaud]

- Still cleaning up. [Martin Raspaud]

- Cleanup. [Martin Raspaud]

- Add tests to the package list in setup.py. [Martin Raspaud]

- Make pylint happy. [Martin Raspaud]

- Fix tests for projectable to pass on 2.6. [Martin Raspaud]

- Start testing the new stuff in travis. [Martin Raspaud]

- Cleanup. [Martin Raspaud]

- Renamed newscene to scene. [Martin Raspaud]

- Moved updated readers from satpy.satin to satpy.readers. [Martin
  Raspaud]

- Changed 'uid' to 'name' for all new components. [davidh-ssec]

- Moved composite configs to separate subdirectory. [davidh-ssec]

- Add an RGBCompositor class and cleanup. [Martin Raspaud]

- Allow passing "areas" to mipp_xrit. [Martin Raspaud]

- Fix the overview composite giving sensible defaults. [Martin Raspaud]

- Fixed bug with RGB composites with passing the wrong info keywords.
  [davidh-ssec]

- Changed sensor keyword in scene to reader and added new sensor keyword
  behavior to find readers based on sensor names. [davidh-ssec]

- Changed new style composites to use a list of projectables instead of
  the scene object implemented __setitem__ for scene. [davidh-ssec]

- Reworked viirs and xrit reader to use .channels instead of .info.
  Simplified reader loading in newscene. [davidh-ssec]

- Test and fix projectable. [Martin Raspaud]

- Allow reading from wavelength, and add Meteosat HRIT support. [Martin
  Raspaud]

- Moved reader init to scene init. Successfully created resampled fog
  image using composite configs. [davidh-ssec]

- Added some default configs for new scene testing. [davidh-ssec]

- Started rewriting viirs sdr reader to not need scene and produce
  projectables. [davidh-ssec]

- Better config reading, and scene init. [Martin Raspaud]

- WIP: removed CONFIG_PATH and changed projectables list into dict.
  [davidh-ssec]

- Add resampling. Simple for now, with elementary caching. [Martin
  Raspaud]

- WIP. [Martin Raspaud]

  * Product dependencies
  * loading from viirs
  * generating images

- WIP: successfully loaded the first viirs granule with newscene!
  [Martin Raspaud]

- Rewriting scene. [Martin Raspaud]

- Add helper function to find files. [Martin Raspaud]

- Fix the config eval thing in scene. [Martin Raspaud]

v1.2.1 (2015-12-14)
-------------------

- Update changelog. [Martin Raspaud]

- Bump version: 1.2.0 → 1.2.1. [Martin Raspaud]

- Merge branch 'pre-master' [Martin Raspaud]

- Merge branch 'pre-master' [Martin Raspaud]

  Conflicts:
  	doc/source/pp.rst

- Update changelog. [Martin Raspaud]

- Bump version: 1.1.0 → 1.2.0. [Martin Raspaud]

- Merge branch 'pre-master' [Martin Raspaud]

  Conflicts:
  	satpy/version.py
  	setup.py


v1.2.0 (2015-12-14)
-------------------

Fix
~~~

- Bugfix: converted MSG products should be saveable. [Martin Raspaud]

- Bugfix: satellite name in msg_hdf now supports missing number. [Martin
  Raspaud]

- Bugfix: misspelling. [Martin Raspaud]

- Bugfix: mipp_xrit: do not crash on unknown channels, just warn and
  skip. [Martin Raspaud]

- Bugfix: setup.py includes now eps xml format description. [Martin
  Raspaud]

- Close all h5files in viirs_sdr, not only the last one.
  [Martin.Raspaud]

- Bugfix: close h5 files when done. [Martin Raspaud]

  Prior to h5py 3.0, the h5 files open with h5py are not closed upon
  deletion, so we have to do it ourselves...

- Bugfix: area.id doesn't exist, use area.area_id. [Martin Raspaud]

- Bugfix: return when each file has been loaded independently. [Martin
  Raspaud]

- Bugfix: Do not crash on multiple non-nwc files. [Martin Raspaud]

- Bugfix: check start and end times from loaded channels only. [Martin
  Raspaud]

- Bugfix: viirs start and end times not relying on non-existant channels
  anymore. [Martin Raspaud]

- Bugfix: type() doesn't support unicode, cast to str. [Martin Raspaud]

Other
~~~~~

- Update changelog. [Martin Raspaud]

- Bump version: 1.1.0 → 1.2.0. [Martin Raspaud]

- Add template parameters for NOAA-19 ears-nwc. [Adam.Dybbroe]

  Parameters needed if you want to load only with time_interval and
  not using the filename argument

- Merge branch 'pre-master' of github.com:pytroll/satpy into pre-master.
  [Adam.Dybbroe]

- Merged (by hand) sentinel1-feature branch. [Lars Orum Rasmussen]

- Added support for gdal's SetNoDataValue if fill_value is not None.
  [Lars Orum Rasmussen]

- Merge branch 'pre-master' of github.com:pytroll/satpy into pre-master.
  [Lars Orum Rasmussen]

- Added a RGB example. [Lars Orum Rasmussen]

- Don't use colormaps for 16b grayscale (Ninjo will fail enhancements)
  [Lars Orum Rasmussen]

  For 16b IR, if specified, set min-is-white

  For 16b grayscale, it seems that transparent pixel (in Ninjo) are forced to be zero

  Transparent pixel for 16b IR are handled bad


- Add template config for ears-nwc Metop-B reading. [Adam.Dybbroe]

- Fix bug when using time_interval argument loading ears-nwc data.
  [Adam.Dybbroe]

- Add brightness temperature calibration to the IR bands. [Adam.Dybbroe]

- Update EARS config files for new (2014) PPS product format.
  [Adam.Dybbroe]

- Remove old FY3 mersi reader. [Adam.Dybbroe]

- Apply VIS/NIR calibration including sun-zenith correction.
  [Adam.Dybbroe]

- Merge branch 'pre-master' of github.com:pytroll/satpy into pre-master.
  [Adam.Dybbroe]

- Now ninjotiff can list tags. [Lars Orum Rasmussen]

  Ninjo tags are now a dictionary


- Add FY-3B template config file. [Adam.Dybbroe]

- Add first draft FY3B VIRR reader. [Adam.Dybbroe]

  No calibration yet, but counts can be projected and displayed

- Added contributions from Christian (DWD) to ninjotiff: now using
  tifffile.py and support for RGBA. [Lars Orum Rasmussen]

  Changed scaling into a value range (so it works for me)


- Merge branch 'pre-master' of https://github.com/pytroll/satpy into pre-
  master. [Panu Lahtinen]

- Delete world_map.ascii. [Martin Raspaud]

- Read DNB using PyTables, separate read() to read_m() and read_dnb()
  [Panu Lahtinen]

- Update coords2area_def with preview mode. [Martin Raspaud]

- Merge branch 'pre-master' of https://github.com/pytroll/satpy into pre-
  master. [Panu Lahtinen]

- Remove debug printout from pps reader. [Adam.Dybbroe]

- Support a list of files which will be concatenated, enables usage of
  granule data. [Panu Lahtinen]

- Fix for channel names and channel loading. [Panu Lahtinen]

- Added Himawari-8 config template file. [Martin Raspaud]

- Mask out 0-counts areas in aapp_l1b. [Martin Raspaud]

- Support saving GeoImages in IO buffers. [Martin Raspaud]

- Add support for noaa gac and lac data. [Martin Raspaud]

- Take care of fill_value in datasets. [Adam.Dybbroe]

- Merge branch 'pre-master' of github.com:pytroll/satpy into pre-master.
  [Adam.Dybbroe]

- Fix the sun zenith angle correction fix. [Martin Raspaud]

- Do not check time_slot type. [Martin Raspaud]

- Bugfix ctth scaling: Only keep same datatype if data are not scaled.
  [Adam.Dybbroe]

- Less debug info. [Adam.Dybbroe]

- Bugfix. Sun zenith correction can now take an additional keyword - and
  data are masked out accordingly. [Adam.Dybbroe]

- Fix overview_sun, avoid redish rgb's when sun is very low (below
  horizon) [Adam.Dybbroe]

- Read also the palette data etc. [Adam.Dybbroe]

- Merge branch 'pre-master' of github.com:pytroll/satpy into pre-master.
  [Adam.Dybbroe]

- Add orbit number info in the scene metadata upon loading. (hdfeos)
  [Martin Raspaud]

- Hdfeos: orbit number is now an int. [Martin Raspaud]

- Fix geolocation reading for multiple-file processing (hdfeos) [Martin
  Raspaud]

- Changed error message to a warning. [Adam.Dybbroe]

- Fix hdf_eos to allow reading several granules. [Martin Raspaud]

- Enhancing the dnb_overview, so that pixels with solar contamination
  are masked out. [Adam.Dybbroe]

- Bringing back the night_overview (=cloudtop) [Adam.Dybbroe]

- Comment out the night_overview. [Adam.Dybbroe]

- Merge branch 'pre-master' of github.com:pytroll/satpy into pre-master.
  [Adam.Dybbroe]

- Bugfix overview_sun. [Martin Raspaud]

- Use builtin sunzen_corr for overview_sun. [Martin Raspaud]

- Switch to nullterm string in msg_hdf for nr products. [Martin Raspaud]

- Bugfix. [Adam.Dybbroe]

- Improve overview for viirs and overview_sun. [Adam.Dybbroe]

- Re-introduce the fix for VIIRS bowtie deletions. [Adam.Dybbroe]

- Shouting when both a list of file names and a time interval is used.
  Accepts tine_interval even for local files. [Adam.Dybbroe]

- Merge branch 'pre-master' of github.com:pytroll/satpy into pre-master.
  [Adam.Dybbroe]

  Conflicts:
  	satpy/satin/nc_pps_l2.py

- Fixed incorrect production sources and geolocation file names for
  'local' products. [Panu Lahtinen]

- Added a unit test to the nc_pps_l2 reader, and adapted the reader a
  bit. [Adam.Dybbroe]

- Merge branch 'pre-master' of https://github.com/pytroll/satpy into pre-
  master. [Panu Lahtinen]

- Fixme reminder. [Adam.Dybbroe]

- Restructure how the data and geolocation files are listed and read.
  [Panu Lahtinen]

- Fixed workaround for DIMENSION_LIST attributes. [Panu Lahtinen]

- Minor fixes - thanks Panu! [Adam.Dybbroe]

- Cleaning up a bit and pep8. [Adam.Dybbroe]

- Merge branch 'pre-master' of github.com:pytroll/satpy into pre-master.
  [Adam.Dybbroe]

- Updated reading to support both M and DNB channel data. [Panu
  Lahtinen]

- Adapt navigation to compact_viirs dnb. [Martin Raspaud]

- Do not crash when an unknown channel is requested in msg_hdf. [Martin
  Raspaud]

- Fix template files. [Adam.Dybbroe]

- Fix template files for NOAA satellites and Metop-A/B. [Adam.Dybbroe]

- Bugfix, treating cases when no geolocation is found for product.
  [Adam.Dybbroe]

- More debug info. [Adam.Dybbroe]

- More debug info. [Adam.Dybbroe]

- Fix save function and bugfix. [Adam.Dybbroe]

- More debug info and better exception handling - pps reader.
  [Adam.Dybbroe]

- Rewritten the netCDF4 PPS reader. [Adam.Dybbroe]

- Cleaning up for unused code. [Adam.Dybbroe]

- Add the info attribute to NordRadCType. [Martin Raspaud]

- Fix filename search in msg_hdf. [Martin Raspaud]

- Fix extension problem in product search for msg_hdf. [Martin Raspaud]

- Replace pyhl with h5py in msg_hdf reader. [Martin Raspaud]

- Bugfix ascat l2 reader. [Adam.Dybbroe]

- Trying to fix odd behaviour when loading list of products. But it
  still doesn't work - need a small refactoring. [Adam.Dybbroe]

- Added support option to select granules in time interval.
  [Adam.Dybbroe]

- More debug info - for custom compositer. [Adam.Dybbroe]

- Merge pull request #17 from spareeth/pre-master. [Martin Raspaud]

  ASCAT SAR soil moisture level 2 netcdf data from EUMETSAT

- Add new reader and config files for ASCAT SAR soil moisture level 2
  netcdf data from EUMETSAT. [Sajid Pareeth]

- Add new reader and config files for ASCAT SAR soil moisture level 2
  netcdf data from EUMETSAT. [Sajid Pareeth]

- Added possibility to read granule data from EARS, also some PEP8 work.
  [Panu Lahtinen]

- Avoid leaking memory. [Martin Raspaud]

- Bugfix. [Adam.Dybbroe]

- Raise an error if projection is attempted when swathdata doesn't have
  full geolocation. [Adam.Dybbroe]

- Remove one verbose debug printout. [Adam.Dybbroe]

- Adapt for new PPS netCDF format modification (adding a dimension of
  length 1) [Adam.Dybbroe]

- Check for cloudtype=None. [Adam.Dybbroe]

- Add option to provide MSG filename to load call. [Adam.Dybbroe]

- Check if PPS file is bzipped, and handle it correctly. [Adam.Dybbroe]

- Fix orbit number attribute name in msg_hdf. [Martin Raspaud]

- Possible to pass value range to save. [Lars Orum Rasmussen]

- Chlorophyll-a palette is gone - now it raise an exception if asked
  for... [Adam.Dybbroe]

- Merge branch 'feature-osisaf-sst-reader' into pre-master.
  [Adam.Dybbroe]

- Adding a reader and palette support for OSISAF SST netCDF products.
  [Adam.Dybbroe]

- Fixed external calibration "newer/older than data" message. [Panu
  Lahtinen]

- Fix ctth writing. [Martin Raspaud]

- Fixed typo. [Martin Raspaud]

- Add orbit number in generated cloud product hdf files. [Martin
  Raspaud]

- Fix new pyspectral calculator signature. [Martin Raspaud]

- Putting back the mipp information in template config files. [Martin
  Raspaud]

- Pyspectral now uses standard platform names. [Martin Raspaud]

- Merge branch 'pre-master' of https://github.com/mraspaud/satpy into
  pre-master. [Panu Lahtinen]

- Add algorithm version in output cloud products. [Martin Raspaud]

- Exception handling for missing external calibration data. [Panu
  Lahtinen]

- Minor PEP8 tweaks. [Panu Lahtinen]

- Script to generate external calibration files for AVHRR instruments.
  [Panu Lahtinen]

- Support for external calibration coefficients for AVHRR. [Panu
  Lahtinen]

- Removed obsolete "satname" and "number" from satellite configs,
  updated documentation. [Panu Lahtinen]

- Renamed satellite configs to conform to OSCAR naming scheme. [Panu
  Lahtinen]

- Add luts to the pps products from msg format. [Martin Raspaud]

- Add metadata to nwcsaf products. [Martin Raspaud]

- Add \0 to palette strings. [Martin Raspaud]

- Fix pps format output for msg products. [Martin Raspaud]

- Remove phase palette from msg products to avoid confusion. [Martin
  Raspaud]

- Bugfix, np.string -> np.string_ [Martin Raspaud]

- Change variable length strings in h5 products to fixed. [Martin
  Raspaud]

- Fix some cloud product conversions. [Martin Raspaud]

- Fix MSG format to PPS format conversion. [Martin Raspaud]

- Merge branch 'pre-master' of github.com:mraspaud/satpy into pre-master.
  [Martin Raspaud]

- Merge pull request #16 from pnuu/simplified_platforms. [Martin
  Raspaud]

  Simplified platform names for reading custom composites

- Simplified platform names for reading custom composites. [Panu
  Lahtinen]

- Change: accept arbitrary kwargs for saving msg hdf products. [Martin
  Raspaud]

- Revert concatenation to it's original place, in order to keep the
  tests working. [Martin Raspaud]

- Fix whole globe area_extent for loading. [Martin Raspaud]

- Fix rpm building. [Martin Raspaud]

- Fix masking of lonlats in viirs_sdr. [Martin Raspaud]

- Fixing pps-nc reader. [Adam Dybbroe]

- Clean temporary files after loading. [Adam Dybbroe]

- Pep8 stuff. [Adam Dybbroe]

- Fixed polar-stereographic projection bugs, thanks to Ron Goodson.
  [Lars Orum Rasmussen]

- Update changelog. [Martin Raspaud]

- Bump version: 1.0.2 → 1.1.0. [Martin Raspaud]

- Put config files in etc/pytroll. [Martin Raspaud]

- Fix version strings. [Martin.Raspaud]

- Don't close the h5 files too soon. [Martin Raspaud]

- Close h5 file uppon reading. [Adam Dybbroe]

- Bugfix. [Adam Dybbroe]

- Try a more clever handling of the case where more level-1b files exist
  for given sat and orbit. [Adam Dybbroe]

- Print out files matching in debug. [Martin Raspaud]

- Bugfix. [Adam Dybbroe]

- Adding debug info. [Adam Dybbroe]

- Bugfix. [Adam Dybbroe]

- Merge branch 'pre-master' of https://github.com/mraspaud/satpy into
  pre-master. [Adam Dybbroe]

- Remove ugly print statements. [Martin Raspaud]

- Load the palettes also. [Martin Raspaud]

- AAPP1b: use operational coefficients for vis calibrating per default.
  [Martin Raspaud]

   - Fallback to pre-launch if not available.
   - load(..., pre_launch_coeffs=True) to force using pre-launch coeffs)

- Correct npp name in h5 files. [Martin Raspaud]

- Add the pps v2014 h5 reader. [Martin Raspaud]

- Use h5py for lonlat reading also. [Martin Raspaud]

- Use h5py instead of netcdf for reading nc files. [Martin Raspaud]

- Fix orbit as int in nc_pps loader. [Martin Raspaud]

- Add overlay from config feature. [Martin Raspaud]

- Remove type testing for orbit number. [Martin Raspaud]

- Merge branch 'pre-master' of https://github.com/mraspaud/satpy into
  pre-master. [Adam Dybbroe]

- Allowing kwargs. [Martin Raspaud]

- Add 10 km to the area extent on each side, to avoid tangent cases.
  [Martin Raspaud]

- Orbit doesn't have to be a string anymore. [Martin Raspaud]

- Fix multiple file loading for metop l1b data. [Martin Raspaud]

- Merge branch 'pre-master' of https://github.com/mraspaud/satpy into
  pre-master. [Adam Dybbroe]

- Implement save for all cloudproducts. [Martin Raspaud]

- Change options names to cloud_product_* and add lookup in os.environ.
  [Martin Raspaud]

- Some fixes to nc_pps_l2 for correct saving. [Martin Raspaud]

- Add saving to the cloudtype object. [Martin Raspaud]

- Add the save method to cloudtype object. [Martin Raspaud]

- Rename _md attribute to mda. [Martin Raspaud]

- Mask out bowtie deleted pixels for Suomi-NPP products. [Martin
  Raspaud]

- When a file is provided in nc_pps_l2, just read this file. [Martin
  Raspaud]

- Fix nc_pps_l2 for filename input and PC readiness. [Martin Raspaud]

- ViirsSDR: Fix not to crash on single file input. [Martin Raspaud]

- Fix aapp1b to be able to run both for given filename and config.
  [Martin Raspaud]

- Try loading according to config if provided file doesn't work, aapp1b.
  [Martin Raspaud]

- Don't crash when reading non aapp1b file. [Martin Raspaud]

- Remove "/" from instrument names when loading custom composites.
  [Martin Raspaud]

- Don't say generate lon lat when returning a cached version. [Martin
  Raspaud]

- Nc_pps_l2: don't crash on multiple files, just go through them one at
  the time. [Martin Raspaud]

- Hdfeos: don't just exit when filename doesn't match, try to look for
  files. [Martin Raspaud]

- Don't crash if the file doesn't match (hdfeos) [Martin Raspaud]

- Revert nc_reader back until generalization is ready. [Martin Raspaud]

- Merge branch 'ppsv2014-reader' of github.com:mraspaud/satpy into
  ppsv2014-reader. [Martin Raspaud]

- Adding dataset attributes to pps reading. [Adam Dybbroe]

- Allow inputing filename in the nc_pps_l2 reader. [Martin Raspaud]

- Merge branch 'pre-master' into ppsv2014-reader. [Martin Raspaud]

- Viirs readers fixes. [Martin Raspaud]

- Hdf_eos now uses 1 out of 4 available cores to interpolate data.
  [Martin Raspaud]

- Merge branch 'pre-master' of github.com:mraspaud/satpy into pre-master.
  [Martin Raspaud]

- Fixed bug, now handling fill_value better. [Lars Orum Rasmussen]

- More robust tiff header file decoder. [Lars Orum Rasmussen]

- Add dnb_overview as a standard product (dnb, dnb, 10.8) [Martin
  Raspaud]

- Merge branch 'pre-master' of github.com:mraspaud/satpy into pre-master.
  [Martin Raspaud]

- Corrected the reader for SAFNWC/PPS v2014. [Sara.Hornquist]

- Allow multiresolution loading in hdf eos reader. [Martin Raspaud]

- Revert back to old nwcsaf-pps reader for hdf. The reading of the new
  netcdf format is done with another reader! [Adam Dybbroe]

- A new pps reader for the netCDF format of v2014. [Adam Dybbroe]

- Adding for new cloudmask and type formats... [Adam Dybbroe]

- Enhance nwc-pps reader to support v2014 format. [Adam Dybbroe]

- Merge branch 'pre-master' of https://github.com/mraspaud/satpy into
  pre-master. [Adam Dybbroe]

- Put the config object back in Projector. [Martin Raspaud]

- Fix area_file central search. [Martin Raspaud]

- Move the area_file search inside Projector. [Martin Raspaud]

- Error when satellite config file is not found. [Martin Raspaud]

- Get rid of the funky logging style. [Martin Raspaud]

- Log the config file used to generate the scene. [Martin Raspaud]

- Support filename list to load in viirs_sdr loader. [Martin Raspaud]

- Add avhrr/3 as aliar to avhrr in aapp reader. [Martin Raspaud]

- Fix name matching in hdfeos_l1b. [Martin Raspaud]

  The full name didn't work with fnmatch, take basename instead.

- Allows hdfeos_l1b to read a batch of files. [Martin Raspaud]

- Add delitem, and code cleanup. [Martin Raspaud]

- Merge branch 'pre-master' of github.com:mraspaud/satpy into pre-master.
  [Martin Raspaud]

- Added a reader for SAFNWC/PPS v2014 PPS v2014 has a different
  fileformat than previous SAFNWC/PPS versions. [Sara.Hornquist]

- Aapp1b reader, be more clever when (re)reading. [Martin Raspaud]

- Merge branch 'pre-master' of https://github.com/mraspaud/satpy into
  pre-master. [Adam Dybbroe]

  Conflicts:
  	satpy/satout/netcdf4.py


- Allow reading several files at once in viirs_compact. [Martin Raspaud]

- Allow reading several files at once in eps_l1b. [Martin Raspaud]

- Style: use in instead for has_key() [Martin Raspaud]

- Adding primitive umarf (native) format reader for meteosat. [Martin
  Raspaud]

- Add logging when an info field can't be save to netcdf. [Martin
  Raspaud]

- Add a name to the area when loading aapp data. [Martin Raspaud]

- Merge branch 'pre-master' of github.com:mraspaud/satpy into pre-master.
  [Martin Raspaud]

- For PNG files, geo_mage.tags will be saved a PNG metadata. [Lars Orum
  Rasmussen]

- Add a save method to cfscene objects. [Martin Raspaud]

- Don't take None as a filename in loading avhrr data. [Martin Raspaud]

- Allow loading a file directly for aapp1b and eps_l1b. [Martin Raspaud]

  Just run global_data.load(..., filename="/path/to/myfile.1b")

- Merge branch 'pre-master' of github.com:mraspaud/satpy into pre-master.
  [Martin Raspaud]

- Viirs_sdr can now load depending on an area. [Martin Raspaud]

- Pep8 cosmetics. [Adam Dybbroe]

- Merge pull request #12 from pnuu/pre-master. [Martin Raspaud]

  Fixed "logger" to "LOGGER"

- Fixed "logger" to "LOGGER" [Panu Lahtinen]

- Moving pysoectral module import down to function where pyspectral is
  used. [Adam Dybbroe]

- Merge branch 'smhi-premaster' into pre-master. [Adam Dybbroe]

- Fixing cloudtype product: palette projection. [Adam Dybbroe]

- Turned on debugging to geo-test. [Adam Dybbroe]

- Added debug printout for cloud product loading. [Adam Dybbroe]

- Make snow and microphysics transparent. [Martin Raspaud]

- Rename day_solar to snow. [Martin Raspaud]

- Keep the name of cloudtype products when projecting. [Martin Raspaud]

- Explicitly load parallax corrected files if present. [Martin Raspaud]

- Adding logging for MSG cloud products loading. [Martin Raspaud]

- Fix the parallax file sorting problem, again. [Martin Raspaud]

- Merge branch 'pre-master' of github.com:mraspaud/satpy into pre-master.
  [Martin Raspaud]

- Merge branch 'pre-master' of https://github.com/mraspaud/satpy into
  pre-master. [Adam Dybbroe]

- Bugfix. [Adam Dybbroe]

- Merge branch '3.9reflectance' into pre-master. [Adam Dybbroe]

  Conflicts:
  	satpy/channel.py
  	satpy/instruments/seviri.py
  	satpy/satin/mipp_xrit.py
  	setup.py


- Support for rgbs using the seviri 3.9 reflectance (pyspectral) [Adam
  Dybbroe]

- Adding a sun-corrected overview rgb. [Adam Dybbroe]

- Adduing for "day microphysics" RGB. [Adam Dybbroe]

- Deriving the day-solar RGB using pyspectral to derive the 3.9
  reflectance. [Adam Dybbroe]

- Use "imp" to find input plugins. [Martin Raspaud]

- Cleanup trailing whitespaces. [Martin Raspaud]

- Use cartesian coordinates for lon/lat computation if near-pole
  situations. [Martin Raspaud]

- Set alpha channel to the same type as the other channels. [Martin
  Raspaud]

- Sort the filenames in get_best_products (msg_hdf) [Martin Raspaud]

- Merge branch 'pre-master' of github.com:mraspaud/satpy into pre-master.
  [Martin Raspaud]

- Merge branch 'pre-master' of https://github.com/mraspaud/satpy into
  pre-master. [Adam Dybbroe]

- Merge pull request #10 from pnuu/pre-master. [Martin Raspaud]

  Fixed failed merging. Thanks Pnuu.

- Fixed failed merging (removed "<<<<<<< HEAD" and ">>>>>>> upstream
  /pre-master" lines) [Panu Lahtinen]

- Merge branch 'pre-master' of https://github.com/mraspaud/satpy into
  pre-master. [Adam Dybbroe]

- Merge branch 'pre-master' of https://github.com/mraspaud/satpy into
  pre-master. [Adam Dybbroe]

- Merge branch 'pre-master' of https://github.com/mraspaud/satpy into
  pre-master. [Adam Dybbroe]

- Fix terra and aqua templates for the dual gain channels (13 & 14)
  [Adam Dybbroe]

- Read both parallax corrected and usual cloudtype products. [Martin
  Raspaud]

- Merge branch 'pre-master' of github.com:mraspaud/satpy into pre-master.
  [Martin Raspaud]

- Merge pull request #9 from pnuu/pre-master. [Martin Raspaud]

  Possibility to get area_extent from area definition(s)

- Tests for satpy.satin.helper_functions.boundaries_to_extent. [Panu
  Lahtinen]

- Separated area definitions and boundary calculations. [Panu Lahtinen]

- Added test if proj string is in + -format or not. [Panu Lahtinen]

- Re-ordered the tests. [Panu Lahtinen]

- Fixed incorrect correct values. [Panu Lahtinen]

- Test using area definitions instead of definition names. [Panu
  Lahtinen]

- Possibility to give also area definition objects to
  area_def_names_to_extent() and log a warning if the area definition is
  not used. [Panu Lahtinen]

- Fixed import. [Panu Lahtinen]

- Added tests for satpy.satin.helper_functions. [Panu Lahtinen]

- Moved to satpy/tests/ [Panu Lahtinen]

- Moved to satpy/tests/ [Panu Lahtinen]

- Merge remote-tracking branch 'upstream/pre-master' into pre-master.
  [Panu Lahtinen]

  Conflicts:
  	satpy/satin/aapp1b.py


- Removed unneeded functions. [Panu Lahtinen]

- Test for area_def_names_to_extent() [Panu Lahtinen]

- Removed unnecessary functions. [Panu Lahtinen]

- Removed swath reduction functions. [Panu Lahtinen]

- Reverted not to reduce swath data. [Panu Lahtinen]

- Added possibility to do data reduction based on target area definition
  names. [Panu Lahtinen]

- Added area extent calculations based on given area definition names.
  [Panu Lahtinen]

- Helper functions for area extent and bondary calculations, and data
  reducing for swath data. [Panu Lahtinen]

- Test for satpy.satin.mipp_xrit.lonlat_to_geo_extent() [Panu Lahtinen]

- Support for lon/lat -based area extents. [Panu Lahtinen]

- Add start and end time defaults for the images (runner). [Martin
  Raspaud]

- Merge branch 'pre-master' of https://github.com/mraspaud/satpy into
  pre-master. [Lars Orum Rasmussen]

- Do not mask out negative reflectances in viirs_sdr reading. [Martin
  Raspaud]

- Added navigation to hrpt_hmf plugin. [Martin Raspaud]

- Started working on a new plugin version of hdfeos_l1b. [Martin
  Raspaud]

- Cleanup. [Martin Raspaud]

- Cleanup. [Martin Raspaud]

- Cleanup. [Martin Raspaud]

- Cleanup. [Martin Raspaud]

- Adding scene tests to the test suite. [Martin Raspaud]

- Revamped scene unittests. [Martin Raspaud]

- Don't crash on errors. [Martin Raspaud]

- Revamped projector tests. [Martin Raspaud]

- More geo_image testing. [Martin Raspaud]

- Don't use "super" in geo_image. [Martin Raspaud]

- Fix testing. [Martin Raspaud]

- Mock pyresample and satpy.projector in geo_image tests. [Martin
  Raspaud]

- More testing geo_image. [Martin Raspaud]

- Add tests for geo_image. [Martin Raspaud]

- Merge branch 'unstable' of ssh://safe/data/proj/SAF/GIT/satpy into
  unstable. [Martin Raspaud]

- Mock gdal for geo_image tests. [Martin Raspaud]

- Added netCDF read support for four more projections. [Adam Dybbroe]

- Adding support for eqc in cf format. [Adam Dybbroe]

- Added config templates for GOES and MTSAT. [Lars Orum Rasmussen]

- Copied visir.night_overview to seviri.night_overview, so
  night_overview.prerequisites is correct when night_overview is called
  from seviri.py. [ras]

- Cloutop in seviri.py now same arguments as cloudtop in visir.py. [Lars
  Orum Rasmussen]

- Fix saving as netcdf. [Martin Raspaud]

- Fix floating point tiff saving. [Martin Raspaud]

- Make pillow a requirement only if PIL is missing. [Martin Raspaud]

- Add some modules to mock in the documentation. [Martin Raspaud]

- Add pyorbital to the list of packets to install in travis. [Martin
  Raspaud]

- Merge branch 'feature-travis' into unstable. [Martin Raspaud]

- Test_projector doesn't pass. [Martin Raspaud]

- Test_projector ? [Martin Raspaud]

- Fix travis. [Martin Raspaud]

- Adding test_geoimage. [Martin Raspaud]

- Test_channel passes, test_image next. [Martin Raspaud]

- Test_pp_core crashes, test_channel on. [Martin Raspaud]

- Commenting out tests to find out the culprit. [Martin Raspaud]

- Ok, last try for travis-ci. [Martin Raspaud]

- What is happening with travis ? [Martin Raspaud]

- More fiddling to find out why travis-ci complains. [Martin Raspaud]

- Testing the simple test way (not coverage) [Martin Raspaud]

- Trying to add the tests package for travis-ci. [Martin Raspaud]

- Add the tests package. [Martin Raspaud]

- Preprare for travis-ci. [Martin Raspaud]

- Support 16 bits images (geotiff only at the moment). [Martin Raspaud]

- Merge pull request #8 from pnuu/pre-master. [Martin Raspaud]

  Sun zenith angle correction added.

- A section on satpy.tools added to documentation. [Panu Lahtinen]

- Extra tests for sun_zen_corr(). [Panu Lahtinen]

- Typo. [Panu Lahtinen]

- Channel descriptions added. [Panu Lahtinen]

- Channel desctiptions are added. [Panu Lahtinen]

- Clarification to help sunzen_corr_cos() desctiption. [Panu Lahtinen]

- Test cases for channel.sunzen_corr(). [Panu Lahtinen]

- Sun zenith angle correction split into two functions. [Panu Lahtinen]

- Revert to original version. [Panu Lahtinen]

- Initial commit of satpy.tools (with Sun zenith angle correction). [Panu
  Lahtinen]

- Sun zenith angle correction added. [Panu Lahtinen]

- Merge branch 'pre-master' of github.com:mraspaud/satpy into pre-master.
  [ras]

- Solve the multiple channel resolution with automatic resampling
  radius. [Martin Raspaud]

- Add the "nprocs" option to projector objects and scene's project
  method. [Martin Raspaud]

- Now saving orbit number (if available) as global attribute. [ras]

- Adding more files to be ignored. [ras]

- Merge branch 'pre-master' of github.com:mraspaud/satpy into pre-master.
  [ras]

- New reader for hrpt level0 format. [Martin Raspaud]

- Fix no calibration reading for aapp1b. [Martin Raspaud]

- Add the product name to the the image info. [Martin Raspaud]

- Add some debugging info about missing pixels in viirs_sdr. [Martin
  Raspaud]

- Merge branch 'unstable' of /data/proj/SAF/GIT/satpy into unstable.
  [Martin Raspaud]

- Corrected a comment. [Adam Dybbroe]

- Fix for M13 load problem - reported by stefano.cerino@gmail.com. [Adam
  Dybbroe]

- Use number of scan to load the right amount of data in compact viirs
  reader. [Martin Raspaud]

- Fix hook to be able to record both filename and uri. [Martin Raspaud]

- Protecting satpy from netcdf4's unicode variables. [ras]

- Merge branch 'unstable' of /data/proj/SAF/GIT/satpy into unstable.
  [Martin Raspaud]

- Merge branch 'unstable' of /data/proj/SAF/GIT/satpy into unstable.
  [Adam Dybbroe]

- Adding a new convection RGB with co2 correction for SEVIRI. [Adam
  Dybbroe]

- Temporary hack to solve for hdf5 files with more than one granule per
  file. [Adam Dybbroe]

- Removing messaging code from saturn and added a more generic "hook"
  argument. [Martin Raspaud]

- Bumped up version. [Martin Raspaud]

- Make viirs_compact scan number independent. [Martin Raspaud]

- Cleanup: marking some deprecated modules, removing unfinished file,
  improving documentation. [Martin Raspaud]

- Adding the ears-viirs compact format reader. Untested. [Martin
  Raspaud]

- Code cleanup. [Martin Raspaud]

- Merge branch 'pre-master' into unstable. [Martin Raspaud]

  Conflicts:
  	satpy/imageo/geo_image.py

- Night_color (should had beed called night_overview) is the same as
  cloudtop. [Lars Orum Rasmussen]

- Bug fix from Bocheng. [Lars Orum Rasmussen]

- Night_overview is just like cloudtop. [Lars Orum Rasmussen]

- Now also handling Polar satellites. [Lars Orum Rasmussen]

- Cosmetic. [Lars Orum Rasmussen]

- Fixed merge conflict. [Lars Orum Rasmussen]

- Trying out a chlorophyll product. [Lars Orum Rasmussen]

- Added a night overview composite. [Lars Orum Rasmussen]

- Better check for empty array. [Lars Orum Rasmussen]

- Fix logging. [Martin Raspaud]

- Fix backward compatibility in, and deprecate image.py. [Martin
  Raspaud]

- Merge branch 'unstable' of /data/proj/SAF/GIT/satpy into unstable.
  [Martin Raspaud]

- Calling numpy percentile only once when doing left and right cut offs.
  [Adam Dybbroe]

- Add support for identifying npp directories by time-date as well as
  orbit number. [Adam Dybbroe]

- Fix histogram-equalization stretch test. [Adam Dybbroe]

- Bugfix in histogram equalization function. [Adam Dybbroe]

- Using percentile function to generate histogram with constant number
  of values in each bin. [Adam Dybbroe]

- Using numpy.pecentile function to cut the data in the linear stretch.
  [Adam Dybbroe]

- Fix histogram stretch unit test. [Adam Dybbroe]

- Correcting the histogram stretching. The com_histogram function was in
  error when asking for "normed" histograms. [Adam Dybbroe]

- Added histogram method that makes a more populated histogram when the
  data are heaviliy skeewed. Fixes problem seen by Bocheng in DNB
  imagery. [Adam Dybbroe]

- Merge branch 'unstable' of /data/proj/SAF/GIT/satpy into unstable.
  [Adam Dybbroe]

- Don't remove GeolocationFlyweight _instances, but reset it. Allowing
  for multiple "loads" [Adam Dybbroe]

- Add imageo.formats to installation. [Martin Raspaud]

- AAPP loading bug fix. [Martin Raspaud]

  the aapp1b.py loader to aapp data was broken as it was loading both
  channels 3a and 3b each time, one of them being entirely masked. This of
  course created some problem further down. Fixed by setting the not loadable
  channel to None.

- Merge branch 'unstable' of /data/proj/SAF/GIT/satpy into unstable.
  [Martin Raspaud]

- Bugfix in npp.cfg template. [Adam Dybbroe]

- Merge branch 'unstable' of /data/proj/SAF/GIT/satpy into unstable.
  [Adam Dybbroe]

- Fixing bug concerning the identification of VIIRS geolocation files.
  Now the configuration specified in npp.cfg overwrites what is actually
  written in the metadata header of the band files. [Adam Dybbroe]

- Make saturn posttroll capable. [Martin Raspaud]

- Bump up version number. [Martin Raspaud]

- Cosmetics. [Martin Raspaud]

- Fixing test cases. [Martin Raspaud]

- Merge branch 'unstable' of /data/proj/SAF/GIT/satpy into unstable.
  [Martin Raspaud]

- Remove dummy test to boost projection performance. [Martin Raspaud]

  satpy was checking in 2 different places if the source and target areas were
  different, leading to pyresample expanding the area definitions to full
  lon/lat arrays when checking against a swath definition, and then running
  an allclose. This was inefficient, and the programming team decided that it
  was the user's task to know before projection if the source and target area
  were the same. In other words, the user should be at least a little smart.

- Remove dummy test to boost projection performance. [Martin Raspaud]

  satpy was checking in 2 different places if the source and target areas were
  different, leading to pyresample expanding the area definitions to full
  lon/lat arrays when checking against a swath definition, and then running
  an allclose. This was inefficient, and the programming team decided that it
  was the user's task to know before projection if the source and target area
  were the same. In other words, the user should be at least a little smart.

- Update channel list for modis lvl2. [Martin Raspaud]

- Bump up version number: 1.0.0. [Martin Raspaud]

- Merge branch 'pre-master' into unstable. [Martin Raspaud]

- Merge branch 'unstable' of /data/proj/SAF/GIT/satpy into unstable.
  [Martin Raspaud]

- Cleanup. [Martin Raspaud]

v1.0.0 (2013-09-25)
-------------------

- Release v1.0.0. [Martin Raspaud]

- Changing palette name to something more intuitive. Allow to have orbit
  number equals None. [Adam Dybbroe]

- Fixing aqua/terra template config files for dual gain channels (13&14)
  [Adam Dybbroe]

- Added Ninjo tiff example areas definitions. [Lars Orum Rasmussen]

- Cosmetic. [Lars Orum Rasmussen]

- Ninjo tiff writer now handles singel channels. [Lars Orum Rasmussen]

  Ninjo tiff meta-data can now all be passed as arguments


- Better documentation. [Lars Orum Rasmussen]

- Merge branch 'unstable' of /data/proj/SAF/GIT/satpy into unstable.
  [Adam Dybbroe]

- Merge branch 'unstable' of /data/proj/SAF/GIT/satpy into unstable.
  [Martin Raspaud]

  Conflicts:
  	etc/npp.cfg.template


- Merge branch 'pre-master' of https://github.com/mraspaud/satpy into
  pre-master. [Adam Dybbroe]

- Changed template to fit new npp reader. [krl]

- Merge branch 'pre-master' of https://github.com/mraspaud/satpy into
  pre-master. [Adam Dybbroe]

- Updated npp confirg file template with geo_filename example. [Adam
  Dybbroe]

- Make overview consistent with the standard overview. [Adam Dybbroe]

- Updated npp-template to fit the new viirs reader using the (new)
  plugin-loader system. [Adam Dybbroe]

- Minor clean up. [Adam Dybbroe]

- Merge branch 'unstable' of /data/proj/SAF/GIT/satpy into unstable.
  [Adam Dybbroe]

  Conflicts:
  	satpy/satin/viirs_sdr.py


- Fix version stuff. [Martin Raspaud]

- Merge branch 'feature-optimize_viirs' into unstable. [Martin Raspaud]

- Make viirs_sdr a plugin of new format. [Martin Raspaud]

- Finalize optimisation i new viirs reader. [Martin Raspaud]

- Optimization ongoing. Mask issues. [Martin Raspaud]

- Clarify failure to load hrit data. [Martin Raspaud]

- Lunar stuff... [Adam Dybbroe]

- Fix install requires. [Martin Raspaud]

- Fix projector unit test. [Martin Raspaud]

- Merge branch 'pre-master' into unstable. [Martin Raspaud]

- Merge branch 'pre-master' of git://github.com/mraspaud/satpy into pre-
  master. [Martin Raspaud]

- Fixed (temporary ?) misuse of Image.SAVE. [Lars Orum Rasmussen]

- Now config reader is a singleton. [Lars Orum Rasmussen]

- Merge branch 'pre-master' into unstable. [Martin Raspaud]

- Merge branch 'pre-master' of git://github.com/mraspaud/satpy into pre-
  master. [Martin Raspaud]

- Tmplate -> template. [Lars Orum Rasmussen]

- Added support for saving in Ninjo tiff format. [Lars Orum Rasmussen]

- Projector cleanup. [Martin Raspaud]

- Merge branch 'unstable' of /data/proj/SAF/GIT/satpy into unstable.
  [Martin Raspaud]

- New VIIRS reader. Better, faster, smarter (consumimg less memory)
  [Adam Dybbroe]

- Fix area hashing. [Martin Raspaud]

- Fix install dependency. [Martin Raspaud]

- Merge branch 'pre-master' into unstable. [Martin Raspaud]

- Merge branch 'pre-master' of git://github.com/mraspaud/satpy into pre-
  master. [Martin Raspaud]

  Conflicts:
  	doc/source/conf.py
  	setup.py


- Optimize. [Martin Raspaud]

- Remove the optional ahamap requirement. [Martin Raspaud]

- Manage version number centrally. [Martin Raspaud]

- Merge branch 'release-v0.13.0' [Martin Raspaud]

  Conflicts:
  	setup.py


- Merge branch 'pre-master' [Martin Raspaud]

  Conflicts:
  	doc/source/conf.py
  	setup.py


v0.13.0 (2013-05-08)
--------------------

- Bump up version number for release. [Martin Raspaud]

- Merge branch 'pre-master' of git://github.com/mraspaud/satpy into pre-
  master. [Martin Raspaud]

- Bump up version number. [Martin Raspaud]

- Make old plugin an info instead of a warning. [Martin Raspaud]

- Merge branch 'pre-master' of git://github.com/mraspaud/satpy into pre-
  master. [Martin Raspaud]

- Pep8. [Adam Dybbroe]

- Merge branch 'aapp1b' into unstable. [Adam Dybbroe]

- Don't mask out IR channel data where count equals zero. [Adam Dybbroe]

- Fixing the masking of the ir calibrated Tbs - count=0 not allowed.
  [Adam Dybbroe]

- Make also vis channels masked arrays. [Adam Dybbroe]

- Checking if file format is post or pre v4 : If bandcor_2 < 0 we are at
  versions higher than 4 Masking a bit more strict. [Adam Dybbroe]

- Now handle data without a mask and handling lons and lats without
  crashing. [Lars Orum Rasmussen]

- Read signed instead of unsigned (aapp1b). [Martin Raspaud]

- Style cleanup. [Martin Raspaud]

- Adding calibration type as an option to the loader. So counts,
  radiances or tbs/refl can be returned. [Adam Dybbroe]

- Better show and more cosmetic. [Lars Orum Rasmussen]

- Making pylint more happy and some cosmetic. [Lars Orum Rasmussen]

- No need to night_overview, use cloudtop with options. [Lars Orum
  Rasmussen]

- Now IR calibration returns a masked array. [Lars Orum Rasmussen]

- Added som options for overview image and added a night overview. [Lars
  Orum Rasmussen]

- Finalize aapp1b python-only reader. [Martin Raspaud]

- Working on a aapp l1b reader. [oananicola]

- Starting a aapp1b branch for directly reading aapp's l1b files. [Lars
  Orum Rasmussen]

- Adding a bit of debug info... [Adam Dybbroe]

- Adding orbit number to the cloud mask object. [Adam Dybbroe]

- Channel cleanup and tests. [Martin Raspaud]

- Merge branch 'feature_plugins' into unstable. [Martin Raspaud]

- Make orbit number an 5-character string (padding with '0') [Martin
  Raspaud]

- New plugin implementation, backward compatible. [Martin Raspaud]

- Merge branch 'pre-master' of github.com:mraspaud/satpy into pre-master.
  [Lars Orum Rasmussen]

- Reverted to previous commit. [Lars Orum Rasmussen]

- Correct green-snow. [Martin Raspaud]

  Use 0.6 instead on 0.8


- Now, if specified in proj4 object, add EPGS code to tiff metadata.
  [Lars Orum Rasmussen]

- Added, a poor man's version, of Adam's DNB RGB image. [Lars Orum
  Rasmussen]

v0.12.1 (2013-03-14)
--------------------

- Cleanup. [Martin Raspaud]

- Add several cores for geoloc in eos. [Martin Raspaud]

- Bugfix hdfeos. [Martin Raspaud]

- Fix loading of terra aqua with multiple cores. [Martin Raspaud]

- Add dust, fog, ash composites to VIIRS. [Martin Raspaud]

- Enhance error messages. [Martin Raspaud]

- Merge branch 'unstable' of /data/proj/SAF/GIT/satpy into unstable.
  [Martin Raspaud]

- New template files for regional EARS (AVHRR and NWC) file support.
  [Adam Dybbroe]

- Minor cosmetics. [Adam Dybbroe]

- Make orbit number an 5-character string (padding with '0') [Martin
  Raspaud]

- Merge branch 'fixrtd' into unstable. [Martin Raspaud]

- Add pyresample to mock for doc building. [Martin Raspaud]

- Get rid of the np.inf error in rtd. [Martin Raspaud]

- Mock some import for the documentation. [Martin Raspaud]

- Introducing clip percentage for SAR average product. [Lars Orum
  Rasmussen]

- Add symlink from README.rst to README. [Martin Raspaud]

- Update download link and README. [Martin Raspaud]

v0.12.0 (2013-01-10)
--------------------

- Bump up version number. [Martin Raspaud]

- Cosmetics. [Martin Raspaud]

- Merge branch 'unstable' of /data/proj/SAF/GIT/satpy into unstable.
  [Martin Raspaud]

- Merge branch 'unstable' of /data/proj/SAF/GIT/satpy into unstable.
  [Adam Dybbroe]

- Support for calibrate option. [Adam Dybbroe]

- Add template file for meteosat 10. [Martin Raspaud]

- Add debug messages to hdf-eos loader. [Martin Raspaud]

v0.11.7 (2012-12-04)
--------------------

Fix
~~~

- Bugfix: allow more than one "-" in section names. [Martin Raspaud]

- Bugfix: read aqua/terra orbit number from file only if not already
  defined. [Martin Raspaud]

- Bugfix: fixed unittest case for wavelengths as lists. [Martin Raspaud]

- Bugfix: remove deprecated mviri testcases. [Martin Raspaud]

- Bugfix: backward compatibility with netcdf files. [Martin Raspaud]

- Bugfix: removed the old mviri compositer. [Martin Raspaud]

- Bugfix: When assembling, keep track of object, not just lon/lats.
  [Martin Raspaud]

- Bugfix: assembling scenes would unmask some lon/lats... [Martin
  Raspaud]

- Bugfix: handling of channels with different resolutions in
  assemble_segments. [Martin Raspaud]

- Bugfix: Runner crashed if called with an area not in product list.
  [Martin Raspaud]

- Bugfix: the nwcsaf_pps reader was crashing if no file was found...
  [Martin Raspaud]

- Bugfix: pynav is not working in some cases, replace with pyorbital.
  [Martin Raspaud]

- Bugfix: can now add overlay in monochromatic images. [Martin Raspaud]

- Bugfix: swath scene projection takes forever from the second time.
  [Martin Raspaud]

  The swath scene, when projected more than once would recompute the nearest neighbours for every channel.


Other
~~~~~

- Support pnm image formats. [Martin Raspaud]

- The pps palette broke msg compatibility. Now there are two palettes,
  one for msg and one for pps. [Adam Dybbroe]

- Merge branch 'unstable' of /data/proj/SAF/GIT/satpy into unstable.
  [Adam Dybbroe]

  Conflicts:
  	satpy/satin/viirs_sdr.py


- Adapted viirs reader to handle aggregated granule files. [Adam
  Dybbroe]

- Fixing nwcsaf-pps ctth height palette. [Adam Dybbroe]

- Take better care of the path (was uri) argument. [Martin Raspaud]

- Don't do url parsing in the hdfeos reader. [Martin Raspaud]

- Fix unit tests. [Martin Raspaud]

- Remove the deprecated append function in scene. [Martin Raspaud]

- Return when not locating hdf eos file. [Martin Raspaud]

- Remove raveling in kd_tree. [Martin Raspaud]

- Make use of the new strftime in the viirs reader. [Martin Raspaud]

- Add a custom strftime. [Martin Raspaud]

  This fixes a bug in windows that prevents running strftime on string that
  contain mapping keys conversion specifiers.

- Catch the error if there is no file to load from. [Martin Raspaud]

- Add a proper logger in hdfeos reader. [Martin Raspaud]

- Get resolution from filename for eos data. [Martin Raspaud]

- Introducing stretch argument for average product. [Lars Orum
  Rasmussen]

- Merge branch 'pre-master' of github.com:mraspaud/satpy into pre-master.
  [Lars Orum Rasmussen]

- Clean up. [Martin Raspaud]

- Bump up version number. [Martin Raspaud]

- Support passing a uri to hdfeos reader. [Martin Raspaud]

- Fix the loading of BT for VIIRS M13 channel. [Martin Raspaud]

  Has no scale and offset

- Merge branch 'pre-master' of github.com:mraspaud/satpy into pre-master.
  [Lars Orum Rasmussen]

- Refactor the unsigned netcdf packing code. [Martin Raspaud]

- Merge branch 'pre-master' of github.com:mraspaud/satpy into pre-master.
  [Lars Orum Rasmussen]

- Support packing data as unsigned in netcdf. [Martin Raspaud]

- Replace auto mask and scale from netcdf4. [Martin Raspaud]

  Eats up too much memory.

- Merge branch 'pre-master' of github.com:mraspaud/satpy into pre-master.
  [Lars Orum Rasmussen]

- Feature: Added template for electro-l satellite. [Martin Raspaud]

- Feature: taking care of missing data in the viirs reader, and allow
  for radiance retrieval. [Martin Raspaud]

- Feature: last adjustments to new netcdf format. [Martin Raspaud]

- Merge branch 'feature-netcdf-upgrade' into unstable. [Martin Raspaud]

  Conflicts:
  	satpy/satout/cfscene.py
  	satpy/satout/netcdf4.py


- Merge branch 'unstable' into feature-netcdf-upgrade. [Martin Raspaud]

- Merge branch 'unstable' into feature-netcdf-upgrade. [Martin Raspaud]

  Conflicts:
  	satpy/satin/mipp_xsar.py


- Work on new netcdf format nearing completion. [Martin Raspaud]

- Feature: wrapping up new netcdf format, cf-satellite 0.2. [Martin
  Raspaud]

- Renamed some global attributes. [Martin Raspaud]

- Netcdf: working towards better matching CF conventions. [Martin
  Raspaud]

- WIP: NetCDF cleaning. [Martin Raspaud]

  - scale_factor and add_offset are now single values.
  - vertical_perspective to geos


- Merge branch 'unstable' into feature-netcdf-upgrade. [Martin Raspaud]

- Group channels by unit and area. [Martin Raspaud]

- Do not apply scale and offset when reading. [Martin Raspaud]

- WIP: updating the netcdf interface. [Martin Raspaud]

- Merge branch 'unstable' of /data/proj/SAF/GIT/satpy into unstable.
  [Martin Raspaud]

- Changed handeling of "_FillValue"-attributes. Added
  find_FillValue_tags function to search for "_FillValue" attributes.
  The "_FillValue" attributes are used and set when variables are
  created. [Nina.Hakansson]

- Cosmetics. [Martin Raspaud]

- Merge branch 'unstable' of /data/proj/SAF/GIT/satpy into unstable.
  [Martin Raspaud]

- Fixing bug concerning viirs bandlist and the issue of preventing the
  loading of channels when only products are requested. [Adam Dybbroe]

- Fixing VIIRS reader - does not try to read SDR data if you only want
  to load a product. Minor fixes in MODIS and AAPP1b readers. [Adam
  Dybbroe]

- Merge branch 'unstable' of /data/proj/SAF/GIT/satpy into unstable.
  [Martin Raspaud]

- Merge branch 'unstable' of /data/proj/SAF/GIT/satpy into unstable.
  [Adam Dybbroe]

- Bugfix in viirs sdr reader. [Adam Dybbroe]

- Added ir108 composite to Viirs. [Martin Raspaud]

- RUN: add possibility to get prerequisites for a list of areas. [Martin
  Raspaud]

- Updating area_id for the channel during viirs loading and assembling
  of segments. [Martin Raspaud]

- Area handling in viirs and assembling segments. [Martin Raspaud]

- Viirs true color should have a transparent background. [Martin
  Raspaud]

- Added enhancements to the image.__call__ function. [Martin Raspaud]

- Fixing runner to warn for missing functions (instead of crashing).
  [Martin Raspaud]

- Merge branch 'unstable' of /data/proj/SAF/GIT/satpy into unstable.
  [Martin Raspaud]

  Conflicts:
  	satpy/satin/viirs_sdr.py


- Bug fix green-snow RGB. [Adam Dybbroe]

- Cleaning up a bit in viirs reader. [Adam Dybbroe]

- Temporary fix to deal with scale-factors (in CLASS archive these are
  not tuples of 2 but 6). Taken from old fix in npp-support branch.
  [Adam Dybbroe]

- Merge branch 'unstable' of /data/proj/SAF/GIT/satpy into unstable.
  [Adam Dybbroe]

- Support for bzip2 compressed NWCSAF products (EARS-NWC) [Adam Dybbroe]

- More flexible viirs reading, and fixes to viirs composites. [Martin
  Raspaud]

- Added a stereographic projection translation. [Lars Orum Rasmussen]

- Added modist as valid name for 'eos1' [Lars Orum Rasmussen]

- Added night_microphysics. [Lars Orum Rasmussen]

- Added stretch option. [Lars Orum Rasmussen]

- Merge branch 'unstable' of /data/proj/SAF/GIT/satpy into unstable.
  [Martin Raspaud]

- Feature: new function to create an image from a scene. [Martin
  Raspaud]

- Fixed a new npp template config file, with geo_filename example. [Adam
  Dybbroe]

- Adding 500meter scan area. [Adam Dybbroe]

- Fixing bug in geolocation reading and removing old style viirs
  composite file. [Adam Dybbroe]

- Using a template from configuration file to find the geolocation file
  to read - for all VIIRS bands. [Adam Dybbroe]

- Fixed bug in hr_natural and added a dnb method. [Adam Dybbroe]

- Fixing Bow-tie effects and geolocation for VIIRS when using Cloudtype.
  Needs to be generalised to all products! [Adam Dybbroe]

- Support for tiepoint grids and interpolation + masking out no-data
  geolocation (handling VIIRS Bow-tie deletetion) [Adam Dybbroe]

- Merge branch 'unstable' of /data/proj/SAF/GIT/satpy into unstable.
  [Adam Dybbroe]

- Adding viirs composites and pps_odim reader for avhrr and viirs
  channel data in satellite projection (swath) [Adam Dybbroe]

- Added a Geo Phys Product to modis level2. [Lars Orum Rasmussen]

- Merge branch 'pre-master' of github.com:mraspaud/satpy into pre-master.
  [Lars Orum Rasmussen]

- Merge branch 'unstable' of /data/proj/SAF/GIT/satpy into unstable.
  [Martin Raspaud]

- Adding support for ob_tran projection even though it is not cf-
  compatible yet. [Adam Dybbroe]

- Merge branch 'unstable' of /data/proj/SAF/GIT/satpy into unstable.
  [Adam Dybbroe]

- Added the reading of geolocation data from the PPS formatet level1
  file. [Adam Dybbroe]

- Added Europe Mesan area to template. [Adam Dybbroe]

- Feature: MSG hdf files are now used to determine the area. [Martin
  Raspaud]

- Fixed error message. [Martin Raspaud]

- Cleanup: clarified import error. [Martin Raspaud]

- Cleanup: More descriptive message when plugin can't be loaded. [Martin
  Raspaud]

- Raised version number. [Martin Raspaud]

- More relevant messages in msg_hdf reading. [Martin Raspaud]

- Adding a RGB for night condition. [Lars Orum Rasmussen]

- Merge branch 'pre-master' into unstable. [Martin Raspaud]

- Merge branch 'pre-master' into unstable. [Martin Raspaud]

v0.11.5 (2012-05-21)
--------------------

Fix
~~~

- Bugfix: importing geotiepoints. [Martin Raspaud]

- Bugfix: hdfeos was not eumetcast compliant :( [Martin Raspaud]

- Bugfix: Do not raise exception on loading failure (nwcsaf_pps) [Martin
  Raspaud]

- Bugfix: fixed misc bugs. [Martin Raspaud]

- Bugfix: comparing directories with samefile is better than ==. [Martin
  Raspaud]

- Bugfix: updating old eps_l1b interface. [Martin Raspaud]

- Bugfix: Fixed typo in gatherer. [Martin Raspaud]

- Bugfix: taking satscene.area into consideration for get_lonlat.
  [Martin Raspaud]

- Bugfix: mipp required version to 0.6.0. [Martin Raspaud]

- Bugfix: updating unittest and setup for new mipp release. [Martin
  Raspaud]

- Bugfix: for eps l1b, get_lonlat did not return coherent values since
  the introduction of pyresample. [Martin Raspaud]

- Bugfix: mipp to mipp_xrit namechange. [Martin Raspaud]

- Bugfix: better detection of needed channels in aapp1b. [Martin
  Raspaud]

- Bugfix: support for other platforms. [Martin Raspaud]

- Bugfix: Support python 2.4 in mipp plugin. [Martin Raspaud]

- Bugfix: masked arrays should be conserved by scene.__setitem__ [Martin
  Raspaud]

- Bugfix: Don't make area and time_slot static in compositer. [Martin
  Raspaud]

- Bugfix: reinit channels_to_load and messages for no loading. [Martin
  Raspaud]

  - When the loading process is interrupted, the channels_to_load attribute was not reinitialized.
  - Added a message when loading for a given level did not load anything.


- Bugfix: Give an informative message when area is missing for msg's hdf
  reader. [Martin Raspaud]

- Bugfix: update satpos file retrieval for hrpt and eps1a. [Martin
  Raspaud]

- Bugfix: fixed unittests for new plugin system. [Martin Raspaud]

- Bugfix: Do not load plugins automatically... [Martin Raspaud]

- Bugfix: satellite vs satname again. [Martin Raspaud]

- Bugfix: don't crash if msg hdf can't be loaded. [Martin Raspaud]

- Bugfix: project now chooses mode automatically by default. [Martin
  Raspaud]

- Bugfix: eps_avhrr adapted to new plugin format. [Martin Raspaud]

- Bugfix: loading in msg_hdf adapted to new plugin system. [Martin
  Raspaud]

- Bugfix: loading plugins should fail on any exception. [Martin Raspaud]

- Bugfix: stupid syntax error. [Martin Raspaud]

- Bugfix: mistook satname for satellite. [Martin Raspaud]

- Bugfix: move to jenkins. [Martin Raspaud]

- Bugfix: affecting area to channel_image. [Martin Raspaud]

- Bugfix: Better handling of alpha channel. [Martin Raspaud]

- Bugfix: filewatcher would wait a long time if no new file has come.
  [Martin Raspaud]

Other
~~~~~

- Bumped up version number. [Martin Raspaud]

- Modis level-2 reader and netcdf writer can now handle scenes
  containing only geo-physical product (and no channels) [Lars Orum
  Rasmussen]

- Feature: Pypi ready. [Martin Raspaud]

- Bufix: updating to use python-geotiepoints. [Martin Raspaud]

- Bumping up the version number for the next release. [Martin Raspaud]

- Doc: updating add_overlay documentation. [Martin Raspaud]

- Merge pull request #2 from cheeseblok/FixViirsRedSnow. [Martin
  Raspaud]

  Fix typo in red_snow check_channels method

- Fix typo in red_snow check_channels method. [Scott Macfarlane]

- Feature: adding interpolation to modis lon lats. [Martin Raspaud]

- Use pynav to get lon/lats if no file can be read. [Martin Raspaud]

- Hack to handle both level2 and granules. [Martin Raspaud]

- Added the possibility to provide a filename to eps_l1b loader. [Martin
  Raspaud]

- Merge branch 'feature_new_eps_reader' into unstable. [Martin Raspaud]

- Added xml file to etc and setup.py. [Martin Raspaud]

- Bugfix in geolocation assignment. [Martin Raspaud]

- Allowing for both 3a and 3A. [Martin Raspaud]

- Put xml file in etc. [Martin Raspaud]

- New eps l1b is now feature complete. Comprehensive testing needed.
  [Martin Raspaud]

- Added a new eps l1b reader based on xml description of the format.
  [Martin Raspaud]

- Corrected longitude interpolation to work around datum shift line.
  [Martin Raspaud]

- Cloudtype channel now called "CT". [Martin Raspaud]

- Merge branch 'pre-master' of git://github.com/mraspaud/satpy into pre-
  master. [Martin Raspaud]

- SetProjCS is now correctly called after ImportFromProj4. [Lars Orum
  Rasmussen]

  Added SetWellKnownGeogCS if available


- Merge branch 'pre-master' into unstable. [Martin Raspaud]

  Conflicts:
  	satpy/satin/mipp_xsar.py


- More correct 'new area' [Lars Orum Rasmussen]

- Mipp restructure. [Lars Orum Rasmussen]

- Merge branch 'pre-master' into area-hash. [Lars Orum Rasmussen]

- Merge branch 'pre-master' into area-hash. [Lars Orum Rasmussen]

- Now more unique projection filenames (using hash of areas) [Lars Orum
  Rasmussen]

- Enhancements to pps hdf format readers. [Martin Raspaud]

- Feature: added support for geotiff float format in geo_image. [Martin
  Raspaud]

- Don't touch satscene.area if already present (mipp reading) [Martin
  Raspaud]

- Feature: get best msg hdf file using area_extent. [Martin Raspaud]

- Duck typing for channel assignation. [Martin Raspaud]

- Fixed meteosat reading. [Martin Raspaud]

  - do not change the scene metadata when no channel is loaded
  - do not crash if no PGE is present


- Added shapes in satpy.cfg.template for pycoast. [Martin Raspaud]

- Cleanup. [Martin Raspaud]

- New add_overlay function, using pycoast. [Martin Raspaud]

- Added test for __setitem__ (scene) [Martin Raspaud]

- Feature: add a global area if possible. [Martin Raspaud]

- Merge branch 'unstable' of /data/proj/SAF/GIT/satpy into unstable.
  [Martin Raspaud]

- Fixing so thar also other products (than Channel data) can be
  assempled. [Adam.Dybbroe]

- Adding data member to CloudType. [Adam.Dybbroe]

- Added support for trucolor image from modis. [Adam.Dybbroe]

- Cleaning up geo_image.py. [Martin Raspaud]

- Merge branch 'unstable' of /data/proj/SAF/GIT/satpy into unstable.
  [Martin Raspaud]

  Conflicts:
  	satpy/satin/hdfeos_l1b.py


- Merge branch 'unstable' of /data/proj/SAF/GIT/satpy into unstable.
  [Adam.Dybbroe]

- Minor cosmetic/editorial stuff. [Adam.Dybbroe]

- Small bugfix - viirs interface. [Adam.Dybbroe]

- Feature: wrapping up hdfeos upgrade. [Martin Raspaud]

  - migrated data to float32 instead of float64
  - support only geoloc a 1km resolution at the moment
  - adjust channel resolution to match loaded data
  - added template terra.cfg file.


- Trimming out dead detectors. [Adam.Dybbroe]

- WIP: hdf eos now reads only the needed channels, and can have several
  resolutions. Geoloc is missing though. [Martin Raspaud]

- WIP: Started working on supporting halv/quarter files for modis.
  [Martin Raspaud]

- Merge branch 'unstable' of /data/proj/SAF/GIT/satpy into unstable.
  [Martin Raspaud]

- Changed MODIS HDF-EOS level 1b reader to accomodate both the thinned
  EUMETCasted data and Direct readout data. Changed name from
  thin_modis.py to hdfeos_l1b.py. Added filename pattern to config.
  [Adam.Dybbroe]

- Fixing indexing bug: missing last line in Metop AVHRR granule.
  [Adam.Dybbroe]

- Revert "Merge branch 'unstable' of /data/proj/SAF/GIT/satpy into
  unstable" [Martin Raspaud]

  This reverts commit 45809273f2f9670c8282c32197ef47071aecaa74, reversing
  changes made to 10ae6838131ae1b6e119e05e08496d1ec9018a4a.


- Revert "Reapplying thin_modis cleaning" [Martin Raspaud]

  This reverts commit 52c63d6fbc9f12c03b645f29dd58250da943d24a.


- Reapplying thin_modis cleaning. [Martin Raspaud]

- Merge branch 'unstable' of /data/proj/SAF/GIT/satpy into unstable.
  [Martin Raspaud]

- Merge branch 'unstable' of /data/proj/SAF/GIT/satpy into unstable.
  [Adam.Dybbroe]

- Merge branch 'unstable' of /data/proj/SAF/GIT/satpy into unstable.
  [Adam.Dybbroe]

- Merge branch 'pre-master' into unstable. [Adam.Dybbroe]

  Conflicts:
  	satpy/satin/eps_avhrr.py


- Minor enhancements to nwcsaf pps cloud type reading: Adding support
  for phase and quality flags. [Adam.Dybbroe]

- Fixing indexing bug: missing last line in Metop AVHRR granule.
  [Adam.Dybbroe]

- Merge branch 'unstable' of /data/proj/SAF/GIT/satpy into unstable.
  [Adam.Dybbroe]

  Conflicts:
  	doc/source/conf.py
  	satpy/instruments/mviri.py
  	satpy/instruments/seviri.py
  	satpy/instruments/test_mviri.py
  	satpy/instruments/test_seviri.py
  	satpy/instruments/test_visir.py
  	satpy/instruments/visir.py
  	satpy/satin/test_mipp.py
  	satpy/satin/thin_modis.py
  	satpy/saturn/runner.py
  	satpy/scene.py
  	setup.py
  	version.py


- Merge branch 'unstable' of https://github.com/mraspaud/satpy into
  unstable. [Adam.Dybbroe]

- Thin_modis Cleanup. [Martin Raspaud]

- Cleanup. [Martin Raspaud]

- Style: Cleaning up. [Martin Raspaud]

- Doc: added screenshots. [Martin Raspaud]

- Cleanup, switch to compositer globaly. [Martin Raspaud]

- Doc: added more documentation to polar_segments.py. [Martin Raspaud]

- Cleanup: remove old unit test for assemble_swath. [Martin Raspaud]

- Bugfix in assemble_segments. [Martin Raspaud]

- Cleanup: removed old assemble_swath function. [Martin Raspaud]

- Doc: update docstring for project. [Martin Raspaud]

- Upgrade: assemble_segments now uses scene factory. [Martin Raspaud]

- DOC: examples are now functional. [Martin Raspaud]

- Cleanup: removed old plugins directory. [Martin Raspaud]

- Merge branch 'new_plugins' into unstable. [Martin Raspaud]

  Conflicts:
  	satpy/plugin_base.py


- Init file for plugins initialization. [Adam.Dybbroe]

- Merge branch 'new_plugins' of https://github.com/mraspaud/satpy into
  new_plugins. [Adam.Dybbroe]

- Removing old deprecated and now buggy part - has been caught by the
  try-exception since long. Adding for plugins directory. [Adam.Dybbroe]

- Corrected import bug. [Adam.Dybbroe]

- Merge branch 'unstable' into new_plugins. [Adam.Dybbroe]

- Bug correction - config file reading section 'format' [Adam.Dybbroe]

- Removing old deprecated and now buggy part - has been caught by the
  try-exception since long. Adding for plugins directory. [Adam.Dybbroe]

- Merge branch 'unstable' of github.com:mraspaud/satpy into unstable.
  [Martin Raspaud]

- Merge branch 'unstable' of https://github.com/mraspaud/satpy into
  unstable. [Adam.Dybbroe]

- First time in git. [Adam.Dybbroe]

- Merge branch 'unstable' of https://github.com/mraspaud/satpy into
  unstable. [Adam.Dybbroe]

- Meris level-2 reader - first commit. [Adam.Dybbroe]

- Minor fixes. [Adam.Dybbroe]

- Fixed typo. [Adam.Dybbroe]

- Feature: updating mipp test to use factory. [Martin Raspaud]

- Cleaning up an old print. [Martin Raspaud]

- Merge branch 'v0.10.2-support' into unstable. [Martin Raspaud]

- Feature: added support for new eumetsat names (modis) and terra.
  [Martin Raspaud]

- Merge branch 'new_plugins' into unstable. [Martin Raspaud]

- Moved mipp plugin back to satin. [Martin Raspaud]

- Feature: all former plugins are adapted to newer format. [Martin
  Raspaud]

- Style: finalizing plugin system. Now plugins directories loaded from
  satpy.cfg. [Martin Raspaud]

- Cleanup: removing old stuff. [Martin Raspaud]

- Feature: added reader plugins as attributes to the scene, called
  "<format>_reader". [Martin Raspaud]

- Feature: new plugin format, added a few getters and made scene
  reference weak. [Martin Raspaud]

- New plugin system. [Martin Raspaud]

  Transfered the mipp plugin.


- DOC: fixed path for examples. [Martin Raspaud]

- DOC: Added documentation examples to the project. [Martin Raspaud]

- Merge branch 'unstable' of github.com:mraspaud/satpy into unstable.
  [Martin Raspaud]

- Using LOG call instead of print. [Adam.Dybbroe]

- Fixed missing LOG import. [Adam.Dybbroe]

- Further improvements to MODIS level2 reader and processor.
  [Adam.Dybbroe]

- Feature: Added projection to the pps_hdf channels. [Martin Raspaud]

- DOC: added use examples in the documentation directory. [Martin
  Raspaud]

- Merge branch 'master' into unstable. [Martin Raspaud]

- Added posibility to have instrument_name in the filenames.
  [Adam.Dybbroe]

- Making sure we pass on orbit number when projecting the scene.
  [Adam.Dybbroe]

- Added colour map for Modis Chlorophyl-A product. [Adam.Dybbroe]

- Taking away the alpha parameters for RGB modes. [Martin Raspaud]

- Added areas in channels for test. [Martin Raspaud]

- Added the radius parameter to runner. [Martin Raspaud]

- Adding preliminary NWCSAF pps product reader. [Adam.Dybbroe]

- Cleaning up. [Martin Raspaud]

- Updated satpos file directories. [Martin Raspaud]

- Cleaning up. [Martin Raspaud]

- Merge branch 'pre-master' into unstable. [Martin Raspaud]

- Updated copyright and version number. [Martin Raspaud]

- Updating setup stuff. [Martin Raspaud]

- Merge branch 'pre-master' into unstable. [Martin Raspaud]

- Adding Day/Night band support. [Adam.Dybbroe]

- Adding area for mapping sample data i-bands. [Adam.Dybbroe]

- Scaling reflectances to percent (%) as required in satpy.
  [Adam.Dybbroe]

- Adding support for I-bands. [Adam.Dybbroe]

- Merge branch 'pre-master' of https://github.com/mraspaud/satpy into
  pre-master. [Adam.Dybbroe]

- Merge branch 'npp-support' into pre-master. [Adam.Dybbroe]

- Renamed to npp1.cfg. [Adam.Dybbroe]

- VIIRS composites - M-bands only so far. [Adam.Dybbroe]

- Cleaning print statements. [Adam.Dybbroe]

- NPP template. [Adam.Dybbroe]

- Adding NPP/VIIRS test area for sample data: M-bands. [Adam.Dybbroe]

- Adding I-band support. [Adam.Dybbroe]

- Fixing for re-projection. [Adam.Dybbroe]

- Various small corrections. [Adam.Dybbroe]

- Corrected band widths - ned to be in microns not nm. [Adam.Dybbroe]

- Support for NPP/JPSS VIIRS. [Adam.Dybbroe]

- Updated copyright in sphinx doc. [Martin Raspaud]

- Deprecating add_overlay in favor of pycoast. [Martin Raspaud]

- Merge branch 'feature-new-nc-format' into unstable. [Martin Raspaud]

- Added support for different ordering of dimensions in band data.
  [Martin Raspaud]

  Use the band_axis keyword argument.


- NC reader support different dimension orderings for band-data. [Martin
  Raspaud]

- NC: now band data is of shape (band, x, y). [Martin Raspaud]

v0.11.0 (2011-09-20)
--------------------

Fix
~~~

- Bugfix: netcdf saving didn't record lat and lon correctly. [Martin
  Raspaud]

- Bugfix: netcdf saving didn't work if only one value was available.
  [Martin Raspaud]

- Bugfix: test_mipp had invalid proj parameters. [Martin Raspaud]

- Bugfix: satellite vs satname again. [Martin Raspaud]

- Bugfix: project now chooses mode automatically by default. [Martin
  Raspaud]

- Bugfix: move to jenkins. [Martin Raspaud]

- Bugfix: fixed unit test for projector reflecting the new mode
  handling. [Martin Raspaud]

- Bugfix: fixed None mode problem in projector. [Martin Raspaud]

- Bugfix: The default projecting mode now take into account the types of
  the in and out areas. [Martin Raspaud]

- Bugfix: forgot the argument to wait in filewatcher. [Martin Raspaud]

- Bugfix: tags and gdal_options were class attributes, they should be
  instance attributes. [Martin Raspaud]

- Bugfix: 0 reflectances were masked in aapp1b loader. [Martin Raspaud]

- Bugfix: corrected parallax values as no_data in msg products reading.
  [Martin Raspaud]

- Bugfix: tags and gdal_options were class attributes, they should be
  instance attributes. [Martin Raspaud]

- Bugfix: Compatibility with nordrad was broken. [Martin Raspaud]

- Bugfix: forgot the argument to wait in filewatcher. [Martin Raspaud]

- Bugfix: forgot strptime = datetime.strptime when python > 2.5. [Martin
  Raspaud]

- Bugfix: corrected parallax values as no_data in msg products reading.
  [Martin Raspaud]

- Bugfix: individual channel areas are preserved when assembled
  together. [Martin Raspaud]

- Bugfix: cleanup tmp directory when convertion to lvl 1b is done.
  [Martin Raspaud]

- Bugfix: remove hardcoded pathes in hrpt and eps lvl 1a. [Martin
  Raspaud]

- Bugfix: use satpy's main config path. [Martin Raspaud]

- Bugfix: added python 2.4 compatibility. [Martin Raspaud]

- Bugfix: allow all masked array as channel data. [Martin Raspaud]

- Better support for channel-bound areas. [Martin Raspaud]

- Bugfix: 0 reflectances were masked in aapp1b loader. [Martin Raspaud]

- Bugfix: tags and gdal_options were class attributes, they should be
  instance attributes. [Martin Raspaud]

- Bugfix: error checking on area_extent for loading. [Martin Raspaud]

- Bugfix: non loaded channels should not induce computation of
  projection. [Martin Raspaud]

- Bugfix: thin modis didn't like area extent and was locked in 2010...
  [Martin Raspaud]

- Bugfix: Compatibility with nordrad was broken. [Martin Raspaud]

Other
~~~~~

- Merge branch 'release-0.11' [Martin Raspaud]

- Merge branch 'pre-master' into release-0.11. [Martin Raspaud]

- Updated copyright dates in setup.py. [Martin Raspaud]

- Bumped version number to 0.11.0. [Martin Raspaud]

- Merge branch 'pre-master' into unstable. [Martin Raspaud]

- Now a channel can be added to a scene dynamically using dict notation.
  [esn]

- Added units to aapp1b reader. [Martin Raspaud]

- Deactivating mipp loading test. [Martin Raspaud]

- Adjusted tests for compositer. [Martin Raspaud]

- Merge branch 'feature-cleaning' into unstable. [Martin Raspaud]

- Merge branch 'unstable' into feature-cleaning. [Martin Raspaud]

- Merge branch 'pre-master' into unstable. [Martin Raspaud]

- Added append function to scene.py. [Esben S. Nielsen]

- New error message when no instrument-levelN section is there in the
  satellite config file. [Martin Raspaud]

- Merge branch 'feature-radius-of-influence' into unstable. [Martin
  Raspaud]

- Syntax bug fixed. [Martin Raspaud]

- Made orbit number default to None for PolarFactory's create_scene.
  [Martin Raspaud]

- Merge branch 'feature-radius-of-influence' into unstable. [Martin
  Raspaud]

- Radius of influence is now a keyword parameter to the scene.project
  method. [Martin Raspaud]

- Merge branch 'pre-master' into unstable. [Martin Raspaud]

- Can now get reader plugin from PYTHONPATH. [Esben S. Nielsen]

- Renamed asimage to as_image. [Martin Raspaud]

- Wavelength and resolution are not requirements in config files
  anymore. [Martin Raspaud]

- Merge branch 'feature-channel-to-image' into unstable. [Martin
  Raspaud]

- Feature: added the asimage method to channels, to retrieve a black and
  white image from the channel data. [Martin Raspaud]

- Merge branch 'feature-doc-examples' into unstable. [Martin Raspaud]

- Doc: added more documentation to polar_segments.py. [Martin Raspaud]

- DOC: examples are now functional. [Martin Raspaud]

- DOC: fixed path for examples. [Martin Raspaud]

- DOC: Added documentation examples to the project. [Martin Raspaud]

- DOC: added use examples in the documentation directory. [Martin
  Raspaud]

- Merge branch 'feature-project-mode' into unstable. [Martin Raspaud]

- Doc: update docstring for project. [Martin Raspaud]

- Cleanup. [Martin Raspaud]

- Switched seviri and mviri to compositer. [Martin Raspaud]

- Cleanup. [Martin Raspaud]

- Style: Cleaning up. [Martin Raspaud]

- Doc: added screenshots. [Martin Raspaud]

- Cleanup, switch to compositer globaly. [Martin Raspaud]

  Conflicts:

  	satpy/instruments/visir.py
  	satpy/satin/hrpt.py
  	satpy/saturn/runner.py


- Cleanup: remove old unit test for assemble_swath. [Martin Raspaud]

- Bugfix in assemble_segments. [Martin Raspaud]

- Cleanup: removed old assemble_swath function. [Martin Raspaud]

  Conflicts:

  	satpy/scene.py


- Upgrade: assemble_segments now uses scene factory. [Martin Raspaud]

- Fixed typo. [Adam.Dybbroe]

- Feature: updating mipp test to use factory. [Martin Raspaud]

- Cleaning up an old print. [Martin Raspaud]

  Conflicts:

  	satpy/satin/mipp.py


- Cleanup: removing old stuff. [Martin Raspaud]

- Cleaned up and updated meteosat 9 cfg template further. [Martin
  Raspaud]

- Updated templates to match pytroll MSG tutorial. [Esben S. Nielsen]

- Simplified reading of log-level. [Lars Orum Rasmussen]

- Proposal for reading loglevel from config file. [Lars Orum Rasmussen]

- Cfscene now handles channels with all masked data. [Esben S. Nielsen]

- Netcdf area fix. [Martin Raspaud]

- Syle: copyright updates. [Martin Raspaud]

- Modified the modis-lvl2 loader and extended a bit the cf-io
  interfaces. [Adam.Dybbroe]

- First time in GIT A new reader for EOS-HDF Modis level-2 files from
  NASA. See http://oceancolor.gsfc.nasa.gov/DOCS/ocformats.html#3 for
  format description. [Adam.Dybbroe]

- Added license. [Martin Raspaud]

- Merge branch 'unstable' of github.com:mraspaud/satpy into unstable.
  [Martin Raspaud]

- Info needs to be an instance attribute. [Lars Orum Rasmussen]

- Fix initialization of self.time_slot. [Lars Orum Rasmussen]

- Merge branch 'v0.10.2-support' into unstable. [Martin Raspaud]

- Added pyc and ~ files to gitignore. [Martin Raspaud]

- Updated thin modis reader for new file name. [Martin Raspaud]

- Merge branch 'v0.10.1-support' into unstable. [Martin Raspaud]

- Compression and tiling as default for geotifs. [Martin Raspaud]

- Merge branch 'v0.10.0-support' into unstable. [Martin Raspaud]

- Feauture: support for qc_straylight. [Martin Raspaud]

- Compression and tiling as default for geotifs. [Martin Raspaud]

- WIP: attempting interrupt switch for sequential runner. [Martin
  Raspaud]

- Feature: changing filewatcher from processes to threads. [Martin
  Raspaud]

- Feauture: support for qc_straylight. [Martin Raspaud]

- Compression and tiling as default for geotifs. [Martin Raspaud]

- Update: modis enhancements. [Martin Raspaud]

- Feature: filewatcher keeps arrival order. [Martin Raspaud]

- Feature: concatenation loads channels. [Martin Raspaud]

- Feature: use local tles instead of downloading systematically. [Martin
  Raspaud]

- Feature: move pyaapp as single module. [Martin Raspaud]

- Feature: added ana geoloc for hrpt and eps lvl 1a. [Martin Raspaud]

- Cosmetics. [Martin Raspaud]

- Added gatherer and two_line_elements. [Martin Raspaud]

- Merge branch 'unstable' of github.com:mraspaud/satpy into unstable.
  [Martin Raspaud]

- Moved a parenthesis six characters to the left. [Lars Orum Rasmussen]

- Feature: assemble_segments function, more clever and should replace
  assemble_swaths. [Martin Raspaud]

- Feature: thin modis reader upgrade, with lonlat estimator and channel
  trimmer for broken sensors. [Martin Raspaud]

- Merge branch 'unstable' of github.com:mraspaud/satpy into unstable.
  [Martin Raspaud]

- Netcdf bandname now only uses integer part of resolution. [Esben S.
  Nielsen]

- Improvement: made resolution int in band names, for netcdf. [Martin
  Raspaud]

- Cleaning. [Martin Raspaud]

- WIP: ears. [Martin Raspaud]

- Trying to revive the pynwclib module. [Martin Raspaud]

- Cleaning. [Martin Raspaud]

- Wip: polar hrpt 0 to 1b. [Martin Raspaud]

- Feature: Added proj4 parameters for meteosat 7. [Martin Raspaud]

- Merge branch 'unstable' of github.com:mraspaud/satpy into unstable.
  [Martin Raspaud]

- Cosmetic. [Esben S. Nielsen]

- Now channels are read and saved in order. Optimized scaling during CF
  save. [Esben S. Nielsen]

- Feature: Adding more factories. [Martin Raspaud]

- Documentation: adding something on factories and area_extent. [Martin
  Raspaud]

- Documentation: added needed files in setup.py. [Martin Raspaud]

v0.10.0 (2011-01-18)
--------------------

Fix
~~~

- Bugfix: fixed matching in git command for version numbering. [Martin
  Raspaud]

- Bugfix: Negative temperatures (in K) should not be valid data when
  reading aapp1b files. [Martin Raspaud]

- Bugfix: remove hudson from tags when getting version. [Martin Raspaud]

- Bugfix: fixed hdf inconstistencies with the old pyhl reading of msg
  ctype and ctth files. [Martin Raspaud]

- Bugfix: Updated code and tests to validate unittests. [Martin Raspaud]

- Bugfix: data reloaded even if the load_again flag was False. [Martin
  Raspaud]

- Bugfix: updated tests for disapearance of avhrr.py. [Martin Raspaud]

- Bugfix: access to CompositerClass would fail if using the old
  interface. [Martin Raspaud]

- Bugfix: typesize for msg's ctth didn't please pps... [Martin Raspaud]

- Bugfix: fixed data format (uint8) in msg_hdf. [Martin Raspaud]

- Bugfix: wrong and forgotten instanciations. [Martin Raspaud]

- Bugfix: crashing on missing channels in mipp loading. [Martin Raspaud]

- Bugfix: forgot to pass along area_extent in mipp loader. [Martin
  Raspaud]

- Bugfix: fixing integration test (duck typing). [Martin Raspaud]

- Bugfix: pyresample.geometry is loaded lazily for area building.
  [Martin Raspaud]

- Bugfix: Updated unit tests. [Martin Raspaud]

- Bugfix: Last change introduced empty channel list for meteosat 09.
  [Martin Raspaud]

- Bugfix: Last change introduced empty channel list for meteosat 09.
  [Martin Raspaud]

- Bugfix: update unittests for new internal implementation. [Martin
  Raspaud]

- Bugfix: compression argument was wrong in
  satelliteinstrumentscene.save. [Martin Raspaud]

- Bugfix: adapted satpy to new equality operation in pyresample. [Martin
  Raspaud]

- Bugfix: More robust config reading in projector and test_projector.
  [Martin Raspaud]

- Bugfix: updated the msg_hrit (nwclib based) reader. [Martin Raspaud]

- Bugfix: swath processing was broken, now fixed. [Martin Raspaud]

- Bugfix: corrected the smaller msg globe area. [Martin Raspaud]

- Bugfix: Erraneous assumption on the position of the 0,0 lon lat in the
  seviri frame led to many wrong things. [Martin Raspaud]

- Bugfix: introduced bugs in with last changes. [Martin Raspaud]

- Bugfix: new area extent for EuropeCanary. [Martin Raspaud]

- Bugfix: Updated setup.py to new structure. [Martin Raspaud]

- Bugfix: updated integration test to new structure. [Martin Raspaud]

- Bugfix: more verbose crashing when building extensions. [Martin
  Raspaud]

- Bugfix: corrected EuropeCanary region. [Martin Raspaud]

- Bugfix: made missing areas message in projector more informative
  (includes missing area name). [Martin Raspaud]

- Bugfix: Added missing import in test_pp_core. [Martin Raspaud]

- Bugfix: fixing missing import in test_scene. [Martin Raspaud]

Other
~~~~~

- Style: remove a print statement and an unused import. [Martin Raspaud]

- Feature: Added natural composite to default composite list. [Martin
  Raspaud]

- Feature: made compositer sensitive to custom composites. [Martin
  Raspaud]

- Documentation: Upgraded documentation to 0.10.0. [Martin Raspaud]

- Merge branch 'unstable' of github.com:mraspaud/satpy into unstable.
  [Martin Raspaud]

- The RELEASE-VERSION file should not be checked into git. [Lars Orum
  Rasmussen]

- Optimized parts of satpy. Fixed projector caching. [Esben S. Nielsen]

- Optimized parts of satpy processing. Made projector caching functional.
  [Esben S. Nielsen]

- Ignore build directory. [Lars Orum Rasmussen]

- Check array in stretch_logarithmic. [Lars Orum Rasmussen]

- Prevent adding unintended logging handlers. [Lars Orum Rasmussen]

- Feature: Adding extra tags to the image allowed in local_runner.
  [Martin Raspaud]

- Style: lines to 80 chars. [Martin Raspaud]

- Merge branch 'unstable' [Martin Raspaud]

- Feature: pps hdf loading and polar production update. [Martin Raspaud]

- Style: cleanup. [Martin Raspaud]

- Merge branch 'unstable' of github.com:mraspaud/satpy into unstable.
  [Martin Raspaud]

  Conflicts:
  	satpy/satin/mipp.py


- Fixed memory problems. Workaround for lazy import of pyresample. Now
  uses weakref for compositor. [Esben S. Nielsen]

- Better logging in scene loading function. [Martin Raspaud]

- Remove unneeded import. [Martin Raspaud]

- New version. [Martin Raspaud]

- Merge branch 'master' of github.com:mraspaud/satpy. [Lars Orum
  Rasmussen]

- Feature: direct_readout chain in place. [Martin Raspaud]

- Removing no longer needed avhrr.py. [Martin Raspaud]

- Made scaling expression in cfscene.py nicer. [Esben S. Nielsen]

- Corrected shallow copy problem with compositor. Simplyfied usage of
  GeostationaryFactory. [Esben S. Nielsen]

- Feature: cleaner hdf reading for both pps and msg. [Martin Raspaud]

- Stability: added failsafe in case no config file is there when
  loading. [Martin Raspaud]

- Merge branch 'pps_hdf' into unstable. [Martin Raspaud]

- Feature: Support area_extent in scene.load. [Martin Raspaud]

- Feature: Cleaning and use the mipp area_extent and sublon. [Martin
  Raspaud]

- Style: Allow to exclude all the *level? sections. [Martin Raspaud]

- Redespached a few composites. [Martin Raspaud]

- Style: cosmetics. [Martin Raspaud]

- Feature: added the power operation to channels. [Martin Raspaud]

- Removed the no longer needed meteosat09.py file. [Martin Raspaud]

- Wip: iterative loading, untested. [Martin Raspaud]

- More on versionning. [Martin Raspaud]

- Merge branch 'unstable' into pps_hdf. [Martin Raspaud]

- Feature: started working on the PPS support. [Martin Raspaud]

- Spelling. [Martin Raspaud]

- Added logarithmic enhancement. [Lars Orum Rasmussen]

- Removed unneeded file. [Martin Raspaud]

- Api: new version of mipp. [Martin Raspaud]

- Added automatic version numbering. [Martin Raspaud]

- Version update to 0.10.0alpha1. [Martin Raspaud]

- Api: unload takes separate channels (not iterable) as input. [Martin
  Raspaud]

- Doc: updated the meteosat 9 template config. [Martin Raspaud]

- Merge branch 'unstable' of github.com:mraspaud/satpy into unstable.
  [Martin Raspaud]

  Conflicts:
  	satpy/satellites/meteosat09.py


- Feature: Introduced compound satscene objects. [Martin Raspaud]

  This is done through the use of an "image" attribute, created by the factory in the "satellites" package.
  The image attribute holds all the compositing functions, while the satscene object remains solely a container for satellite data and metadata.


- Feature: added the get_custom_composites function and a composites
  section in satpy.cfg to load custom made composites on the fly. [Martin
  Raspaud]

- Feature: make use of mipp's area_extent function. [Martin Raspaud]

- Style: cleanup channels_to_load after loading. [Martin Raspaud]

- Doc: introduce satpy.cfg. [Martin Raspaud]

- Feature: make use of the new satpy.cfg file to find the area file.
  Added the get_area_def helper function in projector. [Martin Raspaud]

- Feature: Added the new pge02f product for met09. [Martin Raspaud]

- Feature: New format keyword for images. [Martin Raspaud]

- Update: new version of mipp, putting the image upright when slicing.
  [Martin Raspaud]

- Merge branch 'unstable' of github.com:mraspaud/satpy into unstable.
  [Martin Raspaud]

  Conflicts:
  	satpy/satout/netcdf4.py
  	satpy/scene.py


- Corrected mipp slicing in mipp.py. Added keyword for selecting
  datatype in cfscene.py. Corrected transformation for netCDF data type
  in cfscene.py. [Esben S. Nielsen]

- New add_history function, and some changes in the netcdf handling.
  [Martin Raspaud]

- Upgrade: Upgraded the assemble_segments module to use only one
  coordinate class. [Martin Raspaud]

- Cosmetics: Added log message when slicing in mipp. [Martin Raspaud]

- Move everything to a satpy folder, so that import satpy should be used.
  [Martin Raspaud]

- WIP: Completing the nc4 reader. [Martin Raspaud]

- Doc: Added credits. [Martin Raspaud]

- Doc: updated build for github. [Martin Raspaud]

- Feature: Started to support arithmetic operations on channels. [Martin
  Raspaud]

- Feature: support for calibration flag for met 9. [Martin Raspaud]

- Cosmetics: Added names to copyrigths. [Martin Raspaud]

- Changed default logging. [Esben S. Nielsen]

- Merge branch 'dmi_fix' into unstable. [Martin Raspaud]

  Conflicts:
  	pp/scene.py


- Added fill_valued as a keyworded argument. [Lars Orum Rasmussen]

- Fixed oversampling error when pyresample is not present. Added
  compression as default option when writing netCDF files. [Esben S.
  Nielsen]

- Moved pyresample and osgeo dependency in geo_image.py. [Esben S.
  Nielsen]

- Feature: support umarf files for eps avhrr. [Martin Raspaud]

- Feature: support the load_again flag for meteosat 9. [Martin Raspaud]

- Feature: Allows passing arguments to reader plugins in
  SatelliteScene.load, and in particular "calibrate" to mipp. [Martin
  Raspaud]

- Feature: added the fill_value argument to channel_image function.
  [Martin Raspaud]

- Cosmetics: reorganized imports. [Martin Raspaud]

- Cosmetics: Updated some template files. [Martin Raspaud]

- Feature: Added the resave argument for saving projector objects.
  [Martin Raspaud]

- Installation: Updated version number, removed obsolete file to
  install, and made the package non zip-safe. [Martin Raspaud]

- Testing: Added tests for pp.satellites, and some cosmetics. [Martin
  Raspaud]

- Feature: Handled the case of several instruments for
  get_satellite_class. [Martin Raspaud]

- Cosmetics: changed the name of the satellite classes generated on the
  fly. [Martin Raspaud]

- Testing: more on scene unit tests. [Martin Raspaud]

- Testing: started integration testing of pp core parts. [Martin
  Raspaud]

- Testing: completed seviri tests. [Martin Raspaud]

- Testing: completed avhrr test. [Martin Raspaud]

- Testing: Added tests for instruments : seviri, mviri, avhrr. [Martin
  Raspaud]

- Testing: took away prerequisites tests for python 2.4 compatibility.
  [Martin Raspaud]

- Testing: final adjustments for visir. [Martin Raspaud]

- Testing: visir tests complete. [Martin Raspaud]

- Testing: fixed nosetest running in test_visir. [Martin Raspaud]

- Testing: corrected scene patching for visir tests. [Martin Raspaud]

- Tests: started testing the visir instrument. [Martin Raspaud]

v0.9.0 (2010-10-04)
-------------------

Fix
~~~

- Bugfix: geotiff images were all saved with the wgs84 ellipsoid even
  when another was specified... [Martin Raspaud]

- Bugfix: Corrected the formulas for area_extend computation in geos
  view. [Martin Raspaud]

- Bugfix: satellite number in cf proxy must be an int. Added also
  instrument_name. [Martin Raspaud]

- Bugfix: Erraneous on the fly area building. [Martin Raspaud]

- Bugfix: geo_image: gdal_options and tags where [] and {} by default,
  which is dangerous. [Martin Raspaud]

- Bugfix: Support for new namespace for osr. [Martin Raspaud]

- Bugfix: remove dubble test in test_channel. [Martin Raspaud]

- Bugfix: showing channels couldn't handle masked arrays. [Martin
  Raspaud]

- Bugfix: Scen tests where wrong in project. [Martin Raspaud]

- Bugfix: when loading only CTTH or CloudType, the region name was not
  defined. [Martin Raspaud]

- Bugfix: in test_channel, Channel constructor needs an argument.
  [Martin Raspaud]

- Bugfix: in test_cmp, tested GenericChannel instead of Channel. [Martin
  Raspaud]

- Bugfix: Test case for channel initialization expected the wrong error
  when wavelength argument was of the wrong size. [Martin Raspaud]

- Bugfix: Added length check for "wavelength" channel init argument.
  [Martin Raspaud]

- Bugfix: test case for channel resolution did not follow previous patch
  allowing real resolutions. [Martin Raspaud]

- Bugfix: thin modis lon/lat are now masked arrays. [Martin Raspaud]

- Bugfix: in channel constructor, wavelength triplet was not correctly
  checked for type. [Martin Raspaud]

  Just min wavelength was check three times.


Other
~~~~~

- Cosmetics and documentation in the scene module. [Martin Raspaud]

- Feature: better handling of tags and gdal options in geo_images.
  [Martin Raspaud]

- Cleanup: removed uneeded hardcoded satellites and instruments. [Martin
  Raspaud]

- Documentation: Updated readme, with link to the documentation. [Martin
  Raspaud]

- Documentation: Added a paragraph on geolocalisation. [Martin Raspaud]

- Refactoring: took away the precompute flag from the projector
  constructor, added the save method instead. [Martin Raspaud]

- Cosmetics. [Martin Raspaud]

- Cosmetics. [Martin Raspaud]

- Feature: pyresample 0.7 for projector, and enhanced unittesting.
  [Martin Raspaud]

- New template file for areas. [Martin Raspaud]

- Feature: First draft for the hrpt reading (using aapp) and eps1a
  reading (using aapp and kai). [Martin Raspaud]

- Cosmetics: cleaning up the etc directory. [Martin Raspaud]

- Testing: Basic mipp testing. [Martin Raspaud]

- Cosmetics: cfscene. [Martin Raspaud]

- Feature: One mipp reader fits all :) [Martin Raspaud]

- Feature: helper "debug_on" function. [Martin Raspaud]

- Feature: save method for satscene. Supports only netcdf4 for now.
  [Martin Raspaud]

- Feature: reload keyword for loading channels. [Martin Raspaud]

- Documentation: better pp.satellites docstring. [Martin Raspaud]

- Testing: updated the test_scene file to reflect scene changes. [Martin
  Raspaud]

- Documentation: changed a couple of docstrings. [Martin Raspaud]

- Feature: support pyresample areas in geo images. [Martin Raspaud]

- Cosmetics: changing area_id to area. [Martin Raspaud]

- Feature: adding metadata handling to channels. [Martin Raspaud]

- Feature: now scene and channel accept a pyresample area as area
  attribute. [Martin Raspaud]

- Enhancement: making a better mipp plugin. [Martin Raspaud]

- Feature: Finished the netcdf writer. [Martin Raspaud]

- Feature: updated the netcdf writer and added a proxy scene class for
  cf conventions. [Martin Raspaud]

- Documentation: big update. [Martin Raspaud]

- Documentation: quickstart now passes the doctest. [Martin Raspaud]

- Documentation: reworking. [Martin Raspaud]

- Feature: Moved get_satellite_class and build_satellite_class to
  pp.satellites. [Martin Raspaud]

- Doc: starting documentation update. [Martin Raspaud]

- Enhanced mipp reader. [Martin Raspaud]

  * Added metadata when loading scenes.
  * Added slicing when reading data from seviri
  * Added a draft generic reader


- Cosmetics: enhanced error description and debug message in aapp1b,
  giving names to loaded/missing files. [Martin Raspaud]

- Testing: updated test_scene. [Martin Raspaud]

- Feature: Added automatic retreiving of product list for a given
  satellite. [Martin Raspaud]

- Cleaning: remove class retrieving and building from runner.py. [Martin
  Raspaud]

- Cosmetics: Better error message in scene when a reader is not found,
  plus some code enbelishment. [Martin Raspaud]

- Feature: made scene object iteratable (channels are iterated). [Martin
  Raspaud]

- Feature: Adding functions to retreive a satellite class from the
  satellites name and to build it on the fly from a configuration file.
  [Martin Raspaud]

- Testing: more on channel. [Martin Raspaud]

- Testing: added test for pp.scene.assemble_swaths. [Martin Raspaud]

- Testing: scene loading tested. [Martin Raspaud]

- Cleaning: test_scene is now more pylint friendly. [Martin Raspaud]

- Feature: extended scene test. [Martin Raspaud]

- Feature: more testing of scene.py. [Martin Raspaud]

- Merge branch 'unstable' of github.com:mraspaud/satpy into unstable.
  [Martin Raspaud]

  Conflicts:
  	pp/test_scene.py


- Feature: Enhanced unitests for scene. [Martin Raspaud]

- Feature: Enhanced unitests for scene. [Martin Raspaud]

- Tests: Improving unittests for channel classes. [Martin Raspaud]

- Feature: Project function won't crash if pyresample can't be loaded.
  Returns the untouched scene instead. [Martin Raspaud]

- Rewrote Filewatcher code. [Martin Raspaud]

- Feature: added the refresh option to filewatcher to call the
  processing function even if no new file has come. [Martin Raspaud]

- Refactoring: satellite, number, variant arguments to runner __init__
  are now a single list argument. [Martin Raspaud]

- Cleaning: Removing pylint errors from runner.py code. [Martin Raspaud]

- Resolution can now be a floating point number. [Martin Raspaud]

- Added the osgeo namespace when importing gdal. [Martin Raspaud]

- Warning: Eps spline interpolation does not work around poles. [Martin
  Raspaud]

- Added the "info" attribute to channel and scene as metadata holder.
  [Martin Raspaud]

- Functionality: Automatically build satellite classes from config
  files. [Martin Raspaud]

- Added copyright notices and updated version. [Martin Raspaud]

- Changed channel names for seviri. [Martin Raspaud]

- Added info stuff in mipp reader. [Martin Raspaud]

- Added info.area_name update on projection. [Martin Raspaud]

- Added quick mode for projecting fast and dirty. [Martin Raspaud]

- Added single channel image building. [Martin Raspaud]

- Added support for gdal_options when saving a geo_image. [Martin
  Raspaud]

- Made satout a package. [Martin Raspaud]

- Added a few information tags. [Martin Raspaud]

- Added support for mipp reading of met 09. [Martin Raspaud]

- Added reader and writer to netcdf format. [Martin Raspaud]

- Added info object to the scene object in preparation for the netCDF/CF
  writer. [Adam Dybbroe]

- Added support for FY3 satellite and MERSI instrument. [Adam Dybbroe]

- Merge branch 'unstable' of git@github.com:mraspaud/satpy into unstable.
  [Martin Raspaud]

  Conflicts:
  	imageo/test_image.py

  Conflicts:
  	imageo/test_image.py


- Bugfix in image unit test: testing "almost equal" instead of "equal"
  for image inversion (floating point errors). [Martin Raspaud]

- Bugfix in image unit test: testing "almost equal" instead of "equal"
  for image inversion (floating point errors). [Martin Raspaud]

- Modified image inversion unit test to reflect new behaviour. [Martin
  Raspaud]

- New rebase. [Martin Raspaud]


