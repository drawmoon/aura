# pyright: basic

from pydantic import BaseModel, ConfigDict, Field


class Config(BaseModel):
    model_config = ConfigDict(extra="allow")

    model_name: str = Field(
        default="Qwen3.5-35B-A3B", description="The name of the AI model being used"
    )
    temperature: float = Field(
        default=0.5,
        description="Controls randomness; higher values result in more random responses",
    )
    max_tokens: int = Field(
        default=4000, description="Maximum token limit for a single response"
    )
    top_p: float = Field(
        default=1,
        description="Nucleus sampling; similar to temperature, but avoid changing both simultaneously",
    )
    presence_penalty: float = Field(
        default=0,
        description="Topic freshness; higher values increase the likelihood of introducing new topics",
    )
    frequency_penalty: float = Field(
        default=0,
        description="Frequency penalty; higher values decrease the likelihood of repeating words or phrases",
    )
    input_template: str = Field(
        default="{user_input}",
        description="Pre-processing template for user input; the latest message will be injected here",
    )
    history_message_count: int = Field(
        default=4,
        description="Number of historical messages to include in each request",
    )
    compress_threshold: int = Field(
        default=1000,
        description="Threshold for compressing history; compression triggers when uncompressed history exceeds this length",
    )
    enable_history_summary: bool = Field(
        default=True,
        description="Enable history summarization; automatically compresses conversation history to provide as context",
    )
    summary_model: str = Field(
        default="Qwen3.5-35B-A3B",
        description="Model used for summarizing conversation history and generating chat titles",
    )
