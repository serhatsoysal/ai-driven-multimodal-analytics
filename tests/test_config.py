import pytest
from app.config import settings


def test_settings_loaded():
    assert settings.openai_api_key is not None
    assert settings.api_secret_key is not None
    assert settings.jwt_secret_key is not None


def test_settings_defaults():
    assert settings.app_host == "0.0.0.0"
    assert settings.app_port == 8000
    assert settings.openai_model == "gpt-4o"
    assert settings.openai_vision_model == "gpt-4o"
    assert settings.openai_audio_model == "whisper-1"
    assert settings.openai_tts_model == "tts-1"
    assert settings.openai_tts_voice == "alloy"
    assert settings.max_tokens == 1000
    assert settings.temperature == 0.7
    assert settings.cache_ttl == 3600
    assert settings.log_level == "INFO"


def test_redis_configuration():
    assert settings.redis_url is not None
    assert isinstance(settings.redis_enabled, bool)

