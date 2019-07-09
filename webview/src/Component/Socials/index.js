import React, { Component } from "react";

import axios from "axios";

export default class SocialButtons extends Component {
  constructor(props) {
    super(props);
    this.state = {
      socials: [],
    };
    this.loadSocialButtons = this.loadSocialButtons.bind(this);
  }

  componentWillMount() {
    this.loadSocialButtons();
  }

  async loadSocialButtons()
  {
    const promise = await axios.get("/api/socials/");
    const status = promise.status;
    
    if(status===200)
    {
      const data = promise.data;
      this.setState({socials: data});
    }
  }

  render() {

    let myData = this.state.socials || {}

    return(
      myData.forEach(mapping => {
          <div>id: {mapping.id}, url: {mapping.icon}</div>
      })
    )
  }
}