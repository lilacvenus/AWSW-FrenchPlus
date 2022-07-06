from modloader import modast, modinfo
from modloader.modclass import Mod, loadable_mod

@loadable_mod
class AWSWMod(Mod):
    name = "French Mod Plus"
    version = "1.00"
    author = "Venus"
    #dependencies = ["MagmaLink"]

    def mod_load(self):
        pass

    def mod_complete(self):
        pass
