import React from 'react';
import LandingPage from './components/LandingPage';
import ProfileSetup from './components/ProfileSetup';
import SponsorDashboard from './components/SponsorDashboard';
import CareerFair from './components/CareerFair';
import FeedbackSystem from './components/FeedbackSystem';

function App() {
    return (
        <div>
            <LandingPage />
            <ProfileSetup />
            <SponsorDashboard />
            <CareerFair />
            <FeedbackSystem />
        </div>
    );
}

export default App;
