/** @odoo-module */
import publicWidget from "@web/legacy/js/public/public_widget";
import { renderToFragment } from "@web/core/utils/render";

publicWidget.registry.MetaFeaturedAuthors = publicWidget.Widget.extend({
    selector: ".meta_featured_authors",
    template: 'meta_feature_author.meta_feature_author_authors_layout',
    init() {
        this._super.apply(this, arguments);
        this.rpc = this.bindService("rpc");
    },

    async start(){
        try {
            const values = await this.rpc('/featured_authors');
            // console.log(`featured_authors ${values}`);
            
            if (values && values.featured_authors && values.featured_authors.length > 0) {
                const content = renderToFragment(this.template, values);
                this.$('.featured_author_render').html(content);
                this._renderOwlSlider(values.featured_authors.length);
            } else {
                console.log("No featured_author in values or it's empty:", values);
                this.$('.featured_author_render').html('<p>No products found.</p>');
            }
        } catch (error) {
            // console.error("Error in start method:", error);
            this.$('.featured_author_render').html('<p>An error occurred while loading products.</p>');
        }
    },

    _renderOwlSlider(productCount){
        var $container = this.$el.find(".owl_slider_wrapper");
        if (productCount < 5) {
            this._displayWithoutCarousel();
        } else if ($.fn.owlCarousel) {
            $container.owlCarousel({
                loop: true,
                autoHeight: true,
                margin: 15,
                nav: true,
                dots: false,
                autoplay: true,
                autoplayHoverPause: true,
                responsiveClass: true,
                responsive: {
                    0: { items: 2 , nav:false},
                    480: { items: 2 , nav:false},
                    768: { items: 3 },
                    992: { items: 4 },
                    1200:{
                        items: 5
                    }
                },
                navText : ["<i class='dri dri-arrow-left-l'></i>","<i class='dri dri-arrow-right-l'></i>"]
            });
        } else {
            console.warn("Owl Carousel not found. Displaying without carousel.");
        }
    },

        
    _displayWithoutCarousel: function(){
        var $container = this.$el.find(".categ_slider_wrapper");
        $container.addClass('row');
        $container.removeClass('owl-carousel');
        $container.find(".item").addClass('col-lg-3 col-sm-4 col-6 mb-4').removeClass('article-items');
    },

});

export default publicWidget.registry.MetaFeaturedAuthors;
