// $(document).ready(function(){
    
//     // $('.main_img01').css('left', 0);
//     // $('.main_img01').animate({
//     //     left: 0,
//     //     opacity: 1
//     // },'slow');

//     $('.main_img01').click(function(){
//         $('.main_img01').animate({
//             left: 0,
//             opacity: 1
//         },'slow');
//     })
    
// });




// //flexslider
// $(document).ready(function(){
//     function fs01Play(){
//         var w = $(window).width();
//         if(w>959){
//             $('.ms01 .ms01_d01').animate({
//                 width : 1030,
//                 right: 0,
//                 opacity: 1
//             },'slow');
//             $('.ms01 .ms01_d02').animate({
//                 width: 1070,
//                 left: 0,
//                 opacity: 1
//             },'slow');

//             $('.mSlider .flexslider .slides > .ms01 > a > .ms01_d04, .mSlider .flexslider .slides > .ms01 > a > .ms01_d05').delay(500).fadeIn('fast');
//         }
//     }
//     function fs01Reset(){
//         $('.ms01 .ms01_d01').animate({
//             width : 3000,
//             right: -1000,
//             opacity: 0
//         },0);
//         $('.ms01 .ms01_d02').animate({
//             width: 3000,
//             left: -1000,
//             opacity: 0
//         },0);

//         $('.mSlider .flexslider .slides > .ms01 > a > .ms01_d04, .mSlider .flexslider .slides > .ms01 > a > .ms01_d05').fadeOut(0);
//     }
    
//     function fs02Play(){
//         var w = $(window).width();
//         if(w>959){
//             $('.mSlider .flexslider .slides > .ms02 > a > .ms02Wrap > .ms02_d01').addClass('on');
//             $('.mSlider .flexslider .slides > .ms02 > a > .ms02Wrap > .ms02_d01').css('opacity',1);
//             $('.ms02_d02').delay(450).animate({
//                 top: 300,
//                 left: 0
//             },700);
//             $('.ms02_d04 img').delay(450).animate({
//                 top: 90,
//                 left: -482
//             },700);
//             $('.ms02_d03').delay(600).animate({
//                 top: 500,
//                 left: -20
//             },700);
//             $('.ms02_d05 img').delay(600).animate({
//                 top: 290,
//                 left: -502
//             },700);
//             $('.ms02_d06').delay(650).fadeIn(0);
//             $('.ms02_d06').delay(50).animate({
//                 top: 200,
//                 right: 0
//             },700);
//             $('.ms02BtnWrap').delay(700).fadeIn('fast');
//         }
//     }
    
    
//     function fs03Play(){
//         var w = $(window).width();
//         if(w>959){
//             $('.mSlider .flexslider .slides > .ms03 > a > .ms03Wrap01 > div:nth-child(1)').animate({
//                 width: '100%'
//             },'fast');
//             $('.mSlider .flexslider .slides > .ms03 > a > .ms03Wrap01 > div:nth-child(2)').delay(180).animate({
//                 width: '100%'
//             },'fast');
//             $('.mSlider .flexslider .slides > .ms03 > a > .ms03Wrap01 > div:nth-child(3)').delay(360).animate({
//                 width: '100%'
//             },'fast');
//             $('.mSlider .flexslider .slides > .ms03 > a > .ms03Wrap01 > div:nth-child(4)').delay(540).animate({
//                 width: '100%'
//             },'fast');
//             $('.mSlider .flexslider .slides > .ms03 > a > .ms03Wrap01 > div:nth-child(5)').delay(720).animate({
//                 width: '100%'
//             },'fast');

