'''maven 对象'''
class maven:
    Element = ['properties', 'dependencies', 'profiles', 'build']
    dependenciesKey = ['groupId', 'artifactId', 'version']
    dependencies = {}
    artifact = []