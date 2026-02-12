"""
Setup script for DUCE - Discounted Udemy Course Enroller
"""

from pathlib import Path

from setuptools import find_packages, setup

# Read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

# Read requirements
requirements = (
    (this_directory / "requirements.txt").read_text(encoding="utf-8").splitlines()
)
requirements = [
    req.strip() for req in requirements if req.strip() and not req.startswith("#")
]

setup(
    name="duce-cli",
    version="0.1.0",
    author="ahmed mustafa",
    author_email="ahmedelzainy44@gmail.com",  # Add your email
    description="Automatically enroll in free Udemy courses with coupons",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ahmed-El-Zainy/Discounted-Udemy-Course-Enroller",
    project_urls={
        "Bug Tracker": "https://github.com/Ahmed-El-Zainy/Discounted-Udemy-Course-Enroller",
        "Documentation": "https://Ahmed-El-Zainy.github.io/duce/",
        "Discord": "https://discord.gg/wFsfhJh4Rh",
        "Source Code": "https://github.com/Ahmed-El-Zainy/Discounted-Udemy-Course-Enroller",
    },
    packages=find_packages(exclude=["tests", "tests.*", "*.tests", "*.tests.*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Education",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Natural Language :: English",
    ],
    python_requires=">=3.10",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "duce=duce.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "duce": [
            "config/*.json",
            "*.md",
        ],
    },
    keywords=[
        "udemy",
        "courses",
        "education",
        "automation",
        "enroller",
        "learning",
        "free-courses",
        "coupon",
    ],
    zip_safe=False,
    license="MIT",
)
