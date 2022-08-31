function post_list_call() {
  $.ajax({
    type: "GET",
    url: "/post",
    data: {},
    success: function(res) {
      let posts = res["posts"]

      for (let i = 0; i < posts.length; i++) {
        let title = posts[i]["title"]
        let img = posts[i]["img"]
        let comment = posts[i]["comment"]

        let temp_html = `
          <li class="card-item">
            <div class="card">
                <div class="card-image"><img src="${img}"></div>
                <div class="card_content">
                <h2 class="card_title">${title}</h2>
                <p class="card_text">${comment}</p>
                <a href="/detail"><button class="btn card_btn">Read More</button></a>
              </div>
            </div>
          </li>
        `
        $(".cards").append(temp_html)
      }
    }
  })
}