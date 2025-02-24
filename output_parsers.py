from typing import List, Dict, Any
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser

class Summary(BaseModel):
    summary: str = Field(description="A short summary of the person")
    facts: List[str] = Field(description="interesting facts about the person")

    def to_dict(self) -> Dict[str, Any]:
        return {"summary": self.summary, "facts": self.facts}
    
summary_parser = PydanticOutputParser(pydantic_object=Summary)