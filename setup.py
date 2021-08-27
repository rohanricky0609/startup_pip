import setuptools
from subprocess import check_call
from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools.command.egg_info import egg_info

with open("README.md", "r", encoding="utf-8") as fh:
	long_description = fh.read()

cmds_to_run = [
	"mkdir -p /content/model_data",
	"wget -O /content/model_data/answers_vqa.txt https://dl.fbaipublicfiles.com/pythia/data/answers_vqa.txt",
	"wget -O /content/model_data/vocabulary_100k.txt https://dl.fbaipublicfiles.com/pythia/data/vocabulary_100k.txt",
	"wget -O /content/model_data/detectron_model.pth  https://dl.fbaipublicfiles.com/pythia/detectron_model/detectron_model.pth", 
	"wget -O /content/model_data/pythia.pth https://dl.fbaipublicfiles.com/pythia/pretrained_models/vqa2/pythia_train_val.pth",
	"wget -O /content/model_data/pythia.yaml https://dl.fbaipublicfiles.com/pythia/pretrained_models/vqa2/pythia_train_val.yml",
	"wget -O /content/model_data/detectron_model.yaml https://dl.fbaipublicfiles.com/pythia/detectron_model/detectron_model.yaml",
	"wget -O /content/model_data/detectron_weights.tar.gz https://dl.fbaipublicfiles.com/pythia/data/detectron_weights.tar.gz",
	"tar xf /content/model_data/detectron_weights.tar.gz",
	"git clone https://github.com/facebookresearch/mmf.git /content/dmmf",
	"sed -i /torch/d /content/dmmf/requirements.txt",
	"pip install -e /content/dmmf",
	"git clone https://github.com/rohanricky0609/vqa-maskrcnn-benchmark.git /content/vqa-maskrcnn-benchmark",
	"python /content/vqa-maskrcnn-benchmark/setup.py build",
	"cd /content/vqa-maskrcnn-benchmark && python setup.py develop",
	"mkdir -p /content/done"
]

# "cd /home/rohan/",
#     "git clone https://github.com/facebookresearch/mmf.git mmf && cd mmf",
#     "sed -i '/torch/d' requirements.txt && pip install -e .",
#     "cd /home/rohan && git clone https://github.com/rohanricky0609/vqa-maskrcnn-benchmark.git && cd vqa-maskrcnn-benchmark",
#     "python setup.py build && python setup.py develop",

class PostInstallCommand(install):
	def run(self):
		install.run(self)
		for cmd in cmds_to_run:
			check_call(cmd,shell=True)

		#from mmf_demo import MMFDemo

class CustomDevelopCommand(develop):
	def run(self):
	   develop.run(self)
	   for cmd in cmds_to_run:
		   check_call(cmd,shell=True)

class CustomEggInfoCommand(egg_info):
	def run(self):
		egg_info.run(self)
		for cmd in cmds_to_run:
			check_call(cmd,shell=True)

setuptools.setup(
	name="startup_pip",
	version="0.0.1",
	author="Example Author",
	author_email="author@example.com",
	description="A small example package",
	long_description=long_description,
	long_description_content_type="text/markdown",
	# url="https://github.com/pypa/sampleproject",
	# project_urls={
	#     "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
	# },
	# classifiers=[
	#     "Programming Language :: Python :: 3",
	#     "License :: OSI Approved :: MIT License",
	#     "Operating System :: OS Independent",
	# ],
	# package_dir={"": "src"},
	# packages=setuptools.find_packages(where="src"),
	python_requires=">=3.6",
	cmdclass= {
		'install' : PostInstallCommand,
	}
)
