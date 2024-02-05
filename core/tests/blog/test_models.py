import pytest

pytestmark = pytest.mark.django_db


class TestPostModel:
    # post_factory is from the registerd class PostFactory in the conftest.py
    def test_str_return(self, post_factory):
        post = post_factory(title="test-post")
        assert post.__str__() == "test-post"
