var infinite = new Waypoint.Infinite({
    element: $(".infinite-container")[0],
    onBeforePageLoad: function () {
        $(".spinner-border").show();
    },
    onAfterPageLoad: function () {
        $(".spinner-border").hide();
    }
});