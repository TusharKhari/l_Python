


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time


# Your email credentials
sender_email = "tusharkhari57@gmail.com"
password = "xziu ruwe hhzd pcqf deleteThisWithSpace"
your_name = "Tushar Khari"

failed_emails = []

# List of professors and their emails + personalized emails

professors = [
    {
        "name": "Prof. Dr. Christian Neumeier",
        "email": "christian.neumeier@hs-aalen.de",
        "email_text": """Respected Prof. Dr. Neumeier,

I am a Master’s student specializing in Machine Learning and Data Analytics at Aalen University. Given your expertise in statistics and computer-aided data analysis, I believe my interests in data analytics and machine learning align well with your work.

I would appreciate the opportunity to undertake my mandatory semester project under your guidance and am open to discussing any suitable topics within your field. If you currently have no project openings, could you kindly advise whom I might contact?

Thank you for your time.

Best regards,
[Your Name]
"""
    },
    {
        "name": "Dr. Miriam Hommel",
        "email": "miriam.hommel@hs-aalen.de",
        "email_text": """Respected Dr. Hommel,

I am currently pursuing my Master’s in Machine Learning and Data Analytics at Aalen University. Your focus on mathematics and machine learning aligns closely with my interests in machine learning and data engineering.

I would be grateful for a chance to work with you on my mandatory semester project and am flexible on the exact topic. If you don’t have current openings, could you please guide me to someone who does?

Thank you very much for your consideration.

Best regards,
[Your Name]
"""
    },
    {
        "name": "Prof. Dr. Tim Dahmen",
        "email": "tim.dahmen@hs-aalen.de",
        "email_text": """Respected Prof. Dr. Dahmen,

I am a Master’s student in Machine Learning and Data Analytics at Aalen University. Your expertise in machine learning and synthetic data generation perfectly matches my interests in machine learning and big data.

I would be eager to undertake my semester project under your supervision and am happy to discuss potential ideas. If no projects are currently available, could you kindly recommend a contact?

Thank you for your time.

Best regards,
[Your Name]
"""
    },
    {
        "name": "Prof. Dr. Gregor Grambow",
        "email": "gregor.grambow@hs-aalen.de",
        "email_text": """Respected Prof. Dr. Grambow,

As a Master’s student at Aalen University specializing in Machine Learning and Data Analytics, I am highly interested in data engineering related topics, which aligns well with your research.

I would appreciate the opportunity to collaborate with you on my semester project. I am flexible regarding the topic and happy to discuss ideas. If you currently have no openings, could you kindly point me to a colleague?

Thank you very much.

Best regards,
[Your Name]
"""
    },
    {
        "name": "Prof. Dr. Martin Heckmann",
        "email": "martin.heckmann@hs-aalen.de",
        "email_text": """Respected Prof. Dr. Heckmann,

I am pursuing my Master’s in Machine Learning and Data Analytics at Aalen University. Your work in data science and predictive analytics closely matches my interests in machine learning and data analytics.

I would be grateful to conduct my mandatory semester project under your guidance. I am open to discussing ideas and flexible on the topic. If no project opportunities are available, could you please advise whom to contact?

Thank you for your time.

Best regards,
[Your Name]
"""
    },
    {
"name": "Prof. Dr. habil. Christian Heinlein",
"email": "christian.heinlein@hs-aalen.de",
"email_text": """Respected Prof. Dr. Heinlein,

I am a Master’s student in Machine Learning and Data Analytics at Aalen University. Your expertise in software engineering and basics of computer science complements my interests in IT.

I would appreciate the opportunity to undertake my semester project under your guidance and discuss potential topics. If there are no openings, could you kindly direct me to someone suitable?

Thank you for your time and consideration.

Best regards,
[Your Name]
"""
},
    {
"name": "Dr. Marc Hermann",
"email": "marc.hermann@hs-aalen.de",
"email_text": """Respected Dr. Hermann,

I am pursuing my Master’s in Machine Learning and Data Analytics at Aalen University. Your work in software engineering and object-oriented programming aligns well with my background in IT.

I would be grateful for the opportunity to complete my semester project under your supervision and discuss possible topics. If no projects are available, could you kindly point me to someone suitable?

Thank you for your consideration.

Best regards,
[Your Name]
"""
},
    {
"name": "Prof. Dr. Ulrich Klauck",
"email": "ulrich.klauck@hs-aalen.de",
"email_text": """Respected Prof. Dr. Klauck,

I am a Master’s student in Machine Learning and Data Analytics at Aalen University. I am keen to explore semester project opportunities under your guidance, especially related to data analytics, machine learning, or data engineering.

I am flexible with the project topic and would be happy to discuss ideas at your convenience. If no projects are available, could you kindly advise whom I might contact?

Thank you for your time and consideration.

Best regards,
[Your Name]
"""
},
    {
"name": "Sandro Sabella",
"email": "sandro.sabella@hs-aalen.de",
"email_text": """Respected Mr. Sabella,

I am currently pursuing my Master’s in Machine Learning and Data Analytics at Aalen University. I am interested in exploring semester project opportunities related to data engineering, machine learning, or data analytics and would appreciate the chance to work under your guidance.

I am flexible with the topic and would be happy to discuss possible ideas. If you do not have available projects, could you kindly direct me to someone suitable?

Thank you for your consideration.

Best regards,
[Your Name]
"""
},
    {
"name": "Prof. Sebastian Stigler",
"email": "sebastian.stigler@hs-aalen.de",
"email_text": """Respected Mr. Stigler,

I am currently pursuing my Master’s in Machine Learning and Data Analytics at Aalen University. I am interested in exploring semester project opportunities related to software development, data engineering, machine learning, or data analytics and would appreciate the chance to work under your guidance.

I am flexible with the topic and would be happy to discuss possible ideas. If you do not have available projects, could you kindly direct me to someone suitable?

Thank you for your time and consideration.

Best regards,
[Your Name]
"""
},
    {
"name": "Prof. Stefan Wehrenberg",
"email": "stefan.wehrenberg@hs-aalen.de",
"email_text": """Respected Mr. Wehrenberg,

I am currently pursuing my Master’s in Machine Learning and Data Analytics at Aalen University. I am looking for a semester project opportunity and am particularly interested in areas like big data processing, software systems, or data engineering, which I believe align well with your expertise.

I am open to discussing potential topics and flexible to work within your current research areas. If you do not have any projects available, I would be grateful if you could kindly suggest someone I could reach out to.

Thank you for your time and consideration.

Best regards,
[Your Name]
"""
},
    {
"name": "Prof. Dr.-Ing. Markus Glück",
"email": "markus.glueck@hs-aalen.de",
"email_text": """Respected Prof. Glück,

I am currently pursuing my Master’s in Machine Learning and Data Analytics at Aalen University. I am looking for a semester project opportunity and am particularly interested in topics like robotics, digital manufacturing, or automation, which I believe relate well to your subject areas.

I am flexible with the project scope and would be happy to discuss possible ideas. If you currently do not have any open projects, I would appreciate it if you could suggest someone I could contact.

Thank you for your time and consideration.

Best regards,
[Your Name]
"""
}
,
    {
        "name": "Prof. Dr. Holger Schmidt",
        "email": "holger.schmidt@hs-aalen.de",
        "email_text": """Respected Prof. Dr. Schmidt,

I am a Master’s student at Aalen University specializing in Machine Learning and Data Analytics. Your expertise in machine learning and mathematics aligns well with my interests.

I would appreciate the opportunity to undertake my semester project with your guidance. I am flexible on the topic and happy to discuss ideas. If you currently have no projects, could you kindly suggest another contact?

Thank you for your time.

Best regards,
[Your Name]
"""
    },
    {
        "name": "Prof. Dr. Marc Fernandes",
        "email": "marc.fernandes@hs-aalen.de",
        "email_text": """Respected Prof. Dr. Fernandes,

I am currently pursuing my Master’s in Machine Learning and Data Analytics at Aalen University. Your areas of information systems and databases align with my interests in data engineering and analytics.

I would be glad to undertake my semester project under your supervision and discuss potential topics. If you do not have openings, could you kindly direct me to a suitable contact?

Thank you for your consideration.

Best regards,
[Your Name]
"""
    },
    {
"name": "Prof. Dr. Doris Aschenbrenner",
"email": "doris.aschenbrenner@hs-aalen.de",
"email_text": """Respected Prof. Aschenbrenner,

I am currently pursuing my Master’s in Machine Learning and Data Analytics at Aalen University. I am looking for a semester project opportunity and am particularly interested in topics like AI applications, digital transformation, databases, or production system networking, which seem to align well with your focus areas.

I am flexible with the topic and open to discussing possible directions. If no projects are currently available, I would be grateful if you could point me to someone appropriate.

Thank you for your time and consideration.

Best regards,
[Your Name]
"""
}
,
{
"name": "Prof. Dr.-Ing. Yours Berger",
"email": "yours.berger@hs-aalen.de",
"email_text": """Respected Prof. Berger,

I am currently pursuing my Master’s in Machine Learning and Data Analytics at Aalen University. I am looking for a semester project opportunity and am particularly interested in areas such as automation, manufacturing informatics, or digital product development, which align well with your expertise.

I am open to discussing ideas and flexible with the topic. If no projects are available, I would appreciate it if you could suggest someone I could contact.

Thank you for your time and consideration.

Best regards,
[Your Name]
"""
}
,
{
"name": "Prof. Dr. Rainer Eber",
"email": "rainer.eber@hs-aalen.de",
"email_text": """Respected Prof. Eber,

I am currently pursuing my Master’s in Machine Learning and Data Analytics at Aalen University. I am seeking a semester project opportunity and am particularly interested in topics like data-driven approaches in supply chain management, which I believe relate well to your areas of expertise.

I am flexible regarding the topic and would be happy to discuss possible ideas. If no projects are currently available, I would be grateful if you could recommend someone I could approach.

Thank you for your time and consideration.

Best regards,
[Your Name]
"""
}, 
    {
        "name": "Prof. Dr. Andreas Theissler",
        "email": "andreas.theissler@hs-aalen.de",
        "email_text": """Respected Prof. Dr. Theissler,

I am a Master’s student specializing in Machine Learning and Data Analytics at Aalen University. Your focus on data mining, machine learning, and big data closely aligns with my academic interests.

I would welcome the chance to work under your guidance for my semester project. I am flexible regarding the topic and open to discussing ideas. If you have no available projects, could you please advise whom I might contact?

Thank you for your time.

Best regards,
[Your Name]
"""
    },
    {
        "name": "Prof. Dr. Christian Koot",
        "email": "christian.koot@hs-aalen.de",
        "email_text": """Respected Prof. Dr. Koot,

I am pursuing my Master’s in Machine Learning and Data Analytics at Aalen University. Your expertise in business analytics and data science programming aligns well with my interests.

I would be glad to conduct my semester project under your guidance and discuss relevant topics. If you have no project opportunities at the moment, could you kindly advise whom to approach?

Thank you for your consideration.

Best regards,
[Your Name]
"""
    },
    {
        "name": "Dominik Hahn",
        "email": "dominik.hahn@hs-aalen.de",
        "email_text": """Respected Mr. Hahn,

I am a Master’s student at Aalen University specializing in Machine Learning and Data Analytics. Your expertise in machine learning and databases matches my interests closely.

I would appreciate the opportunity to collaborate on my semester project under your guidance and am flexible on the topic. If you don’t have openings, could you kindly direct me to someone suitable?

Thank you for your time.

Best regards,
[Your Name]
"""
    },
    {
"name": "Prof. Christoph Mattmann",
"email": "christoph.mattmann@hs-aalen.de",
"email_text": """Respected Prof. Mattmann,

I am currently pursuing my Master’s in Machine Learning and Data Analytics at Aalen University. I am looking for a semester project opportunity and am particularly interested in areas such as databases, data engineering, or related topics that align with your research.

I am flexible with the project scope and would be happy to discuss any ideas. If you do not currently have any open projects, I would appreciate it if you could suggest someone I could reach out to.

Thank you for your time and consideration.

Best regards,
[Your Name]
"""
}
,
{
"name": "Prof. Detlef Küpper",
"email": "detlef.kuepper@hs-aalen.de",
"email_text": """Respected Prof. Küpper,

I am currently pursuing my Master’s in Machine Learning and Data Analytics at Aalen University. I am looking for a semester project opportunity and am particularly interested in topics such as AI methods, database systems, or internet-based applications, which align well with your expertise.

I am open to discussing ideas and flexible with the topic. If you currently do not have any available projects, I would be grateful if you could suggest someone I could contact.

Thank you for your time and consideration.

Best regards,
[Your Name]
"""
}
,
{
"name": "Prof. Dr. Manfred Rössle",
"email": "manfred.roessle@hs-aalen.de",
"email_text": """Respected Prof. Rössle,

I am currently pursuing my Master’s in Machine Learning and Data Analytics at Aalen University. I am looking for a semester project opportunity and am particularly interested in areas like data-driven logistics, which I believe align well with your expertise.

I am flexible with the topic and open to discussing any suitable ideas. If no projects are currently available, I would appreciate it if you could suggest someone I could reach out to.

Thank you for your time and consideration.

Best regards,
[Your Name]
"""
}
,
{
"name": "Prof. Dr.-Ing. Sara Sommer",
"email": "sara.sommer@hs-aalen.de",
"email_text": """Respected Prof. Sommer,

I am currently pursuing my Master’s in Machine Learning and Data Analytics at Aalen University. I am looking for a semester project opportunity and am particularly interested in industrial data analytics or data-driven logistics, which closely align with your subject areas.

I am open to discussing possible topics and flexible with the direction of the project. If you currently do not have any available projects, I would appreciate it if you could kindly refer me to someone appropriate.

Thank you for your time and consideration.

Best regards,
[Your Name]
"""
}
,
{
"name": "Marco Klaiber",
"email": "marco.klaiber@hs-aalen.de",
"email_text": """Respected Mr. Klaiber,

I am currently pursuing my Master’s in Machine Learning and Data Analytics at Aalen University. I am looking for a semester project opportunity and am particularly interested in machine learning research, which aligns well with your work.

I am flexible with the topic and would be happy to discuss potential ideas. If you do not have any projects available, I would appreciate it if you could kindly direct me to someone suitable.

Thank you for your time and consideration.

Best regards,
[Your Name]
"""
}
,
{
"name": "Dominik Raab",
"email": "dominik.raab@hs-aalen.de",
"email_text": """Respected Mr. Raab,

I am currently pursuing my Master’s in Machine Learning and Data Analytics at Aalen University. I am seeking a semester project opportunity and am particularly interested in visual analytics, which aligns well with your expertise.

I am flexible with the topic and would be glad to discuss potential ideas. If you do not have any projects available, I would appreciate it if you could kindly direct me to someone suitable.

Thank you for your time and consideration.

Best regards,
[Your Name]
"""
}
,
 
{
"name": "Prof. Dr. Winfried Bantel",
"email": "winfried.bantel@hs-aalen.de",
"email_text": """Respected Prof. Bantel,

I am currently pursuing my Master’s in Machine Learning and Data Analytics at Aalen University. I am looking for a semester project opportunity and am particularly interested in topics such as natural language processing, which align well with your expertise.

I am open to discussing ideas and flexible with the project topic. If no projects are currently available, I would appreciate it if you could kindly refer me to someone suitable.

Thank you for your time and consideration.

Best regards,
[Your Name]
"""
},
{
"name": "Prof. Dr. Walter Gillner",
"email": "walter.gillner@hs-aalen.de",
"email_text": """Respected Prof. Gillner,

I am currently pursuing my Master’s in Machine Learning and Data Analytics at Aalen University. I am seeking a semester project opportunity and am particularly interested in machine learning and sensor technologies, which align closely with your expertise.

I am flexible with the topic and would be happy to discuss potential ideas. If no projects are currently available, I would appreciate it if you could kindly direct me to someone suitable.

Thank you for your time and consideration.

Best regards,
[Your Name]
"""
}
,
{
"name": "Prof. Dr. Anna Nagl",
"email": "anna.nagl@hs-aalen.de",
"email_text": """Respected Prof. Nagl,

I am currently pursuing my Master’s in Machine Learning and Data Analytics at Aalen University. I am looking for a semester project opportunity and am particularly interested in AI-supported business models, strategic management, or data-driven market research, which align well with your expertise.

I am flexible with the project topic and open to discussing ideas. If you currently do not have any available projects, I would appreciate it if you could kindly refer me to someone suitable.

Thank you for your time and consideration.

Best regards,
[Your Name]
"""
}
,
{
"name": "Prof. Dr. Simone Philp",
"email": "simone.philp@hs-aalen.de",
"email_text": """Respected Prof. Philp,

I am currently pursuing my Master’s in Machine Learning and Data Analytics at Aalen University. I am seeking a semester project opportunity and am particularly interested in data-driven sustainable supply chains, or sustainability reporting, which align well with your expertise.

I am flexible with the topic and would be happy to discuss potential ideas. If you do not currently have any available projects, I would appreciate it if you could kindly refer me to someone suitable.

Thank you for your time and consideration.

Best regards,
[Your Name]
"""
}
,


    {
        "name": "Prof. Dr. Alexander Strehl",
        "email": "alexander.strehl@hs-aalen.de",
        "email_text": """Respected Prof. Dr. Strehl,

I am a Master’s student in Machine Learning and Data Analytics at Aalen University. Your work in advanced analytics and business intelligence closely matches my interests.

I would be grateful to work with you on my semester project and am open to discussing any relevant ideas. If no projects are available, could you kindly suggest whom to contact?

Thank you for your time.

Best regards,
[Your Name]
"""
    },
    {
"name": "Prof. Dr. Roland Dietrich",
"email": "roland.dietrich@hs-aalen.de",
"email_text": """Respected Prof. Dietrich,

I am currently pursuing my Master’s in Machine Learning and Data Analytics at Aalen University. I am seeking a semester project opportunity and am particularly interested in artificial intelligence, modeling, or software engineering, which align well with your expertise.

I am flexible with the topic and open to discussing potential ideas. If no projects are currently available, I would appreciate it if you could kindly refer me to someone suitable.

Thank you for your time and consideration.

Best regards,
[Your Name]
"""
}
,
{
"name": "Tobias Gold",
"email": "tobias.gold@hs-aalen.de",
"email_text": """Respected Mr. Gold,

I am currently pursuing my Master’s in Machine Learning and Data Analytics at Aalen University. I am looking for a semester project opportunity and am particularly interested in business intelligence and data-driven controlling, which align well with your expertise.

I am flexible with the topic and would be happy to discuss possible ideas. If you do not have any projects available, I would appreciate it if you could kindly direct me to someone suitable.

Thank you for your time and consideration.

Best regards,
[Your Name]
"""
}
,
    
]




