jasmine.getFixtures().fixturesPath = '/static/js/jasmine/spec/javascripts/fixtures'
beforeEach(function() {
    loadFixtures('myfixture.html')
    $.fx.off = true;
});

describe("Preloader", function() {
    it("Should be shown by default.", function(){
        expect($(".preloader")).toBeVisible()
    })
    it("Should fade out.", function(){
        fadePreload()
        expect($(".preloader")).toBeHidden()
    })
})

describe("lazyLoad", function () {
    it("Should have full images data.", function () {
        expect($(".card-image")).toHaveAttr('data-image-full')
    })
    it("Should have a background image thumbnail.", function () {
        let imgSrc = $(".card-image > img").first().attr('src')
        expect($(".card-image").first().attr('style')).toBe(`background-image: url(${imgSrc});`)
    })
    it("Should swap image data after the function.", function () {
            lazyLoad()
            expect($(`.card-image > img`).first()).toHaveAttr('src', $(`img`).parent().attr('data-image-full'))
    })
    it("Should trigger a load event.", function () {
            lazyLoad()
            spyEvent = spyOnEvent(".card-image > img", "load")
            $(".card-image > img").trigger( "load" )

            expect("load").toHaveBeenTriggeredOn(".card-image > img")
            expect(spyEvent).toHaveBeenTriggered()
    })
    // WIll figure out in the future.
    // it("Should add the is-loaded class", function () {
    //         lazyLoad()
    //         $(".card-image > img").trigger( "load" )
    //         console.log(($(`.card-image`))[0])
    //         expect($(`.card-image`)[0]).toHaveAttr('class', 'is-loaded')
    // })
})