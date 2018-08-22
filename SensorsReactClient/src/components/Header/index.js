import React, { Component } from "react";
import DeviceButton from './DeviceButton';
import './Header.css';

export default class Header extends Component {
    constructor(props) {
        super(props);
        this.state = {
            extended: false,
            data: []
        }
    }

    generateButtons(number) {
        var indents = [];
        for (var i = 0; i < number; i++) {
            var j = i + 1;
            indents.push(<DeviceButton onClick={() => { console.log("Button clicked") }} name = {"B300" + "-" + j} />
            );
        }
        return indents;
    }

    render() {
        return (
            <div className={"Header" + (this.state.extended ? " extended" : "")} style={{textAlign: "center", color: "white"}}>
                Parameters
                {this.generateButtons(0)}
            </div>
        )
    }
    toggle() {
        if (!this.state.extended) {
            let random = Math.ceil(Math.random() * 20);
            let randomShit = [];
            for (let i = 0; i < random; i++) {
                randomShit.push(Math.random());
            }
            this.setState({ data: randomShit });
        }
        this.setState({
            extended: !this.state.extended
        });
    }

}