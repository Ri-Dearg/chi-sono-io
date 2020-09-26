function fadePreload() {
    $(".preloader").fadeOut(1200);
}

var interviewVideo;
var player;
var firstRun = true 

function onPlayerReady(event) {
    const modal = $("#person-modal").contents();
    modal.find(".fade-load").on("load", fadePreload)
}

function createVideoListener() {
    $('#person-modal').on('show.bs.modal', function (e) {
        player = new YT.Player('player', {
            height: '390',
            width: '640',
            videoId: interviewVideo,
            playerVars: {
                'hl': 'it',
                'enablejsapi': 1,
                'origin': window.location.origin,
            },
            events: {
                'onReady': onPlayerReady,
            }
        });
    })
    $('#person-modal').on('hide.bs.modal', function (e) {
        player.destroy()
    })
}

function onYouTubeIframeAPIReady() {
    createVideoListener()
    }

function createVideo(videoUrl) {
    interviewVideo = videoUrl.split("=")[1]
    if (firstRun) {
        var tag = document.createElement('script');

        tag.src = "https://www.youtube.com/iframe_api";
        var firstScriptTag = document.getElementsByTagName('script')[0];
        firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
        firstRun = false
    }
}

/**
 * Runs the form to like the post through an ajax function.
 */
function openDetail(id, serializedData, formUrl) {
    $.ajax({
        method: "GET",
        url: formUrl,
        data: serializedData,
        datatype: "json",
        success: function (data) {

            if (data.status == 200) {
                $(".detail-overlay").html(data.content[0])
                createVideo(data.content[1].video)
                $(".preloader").fadeIn(1200, function() {
                    $("#modal-trigger").click()
                })
        }
        }
    });
}

function ajaxModal() {
    $(`.detail-form`).on("submit", function (ev) {
        // stops form from sending
        ev.preventDefault();
        var id = this.id.slice(3);
        var serializedData = $(this).serialize();
        var formUrl = this.action;
        openDetail(id, serializedData, formUrl);
    });
}

function lazyLoad() {
	const cardImages = document.querySelectorAll(".card-image");

	// loop over each image
	cardImages.forEach(function (cardImage) {
		const imageUrl = cardImage.getAttribute("data-image-full");
		const contentImage = cardImage.querySelector("img");

		// change src to full res image
		contentImage.src = imageUrl;

		// fires the swap function on load
		contentImage.addEventListener("load", function () {
			// sets the background as the full res image
			cardImage.style.backgroundImage = "url(" + imageUrl + ")";

			// applies class for a smooth transition to the gallery images
			cardImage.classList.add("is-loaded");
		});
	});
}