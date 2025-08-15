import React from 'react';

const ProfileSetup = () => {
    return (
        <div id="profile">
            <h2>Profile Setup</h2>
            <form>
                <label>Work Experience:</label>
                <input type="text" />
                <label>Skills:</label>
                <input type="text" />
                <label>Interests:</label>
                <input type="text" />
                <button type="submit">Save Profile</button>
            </form>
        </div>
    );
};

export default ProfileSetup;
