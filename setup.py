import setuptools

setuptools.setup(
    name="xgit",
    packages=setuptools.find_packages(),
    install_requires=["typer", "rich"],
    entry_points={"console_scripts": ["xgit = xgit.cli:app"]},
)
