const express = require('express');
const mongoose = require('mongoose');
const matchApplicants = require('./matchApplicants');

const app = express();
app.use(express.json());

mongoose.connect('mongodb://localhost:27017/job-matching', { useNewUrlParser: true, useUnifiedTopology: true });

app.post('/api/search', async (req, res) => {
    const { jobDescription } = req.body;
    const topApplicants = await matchApplicants(jobDescription);
    res.json(topApplicants);
});

app.listen(3000, () => {
    console.log('Server running on port 3000');
});
