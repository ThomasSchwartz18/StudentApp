# utils/navigation.py

def navigate_to(new_view_class, previous_view=None, **kwargs):
    """
    Transitions from the current view to a new view.
    
    Args:
        new_view_class (class): The class of the new view to instantiate.
        previous_view (object, optional): The current view to hide or destroy.
        **kwargs: Additional parameters required by the new view.
    
    Returns:
        instance: An instance of the new view.
    """
    if previous_view:
        try:
            previous_view.close()  # Or use hide() if you plan to reuse the view.
        except Exception as e:
            print("Error closing previous view:", e)
    new_view = new_view_class(**kwargs)
    new_view.show()  # Assumes new_view has a show() method (as in PyQt widgets).
    return new_view

def go_back(current_view, previous_view):
    """
    Hides/destroys the current view and restores the previous view.
    
    Args:
        current_view (object): The currently displayed view.
        previous_view (object): The previous view to be restored.
    """
    try:
        current_view.close()  # Or current_view.hide()
    except Exception as e:
        print("Error closing current view:", e)
    previous_view.show()  # Assumes previous_view has a show() method.
