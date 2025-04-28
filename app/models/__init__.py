import importlib
import os
import pkgutil

package_dir = os.path.dirname(__file__)

for (_, module_name, _) in pkgutil.iter_modules([package_dir]):
    if not module_name.startswith('_'):
        importlib.import_module(f"{__package__}.{module_name}")