(function () {
  window.PredictSDK = {
    track: function (event, data = {}) {
      fetch("https://your-app.onrender.com/events", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          user_id: window.userId || "anon",
          event: event,
          data: data,
          timestamp: Date.now()
        })
      });
    }
  };

  // auto track page load
  window.PredictSDK.track("page_view");
})();