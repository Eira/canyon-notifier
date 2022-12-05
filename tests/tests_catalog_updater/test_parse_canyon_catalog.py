from lxml import etree

from app.catalog.catalog_operations import _parse_canyon_catalog
from app.models import Bike


def test_parse_canyon_catalog_one_bike():
    one_bike_tree = etree.HTML(
        '''
    <li class="productGrid__listItem xlt-producttile">
    <div data-pid="50015563" class="js-productTileWrapper productTileDefault productTileDefault--bike link-already-checked" data-gtm-impression="[{&quot;event&quot;:&quot;EEC-productImpression&quot;,&quot;ecommerce&quot;:{&quot;currencyCode&quot;:&quot;CZK&quot;,&quot;impressions&quot;:[{&quot;name&quot;:&quot;Spectral:ON CF 8&quot;,&quot;id&quot;:&quot;3116&quot;,&quot;brand&quot;:&quot;Canyon&quot;,&quot;category&quot;:&quot;E-Bikes/E-Mountain/Spectral:ON/Spectral:ON CF&quot;,&quot;variant&quot;:&quot;&quot;,&quot;dimension50&quot;:&quot;2022&quot;,&quot;dimension52&quot;:&quot;Spectral:ON&quot;,&quot;dimension63&quot;:&quot;unisex&quot;,&quot;dimension64&quot;:&quot;&quot;,&quot;dimension65&quot;:&quot;ZFER&quot;,&quot;dimension66&quot;:&quot;CompleteBikeMT EBIKE&quot;,&quot;dimension67&quot;:&quot;false&quot;,&quot;dimension68&quot;:&quot;true&quot;,&quot;feedProductId&quot;:&quot;50015563&quot;,&quot;dimension54&quot;:&quot;not defined&quot;,&quot;dimension51&quot;:&quot;Stealth&quot;,&quot;dimension53&quot;:&quot;not defined&quot;,&quot;quantity&quot;:1,&quot;price&quot;:&quot;&quot;,&quot;metric4&quot;:&quot;&quot;,&quot;dimension56&quot;:&quot;not defined&quot;}]}},{&quot;event&quot;:&quot;view_item_list&quot;,&quot;event_name&quot;:&quot;Ecommerce - Item list view&quot;,&quot;ecommerce&quot;:{&quot;items&quot;:[{&quot;item_id&quot;:&quot;3116&quot;,&quot;item_name&quot;:&quot;Spectral:ON CF 8&quot;,&quot;coupon&quot;:&quot;&quot;,&quot;currency&quot;:&quot;CZK&quot;,&quot;discount&quot;:&quot;&quot;,&quot;item_brand&quot;:&quot;Canyon&quot;,&quot;item_category&quot;:&quot;E-Bikes&quot;,&quot;item_category2&quot;:&quot;E-Mountain&quot;,&quot;item_category3&quot;:&quot;Spectral:ON&quot;,&quot;item_category4&quot;:&quot;Spectral:ON CF&quot;,&quot;item_variant&quot;:&quot;&quot;,&quot;price&quot;:&quot;&quot;,&quot;quantity&quot;:1}]}}]">
    <div class="productTileDefault__imageWrapper">
    <a title="Spectral:ON CF 8" aria-label="Spectral:ON CF 8 Price: 155.599 CZK" class="js-productTile productTileDefault__imageLink" href="https://www.canyon.com/en-cz/electric-bikes/electric-mountain-bikes/spectral-on/spectral-on-cf/spectral-on-cf-8/3116.html?dwvar_3116_pv_rahmenfarbe=BK" aria-hidden="false" tabindex="0" data-gtm-click="[{&quot;event&quot;:&quot;EEC-productClick&quot;,&quot;ecommerce&quot;:{&quot;click&quot;:{&quot;actionField&quot;:{&quot;list&quot;:&quot;&quot;},&quot;products&quot;:[{&quot;name&quot;:&quot;Spectral:ON CF 8&quot;,&quot;id&quot;:&quot;3116&quot;,&quot;brand&quot;:&quot;Canyon&quot;,&quot;category&quot;:&quot;E-Bikes/E-Mountain/Spectral:ON/Spectral:ON CF&quot;,&quot;variant&quot;:&quot;&quot;,&quot;dimension50&quot;:&quot;2022&quot;,&quot;dimension52&quot;:&quot;Spectral:ON&quot;,&quot;dimension63&quot;:&quot;unisex&quot;,&quot;dimension64&quot;:&quot;&quot;,&quot;dimension65&quot;:&quot;ZFER&quot;,&quot;dimension66&quot;:&quot;CompleteBikeMT EBIKE&quot;,&quot;dimension67&quot;:&quot;false&quot;,&quot;dimension68&quot;:&quot;true&quot;,&quot;feedProductId&quot;:&quot;50015563&quot;,&quot;dimension54&quot;:&quot;not defined&quot;,&quot;dimension51&quot;:&quot;Stealth&quot;,&quot;dimension53&quot;:&quot;not defined&quot;,&quot;quantity&quot;:&quot;&quot;,&quot;price&quot;:&quot;&quot;,&quot;metric4&quot;:&quot;&quot;,&quot;dimension56&quot;:&quot;not defined&quot;}]},&quot;currencyCode&quot;:&quot;CZK&quot;}},{&quot;event&quot;:&quot;select_item&quot;,&quot;event_name&quot;:&quot;Ecommerce - Select item&quot;,&quot;ecommerce&quot;:{&quot;items&quot;:[{&quot;item_id&quot;:&quot;3116&quot;,&quot;item_name&quot;:&quot;Spectral:ON CF 8&quot;,&quot;coupon&quot;:&quot;&quot;,&quot;currency&quot;:&quot;CZK&quot;,&quot;discount&quot;:&quot;&quot;,&quot;item_brand&quot;:&quot;Canyon&quot;,&quot;item_category&quot;:&quot;E-Bikes&quot;,&quot;item_category2&quot;:&quot;E-Mountain&quot;,&quot;item_category3&quot;:&quot;Spectral:ON&quot;,&quot;item_category4&quot;:&quot;Spectral:ON CF&quot;,&quot;item_variant&quot;:&quot;&quot;,&quot;price&quot;:&quot;&quot;,&quot;quantity&quot;:1}]}}]">
    <div class="productTileDefault__pictureWrapper js-noSwatchTileImagesContainer" data-tile-images="[{&quot;title&quot;:&quot;Spectral:ON CF 8&quot;,&quot;alt&quot;:&quot;Spectral:ON CF 8&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.png&quot;},&quot;found&quot;:true}]" data-tile-hover-images="[{&quot;title&quot;:&quot;Spectral:ON CF 8&quot;,&quot;alt&quot;:&quot;Spectral:ON CF 8&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;md&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;},&quot;found&quot;:false}]">
    <picture class="picture productTileDefault__picture productTileDefault__picture--main">
    <source media="(min-width: 1921px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
    <source media="(min-width: 1440px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
    <source media="(min-width: 1200px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
    <source media="(min-width: 992px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
    <source media="(min-width: 768px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
    <source media="(min-width: 534px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
    <source media="(min-width: 0px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
    <img title="Spectral:ON CF 8" alt="Spectral:ON CF 8" class="picture__image lazy productTileDefault__image loaded" data-src="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" src="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" data-was-processed="true">
    </picture>
    </div>
    </a>
    <div class="productTileDefault__awardAndBadges">
    <div class="productTileDefault__badges">
    
    </div>
    <div class="productTileDefault__award">
    
    </div>
    </div>
    </div>
    <div class="productTileDefault__productSummary">
    <div class="productTileDefault__productSummaryTop">
    <div class="productTileDefault__colorsAndCompare">
    <div class="colorPicker__wrapper productTile__colorPickerWrapper">
    <ul class="js-colorPicker colorPicker productTile__colorPicker ">
    <li class="colorPicker__colorListItem ">
    <button aria-hidden="false" aria-label="Stealth" class="colorSwatch colorSwatch--button colorSwatch--small colorSwatch--selected js-noGtmClick js-product-color js-color-swatch colorPicker__colorSwatch" tabindex="0" data-url="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_CZ/Product-Variation?dwvar_3116_pv_rahmenfarbe=&amp;pid=3116&amp;quantity=undefined&amp;imageupdate=color" data-displayvalue="Stealth" data-tile-images="[{&quot;title&quot;:&quot;Spectral:ON CF 8&quot;,&quot;alt&quot;:&quot;Spectral:ON CF 8&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dw8671dc8e/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_bk-bk_P5.png&quot;},&quot;found&quot;:true}]" data-tile-hover-images="[{&quot;title&quot;:&quot;Stealth&quot;,&quot;alt&quot;:&quot;Stealth&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;md&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;},&quot;found&quot;:false}]" data-pdp-url="https://www.canyon.com/en-cz/electric-bikes/electric-mountain-bikes/spectral-on/spectral-on-cf/spectral-on-cf-8/3116.html?dwvar_3116_pv_rahmenfarbe=BK" data-compare-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-AddToCompare?pid=50015560" data-remove-from-compare-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-RemoveFromCompare?pid=50015560" data-compare-pid="50015560" title="Stealth" type="button">
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
    <button aria-hidden="false" aria-label="Green Vastness" class="colorSwatch colorSwatch--button colorSwatch--small  js-product-color js-color-swatch colorPicker__colorSwatch" tabindex="0" data-url="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_CZ/Product-Variation?dwvar_3116_pv_rahmenfarbe=GN&amp;pid=3116&amp;quantity=undefined&amp;imageupdate=color" data-displayvalue="Green Vastness" data-tile-images="[{&quot;title&quot;:&quot;Spectral:ON CF 8&quot;,&quot;alt&quot;:&quot;Spectral:ON CF 8&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw84a1df8f/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_gn-gn_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw84a1df8f/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_gn-gn_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw84a1df8f/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_gn-gn_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw84a1df8f/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_gn-gn_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw84a1df8f/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_gn-gn_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw84a1df8f/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_gn-gn_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw84a1df8f/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_gn-gn_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dw84a1df8f/images/full/full_2022_/2022/full_2022_spectral-on-cf-8_3116_gn-gn_P5.png&quot;},&quot;found&quot;:true}]" data-tile-hover-images="[{&quot;title&quot;:&quot;Green Vastness&quot;,&quot;alt&quot;:&quot;Green Vastness&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;md&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;},&quot;found&quot;:false}]" data-pdp-url="https://www.canyon.com/en-cz/electric-bikes/electric-mountain-bikes/spectral-on/spectral-on-cf/spectral-on-cf-8/3116.html?dwvar_3116_pv_rahmenfarbe=GN" data-compare-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-AddToCompare?pid=50015564" data-remove-from-compare-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-RemoveFromCompare?pid=50015564" data-compare-pid="50015564" title="Green Vastness" type="button">
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
    </ul>
    </div>
    <div class="productTileCompare__wrapper">
    <label class="productTileCompare__checkbox inputCheckbox js-compareWrapper">
    <input type="checkbox" class="productTileCompare__checkboxInput inputCheckbox__input js-selectCompareProduct" aria-hidden="false" aria-label="Compare" tabindex="0" value="productCompareCheckbox" name="productCompareCheckbox" data-remove-pid-compare="50015563" data-compare-remove-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-RemoveFromCompare?pid=50015563" data-add-to-compare-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-AddToCompare?pid=50015563">
    <span class="productTile__compareCheckboxLabel inputCheckbox__label">
    <svg xmlns:xlink="http://www.w3.org/1999/xlink" class="icon icon-check2 inputCheckbox__icon" aria-hidden="false" focusable="false">
    <use xlink:href="/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/iconsNew.svg#sprite-check2"></use>
    </svg>
    <span class="inputCheckbox__labelInner">
    Compare
    </span>
    </span>
    </label>
    </div>
    </div>
    <div class="productTileDefault__productNameWrapper">
    <a title="Spectral:ON CF 8" class="productTileDefault__productName link" href="https://www.canyon.com/en-cz/electric-bikes/electric-mountain-bikes/spectral-on/spectral-on-cf/spectral-on-cf-8/3116.html?dwvar_3116_pv_rahmenfarbe=BK" aria-hidden="false" tabindex="0" data-gtm-click="[{&quot;event&quot;:&quot;EEC-productClick&quot;,&quot;ecommerce&quot;:{&quot;click&quot;:{&quot;actionField&quot;:{&quot;list&quot;:&quot;&quot;},&quot;products&quot;:[{&quot;name&quot;:&quot;Spectral:ON CF 8&quot;,&quot;id&quot;:&quot;3116&quot;,&quot;brand&quot;:&quot;Canyon&quot;,&quot;category&quot;:&quot;E-Bikes/E-Mountain/Spectral:ON/Spectral:ON CF&quot;,&quot;variant&quot;:&quot;&quot;,&quot;dimension50&quot;:&quot;2022&quot;,&quot;dimension52&quot;:&quot;Spectral:ON&quot;,&quot;dimension63&quot;:&quot;unisex&quot;,&quot;dimension64&quot;:&quot;&quot;,&quot;dimension65&quot;:&quot;ZFER&quot;,&quot;dimension66&quot;:&quot;CompleteBikeMT EBIKE&quot;,&quot;dimension67&quot;:&quot;false&quot;,&quot;dimension68&quot;:&quot;true&quot;,&quot;feedProductId&quot;:&quot;50015563&quot;,&quot;dimension54&quot;:&quot;not defined&quot;,&quot;dimension51&quot;:&quot;Stealth&quot;,&quot;dimension53&quot;:&quot;not defined&quot;,&quot;quantity&quot;:&quot;&quot;,&quot;price&quot;:&quot;&quot;,&quot;metric4&quot;:&quot;&quot;,&quot;dimension56&quot;:&quot;not defined&quot;}]},&quot;currencyCode&quot;:&quot;CZK&quot;}},{&quot;event&quot;:&quot;select_item&quot;,&quot;event_name&quot;:&quot;Ecommerce - Select item&quot;,&quot;ecommerce&quot;:{&quot;items&quot;:[{&quot;item_id&quot;:&quot;3116&quot;,&quot;item_name&quot;:&quot;Spectral:ON CF 8&quot;,&quot;coupon&quot;:&quot;&quot;,&quot;currency&quot;:&quot;CZK&quot;,&quot;discount&quot;:&quot;&quot;,&quot;item_brand&quot;:&quot;Canyon&quot;,&quot;item_category&quot;:&quot;E-Bikes&quot;,&quot;item_category2&quot;:&quot;E-Mountain&quot;,&quot;item_category3&quot;:&quot;Spectral:ON&quot;,&quot;item_category4&quot;:&quot;Spectral:ON CF&quot;,&quot;item_variant&quot;:&quot;&quot;,&quot;price&quot;:&quot;&quot;,&quot;quantity&quot;:1}]}}]">
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
    From 155.599 CZK
    </div>
    <div class="productTile__priceMonthly">
    or from 25.933,17 CZK/Mo.
    </div>
    </div>
    
    </div>
    </div>
    </div>
    </li>'''
    )

    res = _parse_canyon_catalog(one_bike_tree)

    assert isinstance(res, list)
    assert len(res) == 1
    assert isinstance(res[0], Bike)
    assert res[0].id == 'spectral:on_cf_8'
    assert res[0].title == 'Spectral:ON CF 8'
    assert res[0].link == 'https://www.canyon.com/en-cz/electric-bikes/electric-mountain-bikes/spectral-on/spectral-on-cf/spectral-on-cf-8/3116.html?dwvar_3116_pv_rahmenfarbe=BK'
    assert res[0].family == 'Spectral:ON'
    assert res[0].model == 'CF 8'


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
	    id: '3058',
	    sku: ''
	}];
	cq_params.categoryId = 'instockbikes';
	cq_params.refinements = '[{\"name\":\"pc_familie\",\"value\":\"Speedmax\"},{\"name\":\"Category\",\"value\":\"instockbikes\"}]';
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
		search_params.refs = '[{\"name\":\"pc_familie\",\"value\":\"Speedmax\"},{\"name\":\"Category\",\"value\":\"instockbikes\"}]';
		search_params.sort = 'sort_master_availability';
		search_params.imageUUID = '';
		search_params.searchID = 'cc194b0e-f538-4eab-af5c-2a2b09052cb4';
		search_params.locale = 'en_CZ';
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
dw.ac._capture({id: "3058", type: "searchhit"});
/* ]]> */
// -->
</script>
<div data-pid="50021193" class="js-productTileWrapper productTileDefault productTileDefault--bike link-already-checked" data-gtm-impression="[{&quot;event&quot;:&quot;EEC-productImpression&quot;,&quot;ecommerce&quot;:{&quot;currencyCode&quot;:&quot;CZK&quot;,&quot;impressions&quot;:[{&quot;name&quot;:&quot;Speedmax CF 7 Disc&quot;,&quot;id&quot;:&quot;3058&quot;,&quot;brand&quot;:&quot;Canyon&quot;,&quot;category&quot;:&quot;Road Bikes/Triathlon/Speedmax/Speedmax CF&quot;,&quot;variant&quot;:&quot;&quot;,&quot;dimension50&quot;:&quot;2023&quot;,&quot;dimension52&quot;:&quot;Speedmax&quot;,&quot;dimension63&quot;:&quot;unisex&quot;,&quot;dimension64&quot;:&quot;&quot;,&quot;dimension65&quot;:&quot;ZFER&quot;,&quot;dimension66&quot;:&quot;Complete Bike TT&quot;,&quot;dimension67&quot;:&quot;false&quot;,&quot;dimension68&quot;:&quot;false&quot;,&quot;feedProductId&quot;:&quot;50021193&quot;,&quot;dimension54&quot;:&quot;not defined&quot;,&quot;dimension51&quot;:&quot;Dark Grey&quot;,&quot;dimension53&quot;:&quot;not defined&quot;,&quot;quantity&quot;:1,&quot;price&quot;:64296.69,&quot;metric4&quot;:77799,&quot;dimension56&quot;:&quot;not defined&quot;}]}},{&quot;event&quot;:&quot;view_item_list&quot;,&quot;event_name&quot;:&quot;Ecommerce - Item list view&quot;,&quot;ecommerce&quot;:{&quot;items&quot;:[{&quot;item_id&quot;:&quot;3058&quot;,&quot;item_name&quot;:&quot;Speedmax CF 7 Disc&quot;,&quot;coupon&quot;:&quot;&quot;,&quot;currency&quot;:&quot;CZK&quot;,&quot;discount&quot;:&quot;&quot;,&quot;item_brand&quot;:&quot;Canyon&quot;,&quot;item_category&quot;:&quot;Road Bikes&quot;,&quot;item_category2&quot;:&quot;Triathlon&quot;,&quot;item_category3&quot;:&quot;Speedmax&quot;,&quot;item_category4&quot;:&quot;Speedmax CF&quot;,&quot;item_variant&quot;:&quot;&quot;,&quot;price&quot;:64296.69,&quot;quantity&quot;:1}]}}]">
<div class="productTileDefault__imageWrapper">
<a title="Speedmax CF 7 Disc" aria-label="Speedmax CF 7 Disc Powermeter Price: 77.799 CZK" class="js-productTile productTileDefault__imageLink" href="https://www.canyon.com/en-cz/road-bikes/triathlon-bikes/speedmax/cf/speedmax-cf-7-disc/3058.html?dwvar_3058_pv_rahmenfarbe=R073_P06" aria-hidden="false" tabindex="0" data-gtm-click="[{&quot;event&quot;:&quot;EEC-productClick&quot;,&quot;ecommerce&quot;:{&quot;click&quot;:{&quot;actionField&quot;:{&quot;list&quot;:&quot;&quot;},&quot;products&quot;:[{&quot;name&quot;:&quot;Speedmax CF 7 Disc&quot;,&quot;id&quot;:&quot;3058&quot;,&quot;brand&quot;:&quot;Canyon&quot;,&quot;category&quot;:&quot;Road Bikes/Triathlon/Speedmax/Speedmax CF&quot;,&quot;variant&quot;:&quot;&quot;,&quot;dimension50&quot;:&quot;2023&quot;,&quot;dimension52&quot;:&quot;Speedmax&quot;,&quot;dimension63&quot;:&quot;unisex&quot;,&quot;dimension64&quot;:&quot;&quot;,&quot;dimension65&quot;:&quot;ZFER&quot;,&quot;dimension66&quot;:&quot;Complete Bike TT&quot;,&quot;dimension67&quot;:&quot;false&quot;,&quot;dimension68&quot;:&quot;false&quot;,&quot;feedProductId&quot;:&quot;50021193&quot;,&quot;dimension54&quot;:&quot;not defined&quot;,&quot;dimension51&quot;:&quot;Dark Grey&quot;,&quot;dimension53&quot;:&quot;not defined&quot;,&quot;quantity&quot;:&quot;&quot;,&quot;price&quot;:64296.69,&quot;metric4&quot;:77799,&quot;dimension56&quot;:&quot;not defined&quot;}]},&quot;currencyCode&quot;:&quot;CZK&quot;}},{&quot;event&quot;:&quot;select_item&quot;,&quot;event_name&quot;:&quot;Ecommerce - Select item&quot;,&quot;ecommerce&quot;:{&quot;items&quot;:[{&quot;item_id&quot;:&quot;3058&quot;,&quot;item_name&quot;:&quot;Speedmax CF 7 Disc&quot;,&quot;coupon&quot;:&quot;&quot;,&quot;currency&quot;:&quot;CZK&quot;,&quot;discount&quot;:&quot;&quot;,&quot;item_brand&quot;:&quot;Canyon&quot;,&quot;item_category&quot;:&quot;Road Bikes&quot;,&quot;item_category2&quot;:&quot;Triathlon&quot;,&quot;item_category3&quot;:&quot;Speedmax&quot;,&quot;item_category4&quot;:&quot;Speedmax CF&quot;,&quot;item_variant&quot;:&quot;&quot;,&quot;price&quot;:64296.69,&quot;quantity&quot;:1}]}}]">
<div class="productTileDefault__pictureWrapper js-noSwatchTileImagesContainer" data-tile-images="[{&quot;title&quot;:&quot;Speedmax CF 7 Disc&quot;,&quot;alt&quot;:&quot;Speedmax CF 7 Disc&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw90f43f48/images/full/full_2023_/2023/full_2023_3058_speedmax-cf-7-disc_P06_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw90f43f48/images/full/full_2023_/2023/full_2023_3058_speedmax-cf-7-disc_P06_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw90f43f48/images/full/full_2023_/2023/full_2023_3058_speedmax-cf-7-disc_P06_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw90f43f48/images/full/full_2023_/2023/full_2023_3058_speedmax-cf-7-disc_P06_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw90f43f48/images/full/full_2023_/2023/full_2023_3058_speedmax-cf-7-disc_P06_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw90f43f48/images/full/full_2023_/2023/full_2023_3058_speedmax-cf-7-disc_P06_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw90f43f48/images/full/full_2023_/2023/full_2023_3058_speedmax-cf-7-disc_P06_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dw90f43f48/images/full/full_2023_/2023/full_2023_3058_speedmax-cf-7-disc_P06_P5.png&quot;},&quot;found&quot;:true}]" data-tile-hover-images="[{&quot;title&quot;:&quot;Speedmax CF 7 Disc&quot;,&quot;alt&quot;:&quot;Speedmax CF 7 Disc&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;md&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;},&quot;found&quot;:false}]">
<picture class="picture productTileDefault__picture productTileDefault__picture--main">
<source media="(min-width: 1921px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw90f43f48/images/full/full_2023_/2023/full_2023_3058_speedmax-cf-7-disc_P06_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw90f43f48/images/full/full_2023_/2023/full_2023_3058_speedmax-cf-7-disc_P06_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<source media="(min-width: 1440px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw90f43f48/images/full/full_2023_/2023/full_2023_3058_speedmax-cf-7-disc_P06_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw90f43f48/images/full/full_2023_/2023/full_2023_3058_speedmax-cf-7-disc_P06_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">

<source media="(min-width: 1200px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw90f43f48/images/full/full_2023_/2023/full_2023_3058_speedmax-cf-7-disc_P06_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw90f43f48/images/full/full_2023_/2023/full_2023_3058_speedmax-cf-7-disc_P06_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<source media="(min-width: 992px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw90f43f48/images/full/full_2023_/2023/full_2023_3058_speedmax-cf-7-disc_P06_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw90f43f48/images/full/full_2023_/2023/full_2023_3058_speedmax-cf-7-disc_P06_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<source media="(min-width: 768px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw90f43f48/images/full/full_2023_/2023/full_2023_3058_speedmax-cf-7-disc_P06_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw90f43f48/images/full/full_2023_/2023/full_2023_3058_speedmax-cf-7-disc_P06_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<source media="(min-width: 534px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw90f43f48/images/full/full_2023_/2023/full_2023_3058_speedmax-cf-7-disc_P06_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw90f43f48/images/full/full_2023_/2023/full_2023_3058_speedmax-cf-7-disc_P06_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<source media="(min-width: 0px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw90f43f48/images/full/full_2023_/2023/full_2023_3058_speedmax-cf-7-disc_P06_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw90f43f48/images/full/full_2023_/2023/full_2023_3058_speedmax-cf-7-disc_P06_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<img title="Speedmax CF 7 Disc" alt="Speedmax CF 7 Disc" class="picture__image lazy productTileDefault__image loaded" data-src="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw90f43f48/images/full/full_2023_/2023/full_2023_3058_speedmax-cf-7-disc_P06_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" src="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw90f43f48/images/full/full_2023_/2023/full_2023_3058_speedmax-cf-7-disc_P06_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" data-was-processed="true">
</picture>
</div>
</a>
<div class="productTileDefault__awardAndBadges">
<div class="productTileDefault__badges">
<ul class="productTileBadges__list">
<li class="productTileBadges__listItem productTileBadges__listItem--marketing">
Powermeter
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
<div class="colorPicker__wrapper productTile__colorPickerWrapper">
<ul class="js-colorPicker colorPicker productTile__colorPicker ">
<li class="colorPicker__colorListItem ">
<button aria-hidden="false" aria-label="Dark Grey" class="colorSwatch colorSwatch--button colorSwatch--small colorSwatch--selected js-noGtmClick js-product-color js-color-swatch colorPicker__colorSwatch" tabindex="0" data-url="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_CZ/Product-Variation?dwvar_3058_pv_rahmenfarbe=&amp;pid=3058&amp;quantity=undefined&amp;imageupdate=color" data-displayvalue="Dark Grey" data-tile-images="[{&quot;title&quot;:&quot;Speedmax CF 7 Disc&quot;,&quot;alt&quot;:&quot;Speedmax CF 7 Disc&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw90f43f48/images/full/full_2023_/2023/full_2023_3058_speedmax-cf-7-disc_P06_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw90f43f48/images/full/full_2023_/2023/full_2023_3058_speedmax-cf-7-disc_P06_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw90f43f48/images/full/full_2023_/2023/full_2023_3058_speedmax-cf-7-disc_P06_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw90f43f48/images/full/full_2023_/2023/full_2023_3058_speedmax-cf-7-disc_P06_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw90f43f48/images/full/full_2023_/2023/full_2023_3058_speedmax-cf-7-disc_P06_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw90f43f48/images/full/full_2023_/2023/full_2023_3058_speedmax-cf-7-disc_P06_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw90f43f48/images/full/full_2023_/2023/full_2023_3058_speedmax-cf-7-disc_P06_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dw90f43f48/images/full/full_2023_/2023/full_2023_3058_speedmax-cf-7-disc_P06_P5.png&quot;},&quot;found&quot;:true}]" data-tile-hover-images="[{&quot;title&quot;:&quot;Dark Grey&quot;,&quot;alt&quot;:&quot;Dark Grey&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;md&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;},&quot;found&quot;:false}]" data-pdp-url="https://www.canyon.com/en-cz/road-bikes/triathlon-bikes/speedmax/cf/speedmax-cf-7-disc/3058.html?dwvar_3058_pv_rahmenfarbe=R073_P06" data-compare-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-AddToCompare?pid=50021189" data-remove-from-compare-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-RemoveFromCompare?pid=50021189" data-compare-pid="50021189" title="Dark Grey" type="button">
<span class="colorSwatch__colorWrapper">
<span class="colorSwatch__color" style="color:#49494a;"></span>
<span class="colorSwatch__color" style="color:#292929;"></span>
</span>
</button>
<span class="colorSwatch__colorLabel" role="tooltip">
<span class="colorSwatch__colorLabelText">
Color:
</span>
<span class="colorSwatch__colorLabelValue">
Dark Grey
</span>
</span>
</li>
<li class="colorPicker__colorListItem ">
<button aria-hidden="false" aria-label="Stealth" class="colorSwatch colorSwatch--button colorSwatch--small  js-product-color js-color-swatch colorPicker__colorSwatch" tabindex="0" data-url="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_CZ/Product-Variation?dwvar_3058_pv_rahmenfarbe=BK%2FSR&amp;pid=3058&amp;quantity=undefined&amp;imageupdate=color" data-displayvalue="Stealth" data-tile-images="[{&quot;title&quot;:&quot;Speedmax CF 7 Disc&quot;,&quot;alt&quot;:&quot;Speedmax CF 7 Disc&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwdb59880d/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_bk-sv_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwdb59880d/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_bk-sv_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwdb59880d/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_bk-sv_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwdb59880d/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_bk-sv_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwdb59880d/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_bk-sv_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwdb59880d/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_bk-sv_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dwdb59880d/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_bk-sv_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dwdb59880d/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_bk-sv_P5.png&quot;},&quot;found&quot;:true}]" data-tile-hover-images="[{&quot;title&quot;:&quot;Stealth&quot;,&quot;alt&quot;:&quot;Stealth&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;md&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;},&quot;found&quot;:false}]" data-pdp-url="https://www.canyon.com/en-cz/road-bikes/triathlon-bikes/speedmax/cf/speedmax-cf-7-disc/3058.html?dwvar_3058_pv_rahmenfarbe=BK%2FSR" data-compare-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-AddToCompare?pid=50016366" data-remove-from-compare-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-RemoveFromCompare?pid=50016366" data-compare-pid="50016366" title="Stealth" type="button">
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
<button aria-hidden="false" aria-label="Flash Yellow" class="colorSwatch colorSwatch--button colorSwatch--small  js-product-color js-color-swatch colorPicker__colorSwatch" tabindex="0" data-url="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_CZ/Product-Variation?dwvar_3058_pv_rahmenfarbe=YE%2FBK&amp;pid=3058&amp;quantity=undefined&amp;imageupdate=color" data-displayvalue="Flash Yellow" data-tile-images="[{&quot;title&quot;:&quot;Speedmax CF 7 Disc&quot;,&quot;alt&quot;:&quot;Speedmax CF 7 Disc&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw72127547/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_ye-bk_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw72127547/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_ye-bk_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw72127547/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_ye-bk_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw72127547/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_ye-bk_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw72127547/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_ye-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw72127547/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_ye-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw72127547/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_ye-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dw72127547/images/full/full_2022_/2022/full_2022_speedmax-cf-7-disc_3058_ye-bk_P5.png&quot;},&quot;found&quot;:true}]" data-tile-hover-images="[{&quot;title&quot;:&quot;Flash Yellow&quot;,&quot;alt&quot;:&quot;Flash Yellow&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;md&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;},&quot;found&quot;:false}]" data-pdp-url="https://www.canyon.com/en-cz/road-bikes/triathlon-bikes/speedmax/cf/speedmax-cf-7-disc/3058.html?dwvar_3058_pv_rahmenfarbe=YE%2FBK" data-compare-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-AddToCompare?pid=50016367" data-remove-from-compare-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-RemoveFromCompare?pid=50016367" data-compare-pid="50016367" title="Flash Yellow" type="button">
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
<div class="productTileCompare__wrapper">
<label class="productTileCompare__checkbox inputCheckbox js-compareWrapper">
<input type="checkbox" class="productTileCompare__checkboxInput inputCheckbox__input js-selectCompareProduct" aria-hidden="false" aria-label="Compare" tabindex="0" value="productCompareCheckbox" name="productCompareCheckbox" data-remove-pid-compare="50021193" data-compare-remove-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-RemoveFromCompare?pid=50021193" data-add-to-compare-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-AddToCompare?pid=50021193">
<span class="productTile__compareCheckboxLabel inputCheckbox__label">
<svg xmlns:xlink="http://www.w3.org/1999/xlink" class="icon icon-check2 inputCheckbox__icon" aria-hidden="false" focusable="false">
<use xlink:href="/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/iconsNew.svg#sprite-check2"></use>
</svg>
<span class="inputCheckbox__labelInner">
Compare
</span>
</span>
</label>
</div>
</div>
<div class="productTileDefault__productNameWrapper">
<a title="Speedmax CF 7 Disc" class="productTileDefault__productName link" href="https://www.canyon.com/en-cz/road-bikes/triathlon-bikes/speedmax/cf/speedmax-cf-7-disc/3058.html?dwvar_3058_pv_rahmenfarbe=R073_P06" aria-hidden="false" tabindex="0" data-gtm-click="[{&quot;event&quot;:&quot;EEC-productClick&quot;,&quot;ecommerce&quot;:{&quot;click&quot;:{&quot;actionField&quot;:{&quot;list&quot;:&quot;&quot;},&quot;products&quot;:[{&quot;name&quot;:&quot;Speedmax CF 7 Disc&quot;,&quot;id&quot;:&quot;3058&quot;,&quot;brand&quot;:&quot;Canyon&quot;,&quot;category&quot;:&quot;Road Bikes/Triathlon/Speedmax/Speedmax CF&quot;,&quot;variant&quot;:&quot;&quot;,&quot;dimension50&quot;:&quot;2023&quot;,&quot;dimension52&quot;:&quot;Speedmax&quot;,&quot;dimension63&quot;:&quot;unisex&quot;,&quot;dimension64&quot;:&quot;&quot;,&quot;dimension65&quot;:&quot;ZFER&quot;,&quot;dimension66&quot;:&quot;Complete Bike TT&quot;,&quot;dimension67&quot;:&quot;false&quot;,&quot;dimension68&quot;:&quot;false&quot;,&quot;feedProductId&quot;:&quot;50021193&quot;,&quot;dimension54&quot;:&quot;not defined&quot;,&quot;dimension51&quot;:&quot;Dark Grey&quot;,&quot;dimension53&quot;:&quot;not defined&quot;,&quot;quantity&quot;:&quot;&quot;,&quot;price&quot;:64296.69,&quot;metric4&quot;:77799,&quot;dimension56&quot;:&quot;not defined&quot;}]},&quot;currencyCode&quot;:&quot;CZK&quot;}},{&quot;event&quot;:&quot;select_item&quot;,&quot;event_name&quot;:&quot;Ecommerce - Select item&quot;,&quot;ecommerce&quot;:{&quot;items&quot;:[{&quot;item_id&quot;:&quot;3058&quot;,&quot;item_name&quot;:&quot;Speedmax CF 7 Disc&quot;,&quot;coupon&quot;:&quot;&quot;,&quot;currency&quot;:&quot;CZK&quot;,&quot;discount&quot;:&quot;&quot;,&quot;item_brand&quot;:&quot;Canyon&quot;,&quot;item_category&quot;:&quot;Road Bikes&quot;,&quot;item_category2&quot;:&quot;Triathlon&quot;,&quot;item_category3&quot;:&quot;Speedmax&quot;,&quot;item_category4&quot;:&quot;Speedmax CF&quot;,&quot;item_variant&quot;:&quot;&quot;,&quot;price&quot;:64296.69,&quot;quantity&quot;:1}]}}]">
Speedmax CF 7 Disc
</a>
</div>
<div class="productTileDefault__infoWrapper">

<div class="productTileDefault__info productTileDefault__info--highlights">
Shimano 105 R7000 SS, DT Swiss P 1800 Spline db
</div>

</div>
</div>
<div class="productTileDefault__productSummaryBottom">
<div class="productTileDefault__price">
<div class="productTile__priceSale">
77.799 CZK
</div>
<div class="productTile__priceMonthly">
or from 12.966,50 CZK/Mo.
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
	    id: '3059',
	    sku: ''
	}];
	cq_params.categoryId = 'instockbikes';
	cq_params.refinements = '[{\"name\":\"pc_familie\",\"value\":\"Speedmax\"},{\"name\":\"Category\",\"value\":\"instockbikes\"}]';
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
		search_params.refs = '[{\"name\":\"pc_familie\",\"value\":\"Speedmax\"},{\"name\":\"Category\",\"value\":\"instockbikes\"}]';
		search_params.sort = 'sort_master_availability';
		search_params.imageUUID = '';
		search_params.searchID = 'cc194b0e-f538-4eab-af5c-2a2b09052cb4';
		search_params.locale = 'en_CZ';
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
dw.ac._capture({id: "3059", type: "searchhit"});
/* ]]> */
// -->
</script>
<div data-pid="50016381" class="js-productTileWrapper productTileDefault productTileDefault--bike link-already-checked" data-gtm-impression="[{&quot;event&quot;:&quot;EEC-productImpression&quot;,&quot;ecommerce&quot;:{&quot;currencyCode&quot;:&quot;CZK&quot;,&quot;impressions&quot;:[{&quot;name&quot;:&quot;Speedmax CF 8 Disc&quot;,&quot;id&quot;:&quot;3059&quot;,&quot;brand&quot;:&quot;Canyon&quot;,&quot;category&quot;:&quot;Road Bikes/Triathlon/Speedmax/Speedmax CF&quot;,&quot;variant&quot;:&quot;&quot;,&quot;dimension50&quot;:&quot;2022&quot;,&quot;dimension52&quot;:&quot;Speedmax&quot;,&quot;dimension63&quot;:&quot;unisex&quot;,&quot;dimension64&quot;:&quot;&quot;,&quot;dimension65&quot;:&quot;ZFER&quot;,&quot;dimension66&quot;:&quot;Complete Bike TT&quot;,&quot;dimension67&quot;:&quot;false&quot;,&quot;dimension68&quot;:&quot;false&quot;,&quot;feedProductId&quot;:&quot;50016381&quot;,&quot;dimension54&quot;:&quot;not defined&quot;,&quot;dimension51&quot;:&quot;Flash Yellow&quot;,&quot;dimension53&quot;:&quot;not defined&quot;,&quot;quantity&quot;:1,&quot;price&quot;:94214.05,&quot;metric4&quot;:113999,&quot;dimension56&quot;:&quot;not defined&quot;}]}},{&quot;event&quot;:&quot;view_item_list&quot;,&quot;event_name&quot;:&quot;Ecommerce - Item list view&quot;,&quot;ecommerce&quot;:{&quot;items&quot;:[{&quot;item_id&quot;:&quot;3059&quot;,&quot;item_name&quot;:&quot;Speedmax CF 8 Disc&quot;,&quot;coupon&quot;:&quot;&quot;,&quot;currency&quot;:&quot;CZK&quot;,&quot;discount&quot;:&quot;&quot;,&quot;item_brand&quot;:&quot;Canyon&quot;,&quot;item_category&quot;:&quot;Road Bikes&quot;,&quot;item_category2&quot;:&quot;Triathlon&quot;,&quot;item_category3&quot;:&quot;Speedmax&quot;,&quot;item_category4&quot;:&quot;Speedmax CF&quot;,&quot;item_variant&quot;:&quot;&quot;,&quot;price&quot;:94214.05,&quot;quantity&quot;:1}]}}]">
<div class="productTileDefault__imageWrapper">
<a title="Speedmax CF 8 Disc" aria-label="Speedmax CF 8 Disc Powermeter Price: 113.999 CZK" class="js-productTile productTileDefault__imageLink" href="https://www.canyon.com/en-cz/road-bikes/triathlon-bikes/speedmax/cf/speedmax-cf-8-disc/3059.html?dwvar_3059_pv_rahmenfarbe=YE%2FBK" aria-hidden="false" tabindex="0" data-gtm-click="[{&quot;event&quot;:&quot;EEC-productClick&quot;,&quot;ecommerce&quot;:{&quot;click&quot;:{&quot;actionField&quot;:{&quot;list&quot;:&quot;&quot;},&quot;products&quot;:[{&quot;name&quot;:&quot;Speedmax CF 8 Disc&quot;,&quot;id&quot;:&quot;3059&quot;,&quot;brand&quot;:&quot;Canyon&quot;,&quot;category&quot;:&quot;Road Bikes/Triathlon/Speedmax/Speedmax CF&quot;,&quot;variant&quot;:&quot;&quot;,&quot;dimension50&quot;:&quot;2022&quot;,&quot;dimension52&quot;:&quot;Speedmax&quot;,&quot;dimension63&quot;:&quot;unisex&quot;,&quot;dimension64&quot;:&quot;&quot;,&quot;dimension65&quot;:&quot;ZFER&quot;,&quot;dimension66&quot;:&quot;Complete Bike TT&quot;,&quot;dimension67&quot;:&quot;false&quot;,&quot;dimension68&quot;:&quot;false&quot;,&quot;feedProductId&quot;:&quot;50016381&quot;,&quot;dimension54&quot;:&quot;not defined&quot;,&quot;dimension51&quot;:&quot;Flash Yellow&quot;,&quot;dimension53&quot;:&quot;not defined&quot;,&quot;quantity&quot;:&quot;&quot;,&quot;price&quot;:94214.05,&quot;metric4&quot;:113999,&quot;dimension56&quot;:&quot;not defined&quot;}]},&quot;currencyCode&quot;:&quot;CZK&quot;}},{&quot;event&quot;:&quot;select_item&quot;,&quot;event_name&quot;:&quot;Ecommerce - Select item&quot;,&quot;ecommerce&quot;:{&quot;items&quot;:[{&quot;item_id&quot;:&quot;3059&quot;,&quot;item_name&quot;:&quot;Speedmax CF 8 Disc&quot;,&quot;coupon&quot;:&quot;&quot;,&quot;currency&quot;:&quot;CZK&quot;,&quot;discount&quot;:&quot;&quot;,&quot;item_brand&quot;:&quot;Canyon&quot;,&quot;item_category&quot;:&quot;Road Bikes&quot;,&quot;item_category2&quot;:&quot;Triathlon&quot;,&quot;item_category3&quot;:&quot;Speedmax&quot;,&quot;item_category4&quot;:&quot;Speedmax CF&quot;,&quot;item_variant&quot;:&quot;&quot;,&quot;price&quot;:94214.05,&quot;quantity&quot;:1}]}}]">
<div class="productTileDefault__pictureWrapper js-noSwatchTileImagesContainer" data-tile-images="[{&quot;title&quot;:&quot;Speedmax CF 8 Disc&quot;,&quot;alt&quot;:&quot;Speedmax CF 8 Disc&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.png&quot;},&quot;found&quot;:true}]" data-tile-hover-images="[{&quot;title&quot;:&quot;Speedmax CF 8 Disc&quot;,&quot;alt&quot;:&quot;Speedmax CF 8 Disc&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;md&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;},&quot;found&quot;:false}]">
<picture class="picture productTileDefault__picture productTileDefault__picture--main">

<source media="(min-width: 1921px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<source media="(min-width: 1440px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<source media="(min-width: 1200px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<source media="(min-width: 992px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<source media="(min-width: 768px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<source media="(min-width: 534px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<source media="(min-width: 0px)" data-srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" srcset="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4">
<img title="Speedmax CF 8 Disc" alt="Speedmax CF 8 Disc" class="picture__image lazy productTileDefault__image loaded" data-src="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" src="https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4" data-was-processed="true">
</picture>
</div>
</a>
<div class="productTileDefault__awardAndBadges">
<div class="productTileDefault__badges">
<ul class="productTileBadges__list">
<li class="productTileBadges__listItem productTileBadges__listItem--marketing">
Powermeter
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
<div class="colorPicker__wrapper productTile__colorPickerWrapper">
<ul class="js-colorPicker colorPicker productTile__colorPicker ">
<li class="colorPicker__colorListItem ">
<button aria-hidden="false" aria-label="Stealth" class="colorSwatch colorSwatch--button colorSwatch--small  js-product-color js-color-swatch colorPicker__colorSwatch" tabindex="0" data-url="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_CZ/Product-Variation?dwvar_3059_pv_rahmenfarbe=BK%2FSR&amp;pid=3059&amp;quantity=undefined&amp;imageupdate=color" data-displayvalue="Stealth" data-tile-images="[{&quot;title&quot;:&quot;Speedmax CF 8 Disc&quot;,&quot;alt&quot;:&quot;Speedmax CF 8 Disc&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw218f0498/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_bk-bk_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw218f0498/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_bk-bk_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw218f0498/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_bk-bk_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw218f0498/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_bk-bk_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw218f0498/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_bk-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw218f0498/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_bk-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw218f0498/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_bk-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dw218f0498/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_bk-bk_P5.png&quot;},&quot;found&quot;:true}]" data-tile-hover-images="[{&quot;title&quot;:&quot;Stealth&quot;,&quot;alt&quot;:&quot;Stealth&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;md&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;},&quot;found&quot;:false}]" data-pdp-url="https://www.canyon.com/en-cz/road-bikes/triathlon-bikes/speedmax/cf/speedmax-cf-8-disc/3059.html?dwvar_3059_pv_rahmenfarbe=BK%2FSR" data-compare-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-AddToCompare?pid=50016372" data-remove-from-compare-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-RemoveFromCompare?pid=50016372" data-compare-pid="50016372" title="Stealth" type="button">
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
<button aria-hidden="false" aria-label="Flash Yellow" class="colorSwatch colorSwatch--button colorSwatch--small colorSwatch--selected js-noGtmClick js-product-color js-color-swatch colorPicker__colorSwatch" tabindex="0" data-url="https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_CZ/Product-Variation?dwvar_3059_pv_rahmenfarbe=&amp;pid=3059&amp;quantity=undefined&amp;imageupdate=color" data-displayvalue="Flash Yellow" data-tile-images="[{&quot;title&quot;:&quot;Speedmax CF 8 Disc&quot;,&quot;alt&quot;:&quot;Speedmax CF 8 Disc&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=460&amp;sh=259&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=703&amp;sh=395&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;md&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=901&amp;sh=507&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=517&amp;sh=291&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.jpg?sw=598&amp;sh=336&amp;sm=fit&amp;sfrm=png&amp;q=90&amp;bgcolor=F4F4F4&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/-/Sites-canyon-master/default/dw62277454/images/full/full_2022_/2022/full_2022_speedmax-cf-8-disc_3059_ye-bk_P5.png&quot;},&quot;found&quot;:true}]" data-tile-hover-images="[{&quot;title&quot;:&quot;Flash Yellow&quot;,&quot;alt&quot;:&quot;Flash Yellow&quot;,&quot;urls&quot;:{&quot;xs&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;sm&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;md&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;lg&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;xl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;xxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;xxxl&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;,&quot;zoom&quot;:&quot;https://www.canyon.com/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/noimage.svg&quot;},&quot;found&quot;:false}]" data-pdp-url="https://www.canyon.com/en-cz/road-bikes/triathlon-bikes/speedmax/cf/speedmax-cf-8-disc/3059.html?dwvar_3059_pv_rahmenfarbe=YE%2FBK" data-compare-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-AddToCompare?pid=50016377" data-remove-from-compare-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-RemoveFromCompare?pid=50016377" data-compare-pid="50016377" title="Flash Yellow" type="button">
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
<div class="productTileCompare__wrapper">
<label class="productTileCompare__checkbox inputCheckbox js-compareWrapper">
<input type="checkbox" class="productTileCompare__checkboxInput inputCheckbox__input js-selectCompareProduct" aria-hidden="false" aria-label="Compare" tabindex="0" value="productCompareCheckbox" name="productCompareCheckbox" data-remove-pid-compare="50016381" data-compare-remove-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-RemoveFromCompare?pid=50016381" data-add-to-compare-url="/on/demandware.store/Sites-RoW-Site/en_CZ/Product-AddToCompare?pid=50016381">
<span class="productTile__compareCheckboxLabel inputCheckbox__label">
<svg xmlns:xlink="http://www.w3.org/1999/xlink" class="icon icon-check2 inputCheckbox__icon" aria-hidden="false" focusable="false">
<use xlink:href="/on/demandware.static/Sites-RoW-Site/-/en_CZ/v1670245716113/images/iconsNew.svg#sprite-check2"></use>
</svg>
<span class="inputCheckbox__labelInner">
Compare
</span>
</span>
</label>
</div>
</div>
<div class="productTileDefault__productNameWrapper">
<a title="Speedmax CF 8 Disc" class="productTileDefault__productName link" href="https://www.canyon.com/en-cz/road-bikes/triathlon-bikes/speedmax/cf/speedmax-cf-8-disc/3059.html?dwvar_3059_pv_rahmenfarbe=YE%2FBK" aria-hidden="false" tabindex="0" data-gtm-click="[{&quot;event&quot;:&quot;EEC-productClick&quot;,&quot;ecommerce&quot;:{&quot;click&quot;:{&quot;actionField&quot;:{&quot;list&quot;:&quot;&quot;},&quot;products&quot;:[{&quot;name&quot;:&quot;Speedmax CF 8 Disc&quot;,&quot;id&quot;:&quot;3059&quot;,&quot;brand&quot;:&quot;Canyon&quot;,&quot;category&quot;:&quot;Road Bikes/Triathlon/Speedmax/Speedmax CF&quot;,&quot;variant&quot;:&quot;&quot;,&quot;dimension50&quot;:&quot;2022&quot;,&quot;dimension52&quot;:&quot;Speedmax&quot;,&quot;dimension63&quot;:&quot;unisex&quot;,&quot;dimension64&quot;:&quot;&quot;,&quot;dimension65&quot;:&quot;ZFER&quot;,&quot;dimension66&quot;:&quot;Complete Bike TT&quot;,&quot;dimension67&quot;:&quot;false&quot;,&quot;dimension68&quot;:&quot;false&quot;,&quot;feedProductId&quot;:&quot;50016381&quot;,&quot;dimension54&quot;:&quot;not defined&quot;,&quot;dimension51&quot;:&quot;Flash Yellow&quot;,&quot;dimension53&quot;:&quot;not defined&quot;,&quot;quantity&quot;:&quot;&quot;,&quot;price&quot;:94214.05,&quot;metric4&quot;:113999,&quot;dimension56&quot;:&quot;not defined&quot;}]},&quot;currencyCode&quot;:&quot;CZK&quot;}},{&quot;event&quot;:&quot;select_item&quot;,&quot;event_name&quot;:&quot;Ecommerce - Select item&quot;,&quot;ecommerce&quot;:{&quot;items&quot;:[{&quot;item_id&quot;:&quot;3059&quot;,&quot;item_name&quot;:&quot;Speedmax CF 8 Disc&quot;,&quot;coupon&quot;:&quot;&quot;,&quot;currency&quot;:&quot;CZK&quot;,&quot;discount&quot;:&quot;&quot;,&quot;item_brand&quot;:&quot;Canyon&quot;,&quot;item_category&quot;:&quot;Road Bikes&quot;,&quot;item_category2&quot;:&quot;Triathlon&quot;,&quot;item_category3&quot;:&quot;Speedmax&quot;,&quot;item_category4&quot;:&quot;Speedmax CF&quot;,&quot;item_variant&quot;:&quot;&quot;,&quot;price&quot;:94214.05,&quot;quantity&quot;:1}]}}]">
Speedmax CF 8 Disc
</a>
</div>
<div class="productTileDefault__infoWrapper">

<div class="productTileDefault__info productTileDefault__info--highlights">
Shimano Ultegra R8000 SS, DT Swiss ARC 1600
</div>
</div>
</div>
<div class="productTileDefault__productSummaryBottom">
<div class="productTileDefault__price">
<div class="productTile__priceSale">
113.999 CZK
</div>
<div class="productTile__priceMonthly">
or from 18.999,83 CZK/Mo.
</div>
</div>

</div>
</div>
</div>

</li>
        '''
    )

    res = _parse_canyon_catalog(few_bike_tree)

    assert len(res) == 2
    assert res[0].id == 'speedmax_cf_7_disc'
    assert res[1].id == 'speedmax_cf_8_disc'
    assert res[0].title == 'Speedmax CF 7 Disc'
    assert res[1].title == 'Speedmax CF 8 Disc'
    assert res[0].link == 'https://www.canyon.com/en-cz/road-bikes/triathlon-bikes/speedmax/cf/speedmax-cf-7-disc/3058.html?dwvar_3058_pv_rahmenfarbe=R073_P06'
    assert res[1].link == 'https://www.canyon.com/en-cz/road-bikes/triathlon-bikes/speedmax/cf/speedmax-cf-8-disc/3059.html?dwvar_3059_pv_rahmenfarbe=YE%2FBK'
    assert res[0].family == 'Speedmax'
    assert res[1].family == 'Speedmax'
    assert res[0].model == 'CF 7 Disc'
    assert res[1].model == 'CF 8 Disc'


def test_parse_canyon_catalog_not_found():
    no_bike_tree = etree.HTML('<ul></ul>')

    res = _parse_canyon_catalog(no_bike_tree)

    assert len(res) == 0



