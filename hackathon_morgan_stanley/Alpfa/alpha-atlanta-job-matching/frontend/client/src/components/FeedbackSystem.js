import React from 'react';

const FeedbackSystem = () => {
    return (
        <div>
            <h2>Feedback System</h2>
            <form>
                <label>Rate your experience:</label>
                <input type="number" min="1" max="5" />
                <label>Comments:</label>
                <textarea />
                <button type="submit">Submit Feedback</button>
            </form>
        </div>
    );
};

export default FeedbackSystem;
