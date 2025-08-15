const mongoose = require('mongoose');

const feedbackSchema = new mongoose.Schema({
    rating: Number,
    comments: String,
});

module.exports = mongoose.model('Feedback', feedbackSchema);