//             $('.mSlider .flexslider .slides > .ms03 > a > .ms03Wrap02 > .ms03_d03').delay(800).animate({
//                 left: '10px',
//                 top: '325px'
//             });
//             $('.ms03BtnWrap').delay(700).fadeIn('fast');
//         }
//     }
    
    
//     function fs02Reset(){
//         var w = $(window).width();
//         if(w>959){
//             $('.mSlider .flexslider .slides > .ms02 > a > .ms02Wrap > .ms02_d01').removeClass('on');
//             $('.mSlider .flexslider .slides > .ms02 > a > .ms02Wrap > .ms02_d01').css('opacity',0);
//             $('.ms02_d02').animate({
//                 top: 300,
//                 left: -3040
//             },0);
//             $('.ms02_d04 img').animate({
//                 top: 40,
//                 left: -3482
//             },0);
//             $('.ms02_d03').animate({
//                 top: 500,
//                 left: -3040
//             },0);
//             $('.ms02_d05 img').animate({
//                 top: 240,
//                 left: -3482
//             },0);
//             $('.ms02_d06').fadeOut(0);
//             $('.ms02_d06').animate({
//                 top: 400,
//                 right: 200
//             },0);
//             $('.ms02BtnWrap').fadeOut(0);
//         }
//     }
    
//     function fs03Reset(){
//         var w = $(window).width();
//         if(w>959){
//             $('.mSlider .flexslider .slides > .ms03 > a > .ms03Wrap01 > div:nth-child(1)').animate({
//                         width: 0
//                     },0);
//                     $('.mSlider .flexslider .slides > .ms03 > a > .ms03Wrap01 > div:nth-child(2)').animate({
//                         width: 0
//                     },0);
//                     $('.mSlider .flexslider .slides > .ms03 > a > .ms03Wrap01 > div:nth-child(3)').animate({
//                         width: 0
//                     },0);
//                     $('.mSlider .flexslider .slides > .ms03 > a > .ms03Wrap01 > div:nth-child(4)').animate({
//                         width: 0
//                     },0);
//                     $('.mSlider .flexslider .slides > .ms03 > a > .ms03Wrap01 > div:nth-child(5)').animate({
//                         width: 0
//                     },0);

//                     $('.mSlider .flexslider .slides > .ms03 > a > .ms03Wrap02 > .ms03_d03').animate({
//                         left: 0,
//                         top: '330px'
//                     });
//                     $('.ms03BtnWrap').fadeOut(0);
//         }
//     }
    
    
//     $('.flexslider').flexslider({
        
//         slideshowSpeed: 10000,
//         pausePlay: true,
//         start: function(){ //1번 슬라이드가 실행될때
//             fs01Play();  
//         },
//             after: function(){
//                 fs01Play(); 
//                 fs02Play();  
//                 fs03Play(); 
                
//             },
//             end: function(){ //마지막 슬라이드가 실행된때 발생하는 콜백함수
                
                
//             },
//             before: function(){ //매 슬라이드 실행되기 전에 발생하는 콜백함수
//                 fs01Reset();
//                 fs02Reset();
//                 fs03Reset();
//             }
//     });
    
//     $(window).resize(function(){
//         pp();
//     });
    
// });


// /* con01 */
// $(document).ready(function(){
//     $('.con01 > div > a').hover(function(){
//         $(this).find('div').first().stop().fadeIn('fast');
//         $(this).find('div:eq(1), div:eq(2)').stop().css('transform','scale(1)');
//         $(this).find('div:eq(4)').stop().css('z-index',30);
//     },function(){
//         $(this).find('div').first().stop().fadeOut('fast');
//         $(this).find('div:eq(1), div:eq(2)').stop().css('transform','scale(0)');
//         $(this).find('div:eq(4)').stop().css('z-index',0);

//     });
// });


// /* con02 */
// $(document).ready(function(){
//     $('.con02 a').hover(function(){
//         $(this).find('img:eq(1)').stop().addClass('on');
//     },function(){
//         $(this).find('img:eq(1)').stop().removeClass('on');

//     });
// });

// /* con02 - swiper */
// /*
// $(document).ready(function(){
//     var swiper = new Swiper('.swiper-container', {
//         navigation: {
//         nextEl: '.swiper-button-next',
//         prevEl: '.swiper-button-prev',
//         },
//     });
    
    
// });
// */

