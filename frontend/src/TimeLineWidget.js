import React, { forwardRef } from "react";
import "./TimeLine.css";
import {VerticalTimelineElement } from 'react-vertical-timeline-component';
import 'react-vertical-timeline-component/style.min.css';
import AdjustIcon from "@material-ui/icons/Adjust";

const TimeLineWidget = forwardRef(
    ({ date,author, content }, ref) => {
    return (
            <VerticalTimelineElement
                className="vertical-timeline-element--work"
                dateClassName
                date={date}
                contentStyle={{width: '260px',background: '#e6ecf0'}}
                iconStyle={{ background: '#fff', color: '#fff', width:'0%'}}
                icon={<></>}
                ref={ref}
            >
                {/* <h3 className="vertical-timeline-element-title">{author}</h3> */}
                <h4 className="vertical-timeline-element-subtitle">{author}</h4>
                <p>
                    {content}
                </p>
            </VerticalTimelineElement>
    );
})

export default TimeLineWidget;