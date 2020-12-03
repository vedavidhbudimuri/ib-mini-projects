from abc import ABC
from abc import abstractmethod


class PresenterInterface(ABC):

    @abstractmethod
    def get_create_post_response(self, post_id: int):
        pass

    @abstractmethod
    def raise_invalid_post_id_exception(self):
        pass

    @abstractmethod
    def get_create_comment_response(self, comment_id: int):
        pass
