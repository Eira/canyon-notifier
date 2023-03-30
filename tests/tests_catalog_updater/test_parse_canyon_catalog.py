from lxml import etree

from app.catalog.catalog_operations import _parse_canyon_catalog
from app.models import Bike


def test_parse_canyon_catalog_one_bike():
    one_bike_tree = etree.HTML(
    '''
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
	    id: '3117',
	    sku: ''
	}];
	cq_params.categoryId = 'instockbikes';
	cq_params.refinements = '[{\"name\":\"pc_rahmengroesse\",\"value\":\"3XS\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"2XS\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"XS\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"S\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"M\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"L\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"XL\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"2XL\"},{\"name\":\"Category\",\"value\":\"instockbikes\"}]';
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
		search_params.refs = '[{\"name\":\"pc_rahmengroesse\",\"value\":\"3XS\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"2XS\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"XS\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"S\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"M\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"L\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"XL\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"2XL\"},{\"name\":\"Category\",\"value\":\"instockbikes\"}]';
		search_params.sort = 'sort_master_availability';
		search_params.imageUUID = '';
		search_params.searchID = '0fd83c46-7984-4cd7-a449-9a6f4b8f744c';
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
<div data-pid="50015574"
        class="js-productTileWrapper productTileDefault productTileDefault--bike"
         data-gtm-impression="[{&quot;event&quot;:&quot;EEC-productImpression&quot;,&quot;ecommerce&quot;:{&quot;currencyCode&quot;:&quot;EUR&quot;,&quot;impressions&quot;:[{&quot;name&quot;:&quot;Spectral:ON CF 7&quot;,&quot;id&quot;:&quot;3117&quot;,&quot;brand&quot;:&quot;Canyon&quot;,&quot;category&quot;:&quot;E-Bikes/E-Mountain/Spectral:ON/Spectral:ON CF&quot;,&quot;variant&quot;:&quot;&quot;,&quot;dimension50&quot;:&quot;2022&quot;,&quot;dimension52&quot;:&quot;Spectral:ON&quot;,&quot;dimension63&quot;:&quot;unisex&quot;,&quot;dimension64&quot;:&quot;&quot;,&quot;dimension65&quot;:&quot;ZFER&quot;,&quot;dimension66&quot;:&quot;CompleteBikeMT EBIKE&quot;,&quot;dimension67&quot;:&quot;false&quot;,&quot;dimension68&quot;:&quot;true&quot;,&quot;feedProductId&quot;:&quot;50015575&quot;,&quot;dimension54&quot;:&quot;not defined&quot;,&quot;dimension51&quot;:&quot;Infinit Red&quot;,&quot;dimension53&quot;:&quot;L&quot;,&quot;quantity&quot;:1,&quot;price&quot;:&quot;&quot;,&quot;metric4&quot;:&quot;&quot;,&quot;dimension56&quot;:&quot;not defined&quot;}]}},{&quot;event&quot;:&quot;view_item_list&quot;,&quot;event_name&quot;:&quot;Ecommerce - Item list view&quot;,&quot;ecommerce&quot;:{&quot;items&quot;:[{&quot;item_id&quot;:&quot;3117&quot;,&quot;item_name&quot;:&quot;Spectral:ON CF 7&quot;,&quot;coupon&quot;:&quot;&quot;,&quot;currency&quot;:&quot;EUR&quot;,&quot;discount&quot;:&quot;&quot;,&quot;item_brand&quot;:&quot;Canyon&quot;,&quot;item_category&quot;:&quot;E-Bikes&quot;,&quot;item_category2&quot;:&quot;E-Mountain&quot;,&quot;item_category3&quot;:&quot;Spectral:ON&quot;,&quot;item_category4&quot;:&quot;Spectral:ON CF&quot;,&quot;item_variant&quot;:&quot;&quot;,&quot;price&quot;:&quot;&quot;,&quot;quantity&quot;:1}]}}]">
<div class="productTileDefault__imageWrapper">
<a title="Spectral:ON CF 7" aria-label="Spectral:ON CF 7 Price: 4.799 &euro;" class="js-productTile productTileDefault__imageLink " href="https://www.canyon.com/en-de/electric-bikes/electric-mountain-bikes/spectral-on/spectral-on-cf/spectral-on-cf-7/3117.html?dwvar_3117_pv_rahmenfarbe=VT" aria-hidden="false" tabindex="0"
                 data-gtm-click="[{&quot;event&quot;:&quot;EEC-productClick&quot;,&quot;ecommerce&quot;:{&quot;click&quot;:{&quot;actionField&quot;:{&quot;list&quot;:&quot;&quot;},&quot;products&quot;:[{&quot;name&quot;:&quot;Spectral:ON CF 7&quot;,&quot;id&quot;:&quot;3117&quot;,&quot;brand&quot;:&quot;Canyon&quot;,&quot;category&quot;:&quot;E-Bikes/E-Mountain/Spectral:ON/Spectral:ON CF&quot;,&quot;variant&quot;:&quot;&quot;,&quot;dimension50&quot;:&quot;2022&quot;,&quot;dimension52&quot;:&quot;Spectral:ON&quot;,&quot;dimension63&quot;:&quot;unisex&quot;,&quot;dimension64&quot;:&quot;&quot;,&quot;dimension65&quot;:&quot;ZFER&quot;,&quot;dimension66&quot;:&quot;CompleteBikeMT EBIKE&quot;,&quot;dimension67&quot;:&quot;false&quot;,&quot;dimension68&quot;:&quot;true&quot;,&quot;feedProductId&quot;:&quot;50015575&quot;,&quot;dimension54&quot;:&quot;not defined&quot;,&quot;dimension51&quot;:&quot;Infinit Red&quot;,&quot;dimension53&quot;:&quot;L&quot;,&quot;quantity&quot;:&quot;&quot;,&quot;price&quot;:&quot;&quot;,&quot;metric4&quot;:&quot;&quot;,&quot;dimension56&quot;:&quot;not defined&quot;}]},&quot;currencyCode&quot;:&quot;EUR&quot;}},{&quot;event&quot;:&quot;select_item&quot;,&quot;event_name&quot;:&quot;Ecommerce - Select item&quot;,&quot;ecommerce&quot;:{&quot;items&quot;:[{&quot;item_id&quot;:&quot;3117&quot;,&quot;item_name&quot;:&quot;Spectral:ON CF 7&quot;,&quot;coupon&quot;:&quot;&quot;,&quot;currency&quot;:&quot;EUR&quot;,&quot;discount&quot;:&quot;&quot;,&quot;item_brand&quot;:&quot;Canyon&quot;,&quot;item_category&quot;:&quot;E-Bikes&quot;,&quot;item_category2&quot;:&quot;E-Mountain&quot;,&quot;item_category3&quot;:&quot;Spectral:ON&quot;,&quot;item_category4&quot;:&quot;Spectral:ON CF&quot;,&quot;item_variant&quot;:&quot;&quot;,&quot;price&quot;:&quot;&quot;,&quot;quantity&quot;:1}]}}]">
<div class="productTileDefault__pictureWrapper js-noSwatchTileImagesContainer"
                    data-tile-images='[{&quot;title&quot;:&quot;Spectral:ON CF 7&quot;,&quot;alt&quot;:&quot;Spectral:ON CF 7&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.png&quot;},&quot;found&quot;:true}]'
                    data-tile-hover-images='[{&quot;title&quot;:&quot;Spectral:ON CF 7&quot;,&quot;alt&quot;:&quot;Spectral:ON CF 7&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;md&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;},&quot;found&quot;:false}]'
                    >
<picture class="picture productTileDefault__picture productTileDefault__picture--main">
<source
                        media="(min-width: 1921px)"

                            srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2"

                    />
<source
                        media="(min-width: 1440px)"

                            srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2"

                    />
<source
                        media="(min-width: 1200px)"

                            srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2"

                    />
<source
                        media="(min-width: 992px)"

                            srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2"

                    />
<source
                        media="(min-width: 768px)"

                            srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2"

                    />
<source
                        media="(min-width: 534px)"

                            srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2"

                    />
<source
                        media="(min-width: 0px)"

                            srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2"

                    />
<img
                title="Spectral:ON CF 7"
                alt="Spectral:ON CF 7"
                class="picture__image  productTileDefault__image"

                    src="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2"

                        loading="lazy"


            />
</picture>
</div>
</a>
<div class="productTileDefault__awardAndBadges">
<div class="productTileDefault__badges">
<ul class="productTileBadges__list">
<li class="productTileBadges__listItem productTileBadges__listItem--availability" >
Available to buy in L
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
<button
                        aria-hidden="false"
                        aria-label="Stealth"
                        class="colorSwatch colorSwatch--button colorSwatch--small  js-color-swatch  colorPicker__colorSwatch"
                        tabindex="0"
                        data-url="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_DE/Product-Variation?dwvar_3117_pv_rahmenfarbe=BK&amp;pid=3117&amp;quantity=undefined&amp;imageupdate=color"
                        data-displayvalue="Stealth"


                            data-tile-images="[{&quot;title&quot;:&quot;Spectral:ON CF 7&quot;,&quot;alt&quot;:&quot;Spectral:ON CF 7&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw98cdce4c/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_bk-bk_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw98cdce4c/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_bk-bk_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw98cdce4c/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_bk-bk_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw98cdce4c/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_bk-bk_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw98cdce4c/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_bk-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw98cdce4c/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_bk-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw98cdce4c/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_bk-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dw98cdce4c/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_bk-bk_P5.png&quot;},&quot;found&quot;:true}]"
                            data-tile-hover-images="[{&quot;title&quot;:&quot;Stealth&quot;,&quot;alt&quot;:&quot;Stealth&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;md&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;},&quot;found&quot;:false}]"
                            data-pdp-url="https://www.canyon.com/en-de/electric-bikes/electric-mountain-bikes/spectral-on/spectral-on-cf/spectral-on-cf-7/3117.html?dwvar_3117_pv_rahmenfarbe=BK"
                            data-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-AddToCompare?pid=50015568"
                            data-remove-from-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-RemoveFromCompare?pid=50015568"
                            data-compare-pid="50015568"
                            title="Stealth"
                            data-quickAddUrl=https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_DE/Tile-Variation?pid=3117&amp;dwvar_3117_pv_rahmenfarbe=BK

                        type="button">
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
<button
                        aria-hidden="false"
                        aria-label="Infinit Red"
                        class="colorSwatch colorSwatch--button colorSwatch--small colorSwatch--selected js-noGtmClick js-color-swatch  colorPicker__colorSwatch"
                        tabindex="0"
                        data-url="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_DE/Product-Variation?dwvar_3117_pv_rahmenfarbe=&amp;pid=3117&amp;quantity=undefined&amp;imageupdate=color"
                        data-displayvalue="Infinit Red"

                            data-selected-color-value="VT"


                            data-tile-images="[{&quot;title&quot;:&quot;Spectral:ON CF 7&quot;,&quot;alt&quot;:&quot;Spectral:ON CF 7&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.png&quot;},&quot;found&quot;:true}]"
                            data-tile-hover-images="[{&quot;title&quot;:&quot;Infinit Red&quot;,&quot;alt&quot;:&quot;Infinit Red&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;md&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;},&quot;found&quot;:false}]"
                            data-pdp-url="https://www.canyon.com/en-de/electric-bikes/electric-mountain-bikes/spectral-on/spectral-on-cf/spectral-on-cf-7/3117.html?dwvar_3117_pv_rahmenfarbe=VT"
                            data-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-AddToCompare?pid=50015572"
                            data-remove-from-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-RemoveFromCompare?pid=50015572"
                            data-compare-pid="50015572"
                            title="Infinit Red"
                            data-quickAddUrl=https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_DE/Tile-Variation?pid=3117&amp;dwvar_3117_pv_rahmenfarbe=VT

                        type="button">
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
<button
                        aria-hidden="false"
                        aria-label="Boundless Grey"
                        class="colorSwatch colorSwatch--button colorSwatch--small  js-color-swatch  colorPicker__colorSwatch"
                        tabindex="0"
                        data-url="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_DE/Product-Variation?dwvar_3117_pv_rahmenfarbe=WH&amp;pid=3117&amp;quantity=undefined&amp;imageupdate=color"
                        data-displayvalue="Boundless Grey"


                            data-tile-images="[{&quot;title&quot;:&quot;Spectral:ON CF 7&quot;,&quot;alt&quot;:&quot;Spectral:ON CF 7&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.png&quot;},&quot;found&quot;:true}]"
                            data-tile-hover-images="[{&quot;title&quot;:&quot;Boundless Grey&quot;,&quot;alt&quot;:&quot;Boundless Grey&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;md&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;},&quot;found&quot;:false}]"
                            data-pdp-url="https://www.canyon.com/en-de/electric-bikes/electric-mountain-bikes/spectral-on/spectral-on-cf/spectral-on-cf-7/3117.html?dwvar_3117_pv_rahmenfarbe=WH"
                            data-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-AddToCompare?pid=50015576"
                            data-remove-from-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-RemoveFromCompare?pid=50015576"
                            data-compare-pid="50015576"
                            title="Boundless Grey"
                            data-quickAddUrl=https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_DE/Tile-Variation?pid=3117&amp;dwvar_3117_pv_rahmenfarbe=WH

                        type="button">
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
<input
                    type="checkbox"
                    class="productTileCompare__checkboxInput inputCheckbox__input js-selectCompareProduct"
                    aria-hidden="false"
                    aria-label="Compare"
                    tabindex="0"
                    value="productCompareCheckbox"
                    name="productCompareCheckbox"
                    data-remove-pid-compare="50015574"
                    data-compare-remove-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-RemoveFromCompare?pid=50015574"
                    data-add-to-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-AddToCompare?pid=50015574"/>
<span class="productTile__compareCheckboxLabel inputCheckbox__label">
<svg
        xmlns:xlink="http://www.w3.org/1999/xlink"
        class="icon icon-check2 inputCheckbox__icon"
        aria-hidden="false"
        focusable="false"

    >
<use xlink:href="/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/iconsNew.svg#sprite-check2"></use>

</svg>
<span class="inputCheckbox__labelInner">
Compare
</span>
</span>
</label>
</div>
</div>
<div class="productTileDefault__productNameWrapper">
<a title="Spectral:ON CF 7" class="productTileDefault__productName link " href="https://www.canyon.com/en-de/electric-bikes/electric-mountain-bikes/spectral-on/spectral-on-cf/spectral-on-cf-7/3117.html?dwvar_3117_pv_rahmenfarbe=VT" aria-hidden="false" tabindex="0"
                         data-gtm-click="[{&quot;event&quot;:&quot;EEC-productClick&quot;,&quot;ecommerce&quot;:{&quot;click&quot;:{&quot;actionField&quot;:{&quot;list&quot;:&quot;&quot;},&quot;products&quot;:[{&quot;name&quot;:&quot;Spectral:ON CF 7&quot;,&quot;id&quot;:&quot;3117&quot;,&quot;brand&quot;:&quot;Canyon&quot;,&quot;category&quot;:&quot;E-Bikes/E-Mountain/Spectral:ON/Spectral:ON CF&quot;,&quot;variant&quot;:&quot;&quot;,&quot;dimension50&quot;:&quot;2022&quot;,&quot;dimension52&quot;:&quot;Spectral:ON&quot;,&quot;dimension63&quot;:&quot;unisex&quot;,&quot;dimension64&quot;:&quot;&quot;,&quot;dimension65&quot;:&quot;ZFER&quot;,&quot;dimension66&quot;:&quot;CompleteBikeMT EBIKE&quot;,&quot;dimension67&quot;:&quot;false&quot;,&quot;dimension68&quot;:&quot;true&quot;,&quot;feedProductId&quot;:&quot;50015575&quot;,&quot;dimension54&quot;:&quot;not defined&quot;,&quot;dimension51&quot;:&quot;Infinit Red&quot;,&quot;dimension53&quot;:&quot;L&quot;,&quot;quantity&quot;:&quot;&quot;,&quot;price&quot;:&quot;&quot;,&quot;metric4&quot;:&quot;&quot;,&quot;dimension56&quot;:&quot;not defined&quot;}]},&quot;currencyCode&quot;:&quot;EUR&quot;}},{&quot;event&quot;:&quot;select_item&quot;,&quot;event_name&quot;:&quot;Ecommerce - Select item&quot;,&quot;ecommerce&quot;:{&quot;items&quot;:[{&quot;item_id&quot;:&quot;3117&quot;,&quot;item_name&quot;:&quot;Spectral:ON CF 7&quot;,&quot;coupon&quot;:&quot;&quot;,&quot;currency&quot;:&quot;EUR&quot;,&quot;discount&quot;:&quot;&quot;,&quot;item_brand&quot;:&quot;Canyon&quot;,&quot;item_category&quot;:&quot;E-Bikes&quot;,&quot;item_category2&quot;:&quot;E-Mountain&quot;,&quot;item_category3&quot;:&quot;Spectral:ON&quot;,&quot;item_category4&quot;:&quot;Spectral:ON CF&quot;,&quot;item_variant&quot;:&quot;&quot;,&quot;price&quot;:&quot;&quot;,&quot;quantity&quot;:1}]}}]">
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
From 4.799 &euro;
</div>
<div class="productTile__priceMonthly">
or from 74,71 €/Mo.
</div>
</div>

</div>
</div>
</div>
</li>
    '''
    )

    res = _parse_canyon_catalog(one_bike_tree)

    assert isinstance(res, list)
    assert len(res) == 1
    assert isinstance(res[0], Bike)
    assert res[0].id == 'spectral:on_cf_7_l'
    assert res[0].title == 'Spectral:ON CF 7'
    assert res[0].link == 'https://www.canyon.com/en-de/electric-bikes/electric-mountain-bikes/spectral-on/spectral-on-cf/spectral-on-cf-7/3117.html?dwvar_3117_pv_rahmenfarbe=VT'
    assert res[0].family == 'Spectral:ON'
    assert res[0].model == 'CF 7'
    assert res[0].size == 'L'


