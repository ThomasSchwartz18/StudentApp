# utils/config_manager.py
import config  # Assumes a config.py file exists at the project root

def get_config(key, default=None):
    """
    Retrieves a configuration value from the config module.
    
    Args:
        key (str): The configuration key.
        default: The default value if the key is not found.
        
    Returns:
        The configuration value.
    """
    return getattr(config, key, default)

def set_config(key, value):
    """
    (Optional) Sets a configuration value at runtime.
    
    Args:
        key (str): The configuration key.
        value: The value to set.
    """
    setattr(config, key, value)
