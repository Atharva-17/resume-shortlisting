import nltk
import re
# from pyresparser import ResumeParser

nltk.download('stopwords')
nltk.download('punkt')

SKILLS_DB =['machine learning' , 'data science' , 'pyhton' , 'word' , 'mongodb', 'flask' , 'php' , 'mysql' , 'css' ,'react' , 'html' , 'aws' , 'jira' , 'git' , 'figma' , 'UI/UX' , 'sql' ,'java' , 'cnn' , 'backend' , 'python' , 'node' , 'node.js' , 'google' , 'firebase' , 'gradle' , 'android' , 'Django' , 'springboot' , 'spring boot' , 'blockchain' ,'web3' , 'nodejs' , 'postman' , 'javascript' , 'express' , 'mongo' ,'graphql' , 'ruby' , 'docker' , 'rest' , 'kubernates' , 'salesforce' , 'clodechef' , 'codeforces' , 'redux' , 'react' , 'angular' , 'js' , 'php' , 'bootstrap' , 'asp' , 'apache']
def analyzeFirst(imageOut):
    #data = ResumeParser(filename).get_extracted_data()
    input = ""
    for i in imageOut['text']:
        input += i + " "
    email = extract_email(input)
    phone = extract_phone_number(input)
    return email , phone

def extract_skills(text):
    stop_words = set(nltk.corpus.stopwords.words('english'))
    word_tokens = nltk.tokenize.word_tokenize(text)

    filtered_tokens = [w for w in word_tokens if w not in stop_words]

    filtered_tokens = [w for w in word_tokens if w.isalpha()]

    bigrams_trigrams = list(map(' '.join, nltk.everygrams(filtered_tokens, 2, 3)))

    found_skills = set()

    for token in filtered_tokens:
        if token.lower() in SKILLS_DB:
            found_skills.add(token.lower())

    for ngram in bigrams_trigrams:
        if ngram.lower() in SKILLS_DB:
            found_skills.add(ngram.lower())

    return found_skills


PHONE_REG = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')
def extract_phone_number(resume_text):
    phone = re.findall(PHONE_REG, resume_text)
    if phone:
        number = ''.join(phone[0])

        if resume_text.find(number) >= 0 and len(number) < 16:
            return number
    return None


Email_REG = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
def extract_email(resume_text):
    email = re.findall(Email_REG , resume_text)
    if email:
        mail_id = ''.join(email[0])
        if resume_text.find(mail_id) >= 0 :
            return mail_id
    return None

def analyze(imageOut):
    input = ""
    for i in imageOut['text']:
        input += i + " "
    skills = extract_skills(input)
    #phone = extract_phone_number(input)
    return skills
    
