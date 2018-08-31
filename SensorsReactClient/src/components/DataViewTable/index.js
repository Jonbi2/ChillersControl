import React, { Component } from 'react';
import { Table } from 'reactstrap';
import './DataViewTable.css';
import ApiConfig from '../../config.json';
import pressureToTemperature from '../../utils/PressureToTemperature';




export default class extends Component {
    constructor(props) {
        super(props);
        this.state = {};
        this.interval = setInterval(() => this.setState({ time: Date.now() }), 1000);
        this.loadSensorsData();
        console.log("Hello world");
    }

    async loadSensorsData() {
        const response = await fetch('http://' + ApiConfig.ApiAddress + ':' + ApiConfig.ApiPort + '/parametersTicker.json');
        const data = await response.json();
        this.setState({ data: data.result });
    }

    countQ(flow, outputTemperature, inputTemperature) {
        flow = Number(flow);
        outputTemperature = Number(outputTemperature);
        inputTemperature = Number(inputTemperature);
        var q = flow * 4.2 * 0.995 * (outputTemperature - inputTemperature) / 60;
        q = parseFloat(Math.abs(q)).toFixed(2);
        if(isNaN(q)) {
            return "Err";
        }
        return q;
    }

    countCop(flows, inputTemperatures, outputTemperatures, power) {
        power = Number(power);
        for(var i = 0; i < flows.length; i++) {
            flows[i] = Number(flows[i]);
        }
        for(var i = 0; i < inputTemperatures.length; i++) {
            inputTemperatures[i] = Number(inputTemperatures[i]);
        }
        for(var i = 0; i < outputTemperatures.length; i++) {
            outputTemperatures[i] = Number(outputTemperatures[i]);
        }
        var q1 = Number(this.countQ(flows[0], outputTemperatures[0], inputTemperatures[0]));
        var q2 = Number(this.countQ(flows[1], outputTemperatures[1], inputTemperatures[1]));
        var result = parseFloat(Number((q1 + q2) / power)).toFixed(2);
        if(isNaN(result)) {
            console.log(q1, q2, power);
            return "Err";
        }
        return result;
    }

    render() {
        const { data } = this.state;
        return (
            <div className="DataViewTable">
                {data ?
                    <div className="Tables">
                        <Table dark>
                            <tbody>
                                <tr>
                                    <td>Tzb  {data.t_zb === null ? "Err" : parseFloat(data.t_zb).toFixed(2)}</td>
                                    <td>Tot  {data.t_ot === null ? "Err" : parseFloat(data.t_ot).toFixed(2)}</td>
                                    <td>Tp1  {data.t_p1 === null ? "Err" : parseFloat(data.t_p1).toFixed(2)}</td>
                                    <td>Tp2  {data.t_p2 === null ? "Err" : parseFloat(data.t_p2).toFixed(2)}</td>
                                </tr>
                                <tr>
                                    <td>Tp3  {data.t_p3 === null ? "Err" : parseFloat(data.t_p3).toFixed(2)}</td>
                                    <td>Tp4  {data.t_p4 === null ? "Err" : parseFloat(data.t_p4).toFixed(2)}</td>
                                    <td>LP  {data.l_p === null ? "Err" : parseFloat(data.l_p).toFixed(2)}</td>
                                    <td>Tevp  {data.l_p === null ? "Err" : parseFloat(pressureToTemperature("R404A", data.l_p)).toFixed(2)}</td>
                                </tr>
                                <tr>
                                    <td>Tsh  {data.t_sh === null ? "Err" : parseFloat(data.t_sh).toFixed(2)}</td>
                                    <td>SH  {data.l_p === null || data.t_sh === null ? "Err"
                                        : parseFloat(data.t_sh - parseFloat(pressureToTemperature("R404A", data.l_p)).toFixed(2)).toFixed(2)}</td>
                                    <td>HP  {data.h_p === null ? "Err" : parseFloat(data.h_p).toFixed(2)}</td>
                                    <td>Tcon  {data.h_p === null ? "Err" : parseFloat(pressureToTemperature("R404A", data.h_p)).toFixed(2)}</td>
                                </tr>
                                <tr>
                                    <td>Tsc  {data.t_sc === null ? "Err" : parseFloat(data.t_sc).toFixed(2)}</td>
                                    <td>Sc  {parseFloat(data.t_sc - parseFloat(pressureToTemperature("R404A", data.h_p)).toFixed(2)).toFixed(2)}</td>
                                    <td>Flow1  {data.flow_1 === null ? "Err" : parseFloat(data.flow_1).toFixed(2)}</td>
                                    <td>Twe1  {data.t_we_1 === null ? "Err" : parseFloat(data.t_we_1).toFixed(2)}</td>
                                </tr>
                                <tr>
                                    <td>Twy1  {data.t_wy_1 === null ? "Err" : parseFloat(data.t_wy_1).toFixed(2)}</td>
                                    <td>&Delta;t1 {data.t_wy_1 == null || data.t_we_1 === null ? "Err" : parseFloat(data.t_wy_1 - data.t_we_1).toFixed(2)}</td>
                                    <td>Q1  {
                                        data.flow_1 === null || data.t_wy_1 === null || data.t_we_1 === null ? "Err" :
                                            this.countQ(data.flow_1, data.t_wy_1, data.t_we_1)
                                    }</td>
                                    <td>Flow2  {data.flow_2 === null ? "Err" : parseFloat(data.flow_2).toFixed(2)}</td>
                                </tr>
                                <tr>
                                    <td>Twe2  {data.t_we_2 === null ? "Err" : parseFloat(data.t_we_2).toFixed(2)}</td>
                                    <td>&Delta;t2  {data.t_wy_2 == null || data.t_we_2 === null ? "Err" : parseFloat(data.t_wy_2 - data.t_we_2).toFixed(2)}</td>
                                    <td>Q2  {
                                        data.flow_1 === null || data.t_wy_2 === null || data.t_we_2 === null ? "Err" :
                                            this.countQ(data.flow_2, data.t_wy_2, data.t_we_2)
                                    }</td>
                                    <td>P  {data.p === null ? "Err" : parseFloat(data.p).toFixed(2)}</td>
                                </tr>
                            </tbody>
                        </Table>
                        <Table dark>
                            <thead>
                                <tr>
                                    <th>CoP  {
                                        data.flow_1 === null || data.t_wy_1 === null || data.t_we_1 === null || data.t_wy_2 === null || data.t_we_2 === null || data.p === null ? "Err" :
                                            this.countCop([data.flow_1, data.flow_2], [data.t_we_1, data.t_we_2], [data.t_wy_1, data.t_wy_2], data.p)
                                    }</th>
                                    <th>Twy2  {data.t_wy_2 === null ? "Err" : parseFloat(data.t_wy_2).toFixed(2)}</th>
                                </tr>
                            </thead>
                        </Table>
                    </div>

                    :
                    <div>Loading...</div>
                }
            </div>)
    }

    componentDidMount() {
        setInterval(() => {
            this.setState(() => {
                this.loadSensorsData();
            });
        }, 2500);
    }
    componentWillUnmount() {
        clearInterval(this.interval);

    }

}

