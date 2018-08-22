import React, { Component } from 'react';
import Sidebar from '../SensorsSidebar';
import './SensorsButton.css';


export default class SensorsButton extends Component {
    constructor(props) {
        super(props);
        this.state = {
            extended: false,
            data: [],
            hovering: false,
            name: "Device"
        };
    }

    render() {
        return (
            <div className="SensorsButton" onClick={this.props.onClick}> {this.props.name}
                {this.state.extended && <Sidebar/>}
            </div>
            
        )
    }
}
