from conans import ConanFile, Meson

class test(ConanFile):
    name = "main"
    version = "0.0.1"
    settings = "os", "compiler", "build_type", "arch"
    generators = "pkg_config"
    exports_sources = "src/*"
    requires = "spdlog/1.10.0"

    def build(self):
        meson = Meson(self)
        meson.configure(source_dir=f"{self.source_folder}/src", build_dir="build")
        meson.build()
