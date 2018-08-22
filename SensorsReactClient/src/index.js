import React from 'react';
import ReactDOM from 'react-dom';
import Home from './containers/Home';
import Details from './containers/Details';
import registerServiceWorker from './registerServiceWorker';
import {
    BrowserRouter as Router,
    Route,
} from 'react-router-dom';

import 'bootstrap/dist/css/bootstrap.min.css';
import './index.css';



ReactDOM.render(
    <Router>
        <div>
            <Route exact path='/' component={Home}/>
            <Route path='/details/:id' component={Details}/>
        </div>
    </Router>
    , document.getElementById('root'));
registerServiceWorker();