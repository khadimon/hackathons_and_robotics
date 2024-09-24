const mongoose = require('mongoose');

const profileSchema = new mongoose.Schema({
    workExperience: String,
    skills: [String],
    interests: [String],
});

module.exports = mongoose.model('Profile', profileSchema);
