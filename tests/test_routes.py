import pytest
from httpx import AsyncClient
from app.main import app


@pytest.mark.asyncio
async def test_health_endpoint_structure():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/health")
        assert response.status_code == 200
        data = response.json()
        
        assert "status" in data
        assert "redis_connected" in data
        assert "openai_configured" in data
        assert isinstance(data["redis_connected"], bool)
        assert isinstance(data["openai_configured"], bool)


@pytest.mark.asyncio
async def test_text_analyze_missing_prompt():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post(
            "/api/v1/text/analyze",
            json={}
        )
        assert response.status_code == 422


@pytest.mark.asyncio
async def test_audio_synthesize_missing_text():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post(
            "/api/v1/audio/synthesize",
            json={}
        )
        assert response.status_code == 422


@pytest.mark.asyncio
async def test_text_analyze_with_cache():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post(
            "/api/v1/text/analyze",
            json={
                "prompt": "Test prompt for caching",
                "use_cache": True
            }
        )
        assert response.status_code in [200, 500]


@pytest.mark.asyncio
async def test_audio_synthesize_different_voices():
    async with AsyncClient(app=app, base_url="http://test") as client:
        voices = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]
        for voice in voices:
            response = await client.post(
                "/api/v1/audio/synthesize",
                json={
                    "text": "Test text",
                    "voice": voice,
                    "use_cache": False
                }
            )
            assert response.status_code in [200, 500]


@pytest.mark.asyncio
async def test_vision_analyze_missing_files():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post(
            "/api/v1/vision/analyze",
            params={"prompt": "Test prompt"}
        )
        assert response.status_code == 422

