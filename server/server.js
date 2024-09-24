const express = require('express');
const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const cors = require('cors');
const bodyParser = require('body-parser');
const multer = require('multer');
const path = require('path');
const fs = require('fs');
const pdf = require('pdf-parse');

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// MongoDB connection
mongoose.connect('mongodb://localhost:27017/alpfa-atlanta', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
});

// User schema
const userSchema = new mongoose.Schema({
    username: { type: String, required: true, unique: true },
    password: { type: String, required: true },
});

const User = mongoose.model('User', userSchema);

// Register route
app.post('/register', async (req, res) => {
    const { username, password } = req.body;
    const hashedPassword = await bcrypt.hash(password, 10);
    const newUser = new User({ username, password: hashedPassword });

    try {
        await newUser.save();
        res.status(201).send('User registered successfully');
    } catch (error) {
        res.status(400).send('Error registering user');
    }
});

// Login route
app.post('/login', async (req, res) => {
    const { username, password } = req.body;
    const user = await User.findOne({ username });

    if (user && (await bcrypt.compare(password, user.password))) {
        const token = jwt.sign({ id: user._id }, 'your_jwt_secret', { expiresIn: '1h' });
        res.json({ token });
    } else {
        res.status(401).send('Invalid credentials');
    }
});

// AI Sorting Implementation (Placeholder)
app.post('/sort-applicants', (req, res) => {
    // Implement your AI sorting logic here
    // For example, you could use a machine learning model to sort applicants based on criteria
    res.send('AI sorting logic goes here');
});

// Resume Upload Implementation
const resumeSchema = new mongoose.Schema({
    filename: String,
    uploadDate: { type: Date, default: Date.now },
    // Add other fields as necessary
});

const Resume = mongoose.model('Resume', resumeSchema);

const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, 'uploads/'); // Directory to save uploaded files
    },
    filename: (req, file, cb) => {
        cb(null, Date.now() + path.extname(file.originalname)); // Unique filename
    }
});

const upload = multer({ storage: storage });

app.post('/upload', upload.single('resume'), (req, res) => {
    const newResume = new Resume({ filename: req.file.filename });
    newResume.save()
        .then(() => res.status(200).send('File uploaded and saved to database.'))
        .catch(err => res.status(500).send('Error saving to database.'));
});

// Function to convert PDF to text
function convertPdfToText(filePath) {
    let dataBuffer = fs.readFileSync(filePath);
    return pdf(dataBuffer).then(function(data) {
        return data.text; // Extracted text from PDF
    });
}

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
