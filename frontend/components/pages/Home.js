// components/pages/Home.js
import React, { useEffect, useState } from "react";
import { getAIRecommendations } from "../services/investmentService";

const Home = () => {
    const [recommendations, setRecommendations] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            const data = await getAIRecommendations();
            setRecommendations(data);
        };
        fetchData();
    }, []);

    return (
        <div>
            <h1>📊 AI Investment Recommendations</h1>
            <ul>
                {recommendations.map((rec, index) => (
                    <li key={index}>{rec.stock_symbol} - {rec.prediction}</li>
                ))}
            </ul>
        </div>
    );
};

export default Home;
