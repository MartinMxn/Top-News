import utils.mongodb_client as client


def test_basic():
    db = client.get_db('test')
    db.demo.drop()
    assert db.test.estimated_document_count() == 0
    db.demo.insert_one({'test': 123})
    assert db.demo.estimated_document_count() == 1
    db.demo.drop()
    assert db.demo.estimated_document_count() == 0
    print('test passed')


if __name__ == "__main__":
    test_basic()