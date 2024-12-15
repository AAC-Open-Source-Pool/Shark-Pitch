# Shark Pitch
<h2>Team Details</h2>
<b>Team Number: </b><p>24AACR20</p>
<b>Senior Mentor: </b><p>Akash Paul</p>
<b>Junior Mentor: </b><p>Preetham Janugam</p>
<b>Team Member 1: </b><p>Raghavendra Chekuri</p>
<b>Team Member 2: </b><p>Chepuri Vaishnavy</p>
<b>Team Member 3: </b><p>Kothakonda Nagasree</p>
<b>Team Member 4: </b><p>Amudala Premendar Reddy</p>
<b>Team Member 5: </b><p>Kurma Shruthika</p>

# Shark Pitch

---

## Abstract  
Shark Pitch is a web platform designed to connect startups and entrepreneurs with potential investors. It allows startups to post pitch videos, company statistics, and other essential details to showcase their business ideas. Investors can browse these profiles, evaluate opportunities, and connect directly via chat or video call.  

Shark Pitch bridges the gap between innovative ventures and investors, fostering seamless communication and collaboration to create a thriving ecosystem for business growth.

---

## Table of Contents  
- [Introduction](#introduction)  
- [Requirements](#requirements)  
- [How to Use](#how-to-use)  
- [Preview](#preview)  
- [Contribution](#contribution)  

---

## Introduction  
Shark Pitch provides a collaborative platform where startups and entrepreneurs can showcase their ideas and connect with potential investors. The project focuses on simplifying the investment process and fostering meaningful interactions by integrating user-friendly features, such as:  

- Posting and viewing pitch videos and company details.  
- Chat and video call functionalities for direct communication.  
- User authentication for secure access.  

This platform aims to empower startups by connecting them with the resources and mentorship they need to thrive.  

---

## Requirements  

| Name           |
|----------------|
| Python 3.10+   |
| Django         |
| PostgreSQL     |
| JavaScript     |
| HTML5 & CSS3   |

---

## How to Use  
To use this project, follow these steps:  

1. **Clone the repository**:  
```bash  
   git clone <repository_url>  
   cd shark-pitch
```

2.  **Set up a virtual environment**:

``` terminal
python -m venv env  
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. **Install dependencies**:

``` terminal
pip install -r requirements.txt
```

4. **Set up environment variables**:

``` terminal
 --Create a .env file in the root directory and add:
SECRET_KEY=your_django_secret_key  
DATABASE_URL=postgresql://username:password@localhost:5432/shark_pitch
```


5. **Run database migrations**:

```terminal
python manage.py migrate
```


6. **Start the development server**:

``` terminal
python manage.py runserver
``` 


7. **Access the application**:
Open your browser and navigate to:

<a href = "http://localhost:8000">http://localhost:8000</a>  

---

## Preview
Screenshot of the project:

<div align = 'center'> 
   <img src = "https://i.imgur.com/5XxOclD_d.webp?maxwidth=1520&fidelity=grand">
</div>

---

## Contribution
We welcome contributions to Shark Pitch! To contribute, follow these steps:

1. Understand the Project Philosophy:
Read through the README.md file to familiarize yourself with the project's goals and structure.

2. Maintain Code Consistency:
Use the same programming language and library versions as the original code.

3. Write Documentation:
Explain the changes you're proposing, including identified problems, proposed solutions, and test cases.

4. Submit a Pull Request:
Follow standard Git etiquette for submitting your contributions.