def send_emails_batch(professors):
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)

        for prof in professors:
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = prof["email"]
            msg['Subject'] = "Semester Project Opportunity Inquiry"

            email_body = prof["email_text"].replace("[Your Name]", your_name)
            msg.attach(MIMEText(email_body, 'plain'))

            try:
                
                server.sendmail(sender_email, prof["email"], msg.as_string())
                print(f" Email sent to {prof['email']}")
            except Exception as e:
                
                failed_emails.append(prof)
                print(f"Failed to send email to {prof['email']}: {str(e)}")
            time.sleep(5)  # Respectful delay


send_emails_batch(professors)
# def send_email(to_email, subject, body):
#     msg = MIMEMultipart()
#     msg['From'] = sender_email
#     msg['To'] = to_email
#     msg['Subject'] = subject
    
#     msg.attach(MIMEText(body, 'plain'))
    
#     try:
#         with smtplib.SMTP('smtp.gmail.com', 587) as server:
#             server.starttls()
#             server.login(sender_email, password)
#             server.sendmail(sender_email, to_email, msg.as_string())
#             print(f"Email sent to {to_email}")
#     except Exception as e:
#         print(f"Failed to send email to {to_email}: {str(e)}")

# print(len(professors))
# for prof in professors:
#     # Replace [Your Name] with your actual name in the email body before sending
#     email_body = prof["email_text"].replace("[Your Name]", "Tushar Khari")
#     send_email(prof["email"], "Semester Project Opportunity Inquiry", email_body)
#     print(f'''{prof["email"]} ''')
    
