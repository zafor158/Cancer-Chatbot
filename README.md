
# Cancer-Chatbot
Cancer is a complex disease that can be difficult to understand. This project develops a chatbot that can answer questions about cancer using a large language model (LLM). The LLM is trained on a dataset of cancer-related text, so it can answer a some range of questions about cancer.

# Problem Statement
Cancer is a deadly disease that can be difficult to understand. This can be especially true for patients who are newly diagnosed or who are seeking information about treatment options. There is a need for a reliable and accessible source of information about cancer that can be easily understood by patients.
# Goals and Objectives
* Develop a chatbot that can answer questions about cancer.

* Train the LLM model on a pdf dataset of cancer-related text.

# Data Collection and Preprocessing
We use a book named Cancer Biology Third Edition written by Roger J.B. King & Mike W. Robins. The book is about cancer, its history, the causes of human cancers, and many more details.

## Brief Contents that exist in the book:

* What is cancer?
* Natural history: the life of a cancer
* Pathology: defining a neoplasm 32
* Epidemiology: identifying causes for human cancers
* Oncogenes, tumor suppressor genes, and viruses
* Chemical and radiation Carcinogenesis 88
* Mutations, DNA repair, and genetic instability
* Familial cancers
* Growth: a balance of cell proliferation, death, and differentiation
* Responding to the environment: Growth regulation and signal transduction
* Invasion and metastasis
* Principles of cancer treatment
* Approaches to cancer prevention

# Model Training
We use the indexing method that works by first splitting the text into chunks of a certain size. Each chunk is then embedded into a vector of floating-point numbers. These vectors are then stored in a knowledge base.

When a user queries the chatbot, the query text is also embedded into a vector. The chatbot then compares the query vector to the vectors in the knowledge base. The most similar vectors are then returned to the user.
Here are the steps in the indexing method:

The text is split into chunks of a certain size.

* Each chunk is embedded into a vector of floating-point numbers.
* The vectors are stored in a knowledge base.
* When a user queries the chatbot, the query text is also embedded into a vector.
* The chatbot compares the query vector to the vectors in the knowledge base.
* The most similar vectors are then returned to the user.
  
![Model_training](https://github.com/Taukir158/Cancer-Chatbot/assets/98481506/3ca8543a-a2d1-43d0-90f7-d799b40c9d21)

# Results and Discussion
## Main Findings
* The size of the data is proportional to the time it takes to create the docs-string.
* The model takes some time to respond, but it usually gives the correct answer.

## Challenges
* One of the most challenging parts was understanding how the LLM works, how to train a model, and what indexing is.
* Setting up Streamlit in Colab was also challenging.

# Conclusion
In conclusion, this project developed a cancer chatbot using a large language model (LLM). The chatbot was trained on a dataset of cancer-related text, so it can answer a some range of questions about cancer. The project also explored the use of indexing.

## Some potential future improvements or directions for further research include:
* Using a larger dataset of cancer-related text to train the chatbot.
* Using more advance model to have better and faster responses
* Integrating the chatbot with other healthcare resources, such as medical records and clinical decision support systems.