// /* con02 - slick(pc) */
// $(document).ready(function(){
//     $('.con02Wrap').slick({
        
//     });
// });


// /* con02 - swiper(tablet mobile) */
// $(document).ready(function(){
//     var swiper = new Swiper('.swiper-container', {
//       slidesPerView: 5,
//       spaceBetween: 50,
//       loop: true,
//       // init: false,
//       navigation: {
//         nextEl: '.swiper-button-next',
//         prevEl: '.swiper-button-prev',
//       },
//       breakpoints: {
//         959: {
//           slidesPerView: 2,
//           spaceBetween: '15%',
//         },
//         767: {
//           slidesPerView: 1
//         },
        
//       }
//     });
   
// });


// $(document).ready(function(){
//     $('.con03 > div > a').hover(function(){
//         $(this).addClass('on');
//         $(this).find('div').addClass('on');
//     },function(){
//         $(this).removeClass('on');
//         $(this).find('div').removeClass('on');
//     });
// });


// /* con03 - mobile swiper */
// $(document).ready(function(){
//     var swiper = new Swiper('.swiper-container_con03M', {
//         loop: true,
//       slidesPerView: 2,
//       centeredSlides: true,
//       spaceBetween: '5%',
//       grabCursor: true
//     });
// });


// /* con04 - flowSlider */
// $(document).ready(function(){
    
//     /*$('.ordermadeItem a img:last-child').fadeOut(0);*/
    
//     $("#shoeSlider").FlowSlider({
//         marginStart:0,
//         marginEnd:0,
//         //position:0.0,
//         startPosition:0.55
//     });
    
//     /*$('.ordermadeItem a').hover(function(){
//         $(this).find('img:last').fadeIn('fast');
//     },function(){
//         $(this).find('img:last').fadeOut('fast');
//     });*/
// });

// /* con04 - tablet & mobile */
// $(document).ready(function(){
//     var swiper = new Swiper('.swiper-container02', {
//       slidesPerView: 4,
//       loop: true,
//       breakpoints: {
//         767: {
//           slidesPerView: 3
//         }
        
//       }
//     });
   
// });

// /* con05 */

// $(document).ready(function(){
//     $('.con05 a').hover(function(){
//         $(this).addClass('on');
//         $(this).find('div:eq(1)').fadeOut('slow');
//     },function(){
//         $(this).removeClass('on');
//         $(this).find('div:eq(1)').fadeIn('slow');
//     });
// });


// /* family site */
// $(document).ready(function(){
//     //초기값코드
//     $('.fSite ul').slideUp(0);   // 처음부터 안보이게 처리 - 아무것도 안적으면 'fast'값 들어간것과 같음
    
//     //스위치 변수
//     var cnt = 0;    //0과 1을 번갈아 담아줄 변수
    
//     //버튼을 클릭했을 때 일어나는 일
//     $('.fSite button').click(function(){
//         $(this).next().slideToggle('fast');
        
//         //0을 1로, 혹은 1을 0으로 변경
        
//         if(cnt==0){ //on클래스 활성화 - ▼
//             cnt = 1;
//             $(this).find('>.icon').addClass('on');
//         }else{      //on클래스 비활성화 - ▲
//             cnt = 0;
//             $(this).find('>.icon').removeClass('on');
//         }
//     });
    
//     //웹접근성 - tab으로 초점 이동, 기능
//     //click - enter키
//     //mouseenter - 자동실행
//     //mouseleave - 자동사라짐
//     //focus() - a나 입력양식에 초점이 왔을때
//     //blur() - a나 입력양식에서 초점을 벗어났을 때
    
//     //마지막 리스트에서 벗어났을때
//     $('.fSite li:last a').blur(function(){
//         $(this).parents('ul').slideUp('fast');
//         $('.fSite button .icon').removeClass('on');
//         cnt = 0; //클릭 이벤트는 하나이지만 cnt(변수)가 변해야 할 상황은 두가지
//     });    
// });




























