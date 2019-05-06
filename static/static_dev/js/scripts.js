$(document).ready(function(){
    var form = $('.form_buying_book');

    function basketUpdating(product_id, nmb){
         var data = {};
             data.product_id = product_id;
             data.nmb = nmb;
             var csrf_token = $('.form_buying_book [name="csrfmiddlewaretoken"]').val();
             data['csrfmiddlewaretoken']=csrf_token;
             var url = form.attr("action");
             $.ajax({
                 url:url,
                 type:'POST',
                 data:data,
                 cache:true,
                 success:function(data){
                    console.log('ok')
                    if(data.products_total_nmb || data.products_total_nmb == 0){
                        $('#basket_total_nmb').text('('+data.products_total_nmb+')');
                        $('.basket-items ul').html('');
                    calculatingBasketAmount()
                    }
                 },

                 error:function(){
                    console.log('error')
                 }
             });
    }

    form.on('submit',function(e){
            e.preventDefault();
            var submit_btn =  $(this).find(".submit_btn");
            var nmb = $(this).children(".number").val();
            var product_id = submit_btn.data('product_id');
            var product_name = submit_btn.data('name');
            var product_price = submit_btn.data('price');
             basketUpdating(product_id, nmb)
    });


     function basket_count(){
         var url = $('.basket-count').attr('href')
         data={};
         $.ajax({
                 url:url,
                 type:'GET',
                 data:data,
                 cache:true,
                 success:function(data){
                    console.log('ok')
                    $('#basket_total_nmb').text('('+data.products_total_nmb+')');
                 },

                 error:function(){
                 console.log('error')
                 }
             });
     }


      basket_count()


      $(document).on('click','.cart-item-qty', function(){
         product_basket_id = $(this).data('product_basket_id');
         qty = $(this).val()
         console.log('product_basket_id',product_basket_id)
         var data = {};
         data.product_basket_id= product_basket_id;
         data.qty= qty;
         var url = $('.cart-qty').attr('action')
         $.ajax({
                 url:url,
                 type:'GET',
                 data:data,
                 cache:true,
                 success:function(data){
                    console.log('ok')
                 },
                 error:function(){
                 console.log('error')
                 }
         });

     })


     $(document).on('click','.delete_item', function(e){
         e.preventDefault()
         product_id = $(this).data('product_id');
         var data = {};
         data.product_id = product_id;
         var url = $(this).attr('href')
         $.ajax({
                 url:url,
                 type:'GET',
                 data:data,
                 cache:true,
                 success:function(data){
                    console.log('ok')
                    $('#basket_total_nmb').text('('+data.products_total_nmb+')');
                    $('.cart-item-'+product_id).remove();
                 },
                 error:function(){
                 console.log('error')
                 }
         });

     })


     function calculatingBasketAmount(){
        var total_order_amount =0;
        $('.total-product-in_basket-amount').each(function(){
        total_order_amount += parseFloat($(this).text());
        })
        $('#total_order_amount').html(total_order_amount.toFixed(2));
     };

     calculatingBasketAmount()


     $(document).on('click' ,".total_amount, .product-in-basket-nmb", function(){
     var current_nmb = $(this).val();
     var current_tr = $(this).closest('tr');
     var current_price = parseFloat(current_tr.find('.product-price').text()).toFixed(2);
     var total_amount = (current_nmb*current_price).toFixed(2);
     current_tr.find('.total-product-in_basket-amount').text(total_amount);
     calculatingBasketAmount()
     })


     $(document).ready(function(){
        $('#div_id_address').css('display','none')
        $('#id_buying_type').on('click', function(){
        buying_type = $(this).val();
        if(buying_type == 'delivery'){$('#div_id_address').css('display','block')}
        else{$('#div_id_address').css('display','none')}

        })
        $('#id_date_day').css('width', '50px').css('display', 'inline')
        $('#id_date_month').css('width', '100px').css('display', 'inline')
        $('#id_date_year').css('width', '100px').css('display', 'inline')﻿
     })



});