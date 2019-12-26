
import logo from './logo.svg';
import './App.css';
import React from 'react';
import Todas from './components/Todas'


import {
  Collapse,
  Navbar,
  NavbarToggler,
  NavbarBrand,
  Nav,
  NavItem,
  NavLink,
  UncontrolledDropdown,
  DropdownToggle,
  DropdownMenu,
  DropdownItem } from 'reactstrap';

export default class App extends React.Component {
  constructor(props) {
    super(props);

    this.toggle = this.toggle.bind(this);
    this.state = {
      isOpen: false
    };
  }
  toggle() {
    this.setState({
      isOpen: !this.state.isOpen
    });
  }
  render() {
    return (
      <div>
        <Navbar color="light" light expand="md">
          <NavbarBrand href="/">Pelis con React</NavbarBrand>
          <NavbarToggler onClick={this.toggle} />
        </Navbar>
        <div class = "container">
          <Todas />
        </div>
      </div>
    );
  }

}
