$('.rating-star').hover(
  function(){ 
    $(this).addClass('rating-star-hover icon icon-star')
    $(this).prevAll().addClass('rating-star-hover icon icon-star')
  },
  function(){ 
    $(this).removeClass('rating-star-hover icon icon-star')
    $(this).prevAll().removeClass('rating-star-hover icon icon-star')
  }
)
