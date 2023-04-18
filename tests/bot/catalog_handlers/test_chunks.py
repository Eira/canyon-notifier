from app.bot.catalog_handlers import _chunks


def test_chunks():
    # todo доделать или удалить
    chunkable_list = []
    chunk_size = 1

    _chunks(chunkable_list, chunk_size)