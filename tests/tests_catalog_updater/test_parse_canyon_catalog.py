from lxml import etree

from app.catalog.catalog_operations import parse_canyon_catalog
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
	    id: '3059',
	    sku: ''
	}];
	cq_params.categoryId = 'orderable-bikes';
	cq_params.refinements = '[{\"name\":\"isInStock\",\"value\":\"In-stock\"},{\"name\":\"masterAvailabilityFlag\",\"value\":\"1\"},{\"name\":\"Category\",\"value\":\"orderable-bikes\"}]';
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
		search_params.refs = '[{\"name\":\"isInStock\",\"value\":\"In-stock\"},{\"name\":\"masterAvailabilityFlag\",\"value\":\"1\"},{\"name\":\"Category\",\"value\":\"orderable-bikes\"}]';
		search_params.sort = 'sort_master_availability';
		search_params.imageUUID = '';
		search_params.searchID = 'd1cc81e7-8335-4d51-b749-30624d31b0bc';
		search_params.locale = 'en_CZ';
		search_params.queryLocale = 'en';
		search_params.showProducts = 'true';
		dw.ac.applyContext({category: "orderable-bikes", searchData: search_params});
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
dw.ac._capture({id: "3059", type: "searchhit"});
/* ]]> */
// -->
</script>
<div itemscope="" itemtype="http://schema.org/Product" data-pid="50016381" class="js-productTileWrapper productTile productTile--hasColorOptions productTile--bike js-ariaLabelChecked" data-gtm-impression="{&quot;event&quot;:&quot;EEC-productImpression&quot;,&quot;ecommerce&quot;:{&quot;currencyCode&quot;:&quot;CZK&quot;,&quot;impressions&quot;:[{&quot;name&quot;:&quot;Speedmax CF 8 Disc&quot;,&quot;id&quot;:&quot;3059&quot;,&quot;brand&quot;:&quot;Canyon&quot;,&quot;category&quot;:&quot;Road/Triathlon/Speedmax/Speedmax CF&quot;,&quot;variant&quot;:&quot;50016381&quot;,&quot;dimension50&quot;:&quot;2022&quot;,&quot;dimension52&quot;:&quot;Speedmax&quot;,&quot;dimension63&quot;:&quot;unisex&quot;,&quot;dimension64&quot;:&quot;&quot;,&quot;dimension65&quot;:&quot;ZFER&quot;,&quot;dimension66&quot;:&quot;Complete Bike TT&quot;,&quot;dimension67&quot;:&quot;false&quot;,&quot;feedProductId&quot;:&quot;50016381&quot;,&quot;dimension54&quot;:&quot;not defined&quot;,&quot;dimension51&quot;:&quot;Flash Yellow&quot;,&quot;dimension53&quot;:&quot;not defined&quot;,&quot;quantity&quot;:1,&quot;price&quot;:96114.88,&quot;metric4&quot;:116299,&quot;dimension56&quot;:&quot;not defined&quot;}]}}">
<div class="productTile__contentContainer">
<div class="productTile__contentWrapper">
<a title="Speedmax CF 8 Disc" aria-label="Speedmax CF 8 Disc Powermeter Price: 116.299,00 CZK" class="js-productTile productTile__link" href="https://www.canyon.com/en-cz/road-bikes/triathlon-bikes/speedmax/cf/speedmax-cf-8-disc/3059.html?dwvar_3059_pv_rahmenfarbe=YE%2FBK" aria-hidden="false" tabindex="0" itemprop="url" data-gtm-click="{&quot;event&quot;:&quot;EEC-productClick&quot;,&quot;ecommerce&quot;:{&quot;click&quot;:{&quot;actionField&quot;:{&quot;list&quot;:&quot;&quot;},&quot;products&quot;:[{&quot;name&quot;:&quot;Speedmax CF 8 Disc&quot;,&quot;id&quot;:&quot;3059&quot;,&quot;brand&quot;:&quot;Canyon&quot;,&quot;category&quot;:&quot;Road/Triathlon/Speedmax/Speedmax CF&quot;,&quot;variant&quot;:&quot;50016381&quot;,&quot;dimension50&quot;:&quot;2022&quot;,&quot;dimension52&quot;:&quot;Speedmax&quot;,&quot;dimension63&quot;:&quot;unisex&quot;,&quot;dimension64&quot;:&quot;&quot;,&quot;dimension65&quot;:&quot;ZFER&quot;,&quot;dimension66&quot;:&quot;Complete Bike TT&quot;,&quot;dimension67&quot;:&quot;false&quot;,&quot;feedProductId&quot;:&quot;50016381&quot;,&quot;dimension54&quot;:&quot;not defined&quot;,&quot;dimension51&quot;:&quot;Flash Yellow&quot;,&quot;dimension53&quot;:&quot;not defined&quot;,&quot;quantity&quot;:&quot;&quot;,&quot;price&quot;:96114.88,&quot;metric4&quot;:116299,&quot;dimension56&quot;:&quot;not defined&quot;}]},&quot;currencyCode&quot;:&quot;CZK&quot;}}">
<div class="productTile__content">
<div class="productTile__pictureWrapper">
<picture class="picture productTile__picture ">
<source media="(min-width: 1921px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<source media="(min-width: 1440px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<source media="(min-width: 1200px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<source media="(min-width: 992px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=460&amp;sh=345&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=460&amp;sh=345&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<source media="(min-width: 768px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=870&amp;sh=653&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=870&amp;sh=653&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<source media="(min-width: 534px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=673&amp;sh=505&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=673&amp;sh=505&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<source media="(min-width: 0px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=439&amp;sh=329&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=439&amp;sh=329&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<img title="Speedmax CF 8 Disc" alt="Speedmax CF 8 Disc" class="picture__image lazy productTile__image loaded" data-src="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=439&amp;sh=329&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" src="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=439&amp;sh=329&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" data-was-processed="true">
</picture>
<meta itemprop="image" content="https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.png">
</div>
</div>
</a>
<div class="productTile__contentOverlayTop">

<div class="productTile__badgeContainer">
<div class="eyebrow productTile__badge" aria-hidden="true">
Powermeter
</div>
</div>
</div>
<div class="productTile__contentOverlayBottom">
<div class="colorPicker__wrapper productTile__colorPickerWrapper">
<div class="js-memberAccessOnlyWrapper memberAccessMessage__wrapper productTile__memberAccessOnlyWrapper u-hide productTile__memberAccessOnlyWrapper--tileHasSwatches">
<div class="memberAccessMessage__content">
<div class="memberAccessMessage__row  productTile__memberAccessOnlyText  ">
<span class="memberAccessMessage__text">
Color only available to members.
<span class="memberAccessMessage__registerHereWrapper js-memberAccessRegisterHere" data-aria-label="Color only available to members.">
Register <span class="memberAccessMessage__registerLink link link--button js-memberAccessRegister" aria-hidden="false" tabindex="0" role="link" aria-label="Color only available to members. Register here.">here</span>.
</span>
</span>
</div>
</div>
</div>
<ul class="js-colorPicker colorPicker productTile__colorPicker ">
<li class="colorPicker__colorListItem ">
<button aria-hidden="false" aria-label="Stealth" class="colorSwatch colorSwatch--button colorSwatch--small js-product-color js-color-swatch colorPicker__colorSwatch" tabindex="0" data-url="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_CZ/Product-Variation?dwvar_3059_pv_rahmenfarbe=BK%2FSR&amp;pid=3059&amp;quantity=undefined&amp;imageupdate=color" data-displayvalue="Stealth" data-tile-images="[{&quot;title&quot;:&quot;Speedmax CF 8 Disc&quot;,&quot;alt&quot;:&quot;Speedmax CF 8 Disc&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw218f0498/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_bk-bk_P5.jpg?sw=439&amp;sh=329&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw218f0498/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_bk-bk_P5.jpg?sw=673&amp;sh=505&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw218f0498/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_bk-bk_P5.jpg?sw=870&amp;sh=653&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw218f0498/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_bk-bk_P5.jpg?sw=460&amp;sh=345&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw218f0498/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_bk-bk_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw218f0498/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_bk-bk_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw218f0498/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_bk-bk_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dw218f0498/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_bk-bk_P5.png&quot;},&quot;found&quot;:true}]" data-pdp-url="https://www.canyon.com/en-cz/road-bikes/triathlon-bikes/speedmax/cf/speedmax-cf-8-disc/3059.html?dwvar_3059_pv_rahmenfarbe=BK%2FSR" data-compare-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-AddToCompare?pid=50016372" data-remove-from-compare-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-RemoveFromCompare?pid=50016372" data-compare-pid="50016372" title="Stealth" type="button">
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
<button aria-hidden="false" aria-label="Flash Yellow" class="colorSwatch colorSwatch--button colorSwatch--small colorSwatch--selected js-noGtmClick js-product-color js-color-swatch colorPicker__colorSwatch" tabindex="0" data-url="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_CZ/Product-Variation?dwvar_3059_pv_rahmenfarbe=&amp;pid=3059&amp;quantity=undefined&amp;imageupdate=color" data-displayvalue="Flash Yellow" data-tile-images="[{&quot;title&quot;:&quot;Speedmax CF 8 Disc&quot;,&quot;alt&quot;:&quot;Speedmax CF 8 Disc&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=439&amp;sh=329&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=673&amp;sh=505&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=870&amp;sh=653&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=460&amp;sh=345&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.png&quot;},&quot;found&quot;:true}]" data-pdp-url="https://www.canyon.com/en-cz/road-bikes/triathlon-bikes/speedmax/cf/speedmax-cf-8-disc/3059.html?dwvar_3059_pv_rahmenfarbe=YE%2FBK" data-compare-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-AddToCompare?pid=50016377" data-remove-from-compare-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-RemoveFromCompare?pid=50016377" data-compare-pid="50016377" title="Flash Yellow" type="button">
<span class="colorSwatch__colorWrapper">
<span class="colorSwatch__color" style="color:#e2eb21;"></span>
<span class="colorSwatch__color" style="color:#3c3d3e;"></span>
</span>
</button>
<span class="colorSwatch__colorLabel" role="tooltip">
<span class="colorSwatch__colorLabelText">
Color:
</span>
<span class="colorSwatch__colorLabelValue">
Flash Yellow
</span>
</span>
</li>
</ul>
</div>
<div class="productTile__compareWrapper">
<label class="productTile__compareCheckbox inputCheckbox js-compareWrapper">
<input type="checkbox" class="productTile__compareCheckboxInput inputCheckbox__input js-selectCompareProduct" aria-hidden="false" aria-label="Compare" tabindex="0" value="productCompareCheckbox" name="productCompareCheckbox" data-remove-pid-compare="50016381" data-compare-remove-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-RemoveFromCompare?pid=50016381" data-add-to-compare-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-AddToCompare?pid=50016381">
<span class="productTile__compareCheckboxLabel inputCheckbox__label">
<span class="inputCheckbox__label--inner">
Compare
</span>
</span>
</label>
</div>
</div>
</div>
</div>
<div class="productTile__productSummary">
<div class="productTile__productSummaryLeft">
<meta itemprop="sku" content="50016381">
 <meta itemprop="mpn" content="50016381">
<meta itemprop="brand" content="Canyon">
<meta itemprop="description" content="Canyon - Exceptional ergonomics and rider-specific customisation come together with next-level aerodynamics to bring you world class-triathlon performance at an unbeatable value. Through thoughtful details like the top tube snake, bottom bracket toolkit and integrated bento box, the Speedmax CF 8 Disc comes out of the box ready for racing.">
<div class="productTile__productName" itemprop="name">
Speedmax CF 8 Disc
<sup class="productNameBadge productNameBadge--new">
New
</sup>
</div>
<div class="productTile__highlights">
Shimano Ultegra R8000 SS, DT Swiss ARC 1600
</div>
<div class="productTile__rating" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating">
<meta itemprop="ratingValue" content="5">
<meta itemprop="reviewCount" content="2">
<div class="productRating__container">
<div class="productRating__stars ratingStars" title="4,5 of 5 stars">
<div class="ratingStars__item">
<svg xmlns:xlink="http://www.w3.org/1999/xlink" class="icon icon-star2-filled ratingStars__icon ratingStars__icon--full" aria-hidden="false" focusable="false">
<use xlink:href="/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1651967522639/images/iconsNew.svg#sprite-star2-filled"></use>
</svg>
</div>
<div class="ratingStars__item">
<svg xmlns:xlink="http://www.w3.org/1999/xlink" class="icon icon-star2-filled ratingStars__icon ratingStars__icon--full" aria-hidden="false" focusable="false">
<use xlink:href="/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1651967522639/images/iconsNew.svg#sprite-star2-filled"></use>
</svg>
</div>
<div class="ratingStars__item">
<svg xmlns:xlink="http://www.w3.org/1999/xlink" class="icon icon-star2-filled ratingStars__icon ratingStars__icon--full" aria-hidden="false" focusable="false">
<use xlink:href="/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1651967522639/images/iconsNew.svg#sprite-star2-filled"></use>
</svg>
</div>
<div class="ratingStars__item">
<svg xmlns:xlink="http://www.w3.org/1999/xlink" class="icon icon-star2-filled ratingStars__icon ratingStars__icon--full" aria-hidden="false" focusable="false">
<use xlink:href="/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1651967522639/images/iconsNew.svg#sprite-star2-filled"></use>
</svg>
</div>
<div class="ratingStars__item">
<svg xmlns:xlink="http://www.w3.org/1999/xlink" class="icon icon-star2-filled ratingStars__icon ratingStars__icon--background" aria-hidden="false" focusable="false">
<use xlink:href="/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1651967522639/images/iconsNew.svg#sprite-star2-filled"></use>
</svg>
<svg xmlns:xlink="http://www.w3.org/1999/xlink" class="icon icon-star2-filled-half ratingStars__icon ratingStars__icon--half" aria-hidden="false" focusable="false">
<use xlink:href="/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1651967522639/images/iconsNew.svg#sprite-star2-filled-half"></use>
</svg>
</div>
</div>
<div class="productRating__reviewCount">
<div aria-hidden="false" class="link productRating__reviewCountButton js-trustpilotReviewPLPModalTrigger" tabindex="0" data-modal-open-param="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-TrustpilotReviews?pid=3059">
<span class="productRating__reviewCountButtonText">
<span class="productRating__reviewCountButtonCount">
(2)
</span>
</span>
</div>
</div>
</div>
</div>
</div>
<div class="productTile__productSummaryRight">
<div class="productTile__price" itemprop="offers" itemscope="" itemtype="http://schema.org/Offer">
<div class="productTile__priceSale">
116.299,00 CZK
</div>
<div class="productTile__priceMonthly">
or from 19.383,17 CZK/Mo.
</div>
<meta itemprop="price" content="116299.00">
<meta itemprop="priceCurrency" content="CZK">
<meta itemprop="url" content="https://www.canyon.com/en-cz/road-bikes/triathlon-bikes/speedmax/cf/speedmax-cf-8-disc/3059.html?dwvar_3059_pv_rahmenfarbe=YE%2FBK">
<meta itemprop="priceValidUntil" content="2022-05-08T08:51:27.957Z">
</div>
</div>
</div>
</div>
</li>
        '''
    )

    res = parse_canyon_catalog(one_bike_tree)

    assert isinstance(res, list)
    assert len(res) == 1
    assert isinstance(res[0], Bike)
    assert res[0].id == 'speedmax_cf_8_disc'
    assert res[0].title == 'Speedmax CF 8 Disc'
    assert res[0].link == 'https://www.canyon.com/en-cz/road-bikes/triathlon-bikes/speedmax/cf/speedmax-cf-8-disc/3059.html?dwvar_3059_pv_rahmenfarbe=YE%2FBK'
    assert res[0].family == 'Speedmax'
    assert res[0].model == 'CF 8 Disc'


def test_parse_canyon_catalog_few_bikes():
    few_bike_tree = etree.HTML(
        '''
        <ul>
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
	    id: '3059',
	    sku: ''
	}];
	cq_params.categoryId = 'orderable-bikes';
	cq_params.refinements = '[{\"name\":\"isInStock\",\"value\":\"In-stock\"},{\"name\":\"Category\",\"value\":\"orderable-bikes\"}]';
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
		search_params.refs = '[{\"name\":\"isInStock\",\"value\":\"In-stock\"},{\"name\":\"Category\",\"value\":\"orderable-bikes\"}]';
		search_params.sort = 'sort_master_availability';
		search_params.imageUUID = '';
		search_params.searchID = '429ec8fe-dec1-43eb-b9cd-0bed13ed4c13';
		search_params.locale = 'en_CZ';
		search_params.queryLocale = 'en';
		search_params.showProducts = 'true';
		dw.ac.applyContext({category: "orderable-bikes", searchData: search_params});
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
dw.ac._capture({id: "3059", type: "searchhit"});
/* ]]> */
// -->
</script>
<div itemscope="" itemtype="http://schema.org/Product" data-pid="50016381" class="js-productTileWrapper productTile productTile--hasColorOptions productTile--bike js-ariaLabelChecked" data-gtm-impression="{&quot;event&quot;:&quot;EEC-productImpression&quot;,&quot;ecommerce&quot;:{&quot;currencyCode&quot;:&quot;CZK&quot;,&quot;impressions&quot;:[{&quot;name&quot;:&quot;Speedmax CF 8 Disc&quot;,&quot;id&quot;:&quot;3059&quot;,&quot;brand&quot;:&quot;Canyon&quot;,&quot;category&quot;:&quot;Road/Triathlon/Speedmax/Speedmax CF&quot;,&quot;variant&quot;:&quot;50016381&quot;,&quot;dimension50&quot;:&quot;2022&quot;,&quot;dimension52&quot;:&quot;Speedmax&quot;,&quot;dimension63&quot;:&quot;unisex&quot;,&quot;dimension64&quot;:&quot;&quot;,&quot;dimension65&quot;:&quot;ZFER&quot;,&quot;dimension66&quot;:&quot;Complete Bike TT&quot;,&quot;dimension67&quot;:&quot;false&quot;,&quot;dimension68&quot;:&quot;false&quot;,&quot;feedProductId&quot;:&quot;50016381&quot;,&quot;dimension54&quot;:&quot;not defined&quot;,&quot;dimension51&quot;:&quot;Flash Yellow&quot;,&quot;dimension53&quot;:&quot;not defined&quot;,&quot;quantity&quot;:1,&quot;price&quot;:96114.88,&quot;metric4&quot;:116299,&quot;dimension56&quot;:&quot;not defined&quot;}]}}">
<div class="productTile__contentContainer">
<div class="productTile__contentWrapper">
<a title="Speedmax CF 8 Disc" aria-label="Speedmax CF 8 Disc Good Availability Price: 116.299,00 CZK" class="js-productTile productTile__link" href="https://www.canyon.com/en-cz/road-bikes/triathlon-bikes/speedmax/cf/speedmax-cf-8-disc/3059.html?dwvar_3059_pv_rahmenfarbe=YE%2FBK" aria-hidden="false" tabindex="0" itemprop="url" data-gtm-click="{&quot;event&quot;:&quot;EEC-productClick&quot;,&quot;ecommerce&quot;:{&quot;click&quot;:{&quot;actionField&quot;:{&quot;list&quot;:&quot;&quot;},&quot;products&quot;:[{&quot;name&quot;:&quot;Speedmax CF 8 Disc&quot;,&quot;id&quot;:&quot;3059&quot;,&quot;brand&quot;:&quot;Canyon&quot;,&quot;category&quot;:&quot;Road/Triathlon/Speedmax/Speedmax CF&quot;,&quot;variant&quot;:&quot;50016381&quot;,&quot;dimension50&quot;:&quot;2022&quot;,&quot;dimension52&quot;:&quot;Speedmax&quot;,&quot;dimension63&quot;:&quot;unisex&quot;,&quot;dimension64&quot;:&quot;&quot;,&quot;dimension65&quot;:&quot;ZFER&quot;,&quot;dimension66&quot;:&quot;Complete Bike TT&quot;,&quot;dimension67&quot;:&quot;false&quot;,&quot;dimension68&quot;:&quot;false&quot;,&quot;feedProductId&quot;:&quot;50016381&quot;,&quot;dimension54&quot;:&quot;not defined&quot;,&quot;dimension51&quot;:&quot;Flash Yellow&quot;,&quot;dimension53&quot;:&quot;not defined&quot;,&quot;quantity&quot;:&quot;&quot;,&quot;price&quot;:96114.88,&quot;metric4&quot;:116299,&quot;dimension56&quot;:&quot;not defined&quot;}]},&quot;currencyCode&quot;:&quot;CZK&quot;}}">
<div class="productTile__content">
<div class="productTile__pictureWrapper">
<picture class="picture productTile__picture ">
<source media="(min-width: 1921px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<source media="(min-width: 1440px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<source media="(min-width: 1200px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<source media="(min-width: 992px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=460&amp;sh=345&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=460&amp;sh=345&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<source media="(min-width: 768px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=870&amp;sh=653&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=870&amp;sh=653&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<source media="(min-width: 534px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=673&amp;sh=505&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=673&amp;sh=505&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<source media="(min-width: 0px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=439&amp;sh=329&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=439&amp;sh=329&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<img title="Speedmax CF 8 Disc" alt="Speedmax CF 8 Disc" class="picture__image lazy productTile__image loaded" data-src="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=439&amp;sh=329&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" src="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=439&amp;sh=329&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" data-was-processed="true">
</picture>
<meta itemprop="image" content="https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.png">
</div>
</div>
</a>
<div class="productTile__contentOverlayTop">
<div class="productTile__badgeContainer">
<div class="eyebrow productTile__badge" aria-hidden="true">
Good Availability
</div>
</div>
</div>
<div class="productTile__contentOverlayBottom">
<div class="colorPicker__wrapper productTile__colorPickerWrapper">
<div class="js-memberAccessOnlyWrapper memberAccessMessage__wrapper productTile__memberAccessOnlyWrapper u-hide productTile__memberAccessOnlyWrapper--tileHasSwatches">
<div class="memberAccessMessage__content">
<div class="memberAccessMessage__row  productTile__memberAccessOnlyText  ">
<span class="memberAccessMessage__text">
Color only available to members.
<span class="memberAccessMessage__registerHereWrapper js-memberAccessRegisterHere" data-aria-label="Color only available to members.">
Register <span class="memberAccessMessage__registerLink link link--button js-memberAccessRegister" aria-hidden="false" tabindex="0" role="link" aria-label="Color only available to members. Register here.">here</span>.
</span>
</span>
</div>
</div>
</div>
<ul class="js-colorPicker colorPicker productTile__colorPicker ">
<li class="colorPicker__colorListItem ">
<button aria-hidden="false" aria-label="Stealth" class="colorSwatch colorSwatch--button colorSwatch--small  js-product-color js-color-swatch colorPicker__colorSwatch" tabindex="0" data-url="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_CZ/Product-Variation?dwvar_3059_pv_rahmenfarbe=BK%2FSR&amp;pid=3059&amp;quantity=undefined&amp;imageupdate=color" data-displayvalue="Stealth" data-tile-images="[{&quot;title&quot;:&quot;Speedmax CF 8 Disc&quot;,&quot;alt&quot;:&quot;Speedmax CF 8 Disc&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw218f0498/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_bk-bk_P5.jpg?sw=439&amp;sh=329&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw218f0498/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_bk-bk_P5.jpg?sw=673&amp;sh=505&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw218f0498/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_bk-bk_P5.jpg?sw=870&amp;sh=653&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw218f0498/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_bk-bk_P5.jpg?sw=460&amp;sh=345&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw218f0498/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_bk-bk_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw218f0498/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_bk-bk_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw218f0498/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_bk-bk_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dw218f0498/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_bk-bk_P5.png&quot;},&quot;found&quot;:true}]" data-pdp-url="https://www.canyon.com/en-cz/road-bikes/triathlon-bikes/speedmax/cf/speedmax-cf-8-disc/3059.html?dwvar_3059_pv_rahmenfarbe=BK%2FSR" data-compare-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-AddToCompare?pid=50016372" data-remove-from-compare-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-RemoveFromCompare?pid=50016372" data-compare-pid="50016372" title="Stealth" type="button">
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
<button aria-hidden="false" aria-label="Flash Yellow" class="colorSwatch colorSwatch--button colorSwatch--small colorSwatch--selected js-noGtmClick js-product-color js-color-swatch colorPicker__colorSwatch" tabindex="0" data-url="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_CZ/Product-Variation?dwvar_3059_pv_rahmenfarbe=&amp;pid=3059&amp;quantity=undefined&amp;imageupdate=color" data-displayvalue="Flash Yellow" data-tile-images="[{&quot;title&quot;:&quot;Speedmax CF 8 Disc&quot;,&quot;alt&quot;:&quot;Speedmax CF 8 Disc&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=439&amp;sh=329&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=673&amp;sh=505&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=870&amp;sh=653&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=460&amp;sh=345&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.png&quot;},&quot;found&quot;:true}]" data-pdp-url="https://www.canyon.com/en-cz/road-bikes/triathlon-bikes/speedmax/cf/speedmax-cf-8-disc/3059.html?dwvar_3059_pv_rahmenfarbe=YE%2FBK" data-compare-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-AddToCompare?pid=50016377" data-remove-from-compare-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-RemoveFromCompare?pid=50016377" data-compare-pid="50016377" title="Flash Yellow" type="button">
<span class="colorSwatch__colorWrapper">
<span class="colorSwatch__color" style="color:#e2eb21;"></span>
<span class="colorSwatch__color" style="color:#3c3d3e;"></span>
</span>
</button>
<span class="colorSwatch__colorLabel" role="tooltip">
<span class="colorSwatch__colorLabelText">
 Color:
</span>
<span class="colorSwatch__colorLabelValue">
Flash Yellow
</span>
</span>
</li>
</ul>
</div>
<div class="productTile__compareWrapper">
<label class="productTile__compareCheckbox inputCheckbox js-compareWrapper">
<input type="checkbox" class="productTile__compareCheckboxInput inputCheckbox__input js-selectCompareProduct" aria-hidden="false" aria-label="Compare" tabindex="0" value="productCompareCheckbox" name="productCompareCheckbox" data-remove-pid-compare="50016381" data-compare-remove-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-RemoveFromCompare?pid=50016381" data-add-to-compare-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-AddToCompare?pid=50016381">
<span class="productTile__compareCheckboxLabel inputCheckbox__label">
<span class="inputCheckbox__label--inner">
Compare
</span>
</span>
</label>
</div>
</div>
</div>
</div>
<div class="productTile__productSummary">
<div class="productTile__productSummaryLeft">
<meta itemprop="sku" content="50016381">
<meta itemprop="mpn" content="50016381">
<meta itemprop="brand" content="Canyon">
<meta itemprop="description" content="Canyon - Exceptional ergonomics and rider-specific customisation come together with next-level aerodynamics to bring you world class-triathlon performance at an unbeatable value. Through thoughtful details like the top tube snake, bottom bracket toolkit and integrated bento box, the Speedmax CF 8 Disc comes out of the box ready for racing.">
<div class="productTile__productName" itemprop="name">
Speedmax CF 8 Disc
<sup class="productNameBadge productNameBadge--new">
New
</sup>
</div>
<div class="productTile__highlights">
Shimano Ultegra R8000 SS, DT Swiss ARC 1600
</div>
<div class="productTile__rating" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating">
<meta itemprop="ratingValue" content="5">
<meta itemprop="reviewCount" content="2">
<div class="productRating__container">
<div class="productRating__stars ratingStars" title="4,5 of 5 stars">
<div class="ratingStars__item">
<svg xmlns:xlink="http://www.w3.org/1999/xlink" class="icon icon-star2-filled ratingStars__icon ratingStars__icon--full" aria-hidden="false" focusable="false">
<use xlink:href="/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1652427939664/images/iconsNew.svg#sprite-star2-filled"></use>
</svg>
</div>
<div class="ratingStars__item">
<svg xmlns:xlink="http://www.w3.org/1999/xlink" class="icon icon-star2-filled ratingStars__icon ratingStars__icon--full" aria-hidden="false" focusable="false">
<use xlink:href="/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1652427939664/images/iconsNew.svg#sprite-star2-filled"></use>
</svg>
</div>
<div class="ratingStars__item">
<svg xmlns:xlink="http://www.w3.org/1999/xlink" class="icon icon-star2-filled ratingStars__icon ratingStars__icon--full" aria-hidden="false" focusable="false">
<use xlink:href="/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1652427939664/images/iconsNew.svg#sprite-star2-filled"></use>
</svg>
</div>
<div class="ratingStars__item">
<svg xmlns:xlink="http://www.w3.org/1999/xlink" class="icon icon-star2-filled ratingStars__icon ratingStars__icon--full" aria-hidden="false" focusable="false">
<use xlink:href="/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1652427939664/images/iconsNew.svg#sprite-star2-filled"></use>
</svg>
</div>
<div class="ratingStars__item">
<svg xmlns:xlink="http://www.w3.org/1999/xlink" class="icon icon-star2-filled ratingStars__icon ratingStars__icon--background" aria-hidden="false" focusable="false">
<use xlink:href="/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1652427939664/images/iconsNew.svg#sprite-star2-filled"></use>
</svg>
<svg xmlns:xlink="http://www.w3.org/1999/xlink" class="icon icon-star2-filled-half ratingStars__icon ratingStars__icon--half" aria-hidden="false" focusable="false">
<use xlink:href="/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1652427939664/images/iconsNew.svg#sprite-star2-filled-half"></use>
</svg>
</div>
</div>
<div class="productRating__reviewCount">
<div aria-hidden="false" class="link productRating__reviewCountButton js-trustpilotReviewPLPModalTrigger" tabindex="0" data-modal-open-param="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-TrustpilotReviews?pid=3059">
<span class="productRating__reviewCountButtonText">
<span class="productRating__reviewCountButtonCount">
(2)
</span>
</span>
</div>
</div>
</div>
</div>
</div>
<div class="productTile__productSummaryRight">
<div class="productTile__price" itemprop="offers" itemscope="" itemtype="http://schema.org/Offer">
<div class="productTile__priceSale">
116.299,00 CZK
</div>
<div class="productTile__priceMonthly">
or from 19.383,17 CZK/Mo.
</div>
<meta itemprop="price" content="116299.00">
<meta itemprop="priceCurrency" content="CZK">
<meta itemprop="url" content="https://www.canyon.com/en-cz/road-bikes/triathlon-bikes/speedmax/cf/speedmax-cf-8-disc/3059.html?dwvar_3059_pv_rahmenfarbe=YE%2FBK">
<meta itemprop="priceValidUntil" content="2022-05-13T12:00:36.533Z">
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
	    id: '3058',
	    sku: ''
	}];
	cq_params.categoryId = 'orderable-bikes';
	cq_params.refinements = '[{\"name\":\"isInStock\",\"value\":\"In-stock\"},{\"name\":\"Category\",\"value\":\"orderable-bikes\"}]';
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
		search_params.refs = '[{\"name\":\"isInStock\",\"value\":\"In-stock\"},{\"name\":\"Category\",\"value\":\"orderable-bikes\"}]';
		search_params.sort = 'sort_master_availability';
		search_params.imageUUID = '';
		search_params.searchID = '429ec8fe-dec1-43eb-b9cd-0bed13ed4c13';
		search_params.locale = 'en_CZ';
		search_params.queryLocale = 'en';
		search_params.showProducts = 'true';
		dw.ac.applyContext({category: "orderable-bikes", searchData: search_params});
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
dw.ac._capture({id: "3058", type: "searchhit"});
/* ]]> */
// -->
</script>
<div itemscope="" itemtype="http://schema.org/Product" data-pid="50016366" class="js-productTileWrapper productTile productTile--hasColorOptions productTile--bike js-ariaLabelChecked" data-gtm-impression="{&quot;event&quot;:&quot;EEC-productImpression&quot;,&quot;ecommerce&quot;:{&quot;currencyCode&quot;:&quot;CZK&quot;,&quot;impressions&quot;:[{&quot;name&quot;:&quot;Speedmax CF 7 Disc&quot;,&quot;id&quot;:&quot;3058&quot;,&quot;brand&quot;:&quot;Canyon&quot;,&quot;category&quot;:&quot;Road/Triathlon/Speedmax/Speedmax CF&quot;,&quot;variant&quot;:&quot;50016366&quot;,&quot;dimension50&quot;:&quot;2022&quot;,&quot;dimension52&quot;:&quot;Speedmax&quot;,&quot;dimension63&quot;:&quot;unisex&quot;,&quot;dimension64&quot;:&quot;&quot;,&quot;dimension65&quot;:&quot;ZFER&quot;,&quot;dimension66&quot;:&quot;Complete Bike TT&quot;,&quot;dimension67&quot;:&quot;false&quot;,&quot;dimension68&quot;:&quot;false&quot;,&quot;feedProductId&quot;:&quot;50016366&quot;,&quot;dimension54&quot;:&quot;not defined&quot;,&quot;dimension51&quot;:&quot;Stealth&quot;,&quot;dimension53&quot;:&quot;not defined&quot;,&quot;quantity&quot;:1,&quot;price&quot;:72147.93,&quot;metric4&quot;:87299,&quot;dimension56&quot;:&quot;not defined&quot;}]}}">
<div class="productTile__contentContainer">
<div class="productTile__contentWrapper">
<a title="Speedmax CF 7 Disc" aria-label="Speedmax CF 7 Disc Good Availability Price: 87.299,00 CZK" class="js-productTile productTile__link" href="https://www.canyon.com/en-cz/road-bikes/triathlon-bikes/speedmax/cf/speedmax-cf-7-disc/3058.html?dwvar_3058_pv_rahmenfarbe=BK%2FSR" aria-hidden="false" tabindex="0" itemprop="url" data-gtm-click="{&quot;event&quot;:&quot;EEC-productClick&quot;,&quot;ecommerce&quot;:{&quot;click&quot;:{&quot;actionField&quot;:{&quot;list&quot;:&quot;&quot;},&quot;products&quot;:[{&quot;name&quot;:&quot;Speedmax CF 7 Disc&quot;,&quot;id&quot;:&quot;3058&quot;,&quot;brand&quot;:&quot;Canyon&quot;,&quot;category&quot;:&quot;Road/Triathlon/Speedmax/Speedmax CF&quot;,&quot;variant&quot;:&quot;50016366&quot;,&quot;dimension50&quot;:&quot;2022&quot;,&quot;dimension52&quot;:&quot;Speedmax&quot;,&quot;dimension63&quot;:&quot;unisex&quot;,&quot;dimension64&quot;:&quot;&quot;,&quot;dimension65&quot;:&quot;ZFER&quot;,&quot;dimension66&quot;:&quot;Complete Bike TT&quot;,&quot;dimension67&quot;:&quot;false&quot;,&quot;dimension68&quot;:&quot;false&quot;,&quot;feedProductId&quot;:&quot;50016366&quot;,&quot;dimension54&quot;:&quot;not defined&quot;,&quot;dimension51&quot;:&quot;Stealth&quot;,&quot;dimension53&quot;:&quot;not defined&quot;,&quot;quantity&quot;:&quot;&quot;,&quot;price&quot;:72147.93,&quot;metric4&quot;:87299,&quot;dimension56&quot;:&quot;not defined&quot;}]},&quot;currencyCode&quot;:&quot;CZK&quot;}}">
<div class="productTile__content">
<div class="productTile__pictureWrapper">
<picture class="picture productTile__picture ">
<source media="(min-width: 1921px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwdb59880d/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_bk-sv_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwdb59880d/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_bk-sv_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<source media="(min-width: 1440px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwdb59880d/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_bk-sv_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwdb59880d/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_bk-sv_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<source media="(min-width: 1200px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwdb59880d/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_bk-sv_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwdb59880d/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_bk-sv_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<source media="(min-width: 992px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwdb59880d/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_bk-sv_P5.jpg?sw=460&amp;sh=345&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwdb59880d/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_bk-sv_P5.jpg?sw=460&amp;sh=345&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<source media="(min-width: 768px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwdb59880d/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_bk-sv_P5.jpg?sw=870&amp;sh=653&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwdb59880d/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_bk-sv_P5.jpg?sw=870&amp;sh=653&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<source media="(min-width: 534px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwdb59880d/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_bk-sv_P5.jpg?sw=673&amp;sh=505&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwdb59880d/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_bk-sv_P5.jpg?sw=673&amp;sh=505&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<source media="(min-width: 0px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwdb59880d/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_bk-sv_P5.jpg?sw=439&amp;sh=329&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwdb59880d/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_bk-sv_P5.jpg?sw=439&amp;sh=329&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<img title="Speedmax CF 7 Disc" alt="Speedmax CF 7 Disc" class="picture__image lazy productTile__image loaded" data-src="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwdb59880d/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_bk-sv_P5.jpg?sw=439&amp;sh=329&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" src="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwdb59880d/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_bk-sv_P5.jpg?sw=439&amp;sh=329&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" data-was-processed="true">
</picture>
<meta itemprop="image" content="https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dwdb59880d/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_bk-sv_P5.png">
</div>
</div>
</a>
<div class="productTile__contentOverlayTop">
<div class="productTile__badgeContainer">
<div class="eyebrow productTile__badge" aria-hidden="true">
Good Availability
</div>
</div>
</div>
<div class="productTile__contentOverlayBottom">
<div class="colorPicker__wrapper productTile__colorPickerWrapper">
<div class="js-memberAccessOnlyWrapper memberAccessMessage__wrapper productTile__memberAccessOnlyWrapper u-hide productTile__memberAccessOnlyWrapper--tileHasSwatches">
<div class="memberAccessMessage__content">
<div class="memberAccessMessage__row  productTile__memberAccessOnlyText  ">
<span class="memberAccessMessage__text">

Color only available to members.
<span class="memberAccessMessage__registerHereWrapper js-memberAccessRegisterHere" data-aria-label="Color only available to members.">
Register <span class="memberAccessMessage__registerLink link link--button js-memberAccessRegister" aria-hidden="false" tabindex="0" role="link" aria-label="Color only available to members. Register here.">here</span>.
</span>
</span>
</div>
</div>
</div>
<ul class="js-colorPicker colorPicker productTile__colorPicker ">
<li class="colorPicker__colorListItem ">
<button aria-hidden="false" aria-label="Stealth" class="colorSwatch colorSwatch--button colorSwatch--small colorSwatch--selected js-noGtmClick js-product-color js-color-swatch colorPicker__colorSwatch" tabindex="0" data-url="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_CZ/Product-Variation?dwvar_3058_pv_rahmenfarbe=&amp;pid=3058&amp;quantity=undefined&amp;imageupdate=color" data-displayvalue="Stealth" data-tile-images="[{&quot;title&quot;:&quot;Speedmax CF 7 Disc&quot;,&quot;alt&quot;:&quot;Speedmax CF 7 Disc&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwdb59880d/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_bk-sv_P5.jpg?sw=439&amp;sh=329&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwdb59880d/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_bk-sv_P5.jpg?sw=673&amp;sh=505&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwdb59880d/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_bk-sv_P5.jpg?sw=870&amp;sh=653&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwdb59880d/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_bk-sv_P5.jpg?sw=460&amp;sh=345&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwdb59880d/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_bk-sv_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwdb59880d/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_bk-sv_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwdb59880d/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_bk-sv_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dwdb59880d/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_bk-sv_P5.png&quot;},&quot;found&quot;:true}]" data-pdp-url="https://www.canyon.com/en-cz/road-bikes/triathlon-bikes/speedmax/cf/speedmax-cf-7-disc/3058.html?dwvar_3058_pv_rahmenfarbe=BK%2FSR" data-compare-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-AddToCompare?pid=50016366" data-remove-from-compare-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-RemoveFromCompare?pid=50016366" data-compare-pid="50016366" title="Stealth" type="button">
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
<button aria-hidden="false" aria-label="Flash Yellow" class="colorSwatch colorSwatch--button colorSwatch--small  js-product-color js-color-swatch colorPicker__colorSwatch" tabindex="0" data-url="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_CZ/Product-Variation?dwvar_3058_pv_rahmenfarbe=YE%2FBK&amp;pid=3058&amp;quantity=undefined&amp;imageupdate=color" data-displayvalue="Flash Yellow" data-tile-images="[{&quot;title&quot;:&quot;Speedmax CF 7 Disc&quot;,&quot;alt&quot;:&quot;Speedmax CF 7 Disc&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw72127547/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_ye-bk_P5.jpg?sw=439&amp;sh=329&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw72127547/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_ye-bk_P5.jpg?sw=673&amp;sh=505&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw72127547/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_ye-bk_P5.jpg?sw=870&amp;sh=653&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw72127547/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_ye-bk_P5.jpg?sw=460&amp;sh=345&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw72127547/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_ye-bk_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw72127547/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_ye-bk_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw72127547/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_ye-bk_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dw72127547/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_ye-bk_P5.png&quot;},&quot;found&quot;:true}]" data-pdp-url="https://www.canyon.com/en-cz/road-bikes/triathlon-bikes/speedmax/cf/speedmax-cf-7-disc/3058.html?dwvar_3058_pv_rahmenfarbe=YE%2FBK" data-compare-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-AddToCompare?pid=50016367" data-remove-from-compare-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-RemoveFromCompare?pid=50016367" data-compare-pid="50016367" title="Flash Yellow" type="button">
<span class="colorSwatch__colorWrapper">
<span class="colorSwatch__color" style="color:#e2eb21;"></span>
<span class="colorSwatch__color" style="color:#3c3d3e;"></span>
</span>
</button>
<span class="colorSwatch__colorLabel" role="tooltip">
<span class="colorSwatch__colorLabelText">
Color:
</span>
<span class="colorSwatch__colorLabelValue">
Flash Yellow
</span>
</span>
</li>
</ul>
</div>
<div class="productTile__compareWrapper">
<label class="productTile__compareCheckbox inputCheckbox js-compareWrapper">
<input type="checkbox" class="productTile__compareCheckboxInput inputCheckbox__input js-selectCompareProduct" aria-hidden="false" aria-label="Compare" tabindex="0" value="productCompareCheckbox" name="productCompareCheckbox" data-remove-pid-compare="50016366" data-compare-remove-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-RemoveFromCompare?pid=50016366" data-add-to-compare-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-AddToCompare?pid=50016366">
<span class="productTile__compareCheckboxLabel inputCheckbox__label">
<span class="inputCheckbox__label--inner">
Compare
</span>
</span>
</label>
</div>
</div>
</div>
</div>
<div class="productTile__productSummary">
<div class="productTile__productSummaryLeft">
<meta itemprop="sku" content="50016366">
<meta itemprop="mpn" content="50016366">
<meta itemprop="brand" content="Canyon">
<meta itemprop="description" content="Canyon - Drawing on the world-level performance DNA of the flagship Speedmax CFR, the Speedmax CF 7 Disc offers superb speed and unprecedented adjustability to newcomers and experienced racers alike thanks to its clever, integrated solutions and one-of-a-kind frame.">
<div class="productTile__productName" itemprop="name">
Speedmax CF 7 Disc
<sup class="productNameBadge productNameBadge--new">
New
</sup>
</div>
<div class="productTile__highlights">
Shimano 105 R7000 SS, DT Swiss P 1800 Spline db
</div>

<div class="productTile__rating" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating">
<meta itemprop="ratingValue" content="5">
<meta itemprop="reviewCount" content="2">
<div class="productRating__container">
<div class="productRating__stars ratingStars" title="5 of 5 stars">
<div class="ratingStars__item">
<svg xmlns:xlink="http://www.w3.org/1999/xlink" class="icon icon-star2-filled ratingStars__icon ratingStars__icon--full" aria-hidden="false" focusable="false">
<use xlink:href="/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1652427939664/images/iconsNew.svg#sprite-star2-filled"></use>
</svg>
</div>
<div class="ratingStars__item">
<svg xmlns:xlink="http://www.w3.org/1999/xlink" class="icon icon-star2-filled ratingStars__icon ratingStars__icon--full" aria-hidden="false" focusable="false">
<use xlink:href="/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1652427939664/images/iconsNew.svg#sprite-star2-filled"></use>
</svg>
</div>
<div class="ratingStars__item">
<svg xmlns:xlink="http://www.w3.org/1999/xlink" class="icon icon-star2-filled ratingStars__icon ratingStars__icon--full" aria-hidden="false" focusable="false">
<use xlink:href="/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1652427939664/images/iconsNew.svg#sprite-star2-filled"></use>
</svg>
</div>
<div class="ratingStars__item">
<svg xmlns:xlink="http://www.w3.org/1999/xlink" class="icon icon-star2-filled ratingStars__icon ratingStars__icon--full" aria-hidden="false" focusable="false">
<use xlink:href="/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1652427939664/images/iconsNew.svg#sprite-star2-filled"></use>
</svg>
</div>
<div class="ratingStars__item">
<svg xmlns:xlink="http://www.w3.org/1999/xlink" class="icon icon-star2-filled ratingStars__icon ratingStars__icon--full" aria-hidden="false" focusable="false">
<use xlink:href="/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1652427939664/images/iconsNew.svg#sprite-star2-filled"></use>
</svg>
</div>
</div>
<div class="productRating__reviewCount">
<div aria-hidden="false" class="link productRating__reviewCountButton js-trustpilotReviewPLPModalTrigger" tabindex="0" data-modal-open-param="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-TrustpilotReviews?pid=3058">
<span class="productRating__reviewCountButtonText">
<span class="productRating__reviewCountButtonCount">
(2)
</span>
</span>
</div>
</div>
</div>
</div>
</div>
<div class="productTile__productSummaryRight">
<div class="productTile__price" itemprop="offers" itemscope="" itemtype="http://schema.org/Offer">
<div class="productTile__priceSale">
87.299,00 CZK
</div>

<div class="productTile__priceMonthly">
or from 14.549,83 CZK/Mo.
</div>
<meta itemprop="price" content="87299.00">
<meta itemprop="priceCurrency" content="CZK">
<meta itemprop="url" content="https://www.canyon.com/en-cz/road-bikes/triathlon-bikes/speedmax/cf/speedmax-cf-7-disc/3058.html?dwvar_3058_pv_rahmenfarbe=BK%2FSR">
<meta itemprop="priceValidUntil" content="2022-05-13T12:00:36.853Z">
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
	    id: '3179',
	    sku: ''
	}];
	cq_params.categoryId = 'orderable-bikes';
	cq_params.refinements = '[{\"name\":\"isInStock\",\"value\":\"In-stock\"},{\"name\":\"Category\",\"value\":\"orderable-bikes\"}]';
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
		search_params.refs = '[{\"name\":\"isInStock\",\"value\":\"In-stock\"},{\"name\":\"Category\",\"value\":\"orderable-bikes\"}]';
		search_params.sort = 'sort_master_availability';
		search_params.imageUUID = '';
		search_params.searchID = '429ec8fe-dec1-43eb-b9cd-0bed13ed4c13';
		search_params.locale = 'en_CZ';
		search_params.queryLocale = 'en';
		search_params.showProducts = 'true';
		dw.ac.applyContext({category: "orderable-bikes", searchData: search_params});
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
dw.ac._capture({id: "3179", type: "searchhit"});
/* ]]> */
// -->
</script>
<div itemscope="" itemtype="http://schema.org/Product" data-pid="50016343" class="js-productTileWrapper productTile productTile--hasColorOptions productTile--bike js-ariaLabelChecked" data-gtm-impression="{&quot;event&quot;:&quot;EEC-productImpression&quot;,&quot;ecommerce&quot;:{&quot;currencyCode&quot;:&quot;CZK&quot;,&quot;impressions&quot;:[{&quot;name&quot;:&quot;Spectral 125 CF 9&quot;,&quot;id&quot;:&quot;3179&quot;,&quot;brand&quot;:&quot;Canyon&quot;,&quot;category&quot;:&quot;Mountain/Trail/Spectral 125/Spectral 125 CF&quot;,&quot;variant&quot;:&quot;50016343&quot;,&quot;dimension50&quot;:&quot;2022&quot;,&quot;dimension52&quot;:&quot;Spectral 125&quot;,&quot;dimension63&quot;:&quot;unisex&quot;,&quot;dimension64&quot;:&quot;&quot;,&quot;dimension65&quot;:&quot;ZFER&quot;,&quot;dimension66&quot;:&quot;Complete Bike MTB&quot;,&quot;dimension67&quot;:&quot;false&quot;,&quot;dimension68&quot;:&quot;false&quot;,&quot;feedProductId&quot;:&quot;50016343&quot;,&quot;dimension54&quot;:&quot;not defined&quot;,&quot;dimension51&quot;:&quot;Funkturm Grey&quot;,&quot;dimension53&quot;:&quot;not defined&quot;,&quot;quantity&quot;:1,&quot;price&quot;:126776.03,&quot;metric4&quot;:153399,&quot;dimension56&quot;:&quot;not defined&quot;}]}}">
<div class="productTile__contentContainer">
<div class="productTile__contentWrapper">
<a title="Spectral 125 CF 9" aria-label="Spectral 125 CF 9 Good Availability Price: 153.399,00 CZK" class="js-productTile productTile__link" href="https://www.canyon.com/en-cz/mountain-bikes/trail-bikes/spectral-125/cf/spectral-125-cf-9/3179.html?dwvar_3179_pv_rahmenfarbe=SR" aria-hidden="false" tabindex="0" itemprop="url" data-gtm-click="{&quot;event&quot;:&quot;EEC-productClick&quot;,&quot;ecommerce&quot;:{&quot;click&quot;:{&quot;actionField&quot;:{&quot;list&quot;:&quot;&quot;},&quot;products&quot;:[{&quot;name&quot;:&quot;Spectral 125 CF 9&quot;,&quot;id&quot;:&quot;3179&quot;,&quot;brand&quot;:&quot;Canyon&quot;,&quot;category&quot;:&quot;Mountain/Trail/Spectral 125/Spectral 125 CF&quot;,&quot;variant&quot;:&quot;50016343&quot;,&quot;dimension50&quot;:&quot;2022&quot;,&quot;dimension52&quot;:&quot;Spectral 125&quot;,&quot;dimension63&quot;:&quot;unisex&quot;,&quot;dimension64&quot;:&quot;&quot;,&quot;dimension65&quot;:&quot;ZFER&quot;,&quot;dimension66&quot;:&quot;Complete Bike MTB&quot;,&quot;dimension67&quot;:&quot;false&quot;,&quot;dimension68&quot;:&quot;false&quot;,&quot;feedProductId&quot;:&quot;50016343&quot;,&quot;dimension54&quot;:&quot;not defined&quot;,&quot;dimension51&quot;:&quot;Funkturm Grey&quot;,&quot;dimension53&quot;:&quot;not defined&quot;,&quot;quantity&quot;:&quot;&quot;,&quot;price&quot;:126776.03,&quot;metric4&quot;:153399,&quot;dimension56&quot;:&quot;not defined&quot;}]},&quot;currencyCode&quot;:&quot;CZK&quot;}}">
<div class="productTile__content">
<div class="productTile__pictureWrapper">
<picture class="picture productTile__picture ">
<source media="(min-width: 1921px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw0711eea4/images/full/full_2022_/2022/full_2022_spectral-125-cf-9_3179_si_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw0711eea4/images/full/full_2022_/2022/full_2022_spectral-125-cf-9_3179_si_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<source media="(min-width: 1440px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw0711eea4/images/full/full_2022_/2022/full_2022_spectral-125-cf-9_3179_si_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw0711eea4/images/full/full_2022_/2022/full_2022_spectral-125-cf-9_3179_si_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<source media="(min-width: 1200px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw0711eea4/images/full/full_2022_/2022/full_2022_spectral-125-cf-9_3179_si_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw0711eea4/images/full/full_2022_/2022/full_2022_spectral-125-cf-9_3179_si_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<source media="(min-width: 992px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw0711eea4/images/full/full_2022_/2022/full_2022_spectral-125-cf-9_3179_si_P5.jpg?sw=460&amp;sh=345&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw0711eea4/images/full/full_2022_/2022/full_2022_spectral-125-cf-9_3179_si_P5.jpg?sw=460&amp;sh=345&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<source media="(min-width: 768px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw0711eea4/images/full/full_2022_/2022/full_2022_spectral-125-cf-9_3179_si_P5.jpg?sw=870&amp;sh=653&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw0711eea4/images/full/full_2022_/2022/full_2022_spectral-125-cf-9_3179_si_P5.jpg?sw=870&amp;sh=653&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<source media="(min-width: 534px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw0711eea4/images/full/full_2022_/2022/full_2022_spectral-125-cf-9_3179_si_P5.jpg?sw=673&amp;sh=505&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw0711eea4/images/full/full_2022_/2022/full_2022_spectral-125-cf-9_3179_si_P5.jpg?sw=673&amp;sh=505&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<source media="(min-width: 0px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw0711eea4/images/full/full_2022_/2022/full_2022_spectral-125-cf-9_3179_si_P5.jpg?sw=439&amp;sh=329&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw0711eea4/images/full/full_2022_/2022/full_2022_spectral-125-cf-9_3179_si_P5.jpg?sw=439&amp;sh=329&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<img title="Spectral 125 CF 9" alt="Spectral 125 CF 9" class="picture__image lazy productTile__image loaded" data-src="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw0711eea4/images/full/full_2022_/2022/full_2022_spectral-125-cf-9_3179_si_P5.jpg?sw=439&amp;sh=329&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" src="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw0711eea4/images/full/full_2022_/2022/full_2022_spectral-125-cf-9_3179_si_P5.jpg?sw=439&amp;sh=329&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" data-was-processed="true">
</picture>
<meta itemprop="image" content="https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dw0711eea4/images/full/full_2022_/2022/full_2022_spectral-125-cf-9_3179_si_P5.png">
</div>
</div>
</a>
<div class="productTile__contentOverlayTop">
<div class="productTile__badgeContainer">
<div class="eyebrow productTile__badge" aria-hidden="true">
Good Availability
</div>
</div>
<div class="productTile__awardImageWrapper">
<img class="productTile__awardImage loaded" alt="Award: Spectral 125 CF 9" title="Award: Spectral 125 CF 9" data-src="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw365e2c1d/images/awards/mtb/Spectral125_PD2022_BoB_bicycle.png?sw=180" src="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw365e2c1d/images/awards/mtb/Spectral125_PD2022_BoB_bicycle.png?sw=180" data-was-processed="true">
</div>
</div>
<div class="productTile__contentOverlayBottom">
<div class="colorPicker__wrapper productTile__colorPickerWrapper">
<div class="js-memberAccessOnlyWrapper memberAccessMessage__wrapper productTile__memberAccessOnlyWrapper u-hide productTile__memberAccessOnlyWrapper--tileHasSwatches">
<div class="memberAccessMessage__content">
<div class="memberAccessMessage__row  productTile__memberAccessOnlyText  ">
<span class="memberAccessMessage__text">
Color only available to members.
<span class="memberAccessMessage__registerHereWrapper js-memberAccessRegisterHere" data-aria-label="Color only available to members.">
Register <span class="memberAccessMessage__registerLink link link--button js-memberAccessRegister" aria-hidden="false" tabindex="0" role="link" aria-label="Color only available to members. Register here.">here</span>.
</span>
</span>
</div>
</div>
</div>

<ul class="js-colorPicker colorPicker productTile__colorPicker ">
<li class="colorPicker__colorListItem ">
<button aria-hidden="false" aria-label="Funkturm Grey" class="colorSwatch colorSwatch--button colorSwatch--small colorSwatch--selected js-noGtmClick js-product-color js-color-swatch colorPicker__colorSwatch" tabindex="0" data-url="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_CZ/Product-Variation?dwvar_3179_pv_rahmenfarbe=&amp;pid=3179&amp;quantity=undefined&amp;imageupdate=color" data-displayvalue="Funkturm Grey" data-tile-images="[{&quot;title&quot;:&quot;Spectral 125 CF 9&quot;,&quot;alt&quot;:&quot;Spectral 125 CF 9&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw0711eea4/images/full/full_2022_/2022/full_2022_spectral-125-cf-9_3179_si_P5.jpg?sw=439&amp;sh=329&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw0711eea4/images/full/full_2022_/2022/full_2022_spectral-125-cf-9_3179_si_P5.jpg?sw=673&amp;sh=505&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw0711eea4/images/full/full_2022_/2022/full_2022_spectral-125-cf-9_3179_si_P5.jpg?sw=870&amp;sh=653&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw0711eea4/images/full/full_2022_/2022/full_2022_spectral-125-cf-9_3179_si_P5.jpg?sw=460&amp;sh=345&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw0711eea4/images/full/full_2022_/2022/full_2022_spectral-125-cf-9_3179_si_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw0711eea4/images/full/full_2022_/2022/full_2022_spectral-125-cf-9_3179_si_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw0711eea4/images/full/full_2022_/2022/full_2022_spectral-125-cf-9_3179_si_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dw0711eea4/images/full/full_2022_/2022/full_2022_spectral-125-cf-9_3179_si_P5.png&quot;},&quot;found&quot;:true}]" data-pdp-url="https://www.canyon.com/en-cz/mountain-bikes/trail-bikes/spectral-125/cf/spectral-125-cf-9/3179.html?dwvar_3179_pv_rahmenfarbe=SR" data-compare-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-AddToCompare?pid=50016340" data-remove-from-compare-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-RemoveFromCompare?pid=50016340" data-compare-pid="50016340" title="Funkturm Grey" type="button">
<span class="colorSwatch__colorWrapper">
<span class="colorSwatch__color" style="color:#e1e1e1;"></span>
<span class="colorSwatch__color" style="color:#c6c6c6;"></span>
</span>
</button>
<span class="colorSwatch__colorLabel" role="tooltip">
<span class="colorSwatch__colorLabelText">
Color:
</span>
<span class="colorSwatch__colorLabelValue">
Funkturm Grey
</span>
</span>
</li>
<li class="colorPicker__colorListItem ">
<button aria-hidden="false" aria-label="Big Bamboo" class="colorSwatch colorSwatch--button colorSwatch--small  js-product-color js-color-swatch colorPicker__colorSwatch" tabindex="0" data-url="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_CZ/Product-Variation?dwvar_3179_pv_rahmenfarbe=GN&amp;pid=3179&amp;quantity=undefined&amp;imageupdate=color" data-displayvalue="Big Bamboo" data-tile-images="[{&quot;title&quot;:&quot;Spectral 125 CF 9&quot;,&quot;alt&quot;:&quot;Spectral 125 CF 9&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwd0a733dc/images/full/full_2022_/2022/full_2022_spectral-125-cf-9_3179_gn_P5.jpg?sw=439&amp;sh=329&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwd0a733dc/images/full/full_2022_/2022/full_2022_spectral-125-cf-9_3179_gn_P5.jpg?sw=673&amp;sh=505&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwd0a733dc/images/full/full_2022_/2022/full_2022_spectral-125-cf-9_3179_gn_P5.jpg?sw=870&amp;sh=653&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwd0a733dc/images/full/full_2022_/2022/full_2022_spectral-125-cf-9_3179_gn_P5.jpg?sw=460&amp;sh=345&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwd0a733dc/images/full/full_2022_/2022/full_2022_spectral-125-cf-9_3179_gn_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwd0a733dc/images/full/full_2022_/2022/full_2022_spectral-125-cf-9_3179_gn_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwd0a733dc/images/full/full_2022_/2022/full_2022_spectral-125-cf-9_3179_gn_P5.jpg?sw=540&amp;sh=405&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dwd0a733dc/images/full/full_2022_/2022/full_2022_spectral-125-cf-9_3179_gn_P5.png&quot;},&quot;found&quot;:true}]" data-pdp-url="https://www.canyon.com/en-cz/mountain-bikes/trail-bikes/spectral-125/cf/spectral-125-cf-9/3179.html?dwvar_3179_pv_rahmenfarbe=GN" data-compare-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-AddToCompare?pid=50016344" data-remove-from-compare-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-RemoveFromCompare?pid=50016344" data-compare-pid="50016344" title="Big Bamboo" type="button">
<span class="colorSwatch__colorWrapper">
<span class="colorSwatch__color" style="color:#99a575;"></span>
<span class="colorSwatch__color" style="color:#464d3d;"></span>
</span>
</button>
<span class="colorSwatch__colorLabel" role="tooltip">
<span class="colorSwatch__colorLabelText">
Color:
</span>
<span class="colorSwatch__colorLabelValue">
Big Bamboo
</span>
</span>
</li>
</ul>
</div>
<div class="productTile__compareWrapper">
<label class="productTile__compareCheckbox inputCheckbox js-compareWrapper">
<input type="checkbox" class="productTile__compareCheckboxInput inputCheckbox__input js-selectCompareProduct" aria-hidden="false" aria-label="Compare" tabindex="0" value="productCompareCheckbox" name="productCompareCheckbox" data-remove-pid-compare="50016343" data-compare-remove-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-RemoveFromCompare?pid=50016343" data-add-to-compare-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-AddToCompare?pid=50016343">
<span class="productTile__compareCheckboxLabel inputCheckbox__label">
<span class="inputCheckbox__label--inner">
Compare
</span>
</span>
</label>
</div>
</div>
</div>
</div>
<div class="productTile__productSummary">
<div class="productTile__productSummaryLeft">
<meta itemprop="sku" content="50016343">
<meta itemprop="mpn" content="50016343">
<meta itemprop="brand" content="Canyon">
<meta itemprop="description" content="Canyon - Experience pure trail riding fun. The Spectral 125 CF 9 combines the headline advantages of the Spectral 29 – progressive geometry and incredible versatility – with a low overall weight and even more efficient climbing.">
<div class="productTile__productName" itemprop="name">
Spectral 125 CF 9
<sup class="productNameBadge productNameBadge--new">
New
</sup>
</div>
<div class="productTile__highlights">
SRAM GX Eagle AXS 12s, FOX 36 Factory
</div>
<div class="productTile__rating" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating">
<meta itemprop="ratingValue" content="5">
<meta itemprop="reviewCount" content="2">
<div class="productRating__container">
<div class="productRating__stars ratingStars" title="5 of 5 stars">
<div class="ratingStars__item">
<svg xmlns:xlink="http://www.w3.org/1999/xlink" class="icon icon-star2-filled ratingStars__icon ratingStars__icon--full" aria-hidden="false" focusable="false">
<use xlink:href="/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1652427939664/images/iconsNew.svg#sprite-star2-filled"></use>
</svg>
</div>
<div class="ratingStars__item">
<svg xmlns:xlink="http://www.w3.org/1999/xlink" class="icon icon-star2-filled ratingStars__icon ratingStars__icon--full" aria-hidden="false" focusable="false">
<use xlink:href="/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1652427939664/images/iconsNew.svg#sprite-star2-filled"></use>
</svg>
</div>
<div class="ratingStars__item">
<svg xmlns:xlink="http://www.w3.org/1999/xlink" class="icon icon-star2-filled ratingStars__icon ratingStars__icon--full" aria-hidden="false" focusable="false">
<use xlink:href="/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1652427939664/images/iconsNew.svg#sprite-star2-filled"></use>
</svg>
</div>
<div class="ratingStars__item">
<svg xmlns:xlink="http://www.w3.org/1999/xlink" class="icon icon-star2-filled ratingStars__icon ratingStars__icon--full" aria-hidden="false" focusable="false">
<use xlink:href="/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1652427939664/images/iconsNew.svg#sprite-star2-filled"></use>
</svg>
</div>
<div class="ratingStars__item">
<svg xmlns:xlink="http://www.w3.org/1999/xlink" class="icon icon-star2-filled ratingStars__icon ratingStars__icon--full" aria-hidden="false" focusable="false">
<use xlink:href="/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1652427939664/images/iconsNew.svg#sprite-star2-filled"></use>
</svg>
</div>
</div>
<div class="productRating__reviewCount">
<div aria-hidden="false" class="link productRating__reviewCountButton js-trustpilotReviewPLPModalTrigger" tabindex="0" data-modal-open-param="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-TrustpilotReviews?pid=3179">
<span class="productRating__reviewCountButtonText">
<span class="productRating__reviewCountButtonCount">
(2)
</span>
</span>
</div>
</div>
</div>
</div>
</div>
<div class="productTile__productSummaryRight">
<div class="productTile__price" itemprop="offers" itemscope="" itemtype="http://schema.org/Offer">
<div class="productTile__priceSale">
153.399,00 CZK
</div>
<div class="productTile__priceMonthly">
or from 25.566,50 CZK/Mo.
</div>
<meta itemprop="price" content="153399.00">
<meta itemprop="priceCurrency" content="CZK">
<meta itemprop="url" content="https://www.canyon.com/en-cz/mountain-bikes/trail-bikes/spectral-125/cf/spectral-125-cf-9/3179.html?dwvar_3179_pv_rahmenfarbe=SR">
<meta itemprop="priceValidUntil" content="2022-05-13T12:00:37.131Z">
</div>
</div>
</div>
</div>
</li>
        </ul>
        '''
    )

    res = parse_canyon_catalog(few_bike_tree)

    assert len(res) == 3
    assert res[0].id == 'speedmax_cf_8_disc'
    assert res[1].id == 'speedmax_cf_7_disc'
    assert res[2].id == 'spectral_125_cf_9'
    assert res[0].title == 'Speedmax CF 8 Disc'
    assert res[1].title == 'Speedmax CF 7 Disc'
    assert res[2].title == 'Spectral 125 CF 9'
    assert res[0].link == 'https://www.canyon.com/en-cz/road-bikes/triathlon-bikes/speedmax/cf/speedmax-cf-8-disc/3059.html?dwvar_3059_pv_rahmenfarbe=YE%2FBK'
    assert res[1].link == 'https://www.canyon.com/en-cz/road-bikes/triathlon-bikes/speedmax/cf/speedmax-cf-7-disc/3058.html?dwvar_3058_pv_rahmenfarbe=BK%2FSR'
    assert res[2].link == 'https://www.canyon.com/en-cz/mountain-bikes/trail-bikes/spectral-125/cf/spectral-125-cf-9/3179.html?dwvar_3179_pv_rahmenfarbe=SR'
    assert res[0].family == 'Speedmax'
    assert res[1].family == 'Speedmax'
    assert res[2].family == 'Spectral'
    assert res[0].model == 'CF 8 Disc'
    assert res[1].model == 'CF 7 Disc'
    assert res[2].model == '125 CF 9'


def test_parse_canyon_catalog_not_found():
    no_bike_tree = etree.HTML('<ul></ul>')

    res = parse_canyon_catalog(no_bike_tree)

    assert len(res) == 0



