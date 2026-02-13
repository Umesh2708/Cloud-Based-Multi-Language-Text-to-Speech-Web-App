### This section explains how to deploy the same project **manually** (without CloudFormation).

---

# ✅ Deployment Steps (Manual End-to-End)

---

## 1️⃣ Create an S3 Bucket (For Generated MP3 Files)

1. Go to **AWS S3**
2. Click **Create bucket**
3. Bucket name example:
   - `tts-audio-bucket-<yourname>`
4. Keep settings:
   - Block all public access: ✅ ON (recommended)
5. Click **Create bucket**

### (Optional but Recommended) Enable Auto-Delete for 1 Day
To avoid storage cost, you can add a lifecycle rule:

1. Open your bucket
2. Go to **Management → Lifecycle rules**
3. Create rule:
   - Rule name: `DeleteMP3After1Day`
   - Apply to all objects
   - Expire current versions: **1 day**
4. Save rule

---

## 2️⃣ Create an IAM Role for Lambda

1. Go to **IAM → Roles**
2. Click **Create role**
3. Select trusted entity:
   - **AWS Service**
4. Use case:
   - **Lambda**
5. Attach permissions policies:
   - `AmazonS3FullAccess`
   - `AmazonPollyFullAccess`
   - `AWSLambdaBasicExecutionRole`
6. Role name example:
   - `TTSLambdaRole`
7. Click **Create role**

---

## 3️⃣ Create the Lambda Function (Python)

1. Go to **AWS Lambda → Create function**
2. Select:
   - **Author from scratch**
3. Fill details:
   - Function name: `TTSLambdaFunction`
   - Runtime: `Python 3.11`
4. Permissions:
   - Choose **Use an existing role**
   - Select role: `TTSLambdaRole`
5. Click **Create function**

---

## 4️⃣ Add Lambda Code (lambda_function.py)

Inside Lambda → Code tab → paste your `lambda_function.py` code.

📌 Recommended file name:
```text
Lambda/lambda_function.py
```

---

## 5️⃣ Add Required Environment Variables (Recommended)

Go to:
**Lambda → Configuration → Environment variables → Edit**

Add:

| Key | Value |
|-----|-------|
| BUCKET_NAME | `tts-audio-bucket-<yourname>` |

---

## 6️⃣ Create an HTTP API in API Gateway

1. Go to **API Gateway**
2. Click **Create API**
3. Select:
   - ✅ **HTTP API**
4. Click **Build**
5. Integration:
   - Choose: **Lambda**
   - Select: `TTSLambdaFunction`
6. Click **Next**

---

## 7️⃣ Create Route: POST /tts

1. Route:
   - Method: `POST`
   - Resource path: `/tts`
2. Click **Next**

---

## 8️⃣ Create Stage and Deploy

1. Stage name:
   - `prod`
2. Enable:
   - ✅ Auto-deploy
3. Click **Create**

After deployment, you will get an API endpoint like:

```text
https://xxxx.execute-api.ap-south-1.amazonaws.com/prod/tts
```

---

## 9️⃣ Give API Gateway Permission to Invoke Lambda

Normally API Gateway adds permission automatically, but if not:

1. Go to **Lambda → Permissions**
2. Under **Resource-based policy**
3. Ensure API Gateway is allowed to invoke the Lambda

---

## 🔟 Enable CORS in API Gateway (Required)

If CORS is not enabled, frontend will fail due to browser security.

1. Go to **API Gateway**
2. Open your HTTP API
3. Go to **CORS**
4. Configure:

- Allowed origins:
  ```text
  *
  ```

- Allowed methods:
  ```text
  POST, OPTIONS
  ```

- Allowed headers:
  ```text
  content-type
  ```

5. Save changes

---

# 🌐 Frontend Deployment (Amplify Hosting)

---

## 1️⃣1️⃣ Update Frontend API URL

In your frontend code (example: `Frontend/script.js`):

Replace API endpoint with your deployed API URL:

```js
const API_URL = "https://xxxx.execute-api.ap-south-1.amazonaws.com/prod/tts";
```

---

## 1️⃣2️⃣ Push Frontend Code to GitHub

1. Create a GitHub repository
2. Upload:

```text
Frontend/
Lambda/
README.md
```

---

## 1️⃣3️⃣ Deploy Frontend Using AWS Amplify

1. Go to **AWS Amplify**
2. Click **Create new app**
3. Select:
   - **Host web app**
4. Choose:
   - GitHub
5. Select your repository + branch
6. Click **Deploy**

Amplify will generate a URL like:

```text
https://main.xxxxx.amplifyapp.com/
```

---

# ✅ Final Testing

1. Open your Amplify hosted URL
2. Enter text
3. Select voice/language
4. Click **Generate**
5. Audio should play successfully

---

# 🧹 Cleanup (To Avoid Billing)

> If you created this project only for learning/demo purpose, delete all AWS resources after testing to avoid unnecessary charges.

Delete the following resources:

- API Gateway HTTP API
- Lambda function
- IAM role (TTSLambdaRole)
- S3 bucket (audio bucket)
- Amplify app

---
