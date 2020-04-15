import React, { PureComponent } from 'react';
import logo from './logo.svg';
import './App.css';
import TableForm from './components/TableForm';

class App extends React.PureComponent {

  render() {
    return (
      <div className="App">
        <TableForm />
      </div>
    );
  }

}

export default App;
