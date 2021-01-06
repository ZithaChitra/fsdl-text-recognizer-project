from setuptools import setup, find_packages


# Most projects have some dependencies
# A requirements.txt or an environment.yml

setup(

	name="example",
	version="0.1.0",
	packages=find_packages(include=[
		"lab1", "lab1.*"
		]),
	# install_requires=[
	# "PyYAML",
	# "pandas==0.23.3",
	# "numpy>=1.14.5",
	# "matplotlib>=2.2.0",
	# "jupyter"
	# ] # these requirements will automatically be 
	# # installed by pip when you install your package
)