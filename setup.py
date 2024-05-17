from setuptools import find_packages,setup

setup(
    name='MedicBot',
    version='0.0.0',
    author='KRSNA',
    author_email='krisnabadde@gmail.com',
    install_requires=["ctransformers==0.2.5","sentence-transformers==2.2.2","pinecone-client",
    "langchain-pinecone","python-dotenv","pypdf",'langchain==0.0.225',"flask",],
    packages=find_packages()
)