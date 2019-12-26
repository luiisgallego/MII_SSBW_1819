import React, { Component } from 'react'

export default class Peli extends Component {

	render() {

	var peli = this.props.peli   
	return(
	   <div key={peli.id}>
	      <h3>{peli.title}</h3>
		  <h4>Año: {peli.year}  -- Director: {peli.director}</h4>
	      <hr />
	   </div>
	  )
	}
}