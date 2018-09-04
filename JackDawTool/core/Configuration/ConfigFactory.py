from JackDawTool.core.Configuration.ConfigBase import ConfigBase


class ConfigFactory:
    @staticmethod
    def create():
        return ConfigBase()
