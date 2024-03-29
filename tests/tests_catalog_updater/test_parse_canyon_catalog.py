from lxml import etree

from app.catalog.catalog_operations import _parse_canyon_catalog
from app.models import Bike


def test_parse_canyon_catalog_one_bike():
    one_bike_tree = etree.HTML("""<li class="productGrid__listItem xlt-producttile">                            
                                <!-- CQuotient Activity Tracking (viewCategory-cquotient.js) -->
<script type="text/javascript">//<!--
/* <![CDATA[ */
(function(){
try {
    if(window.CQuotient) {
	var cq_params = {};
	
	cq_params.cookieId = window.CQuotient.getCQCookieId();
	cq_params.userId = window.CQuotient.getCQUserId();
	cq_params.emailId = CQuotient.getCQHashedEmail();
	cq_params.loginId = CQuotient.getCQHashedLogin();
	cq_params.accumulate = true;
	cq_params.products = [{
	    id: '3955',
	    sku: ''
	}];
	cq_params.categoryId = 'instockbikes';
	cq_params.refinements = '[{\"name\":\"pc_rahmengroesse\",\"value\":\"3XS\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"2XS\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"XS\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"S\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"M\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"L\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"XL\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"2XL\'\"},{\"name\":\"Category\",\"value\":\"instockbikes\"}]';
	cq_params.personalized = 'false';
	cq_params.sortingRule = 'sort_master_availability';
	cq_params.imageUUID = '__UNDEFINED__';
	cq_params.realm = "BCML";
	cq_params.siteId = "RoW";
	cq_params.instanceType = "prd";
	cq_params.queryLocale = "en";
	cq_params.locale = window.CQuotient.locale;
	
	if(window.CQuotient.sendActivity)
	    window.CQuotient.sendActivity(CQuotient.clientId, 'viewCategory', cq_params);
	else
	    window.CQuotient.activities.push({
	    	activityType: 'viewCategory',
	    	parameters: cq_params
	    });
  }
} catch(err) {}
})();
/* ]]> */
// -->
</script>
<script type="text/javascript">//<!--
/* <![CDATA[ (viewCategoryProduct-active_data.js) */
(function(){
try {
	if (dw.ac) {
		var search_params = {};
		search_params.persd = 'false';
		search_params.refs = '[{\"name\":\"pc_rahmengroesse\",\"value\":\"3XS\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"2XS\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"XS\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"S\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"M\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"L\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"XL\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"2XL\'\"},{\"name\":\"Category\",\"value\":\"instockbikes\"}]';
		search_params.sort = 'sort_master_availability';
		search_params.imageUUID = '';
		search_params.searchID = '5182d786-0858-41e7-9758-51a69d2227c5';
		search_params.locale = 'en_DE';
		search_params.queryLocale = 'en';
		search_params.showProducts = 'true';
		dw.ac.applyContext({category: "instockbikes", searchData: search_params});
		if (typeof dw.ac._scheduleDataSubmission === "function") {
			dw.ac._scheduleDataSubmission();
		}
	}
} catch(err) {}
})();
/* ]]> */
// -->
</script>
<script type="text/javascript">//<!--
/* <![CDATA[ (viewProduct-active_data.js) */
dw.ac._capture({id: "3955", type: "searchhit"});
/* ]]> */
// -->
</script>
                                    









    
        
    

    




    










    

    <div data-pid="50031313" class="js-gtmTileWrapper js-productTileWrapper productTileDefault productTileDefault--bike" data-product-tile-context="grid" data-gtm-impression="[{&quot;event&quot;:&quot;EEC-productImpression&quot;,&quot;ecommerce&quot;:{&quot;currencyCode&quot;:&quot;EUR&quot;,&quot;impressions&quot;:[{&quot;name&quot;:&quot;Aeroad CF SLX 8 Di2&quot;,&quot;id&quot;:&quot;3955&quot;,&quot;brand&quot;:&quot;Canyon&quot;,&quot;category&quot;:&quot;Road Bikes/Aero/Aeroad/Aeroad CF SLX&quot;,&quot;variant&quot;:&quot;&quot;,&quot;dimension50&quot;:&quot;2023&quot;,&quot;dimension52&quot;:&quot;Aeroad&quot;,&quot;dimension63&quot;:&quot;unisex&quot;,&quot;dimension64&quot;:&quot;&quot;,&quot;dimension65&quot;:&quot;ZFER&quot;,&quot;dimension66&quot;:&quot;Complete Bike RR&quot;,&quot;dimension67&quot;:&quot;false&quot;,&quot;dimension68&quot;:&quot;false&quot;,&quot;feedProductId&quot;:&quot;50031322&quot;,&quot;dimension54&quot;:&quot;not defined&quot;,&quot;dimension51&quot;:&quot;Stealth&quot;,&quot;dimension53&quot;:&quot;S | M | L | XL&quot;,&quot;quantity&quot;:1,&quot;price&quot;:5293.28,&quot;metric4&quot;:6299,&quot;dimension56&quot;:&quot;not defined&quot;}]}},{&quot;event&quot;:&quot;view_item_list&quot;,&quot;event_type&quot;:&quot;ecommerce&quot;,&quot;ecommerce&quot;:{&quot;items&quot;:[{&quot;item_id&quot;:&quot;3955&quot;,&quot;item_name&quot;:&quot;Aeroad CF SLX 8 Di2&quot;,&quot;coupon&quot;:&quot;&quot;,&quot;currency&quot;:&quot;EUR&quot;,&quot;discount&quot;:&quot;&quot;,&quot;item_brand&quot;:&quot;Canyon&quot;,&quot;item_gender&quot;:&quot;Unisex&quot;,&quot;item_category&quot;:&quot;Road Bikes&quot;,&quot;item_category2&quot;:&quot;Aero&quot;,&quot;item_category3&quot;:&quot;Aeroad&quot;,&quot;item_category4&quot;:&quot;Aeroad CF SLX&quot;,&quot;item_color&quot;:&quot;Stealth&quot;,&quot;item_size&quot;:&quot;S | M | L | XL&quot;,&quot;item_availability&quot;:&quot;not defined&quot;,&quot;item_set_origin&quot;:&quot;not defined&quot;,&quot;item_material_type&quot;:&quot;ZFER&quot;,&quot;item_outlet_flag&quot;:&quot;false&quot;,&quot;item_customizing_flag&quot;:&quot;false&quot;,&quot;feedProductId&quot;:&quot;50031322&quot;,&quot;item_variant&quot;:&quot;&quot;,&quot;price&quot;:5293.28,&quot;gross_price&quot;:6299,&quot;quantity&quot;:1}]}}]" bis_skin_checked="1">

        <div class="productTileDefault__imageWrapper" bis_skin_checked="1">

            

            <a title="Aeroad CF SLX 8 Di2" aria-label="Aeroad CF SLX 8 Di2 Price: 6.299 €" class="js-productTile productTileDefault__imageLink" aria-hidden="false" tabindex="0" href="https://www.canyon.com/en-de/road-bikes/aero-bikes/aeroad/cf-slx/aeroad-cf-slx-8-di2/3955.html?dwvar_3955_pv_rahmenfarbe=BK%2FBK" data-gtm-click="[{&quot;event&quot;:&quot;EEC-productClick&quot;,&quot;ecommerce&quot;:{&quot;click&quot;:{&quot;actionField&quot;:{&quot;list&quot;:&quot;&quot;},&quot;products&quot;:[{&quot;name&quot;:&quot;Aeroad CF SLX 8 Di2&quot;,&quot;id&quot;:&quot;3955&quot;,&quot;brand&quot;:&quot;Canyon&quot;,&quot;category&quot;:&quot;Road Bikes/Aero/Aeroad/Aeroad CF SLX&quot;,&quot;variant&quot;:&quot;&quot;,&quot;dimension50&quot;:&quot;2023&quot;,&quot;dimension52&quot;:&quot;Aeroad&quot;,&quot;dimension63&quot;:&quot;unisex&quot;,&quot;dimension64&quot;:&quot;&quot;,&quot;dimension65&quot;:&quot;ZFER&quot;,&quot;dimension66&quot;:&quot;Complete Bike RR&quot;,&quot;dimension67&quot;:&quot;false&quot;,&quot;dimension68&quot;:&quot;false&quot;,&quot;feedProductId&quot;:&quot;50031322&quot;,&quot;dimension54&quot;:&quot;not defined&quot;,&quot;dimension51&quot;:&quot;Stealth&quot;,&quot;dimension53&quot;:&quot;S | M | L | XL&quot;,&quot;quantity&quot;:&quot;&quot;,&quot;price&quot;:5293.28,&quot;metric4&quot;:6299,&quot;dimension56&quot;:&quot;not defined&quot;}]},&quot;currencyCode&quot;:&quot;EUR&quot;}},{&quot;event&quot;:&quot;select_item&quot;,&quot;event_type&quot;:&quot;ecommerce&quot;,&quot;ecommerce&quot;:{&quot;items&quot;:[{&quot;item_id&quot;:&quot;3955&quot;,&quot;item_name&quot;:&quot;Aeroad CF SLX 8 Di2&quot;,&quot;coupon&quot;:&quot;&quot;,&quot;currency&quot;:&quot;EUR&quot;,&quot;discount&quot;:&quot;&quot;,&quot;item_brand&quot;:&quot;Canyon&quot;,&quot;item_gender&quot;:&quot;Unisex&quot;,&quot;item_category&quot;:&quot;Road Bikes&quot;,&quot;item_category2&quot;:&quot;Aero&quot;,&quot;item_category3&quot;:&quot;Aeroad&quot;,&quot;item_category4&quot;:&quot;Aeroad CF SLX&quot;,&quot;item_color&quot;:&quot;Stealth&quot;,&quot;item_size&quot;:&quot;S | M | L | XL&quot;,&quot;item_availability&quot;:&quot;not defined&quot;,&quot;item_set_origin&quot;:&quot;not defined&quot;,&quot;item_material_type&quot;:&quot;ZFER&quot;,&quot;item_outlet_flag&quot;:&quot;false&quot;,&quot;item_customizing_flag&quot;:&quot;false&quot;,&quot;feedProductId&quot;:&quot;50031322&quot;,&quot;item_variant&quot;:&quot;&quot;,&quot;price&quot;:5293.28,&quot;gross_price&quot;:6299,&quot;quantity&quot;:1}]}}]">

                
                
                <div class="productTileDefault__pictureWrapper js-noSwatchTileImagesContainer" data-tile-images="[{&quot;title&quot;:&quot;Aeroad CF SLX 8 Di2&quot;,&quot;alt&quot;:&quot;Aeroad CF SLX 8 Di2&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwa0aff968/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P01_P5.jpg?sw=501&amp;sh=282&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwa0aff968/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P01_P5.jpg?sw=735&amp;sh=414&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwa0aff968/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P01_P5.jpg?sw=933&amp;sh=525&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwa0aff968/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P01_P5.jpg?sw=550&amp;sh=310&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwa0aff968/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P01_P5.jpg?sw=630&amp;sh=355&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwa0aff968/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P01_P5.jpg?sw=630&amp;sh=355&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwa0aff968/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P01_P5.jpg?sw=630&amp;sh=355&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dwa0aff968/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P01_P5.png&quot;},&quot;found&quot;:true}]" data-tile-hover-images="[{&quot;title&quot;:&quot;Aeroad CF SLX 8 Di2&quot;,&quot;alt&quot;:&quot;Aeroad CF SLX 8 Di2&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwb9a80d81/images/components/3955_COM-2/2023/3955_COM-2_aeroad-cf-slx-8-di2_P01_laufrad.jpg?sw=1002&amp;sh=564&amp;sm=cut&amp;sfrm=jpg&amp;bgcolor=F2F2F2&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwb9a80d81/images/components/3955_COM-2/2023/3955_COM-2_aeroad-cf-slx-8-di2_P01_laufrad.jpg?sw=1470&amp;sh=828&amp;sm=cut&amp;sfrm=jpg&amp;bgcolor=F2F2F2&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwb9a80d81/images/components/3955_COM-2/2023/3955_COM-2_aeroad-cf-slx-8-di2_P01_laufrad.jpg?sw=1866&amp;sh=1050&amp;sm=cut&amp;sfrm=jpg&amp;bgcolor=F2F2F2&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwb9a80d81/images/components/3955_COM-2/2023/3955_COM-2_aeroad-cf-slx-8-di2_P01_laufrad.jpg?sw=1100&amp;sh=620&amp;sm=cut&amp;sfrm=jpg&amp;bgcolor=F2F2F2&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwb9a80d81/images/components/3955_COM-2/2023/3955_COM-2_aeroad-cf-slx-8-di2_P01_laufrad.jpg?sw=1260&amp;sh=710&amp;sm=cut&amp;sfrm=jpg&amp;bgcolor=F2F2F2&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwb9a80d81/images/components/3955_COM-2/2023/3955_COM-2_aeroad-cf-slx-8-di2_P01_laufrad.jpg?sw=1260&amp;sh=710&amp;sm=cut&amp;sfrm=jpg&amp;bgcolor=F2F2F2&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwb9a80d81/images/components/3955_COM-2/2023/3955_COM-2_aeroad-cf-slx-8-di2_P01_laufrad.jpg?sw=1260&amp;sh=710&amp;sm=cut&amp;sfrm=jpg&amp;bgcolor=F2F2F2&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dwb9a80d81/images/components/3955_COM-2/2023/3955_COM-2_aeroad-cf-slx-8-di2_P01_laufrad.jpg&quot;},&quot;found&quot;:true}]" bis_skin_checked="1">
                    
















    
        
        <picture class="picture productTileDefault__picture productTileDefault__picture--main">
            
                
            
                
                    <source media="(min-width: 1921px)" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwa0aff968/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P01_P5.jpg?sw=630&amp;sh=355&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2">
                
            
                
                    <source media="(min-width: 1440px)" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwa0aff968/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P01_P5.jpg?sw=630&amp;sh=355&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2">
                
            
                
                    <source media="(min-width: 1200px)" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwa0aff968/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P01_P5.jpg?sw=630&amp;sh=355&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2">
                
            
                
                    <source media="(min-width: 992px)" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwa0aff968/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P01_P5.jpg?sw=550&amp;sh=310&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2">
                
            
                
                    <source media="(min-width: 768px)" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwa0aff968/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P01_P5.jpg?sw=933&amp;sh=525&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2">
                
            
                
                    <source media="(min-width: 544px)" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwa0aff968/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P01_P5.jpg?sw=735&amp;sh=414&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2">
                
            
                
                    <source media="(min-width: 0px)" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwa0aff968/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P01_P5.jpg?sw=501&amp;sh=282&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2">
                
            
            <img title="Aeroad CF SLX 8 Di2" alt="Aeroad CF SLX 8 Di2" class="picture__image  productTileDefault__image" src="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwa0aff968/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P01_P5.jpg?sw=501&amp;sh=282&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2" loading="lazy">
        </picture>
    




                </div>
            </a>

            <div class="productTileDefault__awardAndBadges" bis_skin_checked="1">

                

                <div class="productTileDefault__badges" bis_skin_checked="1">
                    


    <ul class="productBadges__list">
        
            <li class="productBadges__listItem">
                <div class="productBadge productBadge--availability" bis_skin_checked="1">
                    Available to buy in S | M | L | XL
                </div>
            </li>
        
    </ul>


                </div>

                

                <div class="productTileDefault__removeWrapper" bis_skin_checked="1">
                    <button aria-hidden="false" aria-label="Remove item from recently viewed list." class="buttonIcon buttonIcon--small productTileDefault__remove js-removeRecentlyVisitedProduct" data-swipe-left="/on/demandware.store/Sites-RoW-Site/en_DE/Include-RecentlyVisitedProducts?removeId=50031313&amp;lazyLoad=false" tabindex="0" type="button">
                        


    <svg xmlns:xlink="http://www.w3.org/1999/xlink" class="icon icon-close buttonIcon__icon productTileDefault__removeIcon" aria-hidden="false" focusable="false">
        
        
        
            <use xlink:href="/on/demandware.static/Sites-RoW-Site/-/en_DE/v1703839529785/images/iconsNew.svg#sprite-close"></use>
        
        
    </svg>


                    </button>
                </div>

                

                <div class="productTileDefault__award" bis_skin_checked="1">
                    


    <!-- No Awards -->


                </div>

            </div>

            

        </div>

        <div class="productTileDefault__productSummary" bis_skin_checked="1">
            <div class="productTileDefault__productSummaryTop" bis_skin_checked="1">

                <div class="productTileDefault__colorsAndCompare" bis_skin_checked="1">

                    

                    
                    




<div class="colorPicker__wrapper colorPicker__wrapper--showOptionalPlusIndicator js-colorPickerWrapper" bis_skin_checked="1">
    
    

        
        

        
            
                
    
        




    
    

    

    <ul class="js-colorPicker colorPicker  colorPicker--colorCount--3 colorPicker--showOptionalPlusIndicator  ">

        
        
            
            
            
                <li class="colorPicker__colorListItem ">
                    

                    






<button aria-hidden="false" aria-label="Stealth" class="colorSwatch colorSwatch--button colorSwatch--small colorSwatch--undefined colorSwatch--selected js-noGtmImpression js-color-swatch  colorPicker__colorSwatch js-hideDirectAddToCarButton " tabindex="0" data-url="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_DE/Product-Variation?dwvar_3955_pv_rahmenfarbe=&amp;pid=3955&amp;quantity=undefined&amp;imageupdate=product" data-displayvalue="Stealth" data-swatch-color-id="BK/BK" data-selected-color-value="BK/BK" data-tile-images="[{&quot;title&quot;:&quot;Aeroad CF SLX 8 Di2&quot;,&quot;alt&quot;:&quot;Aeroad CF SLX 8 Di2&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwa0aff968/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P01_P5.jpg?sw=501&amp;sh=282&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwa0aff968/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P01_P5.jpg?sw=735&amp;sh=414&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwa0aff968/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P01_P5.jpg?sw=933&amp;sh=525&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwa0aff968/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P01_P5.jpg?sw=550&amp;sh=310&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwa0aff968/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P01_P5.jpg?sw=630&amp;sh=355&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwa0aff968/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P01_P5.jpg?sw=630&amp;sh=355&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwa0aff968/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P01_P5.jpg?sw=630&amp;sh=355&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dwa0aff968/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P01_P5.png&quot;},&quot;found&quot;:true}]" data-tile-hover-images="[{&quot;title&quot;:&quot;Aeroad CF SLX 8 Di2&quot;,&quot;alt&quot;:&quot;Aeroad CF SLX 8 Di2&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwb9a80d81/images/components/3955_COM-2/2023/3955_COM-2_aeroad-cf-slx-8-di2_P01_laufrad.jpg?sw=1002&amp;sh=564&amp;sm=cut&amp;sfrm=jpg&amp;bgcolor=F2F2F2&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwb9a80d81/images/components/3955_COM-2/2023/3955_COM-2_aeroad-cf-slx-8-di2_P01_laufrad.jpg?sw=1470&amp;sh=828&amp;sm=cut&amp;sfrm=jpg&amp;bgcolor=F2F2F2&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwb9a80d81/images/components/3955_COM-2/2023/3955_COM-2_aeroad-cf-slx-8-di2_P01_laufrad.jpg?sw=1866&amp;sh=1050&amp;sm=cut&amp;sfrm=jpg&amp;bgcolor=F2F2F2&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwb9a80d81/images/components/3955_COM-2/2023/3955_COM-2_aeroad-cf-slx-8-di2_P01_laufrad.jpg?sw=1100&amp;sh=620&amp;sm=cut&amp;sfrm=jpg&amp;bgcolor=F2F2F2&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwb9a80d81/images/components/3955_COM-2/2023/3955_COM-2_aeroad-cf-slx-8-di2_P01_laufrad.jpg?sw=1260&amp;sh=710&amp;sm=cut&amp;sfrm=jpg&amp;bgcolor=F2F2F2&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwb9a80d81/images/components/3955_COM-2/2023/3955_COM-2_aeroad-cf-slx-8-di2_P01_laufrad.jpg?sw=1260&amp;sh=710&amp;sm=cut&amp;sfrm=jpg&amp;bgcolor=F2F2F2&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwb9a80d81/images/components/3955_COM-2/2023/3955_COM-2_aeroad-cf-slx-8-di2_P01_laufrad.jpg?sw=1260&amp;sh=710&amp;sm=cut&amp;sfrm=jpg&amp;bgcolor=F2F2F2&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dwb9a80d81/images/components/3955_COM-2/2023/3955_COM-2_aeroad-cf-slx-8-di2_P01_laufrad.jpg&quot;},&quot;found&quot;:true}]" data-pdp-url="https://www.canyon.com/en-de/road-bikes/aero-bikes/aeroad/cf-slx/aeroad-cf-slx-8-di2/3955.html?dwvar_3955_pv_rahmenfarbe=BK%2FBK" data-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-AddToCompare?pid=50031309" data-remove-from-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-RemoveFromCompare?pid=50031309" data-compare-pid="50031309" data-color-variant-pid="50031309" title="Stealth" data-quick-add-url="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_DE/Tile-Variation?pid=3955&amp;dwvar_3955_pv_rahmenfarbe=BK%2fBK" type="button">

    
        
    <span class="colorSwatch__colorWrapper">
        <span class="colorSwatch__colorInner">
            
                <span class="colorSwatch__color" style="color:#6e6e6e;"></span>
            
                <span class="colorSwatch__color" style="color:#030303;"></span>
            
        </span>
    </span>


    

    
</button>


                    <span class="colorSwatch__colorLabel" role="tooltip">
                        <span class="colorSwatch__colorLabelText">
                            Color:
                        </span>
                        <span class="colorSwatch__colorLabelValue">
                            Stealth
                        </span>
                    </span>
                </li>
            
        
            
            
            
                <li class="colorPicker__colorListItem ">
                    

                    






<button aria-hidden="false" aria-label="Pale Green" class="colorSwatch colorSwatch--button colorSwatch--small colorSwatch--undefined  js-color-swatch  colorPicker__colorSwatch  " tabindex="0" data-url="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_DE/Product-Variation?dwvar_3955_pv_rahmenfarbe=R081_P08&amp;pid=3955&amp;quantity=undefined&amp;imageupdate=product" data-displayvalue="Pale Green" data-swatch-color-id="R081_P08" data-tile-images="[{&quot;title&quot;:&quot;Aeroad CF SLX 8 Di2&quot;,&quot;alt&quot;:&quot;Aeroad CF SLX 8 Di2&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw789926ac/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P08_P5.jpg?sw=501&amp;sh=282&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw789926ac/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P08_P5.jpg?sw=735&amp;sh=414&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw789926ac/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P08_P5.jpg?sw=933&amp;sh=525&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw789926ac/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P08_P5.jpg?sw=550&amp;sh=310&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw789926ac/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P08_P5.jpg?sw=630&amp;sh=355&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw789926ac/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P08_P5.jpg?sw=630&amp;sh=355&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw789926ac/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P08_P5.jpg?sw=630&amp;sh=355&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dw789926ac/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P08_P5.png&quot;},&quot;found&quot;:true}]" data-tile-hover-images="[{&quot;title&quot;:&quot;Aeroad CF SLX 8 Di2&quot;,&quot;alt&quot;:&quot;Aeroad CF SLX 8 Di2&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw47cd17f0/images/components/3955_COM-2/2023/3955_COM-2_aeroad-cf-slx-8-di2_P08_laufrad_002.jpg?sw=1002&amp;sh=564&amp;sm=cut&amp;sfrm=jpg&amp;bgcolor=F2F2F2&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw47cd17f0/images/components/3955_COM-2/2023/3955_COM-2_aeroad-cf-slx-8-di2_P08_laufrad_002.jpg?sw=1470&amp;sh=828&amp;sm=cut&amp;sfrm=jpg&amp;bgcolor=F2F2F2&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw47cd17f0/images/components/3955_COM-2/2023/3955_COM-2_aeroad-cf-slx-8-di2_P08_laufrad_002.jpg?sw=1866&amp;sh=1050&amp;sm=cut&amp;sfrm=jpg&amp;bgcolor=F2F2F2&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw47cd17f0/images/components/3955_COM-2/2023/3955_COM-2_aeroad-cf-slx-8-di2_P08_laufrad_002.jpg?sw=1100&amp;sh=620&amp;sm=cut&amp;sfrm=jpg&amp;bgcolor=F2F2F2&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw47cd17f0/images/components/3955_COM-2/2023/3955_COM-2_aeroad-cf-slx-8-di2_P08_laufrad_002.jpg?sw=1260&amp;sh=710&amp;sm=cut&amp;sfrm=jpg&amp;bgcolor=F2F2F2&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw47cd17f0/images/components/3955_COM-2/2023/3955_COM-2_aeroad-cf-slx-8-di2_P08_laufrad_002.jpg?sw=1260&amp;sh=710&amp;sm=cut&amp;sfrm=jpg&amp;bgcolor=F2F2F2&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw47cd17f0/images/components/3955_COM-2/2023/3955_COM-2_aeroad-cf-slx-8-di2_P08_laufrad_002.jpg?sw=1260&amp;sh=710&amp;sm=cut&amp;sfrm=jpg&amp;bgcolor=F2F2F2&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dw47cd17f0/images/components/3955_COM-2/2023/3955_COM-2_aeroad-cf-slx-8-di2_P08_laufrad_002.jpg&quot;},&quot;found&quot;:true}]" data-pdp-url="https://www.canyon.com/en-de/road-bikes/aero-bikes/aeroad/cf-slx/aeroad-cf-slx-8-di2/3955.html?dwvar_3955_pv_rahmenfarbe=R081_P08" data-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-AddToCompare?pid=50031316" data-remove-from-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-RemoveFromCompare?pid=50031316" data-compare-pid="50031316" data-color-variant-pid="50031316" title="Pale Green" data-quick-add-url="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_DE/Tile-Variation?pid=3955&amp;dwvar_3955_pv_rahmenfarbe=R081_P08" type="button">

    
        
    <span class="colorSwatch__colorWrapper">
        <span class="colorSwatch__colorInner">
            
                <span class="colorSwatch__color" style="color:#709897;"></span>
            
                <span class="colorSwatch__color" style="color:#222;"></span>
            
        </span>
    </span>


    

    
</button>


                    <span class="colorSwatch__colorLabel" role="tooltip">
                        <span class="colorSwatch__colorLabelText">
                            Color:
                        </span>
                        <span class="colorSwatch__colorLabelValue">
                            Pale Green
                        </span>
                    </span>
                </li>
            
        
            
            
            
                <li class="colorPicker__colorListItem ">
                    

                    






<button aria-hidden="false" aria-label="Dark Blue" class="colorSwatch colorSwatch--button colorSwatch--small colorSwatch--undefined  js-color-swatch  colorPicker__colorSwatch js-hideDirectAddToCarButton " tabindex="0" data-url="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_DE/Product-Variation?dwvar_3955_pv_rahmenfarbe=R081_P09&amp;pid=3955&amp;quantity=undefined&amp;imageupdate=product" data-displayvalue="Dark Blue" data-swatch-color-id="R081_P09" data-tile-images="[{&quot;title&quot;:&quot;Aeroad CF SLX 8 Di2&quot;,&quot;alt&quot;:&quot;Aeroad CF SLX 8 Di2&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw052cae86/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P09_P5.jpg?sw=501&amp;sh=282&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw052cae86/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P09_P5.jpg?sw=735&amp;sh=414&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw052cae86/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P09_P5.jpg?sw=933&amp;sh=525&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw052cae86/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P09_P5.jpg?sw=550&amp;sh=310&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw052cae86/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P09_P5.jpg?sw=630&amp;sh=355&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw052cae86/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P09_P5.jpg?sw=630&amp;sh=355&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw052cae86/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P09_P5.jpg?sw=630&amp;sh=355&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dw052cae86/images/full/full_2023_/2023/full_2023_3955_aeroad-cf-slx-8-disc-di2_P09_P5.png&quot;},&quot;found&quot;:true}]" data-tile-hover-images="[{&quot;title&quot;:&quot;Aeroad CF SLX 8 Di2&quot;,&quot;alt&quot;:&quot;Aeroad CF SLX 8 Di2&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw44cf895b/images/components/3955_COM-2/2023/3955_COM-2_aeroad-cf-slx-8-di2_P09_laufrad.jpg?sw=1002&amp;sh=564&amp;sm=cut&amp;sfrm=jpg&amp;bgcolor=F2F2F2&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw44cf895b/images/components/3955_COM-2/2023/3955_COM-2_aeroad-cf-slx-8-di2_P09_laufrad.jpg?sw=1470&amp;sh=828&amp;sm=cut&amp;sfrm=jpg&amp;bgcolor=F2F2F2&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw44cf895b/images/components/3955_COM-2/2023/3955_COM-2_aeroad-cf-slx-8-di2_P09_laufrad.jpg?sw=1866&amp;sh=1050&amp;sm=cut&amp;sfrm=jpg&amp;bgcolor=F2F2F2&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw44cf895b/images/components/3955_COM-2/2023/3955_COM-2_aeroad-cf-slx-8-di2_P09_laufrad.jpg?sw=1100&amp;sh=620&amp;sm=cut&amp;sfrm=jpg&amp;bgcolor=F2F2F2&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw44cf895b/images/components/3955_COM-2/2023/3955_COM-2_aeroad-cf-slx-8-di2_P09_laufrad.jpg?sw=1260&amp;sh=710&amp;sm=cut&amp;sfrm=jpg&amp;bgcolor=F2F2F2&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw44cf895b/images/components/3955_COM-2/2023/3955_COM-2_aeroad-cf-slx-8-di2_P09_laufrad.jpg?sw=1260&amp;sh=710&amp;sm=cut&amp;sfrm=jpg&amp;bgcolor=F2F2F2&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw44cf895b/images/components/3955_COM-2/2023/3955_COM-2_aeroad-cf-slx-8-di2_P09_laufrad.jpg?sw=1260&amp;sh=710&amp;sm=cut&amp;sfrm=jpg&amp;bgcolor=F2F2F2&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dw44cf895b/images/components/3955_COM-2/2023/3955_COM-2_aeroad-cf-slx-8-di2_P09_laufrad.jpg&quot;},&quot;found&quot;:true}]" data-pdp-url="https://www.canyon.com/en-de/road-bikes/aero-bikes/aeroad/cf-slx/aeroad-cf-slx-8-di2/3955.html?dwvar_3955_pv_rahmenfarbe=R081_P09" data-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-AddToCompare?pid=50031323" data-remove-from-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-RemoveFromCompare?pid=50031323" data-compare-pid="50031323" data-color-variant-pid="50031323" title="Dark Blue" data-quick-add-url="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_DE/Tile-Variation?pid=3955&amp;dwvar_3955_pv_rahmenfarbe=R081_P09" type="button">

    
        
    <span class="colorSwatch__colorWrapper">
        <span class="colorSwatch__colorInner">
            
                <span class="colorSwatch__color" style="color:#2325be;"></span>
            
                <span class="colorSwatch__color" style="color:#222;"></span>
            
        </span>
    </span>


    

    
</button>


                    <span class="colorSwatch__colorLabel" role="tooltip">
                        <span class="colorSwatch__colorLabelText">
                            Color:
                        </span>
                        <span class="colorSwatch__colorLabelValue">
                            Dark Blue
                        </span>
                    </span>
                </li>
            
        

        

        
        
    </ul>

    


    


            
        
            
        

        

    
</div>


                    

                    


    
        <div class="productTileCompare__wrapper" bis_skin_checked="1">
            <label class="productTileCompare__checkbox inputCheckbox js-compareWrapper">
                <input type="checkbox" class="productTileCompare__checkboxInput inputCheckbox__input js-selectCompareProduct" aria-hidden="false" aria-label="Compare" tabindex="0" value="productCompareCheckbox" name="productCompareCheckbox" data-remove-pid-compare="50031313" data-compare-remove-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-RemoveFromCompare?pid=50031313" data-add-to-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-AddToCompare?pid=50031313">
                <span class="productTile__compareCheckboxLabel inputCheckbox__label">
                    


    <svg xmlns:xlink="http://www.w3.org/1999/xlink" class="icon icon-check2 inputCheckbox__icon" aria-hidden="false" focusable="false">
        
        
        
            <use xlink:href="/on/demandware.static/Sites-RoW-Site/-/en_DE/v1703839529785/images/iconsNew.svg#sprite-check2"></use>
        
        
    </svg>


                    <span class="inputCheckbox__labelInner">
                        Compare
                    </span>
                </span>
            </label>
        </div>
    



                </div>

                

                <div class="productTileDefault__productNameWrapper" bis_skin_checked="1">
                    <a title="Aeroad CF SLX 8 Di2" class="productTileDefault__productName link" aria-hidden="false" tabindex="0" href="https://www.canyon.com/en-de/road-bikes/aero-bikes/aeroad/cf-slx/aeroad-cf-slx-8-di2/3955.html?dwvar_3955_pv_rahmenfarbe=BK%2FBK" data-gtm-click="[{&quot;event&quot;:&quot;EEC-productClick&quot;,&quot;ecommerce&quot;:{&quot;click&quot;:{&quot;actionField&quot;:{&quot;list&quot;:&quot;&quot;},&quot;products&quot;:[{&quot;name&quot;:&quot;Aeroad CF SLX 8 Di2&quot;,&quot;id&quot;:&quot;3955&quot;,&quot;brand&quot;:&quot;Canyon&quot;,&quot;category&quot;:&quot;Road Bikes/Aero/Aeroad/Aeroad CF SLX&quot;,&quot;variant&quot;:&quot;&quot;,&quot;dimension50&quot;:&quot;2023&quot;,&quot;dimension52&quot;:&quot;Aeroad&quot;,&quot;dimension63&quot;:&quot;unisex&quot;,&quot;dimension64&quot;:&quot;&quot;,&quot;dimension65&quot;:&quot;ZFER&quot;,&quot;dimension66&quot;:&quot;Complete Bike RR&quot;,&quot;dimension67&quot;:&quot;false&quot;,&quot;dimension68&quot;:&quot;false&quot;,&quot;feedProductId&quot;:&quot;50031322&quot;,&quot;dimension54&quot;:&quot;not defined&quot;,&quot;dimension51&quot;:&quot;Stealth&quot;,&quot;dimension53&quot;:&quot;S | M | L | XL&quot;,&quot;quantity&quot;:&quot;&quot;,&quot;price&quot;:5293.28,&quot;metric4&quot;:6299,&quot;dimension56&quot;:&quot;not defined&quot;}]},&quot;currencyCode&quot;:&quot;EUR&quot;}},{&quot;event&quot;:&quot;select_item&quot;,&quot;event_type&quot;:&quot;ecommerce&quot;,&quot;ecommerce&quot;:{&quot;items&quot;:[{&quot;item_id&quot;:&quot;3955&quot;,&quot;item_name&quot;:&quot;Aeroad CF SLX 8 Di2&quot;,&quot;coupon&quot;:&quot;&quot;,&quot;currency&quot;:&quot;EUR&quot;,&quot;discount&quot;:&quot;&quot;,&quot;item_brand&quot;:&quot;Canyon&quot;,&quot;item_gender&quot;:&quot;Unisex&quot;,&quot;item_category&quot;:&quot;Road Bikes&quot;,&quot;item_category2&quot;:&quot;Aero&quot;,&quot;item_category3&quot;:&quot;Aeroad&quot;,&quot;item_category4&quot;:&quot;Aeroad CF SLX&quot;,&quot;item_color&quot;:&quot;Stealth&quot;,&quot;item_size&quot;:&quot;S | M | L | XL&quot;,&quot;item_availability&quot;:&quot;not defined&quot;,&quot;item_set_origin&quot;:&quot;not defined&quot;,&quot;item_material_type&quot;:&quot;ZFER&quot;,&quot;item_outlet_flag&quot;:&quot;false&quot;,&quot;item_customizing_flag&quot;:&quot;false&quot;,&quot;feedProductId&quot;:&quot;50031322&quot;,&quot;item_variant&quot;:&quot;&quot;,&quot;price&quot;:5293.28,&quot;gross_price&quot;:6299,&quot;quantity&quot;:1}]}}]">
                        Aeroad CF SLX 8 Di2
                        
                    </a>
                </div>

                <div class="productTileDefault__infoWrapper" bis_skin_checked="1">

                    <!-- Additional infos -->

                    

                    
                        <div class="productTileDefault__info productTileDefault__info--highlights" bis_skin_checked="1">
                            DT Swiss ARC 1400 Dicut, Shimano Ultegra Di2 R8150, 12-speed
                        </div>
                    

                    

                    

                    

                    

                    

                    
                </div>
            </div>

            <div class="productTileDefault__productSummaryBottom" bis_skin_checked="1">

                

                <div class="productTileDefault__price" bis_skin_checked="1">
                    


    <div class="productTile__priceSale" bis_skin_checked="1">
        
            
                6.299 €
            
        
    </div>
    
    
        <div class="productTile__priceMonthly" bis_skin_checked="1">
            or from 109,30 €/Mo.
        </div>
    


                </div>

                <!-- Bike Combo Price -->

                

            </div>
        </div>

        
    </div>





                                
                            
                        </li>
        """)

    res = _parse_canyon_catalog(one_bike_tree)

    assert isinstance(res, list)
    assert len(res) == 4
    assert isinstance(res[0], Bike)
    assert res[0].id == 'aeroad_cf_slx_8_di2_s'
    assert res[0].title == 'Aeroad CF SLX 8 Di2'
    assert res[0].link == 'https://www.canyon.com/en-de/road-bikes/aero-bikes/aeroad/cf-slx/aeroad-cf-slx-8-di2/3955.html?dwvar_3955_pv_rahmenfarbe=BK%2FBK'
    assert res[0].family == 'Aeroad'
    assert res[0].model == 'CF SLX 8 Di2'
    assert res[0].size == 'S'


