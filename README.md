# Cloud-Based Multi-Language Text-to-Speech Web App (AWS)

A serverless, cloud-based **Text-to-Speech (TTS)** web application built on AWS.  
Users can enter text, select a voice/language, and generate an MP3 audio file using **Amazon Polly**. The generated audio is stored in **Amazon S3** and delivered back to the user via a secure **pre-signed URL**.

This project is designed to look advanced and professional, but is simple to implement and works well under the AWS Free Tier (with normal usage).

---

## 🚀 Features

- Convert text into speech (MP3 output)
- Multi-language support (depends on selected voice)
- Multiple voices available (male/female based on Polly voice list)
- Audio stored in S3 automatically
- Pre-signed URL returned to play audio securely
- Fully serverless architecture
- Backend infrastructure deployed using **AWS CloudFormation**
- Frontend hosted using **AWS Amplify**

---

## 🧰 AWS Services Used

- Amazon S3  
- AWS Lambda  
- Amazon Polly  
- Amazon API Gateway (HTTP API)  
- AWS IAM  
- AWS CloudFormation  
- AWS Amplify  

---

## 📌 Project Files (Included in This Repository)

Refer to these files for complete working code:

- **Frontend:** `index.html`
- **Lambda Code:** `Lambda/lambda_function.py`
- **CloudFormation Template:** `CloudFormation/tts-internship-project.yml`

---

## ✅ Deployment Steps (End-to-End)

Follow these steps to deploy this project from scratch.

---

### 1️⃣ Create 1 S3 Bucket (Manual)

Create **only one S3 bucket manually**:

- Purpose: Upload the Lambda ZIP file (`tts_lambda.zip`)
- Example name: `your-lambda-zip-bucket-name`

⚠️ Keep this bucket **PRIVATE**.

---

### 2️⃣ Upload Lambda ZIP File to S3

1. Create a ZIP file of the Lambda code  
   - Refer to: `Lambda/lambda_function.py`

2. ZIP file name should be:
          tts_lambda.zip

3. Upload `tts_lambda.zip` into your manually created S3 bucket.

---

### 3️⃣ Deploy Backend Using CloudFormation

1. Go to **AWS CloudFormation**
2. Click **Create Stack**
3. Choose **Upload a template file**
4. Upload:
- `CloudFormation/tts-internship-project.yml`

---

### 4️⃣ Enter CloudFormation Parameters

During stack creation, CloudFormation will ask for these parameters:

- `LambdaCodeBucket`  
→ Enter the name of the S3 bucket you created manually (ZIP bucket)

- `LambdaCodeKey`  
→ Enter:
    tts_lambda.zip

Then complete the stack creation.

---

### 5️⃣ Copy API Endpoint and Update Frontend

1. After CloudFormation completes, go to:  
 **CloudFormation → Stack → Outputs**

2. Copy the API endpoint (example format):
        https://xxxx.execute-api.<region>.amazonaws.com/prod/tts

✅ Important:
- Resource path is:  
      /tts

3. Open `index.html` and replace the API URL in the JavaScript `fetch()` call with your own API endpoint.

---

### 6️⃣ Upload Frontend Code to GitHub

1. Go to GitHub
2. Create a new repository
3. Upload:
 - `index.html`

(You can also upload the Lambda + CloudFormation folders for reference.)

---

### 7️⃣ Deploy Frontend Using AWS Amplify

1. Go to **AWS Amplify**
2. Click **Create new app**
3. Select **Host web app**
4. Choose **GitHub**
5. Connect your GitHub account
6. Select your repository and branch
7. Click **Deploy**

Amplify will generate a live website URL like:
      https://main.xxxxx.amplifyapp.com/

---

### 8️⃣ Enable CORS in API Gateway (Required)

If CORS is not enabled, the frontend will fail and show errors like:
- connection failed
- blocked by CORS policy

To enable CORS:

1. Go to **AWS API Gateway**
2. Open the HTTP API created by CloudFormation
3. Click **CORS**
4. Configure these settings:

- **Allowed origins:**  
      *
- **Allowed methods:**  
    POST, OPTIONS
- **Allowed headers:**  
   content-type

5. Click **Save**

---

### 9️⃣ Final Testing

1. Open your Amplify URL
2. Enter text
3. Select voice/language
4. Click Generate
5. Audio should play successfully

---

## 🧩 Architecture Overview

**Frontend (Amplify) → API Gateway (HTTP API) → Lambda → Polly → S3 → Pre-signed URL → Browser Playback**

---

## ⚠️ Configuration Checklist

Before running the project, ensure:

- [ ] API endpoint is updated in `index.html`
- [ ] API endpoint includes `/prod/tts`
- [ ] CORS is enabled in API Gateway
- [ ] `tts_lambda.zip` is uploaded in your manual S3 bucket
- [ ] CloudFormation parameters are filled correctly

---

## 🌟 Future Scope (Enhancements)

- Add authentication using Amazon Cognito  
- Store user history using DynamoDB  
- Add SSML support (speech speed, pauses, emphasis)  
- Add download button for MP3  
- Add voice preview feature  
- Add analytics dashboard using CloudWatch  

---

## 👨‍💻 Author

**Sujit Saini**  
Cloud Computing Internship Project  
2026
