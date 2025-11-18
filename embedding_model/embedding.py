from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
documents = [
    "Soccer is the most popular sport in the world, played by millions.",
    "Football is enjoyed globally and has millions of fans.",
    "The FIFA World Cup is the biggest football tournament internationally.",
    "Many countries participate in the World Cup every four years.",
    "Lionel Messi is one of the greatest football players of all time.",
    "Cristiano Ronaldo has won many awards in football throughout his career.",
    "Football matches are played on a rectangular field with goals at each end.",
    "A standard football match lasts 90 minutes divided into two halves.",
    "Players use teamwork and strategy to score goals in football.",
    "Football clubs compete in domestic leagues and international tournaments.",
    "The Premier League in England is one of the most famous football leagues.",
    "Football fans often wear their team jerseys during matches.",
    "Goalkeepers are the only players allowed to use their hands in football.",
    "Offside is a common rule that players must follow in football games.",
    "Football training involves improving fitness, skills, and tactics."
]

embedding = HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")
query = "who is the greatest football playyer ?"
document_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)
scores = cosine_similarity([query_embedding],document_embeddings)[0]
index,score  = sorted(list(enumerate(scores)),key=lambda x : x[1])[-1]
print(query)
print(documents[index])
print("similarity score is : ",score)
