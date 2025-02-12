"""
The event_handler class must be used as a base class for implementing
what needs to be done when the sync-with-sram main loopt emits events.
"""

from abc import ABC, abstractmethod


class EventHandler(ABC):
    """Abstract implementatation of the EventHandler class."""

    @abstractmethod
    def __init__(self, service, cfg, cfg_path, args):
        pass

    @abstractmethod
    def start_of_co_processing(self, co):
        """start_of_co_processing event."""

    @abstractmethod
    def add_new_user(self, co, group, givenname, sn, user, mail):
        """add_new_user event."""

    @abstractmethod
    def add_public_ssh_key(self, co, user, key):
        """add_public_ssh_key event."""

    @abstractmethod
    def delete_public_ssh_key(self, co, user, key):
        """delete_public_ssh_key event."""

    @abstractmethod
    def add_new_group(self, co, group, group_attributes):
        """add_new_group event."""

    @abstractmethod
    def remove_group(self, co, group, group_attributes):
        """remove_group event."""

    @abstractmethod
    def add_user_to_group(self, co, group, group_attributes, user):
        """add_user_to_group event."""

    @abstractmethod
    def start_grace_period_for_user(self, co, group, group_attributes, user, duration):
        """start_grace_period_for_user event."""

    @abstractmethod
    def remove_user_from_group(self, co, group, group_attributes: list, user):
        """remove_user_from_group event."""

    @abstractmethod
    def remove_graced_user_from_group(self, co, group, group_attributes, user):
        """remove_graced_user_from_group event."""

    @abstractmethod
    def finalize(self):
        """finalize event."""
