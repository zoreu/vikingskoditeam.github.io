import os
import sys
import hashlib

dir_path = os.path.dirname(os.path.realpath(__file__))
addonsxml_file = os.path.join(dir_path, "addons.xml")
addons_md5 = os.path.join(dir_path, "addons.xml.md5")

# Compatibility with 3.0, 3.1 and 3.2 not supporting u"" literals
if sys.version < '3':
    import codecs
    def u(x):
        return codecs.unicode_escape_decode(x)[0]
else:
    def u(x):
        return x

class Generator:
    def __init__(self):
        self._generate_addons_file()
        self._generate_md5_file()
        print("Finished updating addons xml and md5 files")
    
    def _generate_addons_file(self):
        addons = os.listdir(dir_path)
        addons_xml = u("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n<addons>\n")
        for addon in addons:
            addon = os.path.join(dir_path, addon)
            try:
                if not os.path.isdir(addon) or addon.endswith(".svn") or addon.endswith(".git"):
                    continue
                _path = os.path.join(addon, "addon.xml")
                with open(_path, "r", encoding="UTF-8") as f:
                    xml_lines = f.read().splitlines()
                addon_xml = ""
                for line in xml_lines:
                    if line.find("<?xml") >= 0:
                        continue
                    addon_xml += line.rstrip() + "\n"
                addons_xml += addon_xml.rstrip() + "\n\n"
            except Exception as e:
                print(f"Excluding {_path} for {e}")
        addons_xml = addons_xml.strip() + u("\n</addons>\n")
        self._save_file(addons_xml.encode("UTF-8"), file=addonsxml_file)
    
    def _generate_md5_file(self):
        m = hashlib.md5(open(addonsxml_file, "r", encoding="UTF-8").read().encode("UTF-8")).hexdigest()
        self._save_file(m.encode("UTF-8"), file=addons_md5)
    
    def _save_file(self, data, file):
        try:
            with open(file, "wb") as f:
                f.write(data)
        except Exception as e:
            print(f"An error occurred saving {file} file!\n{e}")

if __name__ == "__main__":
    Generator()
