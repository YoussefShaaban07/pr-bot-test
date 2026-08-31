import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_KEY)

def review_diff(diff_text):
    """Send a PR diff to Gemini and get back a code review."""
    prompt = f"""You are a helpful code reviewer. Review the following pull request diff.
Point out bugs, style issues, missing tests, or security concerns.
Be concise and specific. Reference line numbers or code snippets where relevant.
If the code looks fine, say so briefly.

Diff:
{diff_text}
"""

    response = client.models.generate_content(
        model="gemini-3.7-flash",
        contents=prompt
    )
    return response.text

if __name__ == "__main__":
    # quick test with a fake diff, before we hook it up to the real one
    test_diff = """
diff --git a/app.py b/app.py
index abc123..def456 100644
--- a/app.py
+++ b/app.py
@@ -1,3 +1,6 @@
 def divide(a, b):
-    return a / b
+    if b == 0:
+        return None
+    return a / b
"""
    review = review_diff(test_diff)
    print(review)