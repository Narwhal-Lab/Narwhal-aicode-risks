(function ($) {
    'use strict';

    let tooltipster_args = {
        animationDuration: parseInt(Encyclopedia_Tooltips.animation_duration), // duration of the animation, in milliseconds
        delay: parseInt(Encyclopedia_Tooltips.delay), // delay before the tooltip starts its opening and closing animations
        distance: 5, // distance between the origin and the tooltip, in pixels
        maxWidth: 480, // maximum width for the tooltip
        theme: 'encyclopedia-tooltip', // this will be added as class to the tooltip wrapper
        trigger: Encyclopedia_Tooltips.trigger, // Sets when the tooltip should open and close. 'hover' and 'click' correspond to predefined sets of built-in triggers
        /*
        functionFormat: function(instance, helper, content){
          let
            url = console.log(instance.elementOrigin().href ),
            displayedContent = content +  '<p><a href="'+url+'">Das ist ein link</a></p>';
          return displayedContent;
        },
        contentAsHTML: true,
        interactive: true,
        */
    };

    Encyclopedia_Tooltips.$links = $('a.encyclopedia, .widget_encyclopedia_taxonomies ul.taxonomy-list li.cat-item > a');

    // Disbale the link if the trigger is the click event
    if (Encyclopedia_Tooltips.trigger == 'click') {
        Encyclopedia_Tooltips.$links.on(Encyclopedia_Tooltips.trigger, function (event) {
            event.preventDefault();
        });
    }

    // initialize the tooltips
    Encyclopedia_Tooltips.links = Encyclopedia_Tooltips.$links.tooltipster(tooltipster_args);

}(jQuery));
