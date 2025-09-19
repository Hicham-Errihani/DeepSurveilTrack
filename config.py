import os

class Config:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    DEBUG = False
    TESTING = False
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///default.db')

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///dev.db')

class TestingConfig(Config):
    """Testing configuration."""
    DEBUG = False
    TESTING = True
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///test.db')

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///prod.db')
