import React, { Component } from "react";
import './SensorsSidebar.css';


export default class SensorsSidebar extends Component {
    constructor(props) {
        super(props);
        this.state = {
            extended: false,
            data: []
        }
    }

    render() {
        return (
            <div className={"SensorsSidebar" + (this.state.extended ? " extended" : "")}>
                <div onClick={() => console.log("New sidebar <div> is being render")} className="SensorsSidebar-button">
                </div>
            </div>
        )
    }
}