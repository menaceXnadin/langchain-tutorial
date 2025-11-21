from pydantic import BaseModel,Field
from typing import  Optional,Annotated,Literal
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
class Review(BaseModel):
    key_themes : list[str]=Field(description="write down all the key themes discussed in the review")
    summary : str = Field(description="a brief summary of the review")
    sentiment : Literal["positive","negative","neutral"]=Field(description="return either the review is positive negative or neutral")
    pros : Optional[list[str]] = Field(default = None,description="return the pros in a list from the review")
    cons : Optional[list[str]] = Field(default=None,description="return the cons in a list from the review")

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""I have been using the VoltX Pro Wireless Headphones for about two weeks and the experience has been surprisingly solid considering the price point. The build quality feels sturdy with a lightweight frame that sits comfortably during long sessions. The sound profile is balanced with clear mids and a decent low end that does not overpower vocals.
Battery life is the standout feature. I consistently get around 28 to 30 hours on a single charge, and the quick charge function adds roughly four hours of playback with a fifteen minute top up. Bluetooth connectivity is stable within a reasonable distance and there is no noticeable audio delay during videos.
Noise isolation is not perfect but acceptable for daily commuting. The onboard controls work well, although the touch sensors can occasionally misread swipes.
Overall, the VoltX Pro offers strong value for anyone looking for reliable wireless headphones without stretching their budget.""")

print(result)
print("==============================")
print(result.pros)
# print(result['sentiment'])
# print("==============================")
# print(result['summary'])
# print("==============================")
print(type(result))