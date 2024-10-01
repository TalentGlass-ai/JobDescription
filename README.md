Flask JD Generator using Google Generative AI
git clone
This Flask application accepts a POST request with a description and uses Google's Generative AI (`gemini-1.5-flash`) to generate content based on the input description. The generated content is returned in the response.
## Requirements
- Python 3.x
- Flask
- google-generativeai
pip install Flask google-generativeai
api_key = "your-api-key"
Run the application
python app.py

Once the Flask app is running, you can send a POST request to generate content. Here's an example using `curl`:

```bash
curl -X POST http://127.0.0.1:5000/generate-description -H "Content-Type: application/json" -d '{"description": "generate a job description for the software developer with 5+ years of exprience"}
