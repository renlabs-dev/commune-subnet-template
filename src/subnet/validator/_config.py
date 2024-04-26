from pydantic_settings import BaseSettings


class ValidatorSettings(BaseSettings):
    # == Scoring ==
    iteration_interval: int = 800  # set, accordingly to your tempo
    foo: int | None = None
