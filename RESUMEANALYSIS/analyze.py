import nltk
import re
nltk.download('stopwords')
nltk.download('punkt')

SKILLS_DB =['machine learning' , 'data science' , 'pyhton' , 'word' , 'mongodb' 'flask' , 'php' , 'mysql' , 'css' ,'react' , 'html' , 'aws' , 'jira' , 'git' , 'figma' , 'UI/UX']
def extract_skills(text):
    stop_words = set(nltk.corpus.stopwords.words('english'))
    word_tokens = nltk.tokenize.word_tokenize(text)

    filtered_tokens = [w for w in word_tokens if w not in stop_words]

    filtered_tokens = [w for w in word_tokens if w.isalpha()]

    bigrams_trigrams = list(map(' '.join, nltk.everygrams(filtered_tokens, 2, 3)))

    found_skills = set()

    for token in filtered_tokens:
        print(token)
        if token.lower() in SKILLS_DB:
            found_skills.add(token)

    for ngram in bigrams_trigrams:
        print(ngram)
        if ngram.lower() in SKILLS_DB:
            found_skills.add(ngram)

    return found_skills


PHONE_REG = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')
def extract_phone_number(resume_text):
    phone = re.findall(PHONE_REG, resume_text)

    if phone:
        number = ''.join(phone[0])

        if resume_text.find(number) >= 0 and len(number) < 16:
            return number
    return None
def analyze(imageOut):
    input = ""
    for i in imageOut['text']:
        input += i + " "
    skills = extract_skills(input)
    phone = extract_phone_number(input)
    return skills, phone
    
