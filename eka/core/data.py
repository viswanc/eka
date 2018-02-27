r"""
Eka - Data.
"""
import pkg_resources

# Exports
pluginsEntryPoint = 'eka.plugins.classes'
Plugins = {EntryPoint.name: EntryPoint for EntryPoint in pkg_resources.iter_entry_points(pluginsEntryPoint)} # #Note: A dictionary is maintained, as there wasn't a way to load a plugin without knowing its distro.
