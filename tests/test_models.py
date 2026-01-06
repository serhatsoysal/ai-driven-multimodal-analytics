import pytest
from pydantic import ValidationError
from app.models.schemas import (
    TextAnalysisRequest,
    AudioTranscriptionRequest,
    AudioSynthesisRequest,
    VisionAnalysisRequest,
    MultimodalTask,
    MultimodalPipelineRequest
)


def test_text_analysis_request_validation():
    request = TextAnalysisRequest(
        prompt="Test prompt",
        system_prompt="You are a helpful assistant",
        temperature=0.7,
        max_tokens=500,
        use_cache=True
    )
    assert request.prompt == "Test prompt"
    assert request.temperature == 0.7
    assert request.max_tokens == 500


def test_text_analysis_request_defaults():
    request = TextAnalysisRequest(prompt="Test")
    assert request.use_cache is True
    assert request.system_prompt is None
    assert request.temperature is None


def test_audio_synthesis_request_validation():
    request = AudioSynthesisRequest(
        text="Hello world",
        voice="alloy",
        use_cache=True
    )
    assert request.text == "Hello world"
    assert request.voice == "alloy"


def test_multimodal_task_text():
    task = MultimodalTask(
        type="text",
        prompt="What is AI?",
        use_cache=False
    )
    assert task.type == "text"
    assert task.prompt == "What is AI?"


def test_multimodal_task_audio():
    task = MultimodalTask(
        type="audio",
        action="transcribe",
        use_cache=False
    )
    assert task.type == "audio"
    assert task.action == "transcribe"


def test_multimodal_task_vision():
    task = MultimodalTask(
        type="vision",
        prompt="Describe image",
        use_cache=False
    )
    assert task.type == "vision"
    assert task.prompt == "Describe image"


def test_multimodal_pipeline_request():
    request = MultimodalPipelineRequest(
        tasks=[
            MultimodalTask(type="text", prompt="Test", use_cache=False)
        ]
    )
    assert len(request.tasks) == 1
    assert request.tasks[0].type == "text"


def test_text_analysis_request_invalid_temperature():
    with pytest.raises(ValidationError):
        TextAnalysisRequest(
            prompt="Test",
            temperature=2.5
        )


def test_text_analysis_request_invalid_max_tokens():
    with pytest.raises(ValidationError):
        TextAnalysisRequest(
            prompt="Test",
            max_tokens=-100
        )

