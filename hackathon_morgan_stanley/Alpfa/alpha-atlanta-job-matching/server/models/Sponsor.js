const mongoose = require('mongoose');

const sponsorSchema = new mongoose.Schema({
    name: String,
    jobPostings: [String],
});

module.exports = mongoose.model('Sponsor', sponsorSchema);
