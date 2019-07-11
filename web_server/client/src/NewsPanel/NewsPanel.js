import React, { Component } from "react";
import "./NewsPanel.css";
import NewsCard from "../NewsCard/NewsCard";
import _ from "lodash";
import Auth from '../Auth/Auth';

export default class NewsPanel extends Component {
  constructor() {
    super();
    this.state = {
      news: null,
      pageNum: 1,
      loadedAll: false
    };
  }

  handleScroll() {
    const scrollY =
      window.scrollY ||
      window.pageYOffset ||
      document.documentElement.scrollYTop;
    if (window.innerHeight + scrollY >= document.body.offsetHeight - 50) {
      console.log("Loading more news!");
      this.loadMoreNews();
    }
  }

  componentDidMount() {
    this.loadMoreNews();
    // this.loadMoreNews = _.debounce(this.loadMoreNews, 1000);
    console.log("load more news");
    window.addEventListener("scroll", () => this.handleScroll());
  }

  loadMoreNews() {
    // if (this.state.loadedAll == true) {
    //   return;
    // }

    // const news_url =
    //   "http://" +
    //   window.location.hostname +
    //   ":3000" +
    //   "/news/userId/" +
    //   Auth.getEmail() +
    //   "/pageNum/" +
    //   this.state.pageNum;

    // const request = new Request(news_url, {
    //   method: "GET",
    //   headers: {
    //     Authorization: "bearer " + Auth.getToken()
    //   }
    // });

    let request = new Request('http://localhost:3000/news', {
      method: 'GET',
      headers: {
        Authorization: "bearer " + Auth.getToken()
      }
    });

    fetch(request)
      .then(res => res.json())
      .then(news => {
        this.setState({
          news: this.state.news ? this.state.news.concat(news) : news,
        })
      })
      // .then(news => {
      //   if (!news || news.length == 0) {
      //     this.setState({ loadedAll: true });
      //   }

      //   this.setState({
      //     news: this.state.news ? this.state.news.concat(news) : news,
      //     pageNum: this.state.pageNum + 1
      //   });
      // });
  }

  renderNews() {
    let news_list = this.state.news.map(function(news) {
      return (
        <a className="list-group-item" href="#">
          <NewsCard news={news} />
        </a>
      );
    });

    return (
      <div className="container-fluid">
        <div className="list-group">{news_list}</div>
      </div>
    );
  }

  render() {
    if (this.state.news) {
      return <div>{this.renderNews()}</div>;
    } else {
      return (
        <div>
          <div id="msg-app-loading">Loading</div>
        </div>
      );
    }
  }
}
