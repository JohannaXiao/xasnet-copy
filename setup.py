from setuptools import setup, find_packages


setup(
    name="XASNet-XAI",
    packages=find_packages("src"),
    package_dir={"": "src"},
    version="1.0.0",
    author="Amir Kotobi",
    scripts=[],
    include_package_data=True,
    install_requires=[
        "torch>=1.12",
        "torch_geometric",
        "numpy",
        "ase>=3.21",
        "torch_scatter",
        "scikit-learn",
        "tqdm",
        "scipy",
        "rdkit",
    ],
)