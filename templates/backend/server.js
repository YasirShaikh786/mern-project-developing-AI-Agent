import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import { connectDb } from './db/connectDatabase.js';

dotenv.config();
const app = express();

const PORT = process.env.PORT || 5000;

// Define allowed frontend URLs
const allowedOrigins = [
  "http://localhost:3001"
];

// Configure CORS
app.use(
  cors({
    origin: function (origin, callback) {
      // Allow requests with no origin (e.g., mobile apps, Postman)
      if (!origin) return callback(null, true);

      // Check if the origin is in the allowed list
      if (allowedOrigins.includes(origin)) {
        callback(null, true);
      } else {
        callback(new Error('Not allowed by CORS'));
      }
    },
    credentials: true, // Allow cookies
    allowedHeaders: ['Authorization', 'Content-Type'],
  })
);

app.use(express.json());

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
  connectDb();
});