import React from 'react';

const LandingPage = () => {
    return (
        <div>
            <header>
                <h1>ALPFA Atlanta Job Matching</h1>
                <nav>
                    <a href="#profile">Profile</a>
                    <a href="#sponsor-dashboard">Sponsor Dashboard</a>
                    <a href="#career-fair">Career Fair</a>
                </nav>
            </header>
            <div>
                <h2>Job Opportunities</h2>
                {/* Job Cards would be dynamically generated here */}
            </div>
            <div>
                <h2>Event Invitations</h2>
                {/* Event invitations would be displayed here */}
            </div>
        </div>
    );
};

export default LandingPage;
