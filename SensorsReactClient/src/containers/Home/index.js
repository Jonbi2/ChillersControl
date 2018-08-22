import React, { Component } from 'react';
import Chart from 'chart.js'
import Sidebar from '../../components/Sidebar';
import Header from '../../components/Header';
import DataViewTable from '../../components/DataViewTable';
import './Home.css';

class Home extends Component {
  render() {
    return (
      <div className="Home">
        <Sidebar/>
        <div className="Home-body">
          <Header/>
          <DataViewTable />
        </div>
      </div>
    );
  }
}

export default Home;
