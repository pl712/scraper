import React, { useState, useEffect } from "react";
import "./TimeLine.css";
import { VerticalTimeline, VerticalTimelineElement } from 'react-vertical-timeline-component';
import 'react-vertical-timeline-component/style.min.css';
import TimeLineWidget from "./TimeLineWidget";
import data from "./data/events.json";
import StarIcon from "@material-ui/icons/Star";
function TimeLine(topic) {
    const [events, setEvents] = useState([]);

    useEffect(() => {
        // fetch topic's timeline
        setEvents(data.events);
    }, []);

    return (
        <VerticalTimeline className="timeline" layout="2-columns" lineColor="#50b7f5"  animate={false}>
            {events.map((event) => (
                <TimeLineWidget
                    date={event.date}
                    author={event.author}
                    content={event.content}
                />
            ))}
            <VerticalTimelineElement
                iconStyle={{ background: 'rgb(16, 204, 82)', color: '#fff' }}
                icon={<StarIcon />}
            />
        </VerticalTimeline>
    );
}

export default TimeLine;