def test_parse_canyon_catalog_few_bikes():
    few_bike_tree = etree.HTML(
        '''<li class="productGrid__listItem xlt-producttile">

<script type="text/javascript">//<!--
/* <![CDATA[ */
(function(){
try {
    if(window.CQuotient) {
	var cq_params = {};
	
	cq_params.cookieId = window.CQuotient.getCQCookieId();
	cq_params.userId = window.CQuotient.getCQUserId();
	cq_params.emailId = CQuotient.getCQHashedEmail();
	cq_params.loginId = CQuotient.getCQHashedLogin();
	cq_params.accumulate = true;
	cq_params.products = [{
	    id: '3117',
	    sku: ''
	}];
	cq_params.categoryId = 'instockbikes';
	cq_params.refinements = '[{\"name\":\"pc_rahmengroesse\",\"value\":\"3XS\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"2XS\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"XS\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"S\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"M\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"L\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"XL\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"2XL\"},{\"name\":\"isInStock\",\"value\":\"true\"},{\"name\":\"isInStock\",\"value\":\"Na Sklad\u011B\"},{\"name\":\"isInStock\",\"value\":\"P\u00E5 Lager\"},{\"name\":\"isInStock\",\"value\":\"Ab Lager\"},{\"name\":\"isInStock\",\"value\":\"In-stock\"},{\"name\":\"isInStock\",\"value\":\"Disponible\"},{\"name\":\"isInStock\",\"value\":\"Varastossa\"},{\"name\":\"isInStock\",\"value\":\"En stock\"},{\"name\":\"isInStock\",\"value\":\"Disponibile\"},{\"name\":\"isInStock\",\"value\":\"\u5728\u5EAB\u3042\u308A\"},{\"name\":\"isInStock\",\"value\":\"\uC7AC\uACE0\uC788\uC74C\"},{\"name\":\"isInStock\",\"value\":\"Op voorraad\"},{\"name\":\"isInStock\",\"value\":\"P\u00E5 lager\"},{\"name\":\"isInStock\",\"value\":\"Em stock\"},{\"name\":\"Category\",\"value\":\"instockbikes\"}]';
	cq_params.personalized = 'false';
	cq_params.sortingRule = 'sort_master_availability';
	cq_params.imageUUID = '__UNDEFINED__';
	cq_params.realm = "BCML";
	cq_params.siteId = "RoW";
	cq_params.instanceType = "prd";
	cq_params.queryLocale = "en";
	cq_params.locale = window.CQuotient.locale;
	
	if(window.CQuotient.sendActivity)
	    window.CQuotient.sendActivity(CQuotient.clientId, 'viewCategory', cq_params);
	else
	    window.CQuotient.activities.push({
	    	activityType: 'viewCategory',
	    	parameters: cq_params
	    });
  }
} catch(err) {}
})();
/* ]]> */
// -->
</script>
<script type="text/javascript">//<!--
/* <![CDATA[ (viewCategoryProduct-active_data.js) */
(function(){
try {
	if (dw.ac) {
		var search_params = {};
		search_params.persd = 'false';
		search_params.refs = '[{\"name\":\"pc_rahmengroesse\",\"value\":\"3XS\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"2XS\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"XS\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"S\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"M\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"L\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"XL\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"2XL\"},{\"name\":\"isInStock\",\"value\":\"true\"},{\"name\":\"isInStock\",\"value\":\"Na Sklad\u011B\"},{\"name\":\"isInStock\",\"value\":\"P\u00E5 Lager\"},{\"name\":\"isInStock\",\"value\":\"Ab Lager\"},{\"name\":\"isInStock\",\"value\":\"In-stock\"},{\"name\":\"isInStock\",\"value\":\"Disponible\"},{\"name\":\"isInStock\",\"value\":\"Varastossa\"},{\"name\":\"isInStock\",\"value\":\"En stock\"},{\"name\":\"isInStock\",\"value\":\"Disponibile\"},{\"name\":\"isInStock\",\"value\":\"\u5728\u5EAB\u3042\u308A\"},{\"name\":\"isInStock\",\"value\":\"\uC7AC\uACE0\uC788\uC74C\"},{\"name\":\"isInStock\",\"value\":\"Op voorraad\"},{\"name\":\"isInStock\",\"value\":\"P\u00E5 lager\"},{\"name\":\"isInStock\",\"value\":\"Em stock\"},{\"name\":\"Category\",\"value\":\"instockbikes\"}]';
		search_params.sort = 'sort_master_availability';
		search_params.imageUUID = '';
		search_params.searchID = 'cce3209f-1eca-4f81-a5ef-19c86ba5ca98';
		search_params.locale = 'en_DE';
		search_params.queryLocale = 'en';
		search_params.showProducts = 'true';
		dw.ac.applyContext({category: "instockbikes", searchData: search_params});
		if (typeof dw.ac._scheduleDataSubmission === "function") {
			dw.ac._scheduleDataSubmission();
		}
	}
} catch(err) {}
})();
/* ]]> */
// -->
</script>
<script type="text/javascript">//<!--
/* <![CDATA[ (viewProduct-active_data.js) */
dw.ac._capture({id: "3117", type: "searchhit"});
/* ]]> */
// -->
</script>
<div data-pid="50015577" class="js-productTileWrapper productTileDefault productTileDefault--bike" data-gtm-impression="[{&quot;event&quot;:&quot;EEC-productImpression&quot;,&quot;ecommerce&quot;:{&quot;currencyCode&quot;:&quot;EUR&quot;,&quot;impressions&quot;:[{&quot;name&quot;:&quot;Spectral:ON CF 7&quot;,&quot;id&quot;:&quot;3117&quot;,&quot;brand&quot;:&quot;Canyon&quot;,&quot;category&quot;:&quot;E-Bikes/E-Mountain/Spectral:ON/Spectral:ON CF&quot;,&quot;variant&quot;:&quot;&quot;,&quot;dimension50&quot;:&quot;2022&quot;,&quot;dimension52&quot;:&quot;Spectral:ON&quot;,&quot;dimension63&quot;:&quot;unisex&quot;,&quot;dimension64&quot;:&quot;&quot;,&quot;dimension65&quot;:&quot;ZFER&quot;,&quot;dimension66&quot;:&quot;CompleteBikeMT EBIKE&quot;,&quot;dimension67&quot;:&quot;false&quot;,&quot;dimension68&quot;:&quot;true&quot;,&quot;feedProductId&quot;:&quot;50015575&quot;,&quot;dimension54&quot;:&quot;not defined&quot;,&quot;dimension51&quot;:&quot;Boundless Grey&quot;,&quot;dimension53&quot;:&quot;M | L | XL&quot;,&quot;quantity&quot;:1,&quot;price&quot;:&quot;&quot;,&quot;metric4&quot;:&quot;&quot;,&quot;dimension56&quot;:&quot;not defined&quot;}]}},{&quot;event&quot;:&quot;view_item_list&quot;,&quot;event_type&quot;:&quot;ecommerce&quot;,&quot;ecommerce&quot;:{&quot;items&quot;:[{&quot;item_id&quot;:&quot;3117&quot;,&quot;item_name&quot;:&quot;Spectral:ON CF 7&quot;,&quot;coupon&quot;:&quot;&quot;,&quot;currency&quot;:&quot;EUR&quot;,&quot;discount&quot;:&quot;&quot;,&quot;item_brand&quot;:&quot;Canyon&quot;,&quot;item_category&quot;:&quot;E-Bikes&quot;,&quot;item_category2&quot;:&quot;E-Mountain&quot;,&quot;item_category3&quot;:&quot;Spectral:ON&quot;,&quot;item_category4&quot;:&quot;Spectral:ON CF&quot;,&quot;item_variant&quot;:&quot;&quot;,&quot;price&quot;:&quot;&quot;,&quot;quantity&quot;:1}]}}]">
<div class="productTileDefault__imageWrapper">
<a title="Spectral:ON CF 7" aria-label="Spectral:ON CF 7 Price: 4.799 €" class="js-productTile productTileDefault__imageLink " href="https://www.canyon.com/en-de/electric-bikes/electric-mountain-bikes/spectral-on/spectral-on-cf/spectral-on-cf-7/3117.html?dwvar_3117_pv_rahmenfarbe=WH" aria-hidden="false" tabindex="0" data-gtm-click="[{&quot;event&quot;:&quot;EEC-productClick&quot;,&quot;ecommerce&quot;:{&quot;click&quot;:{&quot;actionField&quot;:{&quot;list&quot;:&quot;&quot;},&quot;products&quot;:[{&quot;name&quot;:&quot;Spectral:ON CF 7&quot;,&quot;id&quot;:&quot;3117&quot;,&quot;brand&quot;:&quot;Canyon&quot;,&quot;category&quot;:&quot;E-Bikes/E-Mountain/Spectral:ON/Spectral:ON CF&quot;,&quot;variant&quot;:&quot;&quot;,&quot;dimension50&quot;:&quot;2022&quot;,&quot;dimension52&quot;:&quot;Spectral:ON&quot;,&quot;dimension63&quot;:&quot;unisex&quot;,&quot;dimension64&quot;:&quot;&quot;,&quot;dimension65&quot;:&quot;ZFER&quot;,&quot;dimension66&quot;:&quot;CompleteBikeMT EBIKE&quot;,&quot;dimension67&quot;:&quot;false&quot;,&quot;dimension68&quot;:&quot;true&quot;,&quot;feedProductId&quot;:&quot;50015575&quot;,&quot;dimension54&quot;:&quot;not defined&quot;,&quot;dimension51&quot;:&quot;Boundless Grey&quot;,&quot;dimension53&quot;:&quot;M | L | XL&quot;,&quot;quantity&quot;:&quot;&quot;,&quot;price&quot;:&quot;&quot;,&quot;metric4&quot;:&quot;&quot;,&quot;dimension56&quot;:&quot;not defined&quot;}]},&quot;currencyCode&quot;:&quot;EUR&quot;}},{&quot;event&quot;:&quot;select_item&quot;,&quot;event_type&quot;:&quot;ecommerce&quot;,&quot;ecommerce&quot;:{&quot;items&quot;:[{&quot;item_id&quot;:&quot;3117&quot;,&quot;item_name&quot;:&quot;Spectral:ON CF 7&quot;,&quot;coupon&quot;:&quot;&quot;,&quot;currency&quot;:&quot;EUR&quot;,&quot;discount&quot;:&quot;&quot;,&quot;item_brand&quot;:&quot;Canyon&quot;,&quot;item_category&quot;:&quot;E-Bikes&quot;,&quot;item_category2&quot;:&quot;E-Mountain&quot;,&quot;item_category3&quot;:&quot;Spectral:ON&quot;,&quot;item_category4&quot;:&quot;Spectral:ON CF&quot;,&quot;item_variant&quot;:&quot;&quot;,&quot;price&quot;:&quot;&quot;,&quot;quantity&quot;:1}]}}]">
<div class="productTileDefault__pictureWrapper js-noSwatchTileImagesContainer" data-tile-images="[{&quot;title&quot;:&quot;Spectral:ON CF 7&quot;,&quot;alt&quot;:&quot;Spectral:ON CF 7&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.png&quot;},&quot;found&quot;:true}]" data-tile-hover-images="[{&quot;title&quot;:&quot;Spectral:ON CF 7&quot;,&quot;alt&quot;:&quot;Spectral:ON CF 7&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;md&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;},&quot;found&quot;:false}]">
<picture class="picture productTileDefault__picture productTileDefault__picture--main">
<source media="(min-width: 1921px)" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2">
<source media="(min-width: 1440px)" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2">
<source media="(min-width: 1200px)" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2">
<source media="(min-width: 992px)" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2">
<source media="(min-width: 768px)" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2">
<source media="(min-width: 534px)" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2">
<source media="(min-width: 0px)" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2">
<img title="Spectral:ON CF 7" alt="Spectral:ON CF 7" class="picture__image  productTileDefault__image" src="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2" loading="lazy">
</picture>
</div>
</a>
<div class="productTileDefault__awardAndBadges">
<div class="productTileDefault__badges">
<ul class="productBadges__list">
<li class="productBadges__listItem productBadges__listItem--availability">
<div class="productBadge productBadge--availability" bis_skin_checked="1">
Available to buy in M | L | XL
                </div>
</li>
</ul>
</div>
<div class="productTileDefault__award">

</div>
</div>
</div>
<div class="productTileDefault__productSummary">
<div class="productTileDefault__productSummaryTop">
<div class="productTileDefault__colorsAndCompare">
<div class="colorPicker__wrapper colorPicker__wrapper--showOptionalPlusIndicator">
<ul class="js-colorPicker colorPicker colorPicker--colorCount--3 colorPicker--showOptionalPlusIndicator  ">
<li class="colorPicker__colorListItem ">
<button aria-hidden="false" aria-label="Stealth" class="colorSwatch colorSwatch--button colorSwatch--small  js-color-swatch  colorPicker__colorSwatch" tabindex="0" data-url="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_DE/Product-Variation?dwvar_3117_pv_rahmenfarbe=BK&amp;pid=3117&amp;quantity=undefined&amp;imageupdate=color" data-displayvalue="Stealth" data-tile-images="[{&quot;title&quot;:&quot;Spectral:ON CF 7&quot;,&quot;alt&quot;:&quot;Spectral:ON CF 7&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw98cdce4c/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_bk-bk_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw98cdce4c/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_bk-bk_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw98cdce4c/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_bk-bk_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw98cdce4c/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_bk-bk_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw98cdce4c/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_bk-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw98cdce4c/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_bk-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw98cdce4c/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_bk-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dw98cdce4c/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_bk-bk_P5.png&quot;},&quot;found&quot;:true}]" data-tile-hover-images="[{&quot;title&quot;:&quot;Stealth&quot;,&quot;alt&quot;:&quot;Stealth&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;md&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;},&quot;found&quot;:false}]" data-pdp-url="https://www.canyon.com/en-de/electric-bikes/electric-mountain-bikes/spectral-on/spectral-on-cf/spectral-on-cf-7/3117.html?dwvar_3117_pv_rahmenfarbe=BK" data-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-AddToCompare?pid=50015568" data-remove-from-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-RemoveFromCompare?pid=50015568" data-compare-pid="50015568" title="Stealth" data-quickaddurl="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_DE/Tile-Variation?pid=3117&amp;dwvar_3117_pv_rahmenfarbe=BK" type="button">
<span class="colorSwatch__colorWrapper">
<span class="colorSwatch__color" style="color:#6e6e6e;"></span>
<span class="colorSwatch__color" style="color:#030303;"></span>
</span>
</button>
<span class="colorSwatch__colorLabel" role="tooltip">
<span class="colorSwatch__colorLabelText">
Color:
</span>
<span class="colorSwatch__colorLabelValue">
Stealth
</span>
</span>
</li>
<li class="colorPicker__colorListItem ">
<button aria-hidden="false" aria-label="Infinit Red" class="colorSwatch colorSwatch--button colorSwatch--small  js-color-swatch  colorPicker__colorSwatch" tabindex="0" data-url="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_DE/Product-Variation?dwvar_3117_pv_rahmenfarbe=VT&amp;pid=3117&amp;quantity=undefined&amp;imageupdate=color" data-displayvalue="Infinit Red" data-tile-images="[{&quot;title&quot;:&quot;Spectral:ON CF 7&quot;,&quot;alt&quot;:&quot;Spectral:ON CF 7&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.png&quot;},&quot;found&quot;:true}]" data-tile-hover-images="[{&quot;title&quot;:&quot;Infinit Red&quot;,&quot;alt&quot;:&quot;Infinit Red&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;md&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;},&quot;found&quot;:false}]" data-pdp-url="https://www.canyon.com/en-de/electric-bikes/electric-mountain-bikes/spectral-on/spectral-on-cf/spectral-on-cf-7/3117.html?dwvar_3117_pv_rahmenfarbe=VT" data-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-AddToCompare?pid=50015572" data-remove-from-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-RemoveFromCompare?pid=50015572" data-compare-pid="50015572" title="Infinit Red" data-quickaddurl="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_DE/Tile-Variation?pid=3117&amp;dwvar_3117_pv_rahmenfarbe=VT" type="button">
<span class="colorSwatch__colorWrapper">
<span class="colorSwatch__color" style="color:#a39393;"></span>
<span class="colorSwatch__color" style="color:#724d4d;"></span>
</span>
</button>
<span class="colorSwatch__colorLabel" role="tooltip">
<span class="colorSwatch__colorLabelText">
Color:
</span>
<span class="colorSwatch__colorLabelValue">
Infinit Red
</span>
</span>
</li>
<li class="colorPicker__colorListItem ">
<button aria-hidden="false" aria-label="Boundless Grey" class="colorSwatch colorSwatch--button colorSwatch--small colorSwatch--selected js-noGtmClick js-color-swatch  colorPicker__colorSwatch" tabindex="0" data-url="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_DE/Product-Variation?dwvar_3117_pv_rahmenfarbe=&amp;pid=3117&amp;quantity=undefined&amp;imageupdate=color" data-displayvalue="Boundless Grey" data-selected-color-value="WH" data-tile-images="[{&quot;title&quot;:&quot;Spectral:ON CF 7&quot;,&quot;alt&quot;:&quot;Spectral:ON CF 7&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.png&quot;},&quot;found&quot;:true}]" data-tile-hover-images="[{&quot;title&quot;:&quot;Boundless Grey&quot;,&quot;alt&quot;:&quot;Boundless Grey&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;md&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;},&quot;found&quot;:false}]" data-pdp-url="https://www.canyon.com/en-de/electric-bikes/electric-mountain-bikes/spectral-on/spectral-on-cf/spectral-on-cf-7/3117.html?dwvar_3117_pv_rahmenfarbe=WH" data-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-AddToCompare?pid=50015576" data-remove-from-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-RemoveFromCompare?pid=50015576" data-compare-pid="50015576" title="Boundless Grey" data-quickaddurl="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_DE/Tile-Variation?pid=3117&amp;dwvar_3117_pv_rahmenfarbe=WH" type="button">
<span class="colorSwatch__colorWrapper">
<span class="colorSwatch__color" style="color:#ececec;"></span>
</span>
</button>
<span class="colorSwatch__colorLabel" role="tooltip">
<span class="colorSwatch__colorLabelText">
Color:
</span>
<span class="colorSwatch__colorLabelValue">
Boundless Grey
</span>
</span>
</li>
<li class="colorPicker__colorListPlusItems">

</li>
</ul>
</div>
<div class="productTileCompare__wrapper">
<label class="productTileCompare__checkbox inputCheckbox js-compareWrapper">
<input type="checkbox" class="productTileCompare__checkboxInput inputCheckbox__input js-selectCompareProduct" aria-hidden="false" aria-label="Compare" tabindex="0" value="productCompareCheckbox" name="productCompareCheckbox" data-remove-pid-compare="50015577" data-compare-remove-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-RemoveFromCompare?pid=50015577" data-add-to-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-AddToCompare?pid=50015577">
<span class="productTile__compareCheckboxLabel inputCheckbox__label">
<svg xmlns:xlink="http://www.w3.org/1999/xlink" class="icon icon-check2 inputCheckbox__icon" aria-hidden="false" focusable="false">
<use xlink:href="/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/iconsNew.svg#sprite-check2"></use>
</svg>
<span class="inputCheckbox__labelInner">
Compare
</span>
</span>
</label>
</div>
</div>
<div class="productTileDefault__productNameWrapper">
<a title="Spectral:ON CF 7" class="productTileDefault__productName link " href="https://www.canyon.com/en-de/electric-bikes/electric-mountain-bikes/spectral-on/spectral-on-cf/spectral-on-cf-7/3117.html?dwvar_3117_pv_rahmenfarbe=WH" aria-hidden="false" tabindex="0" data-gtm-click="[{&quot;event&quot;:&quot;EEC-productClick&quot;,&quot;ecommerce&quot;:{&quot;click&quot;:{&quot;actionField&quot;:{&quot;list&quot;:&quot;&quot;},&quot;products&quot;:[{&quot;name&quot;:&quot;Spectral:ON CF 7&quot;,&quot;id&quot;:&quot;3117&quot;,&quot;brand&quot;:&quot;Canyon&quot;,&quot;category&quot;:&quot;E-Bikes/E-Mountain/Spectral:ON/Spectral:ON CF&quot;,&quot;variant&quot;:&quot;&quot;,&quot;dimension50&quot;:&quot;2022&quot;,&quot;dimension52&quot;:&quot;Spectral:ON&quot;,&quot;dimension63&quot;:&quot;unisex&quot;,&quot;dimension64&quot;:&quot;&quot;,&quot;dimension65&quot;:&quot;ZFER&quot;,&quot;dimension66&quot;:&quot;CompleteBikeMT EBIKE&quot;,&quot;dimension67&quot;:&quot;false&quot;,&quot;dimension68&quot;:&quot;true&quot;,&quot;feedProductId&quot;:&quot;50015575&quot;,&quot;dimension54&quot;:&quot;not defined&quot;,&quot;dimension51&quot;:&quot;Boundless Grey&quot;,&quot;dimension53&quot;:&quot;M | L | XL&quot;,&quot;quantity&quot;:&quot;&quot;,&quot;price&quot;:&quot;&quot;,&quot;metric4&quot;:&quot;&quot;,&quot;dimension56&quot;:&quot;not defined&quot;}]},&quot;currencyCode&quot;:&quot;EUR&quot;}},{&quot;event&quot;:&quot;select_item&quot;,&quot;event_type&quot;:&quot;ecommerce&quot;,&quot;ecommerce&quot;:{&quot;items&quot;:[{&quot;item_id&quot;:&quot;3117&quot;,&quot;item_name&quot;:&quot;Spectral:ON CF 7&quot;,&quot;coupon&quot;:&quot;&quot;,&quot;currency&quot;:&quot;EUR&quot;,&quot;discount&quot;:&quot;&quot;,&quot;item_brand&quot;:&quot;Canyon&quot;,&quot;item_category&quot;:&quot;E-Bikes&quot;,&quot;item_category2&quot;:&quot;E-Mountain&quot;,&quot;item_category3&quot;:&quot;Spectral:ON&quot;,&quot;item_category4&quot;:&quot;Spectral:ON CF&quot;,&quot;item_variant&quot;:&quot;&quot;,&quot;price&quot;:&quot;&quot;,&quot;quantity&quot;:1}]}}]">
Spectral:ON CF 7
</a>
</div>
<div class="productTileDefault__infoWrapper">

<div class="productTileDefault__info productTileDefault__info--highlights">
Shimano Steps EP8 Motor, Rock Shox Lyrik Select
</div>
</div>
</div>
<div class="productTileDefault__productSummaryBottom">
<div class="productTileDefault__price">
<div class="productTile__priceSale">
From 4.799 €
</div>
<div class="productTile__priceMonthly">
or from 74,71 €/Mo.
</div>
</div>


</div>
</div>
</div>
</li>
<li class="productGrid__listItem xlt-producttile">

<script type="text/javascript">//<!--
/* <![CDATA[ */
(function(){
try {
    if(window.CQuotient) {
	var cq_params = {};
	
	cq_params.cookieId = window.CQuotient.getCQCookieId();
	cq_params.userId = window.CQuotient.getCQUserId();
	cq_params.emailId = CQuotient.getCQHashedEmail();
	cq_params.loginId = CQuotient.getCQHashedLogin();
	cq_params.accumulate = true;
	cq_params.products = [{
	    id: '3123',
	    sku: ''
	}];
	cq_params.categoryId = 'instockbikes';
	cq_params.refinements = '[{\"name\":\"pc_rahmengroesse\",\"value\":\"3XS\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"2XS\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"XS\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"S\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"M\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"L\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"XL\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"2XL\"},{\"name\":\"isInStock\",\"value\":\"true\"},{\"name\":\"isInStock\",\"value\":\"Na Sklad\u011B\"},{\"name\":\"isInStock\",\"value\":\"P\u00E5 Lager\"},{\"name\":\"isInStock\",\"value\":\"Ab Lager\"},{\"name\":\"isInStock\",\"value\":\"In-stock\"},{\"name\":\"isInStock\",\"value\":\"Disponible\"},{\"name\":\"isInStock\",\"value\":\"Varastossa\"},{\"name\":\"isInStock\",\"value\":\"En stock\"},{\"name\":\"isInStock\",\"value\":\"Disponibile\"},{\"name\":\"isInStock\",\"value\":\"\u5728\u5EAB\u3042\u308A\"},{\"name\":\"isInStock\",\"value\":\"\uC7AC\uACE0\uC788\uC74C\"},{\"name\":\"isInStock\",\"value\":\"Op voorraad\"},{\"name\":\"isInStock\",\"value\":\"P\u00E5 lager\"},{\"name\":\"isInStock\",\"value\":\"Em stock\"},{\"name\":\"Category\",\"value\":\"instockbikes\"}]';
	cq_params.personalized = 'false';
	cq_params.sortingRule = 'sort_master_availability';
	cq_params.imageUUID = '__UNDEFINED__';
	cq_params.realm = "BCML";
	cq_params.siteId = "RoW";
	cq_params.instanceType = "prd";
	cq_params.queryLocale = "en";
	cq_params.locale = window.CQuotient.locale;
	
	if(window.CQuotient.sendActivity)
	    window.CQuotient.sendActivity(CQuotient.clientId, 'viewCategory', cq_params);
	else
	    window.CQuotient.activities.push({
	    	activityType: 'viewCategory',
	    	parameters: cq_params
	    });
  }
} catch(err) {}
})();
/* ]]> */
// -->
</script>
<script type="text/javascript">//<!--
/* <![CDATA[ (viewCategoryProduct-active_data.js) */
(function(){
try {
	if (dw.ac) {
		var search_params = {};
		search_params.persd = 'false';
		search_params.refs = '[{\"name\":\"pc_rahmengroesse\",\"value\":\"3XS\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"2XS\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"XS\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"S\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"M\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"L\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"XL\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"2XL\"},{\"name\":\"isInStock\",\"value\":\"true\"},{\"name\":\"isInStock\",\"value\":\"Na Sklad\u011B\"},{\"name\":\"isInStock\",\"value\":\"P\u00E5 Lager\"},{\"name\":\"isInStock\",\"value\":\"Ab Lager\"},{\"name\":\"isInStock\",\"value\":\"In-stock\"},{\"name\":\"isInStock\",\"value\":\"Disponible\"},{\"name\":\"isInStock\",\"value\":\"Varastossa\"},{\"name\":\"isInStock\",\"value\":\"En stock\"},{\"name\":\"isInStock\",\"value\":\"Disponibile\"},{\"name\":\"isInStock\",\"value\":\"\u5728\u5EAB\u3042\u308A\"},{\"name\":\"isInStock\",\"value\":\"\uC7AC\uACE0\uC788\uC74C\"},{\"name\":\"isInStock\",\"value\":\"Op voorraad\"},{\"name\":\"isInStock\",\"value\":\"P\u00E5 lager\"},{\"name\":\"isInStock\",\"value\":\"Em stock\"},{\"name\":\"Category\",\"value\":\"instockbikes\"}]';
		search_params.sort = 'sort_master_availability';
		search_params.imageUUID = '';
		search_params.searchID = 'cce3209f-1eca-4f81-a5ef-19c86ba5ca98';
		search_params.locale = 'en_DE';
		search_params.queryLocale = 'en';
		search_params.showProducts = 'true';
		dw.ac.applyContext({category: "instockbikes", searchData: search_params});
		if (typeof dw.ac._scheduleDataSubmission === "function") {
			dw.ac._scheduleDataSubmission();
		}
	}
} catch(err) {}
})();
/* ]]> */
// -->
</script>
<script type="text/javascript">//<!--
/* <![CDATA[ (viewProduct-active_data.js) */
dw.ac._capture({id: "3123", type: "searchhit"});
/* ]]> */
// -->
</script>
<div data-pid="50016127" class="js-productTileWrapper productTileDefault productTileDefault--bike" data-gtm-impression="[{&quot;event&quot;:&quot;EEC-productImpression&quot;,&quot;ecommerce&quot;:{&quot;currencyCode&quot;:&quot;EUR&quot;,&quot;impressions&quot;:[{&quot;name&quot;:&quot;Grand Canyon:ON 8&quot;,&quot;id&quot;:&quot;3123&quot;,&quot;brand&quot;:&quot;Canyon&quot;,&quot;category&quot;:&quot;E-Bikes/E-Mountain/Grand Canyon:ON&quot;,&quot;variant&quot;:&quot;&quot;,&quot;dimension50&quot;:&quot;2022&quot;,&quot;dimension52&quot;:&quot;Grand Canyon:ON&quot;,&quot;dimension63&quot;:&quot;unisex&quot;,&quot;dimension64&quot;:&quot;&quot;,&quot;dimension65&quot;:&quot;ZFER&quot;,&quot;dimension66&quot;:&quot;CompleteBikeMT EBIKE&quot;,&quot;dimension67&quot;:&quot;false&quot;,&quot;dimension68&quot;:&quot;true&quot;,&quot;feedProductId&quot;:&quot;50015638&quot;,&quot;dimension54&quot;:&quot;not defined&quot;,&quot;dimension51&quot;:&quot;Pale Concrete&quot;,&quot;dimension53&quot;:&quot;S | M | L | XL | XS&quot;,&quot;quantity&quot;:1,&quot;price&quot;:&quot;&quot;,&quot;metric4&quot;:&quot;&quot;,&quot;dimension56&quot;:&quot;not defined&quot;}]}},{&quot;event&quot;:&quot;view_item_list&quot;,&quot;event_type&quot;:&quot;ecommerce&quot;,&quot;ecommerce&quot;:{&quot;items&quot;:[{&quot;item_id&quot;:&quot;3123&quot;,&quot;item_name&quot;:&quot;Grand Canyon:ON 8&quot;,&quot;coupon&quot;:&quot;&quot;,&quot;currency&quot;:&quot;EUR&quot;,&quot;discount&quot;:&quot;&quot;,&quot;item_brand&quot;:&quot;Canyon&quot;,&quot;item_category&quot;:&quot;E-Bikes&quot;,&quot;item_category2&quot;:&quot;E-Mountain&quot;,&quot;item_category3&quot;:&quot;Grand Canyon:ON&quot;,&quot;item_variant&quot;:&quot;&quot;,&quot;price&quot;:&quot;&quot;,&quot;quantity&quot;:1}]}}]">
<div class="productTileDefault__imageWrapper">
<a title="Grand Canyon:ON 8" aria-label="Grand Canyon:ON 8 Price: 2.999 €" class="js-productTile productTileDefault__imageLink " href="https://www.canyon.com/en-de/electric-bikes/electric-mountain-bikes/grandcanyon-on/grand-canyon-on-8/3123.html?dwvar_3123_pv_rahmenfarbe=GY" aria-hidden="false" tabindex="0" data-gtm-click="[{&quot;event&quot;:&quot;EEC-productClick&quot;,&quot;ecommerce&quot;:{&quot;click&quot;:{&quot;actionField&quot;:{&quot;list&quot;:&quot;&quot;},&quot;products&quot;:[{&quot;name&quot;:&quot;Grand Canyon:ON 8&quot;,&quot;id&quot;:&quot;3123&quot;,&quot;brand&quot;:&quot;Canyon&quot;,&quot;category&quot;:&quot;E-Bikes/E-Mountain/Grand Canyon:ON&quot;,&quot;variant&quot;:&quot;&quot;,&quot;dimension50&quot;:&quot;2022&quot;,&quot;dimension52&quot;:&quot;Grand Canyon:ON&quot;,&quot;dimension63&quot;:&quot;unisex&quot;,&quot;dimension64&quot;:&quot;&quot;,&quot;dimension65&quot;:&quot;ZFER&quot;,&quot;dimension66&quot;:&quot;CompleteBikeMT EBIKE&quot;,&quot;dimension67&quot;:&quot;false&quot;,&quot;dimension68&quot;:&quot;true&quot;,&quot;feedProductId&quot;:&quot;50015638&quot;,&quot;dimension54&quot;:&quot;not defined&quot;,&quot;dimension51&quot;:&quot;Pale Concrete&quot;,&quot;dimension53&quot;:&quot;S | M | L | XL | XS&quot;,&quot;quantity&quot;:&quot;&quot;,&quot;price&quot;:&quot;&quot;,&quot;metric4&quot;:&quot;&quot;,&quot;dimension56&quot;:&quot;not defined&quot;}]},&quot;currencyCode&quot;:&quot;EUR&quot;}},{&quot;event&quot;:&quot;select_item&quot;,&quot;event_type&quot;:&quot;ecommerce&quot;,&quot;ecommerce&quot;:{&quot;items&quot;:[{&quot;item_id&quot;:&quot;3123&quot;,&quot;item_name&quot;:&quot;Grand Canyon:ON 8&quot;,&quot;coupon&quot;:&quot;&quot;,&quot;currency&quot;:&quot;EUR&quot;,&quot;discount&quot;:&quot;&quot;,&quot;item_brand&quot;:&quot;Canyon&quot;,&quot;item_category&quot;:&quot;E-Bikes&quot;,&quot;item_category2&quot;:&quot;E-Mountain&quot;,&quot;item_category3&quot;:&quot;Grand Canyon:ON&quot;,&quot;item_variant&quot;:&quot;&quot;,&quot;price&quot;:&quot;&quot;,&quot;quantity&quot;:1}]}}]">
<div class="productTileDefault__pictureWrapper js-noSwatchTileImagesContainer" data-tile-images="[{&quot;title&quot;:&quot;Grand Canyon:ON 8&quot;,&quot;alt&quot;:&quot;Grand Canyon:ON 8&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwe26e7ff4/images/full/full_2023_/2022/full_2023_grand-canyon-on-8_3123_gy-gy_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwe26e7ff4/images/full/full_2023_/2022/full_2023_grand-canyon-on-8_3123_gy-gy_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwe26e7ff4/images/full/full_2023_/2022/full_2023_grand-canyon-on-8_3123_gy-gy_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwe26e7ff4/images/full/full_2023_/2022/full_2023_grand-canyon-on-8_3123_gy-gy_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwe26e7ff4/images/full/full_2023_/2022/full_2023_grand-canyon-on-8_3123_gy-gy_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwe26e7ff4/images/full/full_2023_/2022/full_2023_grand-canyon-on-8_3123_gy-gy_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwe26e7ff4/images/full/full_2023_/2022/full_2023_grand-canyon-on-8_3123_gy-gy_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dwe26e7ff4/images/full/full_2023_/2022/full_2023_grand-canyon-on-8_3123_gy-gy_P5.png&quot;},&quot;found&quot;:true}]" data-tile-hover-images="[{&quot;title&quot;:&quot;Grand Canyon:ON 8&quot;,&quot;alt&quot;:&quot;Grand Canyon:ON 8&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;md&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;},&quot;found&quot;:false}]">
<picture class="picture productTileDefault__picture productTileDefault__picture--main">
<source media="(min-width: 1921px)" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwe26e7ff4/images/full/full_2023_/2022/full_2023_grand-canyon-on-8_3123_gy-gy_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2">
<source media="(min-width: 1440px)" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwe26e7ff4/images/full/full_2023_/2022/full_2023_grand-canyon-on-8_3123_gy-gy_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2">
<source media="(min-width: 1200px)" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwe26e7ff4/images/full/full_2023_/2022/full_2023_grand-canyon-on-8_3123_gy-gy_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2">
<source media="(min-width: 992px)" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwe26e7ff4/images/full/full_2023_/2022/full_2023_grand-canyon-on-8_3123_gy-gy_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2">
<source media="(min-width: 768px)" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwe26e7ff4/images/full/full_2023_/2022/full_2023_grand-canyon-on-8_3123_gy-gy_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2">
<source media="(min-width: 534px)" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwe26e7ff4/images/full/full_2023_/2022/full_2023_grand-canyon-on-8_3123_gy-gy_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2">
<source media="(min-width: 0px)" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwe26e7ff4/images/full/full_2023_/2022/full_2023_grand-canyon-on-8_3123_gy-gy_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2">
<img title="Grand Canyon:ON 8" alt="Grand Canyon:ON 8" class="picture__image  productTileDefault__image" src="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwe26e7ff4/images/full/full_2023_/2022/full_2023_grand-canyon-on-8_3123_gy-gy_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2" loading="lazy">
</picture>
</div>
</a>
<div class="productTileDefault__awardAndBadges">
<div class="productTileDefault__badges">
<ul class="productBadges__list">
<li class="productBadges__listItem productBadges__listItem--availability">
<div class="productBadge productBadge--availability" bis_skin_checked="1">
Available to buy in S | M | L | XL | XS
                </div>
</li>
</ul>
</div>
<div class="productTileDefault__award">

</div>
</div>
</div>
<div class="productTileDefault__productSummary">
<div class="productTileDefault__productSummaryTop">
<div class="productTileDefault__colorsAndCompare">
<div class="colorPicker__wrapper colorPicker__wrapper--showOptionalPlusIndicator">
<ul class="js-colorPicker colorPicker colorPicker--colorCount--3 colorPicker--showOptionalPlusIndicator  ">
<li class="colorPicker__colorListItem ">
<button aria-hidden="false" aria-label="Stealth" class="colorSwatch colorSwatch--button colorSwatch--small  js-color-swatch  colorPicker__colorSwatch" tabindex="0" data-url="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_DE/Product-Variation?dwvar_3123_pv_rahmenfarbe=BK&amp;pid=3123&amp;quantity=undefined&amp;imageupdate=color" data-displayvalue="Stealth" data-tile-images="[{&quot;title&quot;:&quot;Grand Canyon:ON 8&quot;,&quot;alt&quot;:&quot;Grand Canyon:ON 8&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwa7c04261/images/full/full_2023_/2022/full_2023_grand-canyon-on-9_3123_bk-bk_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwa7c04261/images/full/full_2023_/2022/full_2023_grand-canyon-on-9_3123_bk-bk_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwa7c04261/images/full/full_2023_/2022/full_2023_grand-canyon-on-9_3123_bk-bk_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwa7c04261/images/full/full_2023_/2022/full_2023_grand-canyon-on-9_3123_bk-bk_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwa7c04261/images/full/full_2023_/2022/full_2023_grand-canyon-on-9_3123_bk-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwa7c04261/images/full/full_2023_/2022/full_2023_grand-canyon-on-9_3123_bk-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwa7c04261/images/full/full_2023_/2022/full_2023_grand-canyon-on-9_3123_bk-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dwa7c04261/images/full/full_2023_/2022/full_2023_grand-canyon-on-9_3123_bk-bk_P5.png&quot;},&quot;found&quot;:true}]" data-tile-hover-images="[{&quot;title&quot;:&quot;Stealth&quot;,&quot;alt&quot;:&quot;Stealth&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;md&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;},&quot;found&quot;:false}]" data-pdp-url="https://www.canyon.com/en-de/electric-bikes/electric-mountain-bikes/grandcanyon-on/grand-canyon-on-8/3123.html?dwvar_3123_pv_rahmenfarbe=BK" data-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-AddToCompare?pid=50015635" data-remove-from-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-RemoveFromCompare?pid=50015635" data-compare-pid="50015635" title="Stealth" data-quickaddurl="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_DE/Tile-Variation?pid=3123&amp;dwvar_3123_pv_rahmenfarbe=BK" type="button">
<span class="colorSwatch__colorWrapper">
<span class="colorSwatch__color" style="color:#6e6e6e;"></span>
<span class="colorSwatch__color" style="color:#030303;"></span>
</span>
</button>
<span class="colorSwatch__colorLabel" role="tooltip">
<span class="colorSwatch__colorLabelText">
Color:
</span>
<span class="colorSwatch__colorLabelValue">
Stealth
</span>
</span>
</li>
<li class="colorPicker__colorListItem ">
<button aria-hidden="false" aria-label="Pale Concrete" class="colorSwatch colorSwatch--button colorSwatch--small colorSwatch--selected js-noGtmClick js-color-swatch  colorPicker__colorSwatch" tabindex="0" data-url="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_DE/Product-Variation?dwvar_3123_pv_rahmenfarbe=&amp;pid=3123&amp;quantity=undefined&amp;imageupdate=color" data-displayvalue="Pale Concrete" data-selected-color-value="GY" data-tile-images="[{&quot;title&quot;:&quot;Grand Canyon:ON 8&quot;,&quot;alt&quot;:&quot;Grand Canyon:ON 8&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwe26e7ff4/images/full/full_2023_/2022/full_2023_grand-canyon-on-8_3123_gy-gy_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwe26e7ff4/images/full/full_2023_/2022/full_2023_grand-canyon-on-8_3123_gy-gy_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwe26e7ff4/images/full/full_2023_/2022/full_2023_grand-canyon-on-8_3123_gy-gy_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwe26e7ff4/images/full/full_2023_/2022/full_2023_grand-canyon-on-8_3123_gy-gy_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwe26e7ff4/images/full/full_2023_/2022/full_2023_grand-canyon-on-8_3123_gy-gy_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwe26e7ff4/images/full/full_2023_/2022/full_2023_grand-canyon-on-8_3123_gy-gy_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwe26e7ff4/images/full/full_2023_/2022/full_2023_grand-canyon-on-8_3123_gy-gy_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dwe26e7ff4/images/full/full_2023_/2022/full_2023_grand-canyon-on-8_3123_gy-gy_P5.png&quot;},&quot;found&quot;:true}]" data-tile-hover-images="[{&quot;title&quot;:&quot;Pale Concrete&quot;,&quot;alt&quot;:&quot;Pale Concrete&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;md&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;},&quot;found&quot;:false}]" data-pdp-url="https://www.canyon.com/en-de/electric-bikes/electric-mountain-bikes/grandcanyon-on/grand-canyon-on-8/3123.html?dwvar_3123_pv_rahmenfarbe=GY" data-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-AddToCompare?pid=50015639" data-remove-from-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-RemoveFromCompare?pid=50015639" data-compare-pid="50015639" title="Pale Concrete" data-quickaddurl="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_DE/Tile-Variation?pid=3123&amp;dwvar_3123_pv_rahmenfarbe=GY" type="button">
<span class="colorSwatch__colorWrapper">
<span class="colorSwatch__color" style="color:#b0b3b8;"></span>
<span class="colorSwatch__color" style="color:#dddee2;"></span>
</span>
</button>
<span class="colorSwatch__colorLabel" role="tooltip">
<span class="colorSwatch__colorLabelText">
Color:
</span>
<span class="colorSwatch__colorLabelValue">
Pale Concrete
</span>
</span>
</li>
<li class="colorPicker__colorListItem ">
<button aria-hidden="false" aria-label="Milky Terracotta" class="colorSwatch colorSwatch--button colorSwatch--small  js-color-swatch  colorPicker__colorSwatch" tabindex="0" data-url="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_DE/Product-Variation?dwvar_3123_pv_rahmenfarbe=RD%2FRD&amp;pid=3123&amp;quantity=undefined&amp;imageupdate=color" data-displayvalue="Milky Terracotta" data-tile-images="[{&quot;title&quot;:&quot;Grand Canyon:ON 8&quot;,&quot;alt&quot;:&quot;Grand Canyon:ON 8&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw50435ec6/images/full/full_2023_/2022/full_2023_grand-canyon-on-8_3123_rd-rd_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw50435ec6/images/full/full_2023_/2022/full_2023_grand-canyon-on-8_3123_rd-rd_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw50435ec6/images/full/full_2023_/2022/full_2023_grand-canyon-on-8_3123_rd-rd_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw50435ec6/images/full/full_2023_/2022/full_2023_grand-canyon-on-8_3123_rd-rd_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw50435ec6/images/full/full_2023_/2022/full_2023_grand-canyon-on-8_3123_rd-rd_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw50435ec6/images/full/full_2023_/2022/full_2023_grand-canyon-on-8_3123_rd-rd_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw50435ec6/images/full/full_2023_/2022/full_2023_grand-canyon-on-8_3123_rd-rd_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dw50435ec6/images/full/full_2023_/2022/full_2023_grand-canyon-on-8_3123_rd-rd_P5.png&quot;},&quot;found&quot;:true}]" data-tile-hover-images="[{&quot;title&quot;:&quot;Milky Terracotta&quot;,&quot;alt&quot;:&quot;Milky Terracotta&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;md&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/noimage.svg&quot;},&quot;found&quot;:false}]" data-pdp-url="https://www.canyon.com/en-de/electric-bikes/electric-mountain-bikes/grandcanyon-on/grand-canyon-on-8/3123.html?dwvar_3123_pv_rahmenfarbe=RD%2FRD" data-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-AddToCompare?pid=50015643" data-remove-from-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-RemoveFromCompare?pid=50015643" data-compare-pid="50015643" title="Milky Terracotta" data-quickaddurl="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_DE/Tile-Variation?pid=3123&amp;dwvar_3123_pv_rahmenfarbe=RD%2fRD" type="button">
<span class="colorSwatch__colorWrapper">
<span class="colorSwatch__color" style="color:#a26d75;"></span>
<span class="colorSwatch__color" style="color:#bd898b;"></span>
</span>
</button>
<span class="colorSwatch__colorLabel" role="tooltip">
<span class="colorSwatch__colorLabelText">
Color:
</span>
<span class="colorSwatch__colorLabelValue">
Milky Terracotta
</span>
</span>
</li>
<li class="colorPicker__colorListPlusItems">

</li>
</ul>
</div>
<div class="productTileCompare__wrapper">
<label class="productTileCompare__checkbox inputCheckbox js-compareWrapper">
<input type="checkbox" class="productTileCompare__checkboxInput inputCheckbox__input js-selectCompareProduct" aria-hidden="false" aria-label="Compare" tabindex="0" value="productCompareCheckbox" name="productCompareCheckbox" data-remove-pid-compare="50016127" data-compare-remove-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-RemoveFromCompare?pid=50016127" data-add-to-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-AddToCompare?pid=50016127">
<span class="productTile__compareCheckboxLabel inputCheckbox__label">
<svg xmlns:xlink="http://www.w3.org/1999/xlink" class="icon icon-check2 inputCheckbox__icon" aria-hidden="false" focusable="false">
<use xlink:href="/on/demandware.static/Sites-RoW-Site/-/en_DE/v1683410547481/images/iconsNew.svg#sprite-check2"></use>
</svg>
<span class="inputCheckbox__labelInner">
Compare
</span>
</span>
</label>
</div>
</div>
<div class="productTileDefault__productNameWrapper">
<a title="Grand Canyon:ON 8" class="productTileDefault__productName link " href="https://www.canyon.com/en-de/electric-bikes/electric-mountain-bikes/grandcanyon-on/grand-canyon-on-8/3123.html?dwvar_3123_pv_rahmenfarbe=GY" aria-hidden="false" tabindex="0" data-gtm-click="[{&quot;event&quot;:&quot;EEC-productClick&quot;,&quot;ecommerce&quot;:{&quot;click&quot;:{&quot;actionField&quot;:{&quot;list&quot;:&quot;&quot;},&quot;products&quot;:[{&quot;name&quot;:&quot;Grand Canyon:ON 8&quot;,&quot;id&quot;:&quot;3123&quot;,&quot;brand&quot;:&quot;Canyon&quot;,&quot;category&quot;:&quot;E-Bikes/E-Mountain/Grand Canyon:ON&quot;,&quot;variant&quot;:&quot;&quot;,&quot;dimension50&quot;:&quot;2022&quot;,&quot;dimension52&quot;:&quot;Grand Canyon:ON&quot;,&quot;dimension63&quot;:&quot;unisex&quot;,&quot;dimension64&quot;:&quot;&quot;,&quot;dimension65&quot;:&quot;ZFER&quot;,&quot;dimension66&quot;:&quot;CompleteBikeMT EBIKE&quot;,&quot;dimension67&quot;:&quot;false&quot;,&quot;dimension68&quot;:&quot;true&quot;,&quot;feedProductId&quot;:&quot;50015638&quot;,&quot;dimension54&quot;:&quot;not defined&quot;,&quot;dimension51&quot;:&quot;Pale Concrete&quot;,&quot;dimension53&quot;:&quot;S | M | L | XL | XS&quot;,&quot;quantity&quot;:&quot;&quot;,&quot;price&quot;:&quot;&quot;,&quot;metric4&quot;:&quot;&quot;,&quot;dimension56&quot;:&quot;not defined&quot;}]},&quot;currencyCode&quot;:&quot;EUR&quot;}},{&quot;event&quot;:&quot;select_item&quot;,&quot;event_type&quot;:&quot;ecommerce&quot;,&quot;ecommerce&quot;:{&quot;items&quot;:[{&quot;item_id&quot;:&quot;3123&quot;,&quot;item_name&quot;:&quot;Grand Canyon:ON 8&quot;,&quot;coupon&quot;:&quot;&quot;,&quot;currency&quot;:&quot;EUR&quot;,&quot;discount&quot;:&quot;&quot;,&quot;item_brand&quot;:&quot;Canyon&quot;,&quot;item_category&quot;:&quot;E-Bikes&quot;,&quot;item_category2&quot;:&quot;E-Mountain&quot;,&quot;item_category3&quot;:&quot;Grand Canyon:ON&quot;,&quot;item_variant&quot;:&quot;&quot;,&quot;price&quot;:&quot;&quot;,&quot;quantity&quot;:1}]}}]">
Grand Canyon:ON 8
</a>
</div>
<div class="productTileDefault__infoWrapper">

<div class="productTileDefault__info productTileDefault__info--highlights">
RockShox Judy Silver, 120mm, Shimano Steps EP8 Motor
</div>
</div>
</div>
<div class="productTileDefault__productSummaryBottom">
<div class="productTileDefault__price">
<div class="productTile__priceSale">
From 2.999 €
</div>
<div class="productTile__priceMonthly">
or from 46,69 €/Mo.
</div>
</div>

</div>
</div>
</div>
</li>
'''
    )

    res = _parse_canyon_catalog(few_bike_tree)

    assert isinstance(res, list)
    assert len(res) == 8
    assert isinstance(res[0], Bike)
    assert res[0].id == 'spectral:on_cf_7_m'
    assert res[0].title == 'Spectral:ON CF 7'
    assert res[0].link == 'https://www.canyon.com/en-de/electric-bikes/electric-mountain-bikes/spectral-on/spectral-on-cf/spectral-on-cf-7/3117.html?dwvar_3117_pv_rahmenfarbe=WH'
    assert res[0].family == 'Spectral:ON'
    assert res[0].model == 'CF 7'
    assert res[0].size == 'M'
    assert res[4].id == 'grand_canyon:on_8_m'
    assert res[4].title == 'Grand Canyon:ON 8'
    assert res[4].link == 'https://www.canyon.com/en-de/electric-bikes/electric-mountain-bikes/grandcanyon-on/grand-canyon-on-8/3123.html?dwvar_3123_pv_rahmenfarbe=GY'
    assert res[4].family == 'Grand Canyon:ON'
    assert res[4].model == '8'
    assert res[4].size == 'M'


def test_parse_canyon_catalog_not_found():
    no_bike_tree = etree.HTML('<ul></ul>')

    res = _parse_canyon_catalog(no_bike_tree)

    assert len(res) == 0





