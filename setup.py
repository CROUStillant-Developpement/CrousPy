from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as readme:
    description = readme.read()
    
setup(
    name="CrousPy",
    version="2.0.4",
    license="Apache-2.0",
    author="CROUStillant Développement",
    keywords="CROUS API Python CROUStillant",
    description="A Python wrapper for the CROUS API.",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/CROUStillant-Developpement/CrousPy",
    project_urls={
        "Documentation": "https://github.com/CROUStillant-Developpement/CrousPy",
        "Issue tracker": "https://github.com/CROUStillant-Developpement/CrousPy/issues",
      },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
    install_requires=[
        "aiohttp>=3.9.5",
        "async-timeout>=4.0.3",
        "pytz>=2024.2",
    ]
)
