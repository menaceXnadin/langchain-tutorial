from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional
load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

class Review(TypedDict):
    key_themes : Annotated[list[str],"write all the key themes mentioned in the review"]
    summary:Annotated[str,"A brief summary of the review"]
    sentiment:Annotated[str,"Return either Positive, Negatie or Neutral"]
    pros : Annotated[Optional[list[str]],"return the pros in a list from the review"]
    cons : Annotated[Optional[list[str]],"return the cons in a list from the review"]
structured_model = model.with_structured_output(Review)
result = structured_model.invoke("""I have been using the VoltX Pro Wireless Headphones for about two weeks and the experience has been surprisingly solid considering the price point. The build quality feels sturdy with a lightweight frame that sits comfortably during long sessions. The sound profile is balanced with clear mids and a decent low end that does not overpower vocals.
Battery life is the standout feature. I consistently get around 28 to 30 hours on a single charge, and the quick charge function adds roughly four hours of playback with a fifteen minute top up. Bluetooth connectivity is stable within a reasonable distance and there is no noticeable audio delay during videos.
Noise isolation is not perfect but acceptable for daily commuting. The onboard controls work well, although the touch sensors can occasionally misread swipes.
Overall, the VoltX Pro offers strong value for anyone looking for reliable wireless headphones without stretching their budget.""")

print(result)
print("==============================")
print(result['sentiment'])
print("==============================")
print(result['summary'])
print("==============================")
print(type(result))