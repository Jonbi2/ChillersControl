import React, { Component } from "react";

import SensorsButton from './SensorsButton';
import ApiConfig from '../../config.json';

import { saveAs } from 'file-saver/FileSaver';

import getTemperatureFromPressure from '../../utils/PressureToTemperature';

import './Sidebar.css';


export default class Sidebar extends Component {
    constructor(props) {
        super(props);
        this.state = {
            extended: false,
            data: []
        }
        this.loadSensors();
    }

    async loadSensors() {
        const response = await fetch('http://' + ApiConfig.ApiAddress + ':' + ApiConfig.ApiPort + '/getSensors');
        const data = await response.json();
        const sensors = data.sensors
        this.setState({ sensors: sensors });
    }

    async fetch_data(route) {
        const endpoint = 'http://' + ApiConfig.ApiAddress + ':' + ApiConfig.ApiPort + route + "?csv=True&" + "time_range_begin=" + (Date.now()/1000 - 86400).toString()
        fetch(endpoint, {
            headers: {
              'Content-Type': 'text/csv'
            },
            responseType: 'blob'
          }).then(response => response.blob())
            .then(blob => saveAs(blob, route + '.csv'));
    }

    render() {
        const { sensors } = this.state;
        return (
            <div className={"Sidebar" + (this.state.extended ? " extended" : "")}>

                <div onClick={() => {
                    this.setState({
                        extended: !this.state.extended,
                        extendedChild: false
                    });
                }} className="Sidebar-button">
                </div>

                <div className="Sidebar-content">
                    {this.state.extended && sensors ? sensors.map((sensor, key) => <SensorsButton
                        key={key} {...sensor}
                        onClick={ () => {this.fetch_data(sensor.route.toString())}}
                        name = {sensor.name} />) : console.log("loading")}
                </div>
            </div>
        )
    }

}

{/* {this.state.data.map((e, i) => <div key={i}>{e}</div>)} */ }