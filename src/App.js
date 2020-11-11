import React from 'react';
import NavBar from './components/NavBar';
import Home from './pages/Home';
import About from './pages/About';
import Document from './pages/Document';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

function App() {
  return (
    <Router>
      <div className="App">
        <NavBar />
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/about" exact component={About} />
          <Route path="/docs/:id" component={Document} />
        </Switch>
        <style jsx>{`
          @import url('https://fonts.googleapis.com/css2?family=Viga&display=swap');
          @import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
          * {
            font-size: 16px;
          }  
        `}</style>
      </div>
    </Router>
  );
}

export default App;
