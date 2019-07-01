import React, { Component } from 'react'
import './NewsPanel.css'

export default class NewsPanel extends Component {
  constructor() {
    super();
    this.state = { 
      news: null, 
      pageNum: 1, 
      loadedAll: false};
  }

  componentDidMount(){
    this.loadMoreNews();
  }

  loadMoreNews(e) {
    this.setState({

    })
  }

  renderNews() {
    let news_list = this.state.news.map(function(news) {
      return(
        <a className='list-group-item' href="#">
          <NewsCard news={news} />
        </a>
      );
    });

    return(
      <div className="container-fluid">
        <div className='list-group'>
          {news_list}
        </div>
      </div>
    );
  }

  render() {
    if (this.state.news) {
        return(
          <div>
            {this.renderNews()}
          </div>
        );
    } else {
      return(
        <div>
          <div id='msg-app-loading'>
            Loading
          </div>
        </div>
      );
    }
  }
}
