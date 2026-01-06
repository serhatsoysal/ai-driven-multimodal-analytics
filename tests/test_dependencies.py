import pytest
from app.dependencies import (
    get_cache_manager,
    get_text_analyzer,
    get_audio_processor,
    get_vision_analyzer,
    get_multimodal_pipeline
)


@pytest.mark.asyncio
async def test_get_cache_manager():
    cache = await get_cache_manager()
    assert cache is not None


@pytest.mark.asyncio
async def test_get_text_analyzer():
    analyzer = await get_text_analyzer()
    assert analyzer is not None


@pytest.mark.asyncio
async def test_get_audio_processor():
    processor = await get_audio_processor()
    assert processor is not None


@pytest.mark.asyncio
async def test_get_vision_analyzer():
    analyzer = await get_vision_analyzer()
    assert analyzer is not None


@pytest.mark.asyncio
async def test_get_multimodal_pipeline():
    pipeline = await get_multimodal_pipeline()
    assert pipeline is not None


@pytest.mark.asyncio
async def test_singleton_instances():
    analyzer1 = await get_text_analyzer()
    analyzer2 = await get_text_analyzer()
    assert analyzer1 is analyzer2
    
    processor1 = await get_audio_processor()
    processor2 = await get_audio_processor()
    assert processor1 is processor2
    
    vision1 = await get_vision_analyzer()
    vision2 = await get_vision_analyzer()
    assert vision1 is vision2

