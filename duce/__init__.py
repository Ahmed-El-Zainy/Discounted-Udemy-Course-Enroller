"""
DUCE - Discounted Udemy Course Enroller
Automatically enroll in free Udemy courses
"""

__version__ = "0.1.0"
__author__ = "Ahmed-El-Zainy"
__email__ = "ahmed.elzainy@gmail.com"

from .base import LoginException, Scraper, Udemy

__all__ = ["Udemy", "Scraper", "LoginException", "__version__"]
