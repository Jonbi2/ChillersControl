import React, { Component } from 'react';
import './DeviceButton.css';


export default class DeviceButton extends Component {
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

        const style = {
            backgroundColor : this.state.hovering ? "#4f4d4d" : undefined
        };
        
        const handleMouseEnter = () => this.setState({hovering : true});
        const handleMouseLeave = () => this.setState({hovering : false});

        return (
            <div className="DeviceButton" onClick={this.props.onClick} style={style}
                onMouseEnter={handleMouseEnter}
                onMouseLeave={handleMouseLeave}> {this.props.name}
            </div>
        )
    }
}