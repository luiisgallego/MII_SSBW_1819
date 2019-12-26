import React, { Component } from 'react'
import Peli from './Peli'

export default class Todas extends Component {


    constructor(props) {
        super(props)
        this.state = {                
          pelis: []
         }
      }

    // Llamada al API.
    componentDidMount() {
      fetch('http://localhost:8000/pelis/api_pelis')
        .then(res => { return res.json()})
        .then(data => {
          console.log(data)
          this.setState({pelis:data})
        }).catch(error => {
          console.log(error)
        })

      }

      render() {
        // Re-renderiza al cambiar el state.
        return (
          <div>
            <h2 style={{marginBottom: "50px",marginTop: "50px", fontSize: "70px"}}>Todas las pelis:</h2> <br></br>
            {this.state.pelis.map(peli => { 
              return (
                <Peli peli={peli} />
              )
            })
          }
          </div>
        )
      }
}
