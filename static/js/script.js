function fadePreload() {
    $(".preloader").fadeOut(1200);
}

/**
 * Runs the form to like the post through an ajax function.
 */
function openDetail(id, serializedData, formUrl) {
    $(".preloader").fadeIn(1200);
    $.ajax({
        method: "GET",
        url: formUrl,
        data: serializedData,
        datatype: "json",
        success: function (data) {
            console.log(data)
            if (data.status == 200) {
                $(".detail-overlay").html(data.content).toggleClass("d-none")
                $(".preloader").fadeOut(1200);
            }
        }
    });
}

$(`.detail-form`).on("submit", function (ev) {
    // stops form from sending
    ev.preventDefault();
    var id = this.id.slice(3);
    var serializedData = $(this).serialize();
    var formUrl = this.action;
    openDetail(id, serializedData, formUrl);
});
