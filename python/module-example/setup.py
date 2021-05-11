
from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()  # get readme and import it
    # for long description of module
    # you may delete this if you want to manually write it
    
with open("requirments.txt", "r") as f:
  req = f.read()  # Put any requirments (If there is any)

    
setup(
    name='MyModule',  # Your module name  
  # TODO: Make sure THE FOLDER NAME is SAME AS NAME OF THE MODULE!
    packages=find_packages()
    version='0.1.0',  # module version (Make sure it's set it 0.1.0 if this is your first time making this module)
    description='My module made with python!',  # module short description
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/somone/a_repostory",  # link to your github
    author='Me',  # the author of the module, can be more than one
    license='MIT',  # module lisence
    install_requires=req
)
