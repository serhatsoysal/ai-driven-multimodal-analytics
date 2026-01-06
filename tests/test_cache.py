import pytest
from app.cache.redis_cache import CacheManager


@pytest.mark.asyncio
async def test_cache_manager_initialization():
    cache = CacheManager()
    await cache.connect()
    assert cache is not None
    await cache.disconnect()


@pytest.mark.asyncio
async def test_cache_set_get():
    cache = CacheManager()
    await cache.connect()
    
    test_key = "test_key"
    test_value = {"data": "test_value"}
    
    await cache.set(test_key, test_value, ttl=60)
    result = await cache.get(test_key)
    
    assert result is not None
    
    await cache.disconnect()


@pytest.mark.asyncio
async def test_cache_delete():
    cache = CacheManager()
    await cache.connect()
    
    test_key = "test_delete_key"
    test_value = {"data": "test_value"}
    
    await cache.set(test_key, test_value, ttl=60)
    await cache.delete(test_key)
    result = await cache.get(test_key)
    
    assert result is None
    
    await cache.disconnect()

