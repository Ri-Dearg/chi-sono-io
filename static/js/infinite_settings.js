var infinite = new Waypoint.Infinite({
    element: $(".infinite-container")[0],
    onBeforePageLoad: function () {
        $(".infinite-loader").show();
    },
    onAfterPageLoad: function () {
        ajaxModal()
        $(".infinite-loader").hide();
    }
});