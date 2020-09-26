jasmine.getFixtures().fixturesPath = '/static/js/jasmine/spec/javascripts/fixtures'
beforeEach(function() {
    loadFixtures('myfixture.html')
    $.fx.off = true;
});

describe("Preloader", function() {
    it("Should fade out.", function(){
        fadePreload()
        expect($(".preloader")).toBeHidden()
    })
})