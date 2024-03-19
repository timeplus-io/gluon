from timeplus import Schema


def test_schema(test_environment):
    try:
        Schema(env=test_environment).name("test_schema").delete()
    except Exception:
        pass

    exist = Schema(env=test_environment).name("test_schema").exist()
    assert not exist

    schema_list = Schema(env=test_environment).list()
    assert schema_list is not None

    size = len(schema_list)

    try:
        schema = Schema(env=test_environment).name("wrong_type_schema").content("").type("unknown").create()
        assert False
    except Exception:
        assert True

    try:
        schema = Schema(env=test_environment).name("wrong_content").content("something").create()
        assert False
    except Exception:
        assert True

    content = '''
              syntax = "proto3";

              message SearchRequest {
                string query = 1;
                int32 page_number = 2;
                int32 results_per_page = 3;
              }
              '''
    schema = Schema(env=test_environment).name("test_schema").content(content).create()
    assert schema is not None

    schema_list = Schema(env=test_environment).list()
    assert schema_list is not None
    size_new = len(schema_list)
    assert size_new - size == 1

    exist = Schema(env=test_environment).name("test_schema").exist()
    assert exist

    try:
        Schema(env=test_environment).name("test_schema").delete()
        assert True
    except Exception:
        assert False

    schema_list = Schema(env=test_environment).list()
    assert schema_list is not None
    size_new = len(schema_list)
    assert size_new == size

    exist = Schema(env=test_environment).name("test_schema").exist()
    assert not exist