def test_parse_canyon_catalog_few_bikes():
    few_bike_tree = etree.HTML(
        '''
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
        	    id: '3117',
        	    sku: ''
        	}];
        	cq_params.categoryId = 'instockbikes';
        	cq_params.refinements = '[{\"name\":\"pc_rahmengroesse\",\"value\":\"3XS\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"2XS\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"XS\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"S\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"M\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"L\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"XL\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"2XL\"},{\"name\":\"Category\",\"value\":\"instockbikes\"}]';
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
        		search_params.refs = '[{\"name\":\"pc_rahmengroesse\",\"value\":\"3XS\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"2XS\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"XS\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"S\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"M\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"L\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"XL\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"2XL\"},{\"name\":\"Category\",\"value\":\"instockbikes\"}]';
        		search_params.sort = 'sort_master_availability';
        		search_params.imageUUID = '';
        		search_params.searchID = '76d7f617-b0e5-4be5-bb49-284fbe372acd';
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
        <div data-pid="50015578" class="js-productTileWrapper productTileDefault productTileDefault--bike" data-gtm-impression="[{&quot;event&quot;:&quot;EEC-productImpression&quot;,&quot;ecommerce&quot;:{&quot;currencyCode&quot;:&quot;EUR&quot;,&quot;impressions&quot;:[{&quot;name&quot;:&quot;Spectral:ON CF 7&quot;,&quot;id&quot;:&quot;3117&quot;,&quot;brand&quot;:&quot;Canyon&quot;,&quot;category&quot;:&quot;E-Bikes/E-Mountain/Spectral:ON/Spectral:ON CF&quot;,&quot;variant&quot;:&quot;&quot;,&quot;dimension50&quot;:&quot;2022&quot;,&quot;dimension52&quot;:&quot;Spectral:ON&quot;,&quot;dimension63&quot;:&quot;unisex&quot;,&quot;dimension64&quot;:&quot;&quot;,&quot;dimension65&quot;:&quot;ZFER&quot;,&quot;dimension66&quot;:&quot;CompleteBikeMT EBIKE&quot;,&quot;dimension67&quot;:&quot;false&quot;,&quot;dimension68&quot;:&quot;true&quot;,&quot;feedProductId&quot;:&quot;50015575&quot;,&quot;dimension54&quot;:&quot;not defined&quot;,&quot;dimension51&quot;:&quot;Boundless Grey&quot;,&quot;dimension53&quot;:&quot;L&quot;,&quot;quantity&quot;:1,&quot;price&quot;:&quot;&quot;,&quot;metric4&quot;:&quot;&quot;,&quot;dimension56&quot;:&quot;not defined&quot;}]}},{&quot;event&quot;:&quot;view_item_list&quot;,&quot;event_name&quot;:&quot;Ecommerce - Item list view&quot;,&quot;ecommerce&quot;:{&quot;items&quot;:[{&quot;item_id&quot;:&quot;3117&quot;,&quot;item_name&quot;:&quot;Spectral:ON CF 7&quot;,&quot;coupon&quot;:&quot;&quot;,&quot;currency&quot;:&quot;EUR&quot;,&quot;discount&quot;:&quot;&quot;,&quot;item_brand&quot;:&quot;Canyon&quot;,&quot;item_category&quot;:&quot;E-Bikes&quot;,&quot;item_category2&quot;:&quot;E-Mountain&quot;,&quot;item_category3&quot;:&quot;Spectral:ON&quot;,&quot;item_category4&quot;:&quot;Spectral:ON CF&quot;,&quot;item_variant&quot;:&quot;&quot;,&quot;price&quot;:&quot;&quot;,&quot;quantity&quot;:1}]}}]">
        <div class="productTileDefault__imageWrapper">
        <a title="Spectral:ON CF 7" aria-label="Spectral:ON CF 7 Price: 4.799 €" class="js-productTile productTileDefault__imageLink " href="https://www.canyon.com/en-de/electric-bikes/electric-mountain-bikes/spectral-on/spectral-on-cf/spectral-on-cf-7/3117.html?dwvar_3117_pv_rahmenfarbe=WH" aria-hidden="false" tabindex="0" data-gtm-click="[{&quot;event&quot;:&quot;EEC-productClick&quot;,&quot;ecommerce&quot;:{&quot;click&quot;:{&quot;actionField&quot;:{&quot;list&quot;:&quot;&quot;},&quot;products&quot;:[{&quot;name&quot;:&quot;Spectral:ON CF 7&quot;,&quot;id&quot;:&quot;3117&quot;,&quot;brand&quot;:&quot;Canyon&quot;,&quot;category&quot;:&quot;E-Bikes/E-Mountain/Spectral:ON/Spectral:ON CF&quot;,&quot;variant&quot;:&quot;&quot;,&quot;dimension50&quot;:&quot;2022&quot;,&quot;dimension52&quot;:&quot;Spectral:ON&quot;,&quot;dimension63&quot;:&quot;unisex&quot;,&quot;dimension64&quot;:&quot;&quot;,&quot;dimension65&quot;:&quot;ZFER&quot;,&quot;dimension66&quot;:&quot;CompleteBikeMT EBIKE&quot;,&quot;dimension67&quot;:&quot;false&quot;,&quot;dimension68&quot;:&quot;true&quot;,&quot;feedProductId&quot;:&quot;50015575&quot;,&quot;dimension54&quot;:&quot;not defined&quot;,&quot;dimension51&quot;:&quot;Boundless Grey&quot;,&quot;dimension53&quot;:&quot;L&quot;,&quot;quantity&quot;:&quot;&quot;,&quot;price&quot;:&quot;&quot;,&quot;metric4&quot;:&quot;&quot;,&quot;dimension56&quot;:&quot;not defined&quot;}]},&quot;currencyCode&quot;:&quot;EUR&quot;}},{&quot;event&quot;:&quot;select_item&quot;,&quot;event_name&quot;:&quot;Ecommerce - Select item&quot;,&quot;ecommerce&quot;:{&quot;items&quot;:[{&quot;item_id&quot;:&quot;3117&quot;,&quot;item_name&quot;:&quot;Spectral:ON CF 7&quot;,&quot;coupon&quot;:&quot;&quot;,&quot;currency&quot;:&quot;EUR&quot;,&quot;discount&quot;:&quot;&quot;,&quot;item_brand&quot;:&quot;Canyon&quot;,&quot;item_category&quot;:&quot;E-Bikes&quot;,&quot;item_category2&quot;:&quot;E-Mountain&quot;,&quot;item_category3&quot;:&quot;Spectral:ON&quot;,&quot;item_category4&quot;:&quot;Spectral:ON CF&quot;,&quot;item_variant&quot;:&quot;&quot;,&quot;price&quot;:&quot;&quot;,&quot;quantity&quot;:1}]}}]">
        <div class="productTileDefault__pictureWrapper js-noSwatchTileImagesContainer" data-tile-images="[{&quot;title&quot;:&quot;Spectral:ON CF 7&quot;,&quot;alt&quot;:&quot;Spectral:ON CF 7&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.png&quot;},&quot;found&quot;:true}]" data-tile-hover-images="[{&quot;title&quot;:&quot;Spectral:ON CF 7&quot;,&quot;alt&quot;:&quot;Spectral:ON CF 7&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;md&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;},&quot;found&quot;:false}]">
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
        <ul class="productTileBadges__list">
        <li class="productTileBadges__listItem productTileBadges__listItem--availability">
        Available to buy in L
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
        <button aria-hidden="false" aria-label="Stealth" class="colorSwatch colorSwatch--button colorSwatch--small  js-color-swatch  colorPicker__colorSwatch" tabindex="0" data-url="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_DE/Product-Variation?dwvar_3117_pv_rahmenfarbe=BK&amp;pid=3117&amp;quantity=undefined&amp;imageupdate=color" data-displayvalue="Stealth" data-tile-images="[{&quot;title&quot;:&quot;Spectral:ON CF 7&quot;,&quot;alt&quot;:&quot;Spectral:ON CF 7&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw98cdce4c/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_bk-bk_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw98cdce4c/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_bk-bk_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw98cdce4c/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_bk-bk_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw98cdce4c/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_bk-bk_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw98cdce4c/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_bk-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw98cdce4c/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_bk-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw98cdce4c/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_bk-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dw98cdce4c/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_bk-bk_P5.png&quot;},&quot;found&quot;:true}]" data-tile-hover-images="[{&quot;title&quot;:&quot;Stealth&quot;,&quot;alt&quot;:&quot;Stealth&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;md&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;},&quot;found&quot;:false}]" data-pdp-url="https://www.canyon.com/en-de/electric-bikes/electric-mountain-bikes/spectral-on/spectral-on-cf/spectral-on-cf-7/3117.html?dwvar_3117_pv_rahmenfarbe=BK" data-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-AddToCompare?pid=50015568" data-remove-from-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-RemoveFromCompare?pid=50015568" data-compare-pid="50015568" title="Stealth" data-quickaddurl="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_DE/Tile-Variation?pid=3117&amp;dwvar_3117_pv_rahmenfarbe=BK" type="button">
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
        <button aria-hidden="false" aria-label="Infinit Red" class="colorSwatch colorSwatch--button colorSwatch--small  js-color-swatch  colorPicker__colorSwatch" tabindex="0" data-url="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_DE/Product-Variation?dwvar_3117_pv_rahmenfarbe=VT&amp;pid=3117&amp;quantity=undefined&amp;imageupdate=color" data-displayvalue="Infinit Red" data-tile-images="[{&quot;title&quot;:&quot;Spectral:ON CF 7&quot;,&quot;alt&quot;:&quot;Spectral:ON CF 7&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dw2de3a281/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_vt_P5.png&quot;},&quot;found&quot;:true}]" data-tile-hover-images="[{&quot;title&quot;:&quot;Infinit Red&quot;,&quot;alt&quot;:&quot;Infinit Red&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;md&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;},&quot;found&quot;:false}]" data-pdp-url="https://www.canyon.com/en-de/electric-bikes/electric-mountain-bikes/spectral-on/spectral-on-cf/spectral-on-cf-7/3117.html?dwvar_3117_pv_rahmenfarbe=VT" data-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-AddToCompare?pid=50015572" data-remove-from-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-RemoveFromCompare?pid=50015572" data-compare-pid="50015572" title="Infinit Red" data-quickaddurl="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_DE/Tile-Variation?pid=3117&amp;dwvar_3117_pv_rahmenfarbe=VT" type="button">
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
        <button aria-hidden="false" aria-label="Boundless Grey" class="colorSwatch colorSwatch--button colorSwatch--small colorSwatch--selected js-noGtmClick js-color-swatch  colorPicker__colorSwatch" tabindex="0" data-url="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_DE/Product-Variation?dwvar_3117_pv_rahmenfarbe=&amp;pid=3117&amp;quantity=undefined&amp;imageupdate=color" data-displayvalue="Boundless Grey" data-selected-color-value="WH" data-tile-images="[{&quot;title&quot;:&quot;Spectral:ON CF 7&quot;,&quot;alt&quot;:&quot;Spectral:ON CF 7&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dw3f6e7b5f/images/full/full_2022_/2022/full_2022_spectral-on-cf-7_3117_gy-gy_P5.png&quot;},&quot;found&quot;:true}]" data-tile-hover-images="[{&quot;title&quot;:&quot;Boundless Grey&quot;,&quot;alt&quot;:&quot;Boundless Grey&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;md&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;},&quot;found&quot;:false}]" data-pdp-url="https://www.canyon.com/en-de/electric-bikes/electric-mountain-bikes/spectral-on/spectral-on-cf/spectral-on-cf-7/3117.html?dwvar_3117_pv_rahmenfarbe=WH" data-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-AddToCompare?pid=50015576" data-remove-from-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-RemoveFromCompare?pid=50015576" data-compare-pid="50015576" title="Boundless Grey" data-quickaddurl="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_DE/Tile-Variation?pid=3117&amp;dwvar_3117_pv_rahmenfarbe=WH" type="button">
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
        <input type="checkbox" class="productTileCompare__checkboxInput inputCheckbox__input js-selectCompareProduct" aria-hidden="false" aria-label="Compare" tabindex="0" value="productCompareCheckbox" name="productCompareCheckbox" data-remove-pid-compare="50015578" data-compare-remove-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-RemoveFromCompare?pid=50015578" data-add-to-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-AddToCompare?pid=50015578">
        <span class="productTile__compareCheckboxLabel inputCheckbox__label">
        <svg xmlns:xlink="http://www.w3.org/1999/xlink" class="icon icon-check2 inputCheckbox__icon" aria-hidden="false" focusable="false">
        <use xlink:href="/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/iconsNew.svg#sprite-check2"></use>
        </svg>
        <span class="inputCheckbox__labelInner">
        Compare
        </span>
        </span>
        </label>
        </div>
        </div>
        <div class="productTileDefault__productNameWrapper">
        <a title="Spectral:ON CF 7" class="productTileDefault__productName link " href="https://www.canyon.com/en-de/electric-bikes/electric-mountain-bikes/spectral-on/spectral-on-cf/spectral-on-cf-7/3117.html?dwvar_3117_pv_rahmenfarbe=WH" aria-hidden="false" tabindex="0" data-gtm-click="[{&quot;event&quot;:&quot;EEC-productClick&quot;,&quot;ecommerce&quot;:{&quot;click&quot;:{&quot;actionField&quot;:{&quot;list&quot;:&quot;&quot;},&quot;products&quot;:[{&quot;name&quot;:&quot;Spectral:ON CF 7&quot;,&quot;id&quot;:&quot;3117&quot;,&quot;brand&quot;:&quot;Canyon&quot;,&quot;category&quot;:&quot;E-Bikes/E-Mountain/Spectral:ON/Spectral:ON CF&quot;,&quot;variant&quot;:&quot;&quot;,&quot;dimension50&quot;:&quot;2022&quot;,&quot;dimension52&quot;:&quot;Spectral:ON&quot;,&quot;dimension63&quot;:&quot;unisex&quot;,&quot;dimension64&quot;:&quot;&quot;,&quot;dimension65&quot;:&quot;ZFER&quot;,&quot;dimension66&quot;:&quot;CompleteBikeMT EBIKE&quot;,&quot;dimension67&quot;:&quot;false&quot;,&quot;dimension68&quot;:&quot;true&quot;,&quot;feedProductId&quot;:&quot;50015575&quot;,&quot;dimension54&quot;:&quot;not defined&quot;,&quot;dimension51&quot;:&quot;Boundless Grey&quot;,&quot;dimension53&quot;:&quot;L&quot;,&quot;quantity&quot;:&quot;&quot;,&quot;price&quot;:&quot;&quot;,&quot;metric4&quot;:&quot;&quot;,&quot;dimension56&quot;:&quot;not defined&quot;}]},&quot;currencyCode&quot;:&quot;EUR&quot;}},{&quot;event&quot;:&quot;select_item&quot;,&quot;event_name&quot;:&quot;Ecommerce - Select item&quot;,&quot;ecommerce&quot;:{&quot;items&quot;:[{&quot;item_id&quot;:&quot;3117&quot;,&quot;item_name&quot;:&quot;Spectral:ON CF 7&quot;,&quot;coupon&quot;:&quot;&quot;,&quot;currency&quot;:&quot;EUR&quot;,&quot;discount&quot;:&quot;&quot;,&quot;item_brand&quot;:&quot;Canyon&quot;,&quot;item_category&quot;:&quot;E-Bikes&quot;,&quot;item_category2&quot;:&quot;E-Mountain&quot;,&quot;item_category3&quot;:&quot;Spectral:ON&quot;,&quot;item_category4&quot;:&quot;Spectral:ON CF&quot;,&quot;item_variant&quot;:&quot;&quot;,&quot;price&quot;:&quot;&quot;,&quot;quantity&quot;:1}]}}]">
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
	    id: '3116',
	    sku: ''
	}];
	cq_params.categoryId = 'instockbikes';
	cq_params.refinements = '[{\"name\":\"pc_rahmengroesse\",\"value\":\"3XS\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"2XS\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"XS\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"S\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"M\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"L\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"XL\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"2XL\"},{\"name\":\"Category\",\"value\":\"instockbikes\"}]';
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
		search_params.refs = '[{\"name\":\"pc_rahmengroesse\",\"value\":\"3XS\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"2XS\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"XS\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"S\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"M\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"L\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"XL\"},{\"name\":\"pc_rahmengroesse\",\"value\":\"2XL\"},{\"name\":\"Category\",\"value\":\"instockbikes\"}]';
		search_params.sort = 'sort_master_availability';
		search_params.imageUUID = '';
		search_params.searchID = '76d7f617-b0e5-4be5-bb49-284fbe372acd';
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
dw.ac._capture({id: "3116", type: "searchhit"});
/* ]]> */
// -->
</script>
<div data-pid="50015562" class="js-productTileWrapper productTileDefault productTileDefault--bike" data-gtm-impression="[{&quot;event&quot;:&quot;EEC-productImpression&quot;,&quot;ecommerce&quot;:{&quot;currencyCode&quot;:&quot;EUR&quot;,&quot;impressions&quot;:[{&quot;name&quot;:&quot;Spectral:ON CF 8&quot;,&quot;id&quot;:&quot;3116&quot;,&quot;brand&quot;:&quot;Canyon&quot;,&quot;category&quot;:&quot;E-Bikes/E-Mountain/Spectral:ON/Spectral:ON CF&quot;,&quot;variant&quot;:&quot;&quot;,&quot;dimension50&quot;:&quot;2022&quot;,&quot;dimension52&quot;:&quot;Spectral:ON&quot;,&quot;dimension63&quot;:&quot;unisex&quot;,&quot;dimension64&quot;:&quot;&quot;,&quot;dimension65&quot;:&quot;ZFER&quot;,&quot;dimension66&quot;:&quot;CompleteBikeMT EBIKE&quot;,&quot;dimension67&quot;:&quot;false&quot;,&quot;dimension68&quot;:&quot;true&quot;,&quot;feedProductId&quot;:&quot;50015567&quot;,&quot;dimension54&quot;:&quot;not defined&quot;,&quot;dimension51&quot;:&quot;Stealth&quot;,&quot;dimension53&quot;:&quot;L&quot;,&quot;quantity&quot;:1,&quot;price&quot;:&quot;&quot;,&quot;metric4&quot;:&quot;&quot;,&quot;dimension56&quot;:&quot;not defined&quot;}]}},{&quot;event&quot;:&quot;view_item_list&quot;,&quot;event_name&quot;:&quot;Ecommerce - Item list view&quot;,&quot;ecommerce&quot;:{&quot;items&quot;:[{&quot;item_id&quot;:&quot;3116&quot;,&quot;item_name&quot;:&quot;Spectral:ON CF 8&quot;,&quot;coupon&quot;:&quot;&quot;,&quot;currency&quot;:&quot;EUR&quot;,&quot;discount&quot;:&quot;&quot;,&quot;item_brand&quot;:&quot;Canyon&quot;,&quot;item_category&quot;:&quot;E-Bikes&quot;,&quot;item_category2&quot;:&quot;E-Mountain&quot;,&quot;item_category3&quot;:&quot;Spectral:ON&quot;,&quot;item_category4&quot;:&quot;Spectral:ON CF&quot;,&quot;item_variant&quot;:&quot;&quot;,&quot;price&quot;:&quot;&quot;,&quot;quantity&quot;:1}]}}]">
<div class="productTileDefault__imageWrapper">
<a title="Spectral:ON CF 8" aria-label="Spectral:ON CF 8 Price: 5.499 €" class="js-productTile productTileDefault__imageLink " href="https://www.canyon.com/en-de/electric-bikes/electric-mountain-bikes/spectral-on/spectral-on-cf/spectral-on-cf-8/3116.html?dwvar_3116_pv_rahmenfarbe=BK" aria-hidden="false" tabindex="0" data-gtm-click="[{&quot;event&quot;:&quot;EEC-productClick&quot;,&quot;ecommerce&quot;:{&quot;click&quot;:{&quot;actionField&quot;:{&quot;list&quot;:&quot;&quot;},&quot;products&quot;:[{&quot;name&quot;:&quot;Spectral:ON CF 8&quot;,&quot;id&quot;:&quot;3116&quot;,&quot;brand&quot;:&quot;Canyon&quot;,&quot;category&quot;:&quot;E-Bikes/E-Mountain/Spectral:ON/Spectral:ON CF&quot;,&quot;variant&quot;:&quot;&quot;,&quot;dimension50&quot;:&quot;2022&quot;,&quot;dimension52&quot;:&quot;Spectral:ON&quot;,&quot;dimension63&quot;:&quot;unisex&quot;,&quot;dimension64&quot;:&quot;&quot;,&quot;dimension65&quot;:&quot;ZFER&quot;,&quot;dimension66&quot;:&quot;CompleteBikeMT EBIKE&quot;,&quot;dimension67&quot;:&quot;false&quot;,&quot;dimension68&quot;:&quot;true&quot;,&quot;feedProductId&quot;:&quot;50015567&quot;,&quot;dimension54&quot;:&quot;not defined&quot;,&quot;dimension51&quot;:&quot;Stealth&quot;,&quot;dimension53&quot;:&quot;L&quot;,&quot;quantity&quot;:&quot;&quot;,&quot;price&quot;:&quot;&quot;,&quot;metric4&quot;:&quot;&quot;,&quot;dimension56&quot;:&quot;not defined&quot;}]},&quot;currencyCode&quot;:&quot;EUR&quot;}},{&quot;event&quot;:&quot;select_item&quot;,&quot;event_name&quot;:&quot;Ecommerce - Select item&quot;,&quot;ecommerce&quot;:{&quot;items&quot;:[{&quot;item_id&quot;:&quot;3116&quot;,&quot;item_name&quot;:&quot;Spectral:ON CF 8&quot;,&quot;coupon&quot;:&quot;&quot;,&quot;currency&quot;:&quot;EUR&quot;,&quot;discount&quot;:&quot;&quot;,&quot;item_brand&quot;:&quot;Canyon&quot;,&quot;item_category&quot;:&quot;E-Bikes&quot;,&quot;item_category2&quot;:&quot;E-Mountain&quot;,&quot;item_category3&quot;:&quot;Spectral:ON&quot;,&quot;item_category4&quot;:&quot;Spectral:ON CF&quot;,&quot;item_variant&quot;:&quot;&quot;,&quot;price&quot;:&quot;&quot;,&quot;quantity&quot;:1}]}}]">
<div class="productTileDefault__pictureWrapper js-noSwatchTileImagesContainer" data-tile-images="[{&quot;title&quot;:&quot;Spectral:ON CF 8&quot;,&quot;alt&quot;:&quot;Spectral:ON CF 8&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.png&quot;},&quot;found&quot;:true}]" data-tile-hover-images="[{&quot;title&quot;:&quot;Spectral:ON CF 8&quot;,&quot;alt&quot;:&quot;Spectral:ON CF 8&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;md&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;},&quot;found&quot;:false}]">
<picture class="picture productTileDefault__picture productTileDefault__picture--main">
<source media="(min-width: 1921px)" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2">

<source media="(min-width: 1440px)" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2">
<source media="(min-width: 1200px)" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2">
<source media="(min-width: 992px)" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2">
<source media="(min-width: 768px)" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2">
<source media="(min-width: 534px)" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2">
<source media="(min-width: 0px)" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2">
<img title="Spectral:ON CF 8" alt="Spectral:ON CF 8" class="picture__image  productTileDefault__image" src="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2" loading="lazy">
</picture>
</div>
</a>
<div class="productTileDefault__awardAndBadges">
<div class="productTileDefault__badges">
<ul class="productTileBadges__list">
<li class="productTileBadges__listItem productTileBadges__listItem--availability">
Available to buy in L
</li>
</ul>
</div>
<div class="productTileDefault__award">
<div class="productTileAward__imageWrapper">
<img class="productTileAward__image" alt="Award: Spectral:ON CF 8" title="Award: Spectral:ON CF 8" src="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwa7d7b968/images/awards/mtb/EMTB_Urteil_Logo_english.png?sw=180" loading="lazy">
</div>
</div>
</div>
</div>
<div class="productTileDefault__productSummary">
<div class="productTileDefault__productSummaryTop">
<div class="productTileDefault__colorsAndCompare">
<div class="colorPicker__wrapper colorPicker__wrapper--showOptionalPlusIndicator">
<ul class="js-colorPicker colorPicker colorPicker--colorCount--2 colorPicker--showOptionalPlusIndicator  ">
<li class="colorPicker__colorListItem ">
<button aria-hidden="false" aria-label="Stealth" class="colorSwatch colorSwatch--button colorSwatch--small colorSwatch--selected js-noGtmClick js-color-swatch  colorPicker__colorSwatch" tabindex="0" data-url="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_DE/Product-Variation?dwvar_3116_pv_rahmenfarbe=&amp;pid=3116&amp;quantity=undefined&amp;imageupdate=color" data-displayvalue="Stealth" data-selected-color-value="BK" data-tile-images="[{&quot;title&quot;:&quot;Spectral:ON CF 8&quot;,&quot;alt&quot;:&quot;Spectral:ON CF 8&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.png&quot;},&quot;found&quot;:true}]" data-tile-hover-images="[{&quot;title&quot;:&quot;Stealth&quot;,&quot;alt&quot;:&quot;Stealth&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;md&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;},&quot;found&quot;:false}]" data-pdp-url="https://www.canyon.com/en-de/electric-bikes/electric-mountain-bikes/spectral-on/spectral-on-cf/spectral-on-cf-8/3116.html?dwvar_3116_pv_rahmenfarbe=BK" data-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-AddToCompare?pid=50015560" data-remove-from-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-RemoveFromCompare?pid=50015560" data-compare-pid="50015560" title="Stealth" data-quickaddurl="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_DE/Tile-Variation?pid=3116&amp;dwvar_3116_pv_rahmenfarbe=BK" type="button">
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
<button aria-hidden="false" aria-label="Green Vastness" class="colorSwatch colorSwatch--button colorSwatch--small  js-color-swatch  colorPicker__colorSwatch" tabindex="0" data-url="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_DE/Product-Variation?dwvar_3116_pv_rahmenfarbe=GN&amp;pid=3116&amp;quantity=undefined&amp;imageupdate=color" data-displayvalue="Green Vastness" data-tile-images="[{&quot;title&quot;:&quot;Spectral:ON CF 8&quot;,&quot;alt&quot;:&quot;Spectral:ON CF 8&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw84a1df8f/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_gn-gn_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw84a1df8f/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_gn-gn_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw84a1df8f/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_gn-gn_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw84a1df8f/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_gn-gn_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw84a1df8f/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_gn-gn_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw84a1df8f/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_gn-gn_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw84a1df8f/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_gn-gn_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F2F2F2&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dw84a1df8f/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_gn-gn_P5.png&quot;},&quot;found&quot;:true}]" data-tile-hover-images="[{&quot;title&quot;:&quot;Green Vastness&quot;,&quot;alt&quot;:&quot;Green Vastness&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;md&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/noimage.svg&quot;},&quot;found&quot;:false}]" data-pdp-url="https://www.canyon.com/en-de/electric-bikes/electric-mountain-bikes/spectral-on/spectral-on-cf/spectral-on-cf-8/3116.html?dwvar_3116_pv_rahmenfarbe=GN" data-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-AddToCompare?pid=50015564" data-remove-from-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-RemoveFromCompare?pid=50015564" data-compare-pid="50015564" title="Green Vastness" data-quickaddurl="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_DE/Tile-Variation?pid=3116&amp;dwvar_3116_pv_rahmenfarbe=GN" type="button">
<span class="colorSwatch__colorWrapper">
<span class="colorSwatch__color" style="color:#2b6932;"></span>
<span class="colorSwatch__color" style="color:#7fb87a;"></span>
</span>
</button>
 <span class="colorSwatch__colorLabel" role="tooltip">
<span class="colorSwatch__colorLabelText">
Color:
</span>
<span class="colorSwatch__colorLabelValue">
Green Vastness
</span>
</span>
</li>
<li class="colorPicker__colorListPlusItems">

</li>
</ul>
</div>
<div class="productTileCompare__wrapper">
<label class="productTileCompare__checkbox inputCheckbox js-compareWrapper">
<input type="checkbox" class="productTileCompare__checkboxInput inputCheckbox__input js-selectCompareProduct" aria-hidden="false" aria-label="Compare" tabindex="0" value="productCompareCheckbox" name="productCompareCheckbox" data-remove-pid-compare="50015562" data-compare-remove-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-RemoveFromCompare?pid=50015562" data-add-to-compare-url="/on/demandware.store/Sites-RoW-Site/en_DE/Product-AddToCompare?pid=50015562">
<span class="productTile__compareCheckboxLabel inputCheckbox__label">
<svg xmlns:xlink="http://www.w3.org/1999/xlink" class="icon icon-check2 inputCheckbox__icon" aria-hidden="false" focusable="false">
<use xlink:href="/on/demandware.static/Sites-RoW-Site/-/en_DE/v1680162459631/images/iconsNew.svg#sprite-check2"></use>
</svg>
<span class="inputCheckbox__labelInner">
Compare
</span>
</span>
</label>
</div>
</div>
<div class="productTileDefault__productNameWrapper">
<a title="Spectral:ON CF 8" class="productTileDefault__productName link " href="https://www.canyon.com/en-de/electric-bikes/electric-mountain-bikes/spectral-on/spectral-on-cf/spectral-on-cf-8/3116.html?dwvar_3116_pv_rahmenfarbe=BK" aria-hidden="false" tabindex="0" data-gtm-click="[{&quot;event&quot;:&quot;EEC-productClick&quot;,&quot;ecommerce&quot;:{&quot;click&quot;:{&quot;actionField&quot;:{&quot;list&quot;:&quot;&quot;},&quot;products&quot;:[{&quot;name&quot;:&quot;Spectral:ON CF 8&quot;,&quot;id&quot;:&quot;3116&quot;,&quot;brand&quot;:&quot;Canyon&quot;,&quot;category&quot;:&quot;E-Bikes/E-Mountain/Spectral:ON/Spectral:ON CF&quot;,&quot;variant&quot;:&quot;&quot;,&quot;dimension50&quot;:&quot;2022&quot;,&quot;dimension52&quot;:&quot;Spectral:ON&quot;,&quot;dimension63&quot;:&quot;unisex&quot;,&quot;dimension64&quot;:&quot;&quot;,&quot;dimension65&quot;:&quot;ZFER&quot;,&quot;dimension66&quot;:&quot;CompleteBikeMT EBIKE&quot;,&quot;dimension67&quot;:&quot;false&quot;,&quot;dimension68&quot;:&quot;true&quot;,&quot;feedProductId&quot;:&quot;50015567&quot;,&quot;dimension54&quot;:&quot;not defined&quot;,&quot;dimension51&quot;:&quot;Stealth&quot;,&quot;dimension53&quot;:&quot;L&quot;,&quot;quantity&quot;:&quot;&quot;,&quot;price&quot;:&quot;&quot;,&quot;metric4&quot;:&quot;&quot;,&quot;dimension56&quot;:&quot;not defined&quot;}]},&quot;currencyCode&quot;:&quot;EUR&quot;}},{&quot;event&quot;:&quot;select_item&quot;,&quot;event_name&quot;:&quot;Ecommerce - Select item&quot;,&quot;ecommerce&quot;:{&quot;items&quot;:[{&quot;item_id&quot;:&quot;3116&quot;,&quot;item_name&quot;:&quot;Spectral:ON CF 8&quot;,&quot;coupon&quot;:&quot;&quot;,&quot;currency&quot;:&quot;EUR&quot;,&quot;discount&quot;:&quot;&quot;,&quot;item_brand&quot;:&quot;Canyon&quot;,&quot;item_category&quot;:&quot;E-Bikes&quot;,&quot;item_category2&quot;:&quot;E-Mountain&quot;,&quot;item_category3&quot;:&quot;Spectral:ON&quot;,&quot;item_category4&quot;:&quot;Spectral:ON CF&quot;,&quot;item_variant&quot;:&quot;&quot;,&quot;price&quot;:&quot;&quot;,&quot;quantity&quot;:1}]}}]">
Spectral:ON CF 8
</a>
</div>
<div class="productTileDefault__infoWrapper">

<div class="productTileDefault__info productTileDefault__info--highlights">
Fox 36 Rhythm Grip, Shimano Steps EP8 Motor
</div>
</div>
</div>
<div class="productTileDefault__productSummaryBottom">
<div class="productTileDefault__price">
<div class="productTile__priceSale">
From 5.499 €
</div>
<div class="productTile__priceMonthly">
or from 85,61 €/Mo.
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
    assert len(res) == 2
    assert isinstance(res[0], Bike)
    assert res[0].id == 'spectral:on_cf_7_l'
    assert res[0].title == 'Spectral:ON CF 7'
    assert res[0].link == 'https://www.canyon.com/en-de/electric-bikes/electric-mountain-bikes/spectral-on/spectral-on-cf/spectral-on-cf-7/3117.html?dwvar_3117_pv_rahmenfarbe=WH'
    assert res[0].family == 'Spectral:ON'
    assert res[0].model == 'CF 7'
    assert res[0].size == 'L'
    assert res[1].id == 'spectral:on_cf_8_l'
    assert res[1].title == 'Spectral:ON CF 8'
    assert res[1].link == 'https://www.canyon.com/en-de/electric-bikes/electric-mountain-bikes/spectral-on/spectral-on-cf/spectral-on-cf-8/3116.html?dwvar_3116_pv_rahmenfarbe=BK'
    assert res[1].family == 'Spectral:ON'
    assert res[1].model == 'CF 8'
    assert res[1].size == 'L'


def test_parse_canyon_catalog_not_found():
    no_bike_tree = etree.HTML('<ul></ul>')

    res = _parse_canyon_catalog(no_bike_tree)

    assert len(res) == 0





