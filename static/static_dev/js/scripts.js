$(document).ready(function(){
    var form = $('.form_buying_book');
    console.log('form',form);

    function basketUpdating(product_id, nmb){
         console.log('---------------basketUpdating');
         var data = {};
             data.product_id = product_id;
             data.nmb = nmb;

             var csrf_token = $('.form_buying_book [name="csrfmiddlewaretoken"]').val();
             console.log('csrf_token',csrf_token)
             data['csrfmiddlewaretoken']=csrf_token;
//             data['is_delete']=is_delete;
             console.log('---data------',data)

             var url = form.attr("action");
             $.ajax({
                 url:url,
                 type:'POST',
                 data:data,
                 cache:true,
                 success:function(data){
                    console.log('ok')
                    console.log("*******data",data)
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
            console.log('88888888888');

            var submit_btn =  $(this).find(".submit_btn");
            var nmb = $(this).children(".number").val();
            console.log('submit_btn',submit_btn)


            var product_id = submit_btn.data('product_id');
            var product_name = submit_btn.data('name');
            var product_price = submit_btn.data('price');
            console.log(product_id);
            console.log(product_name);
             console.log(product_price);
             basketUpdating(product_id, nmb)
    });


     function basket_count(){
         console.log('*********Basket_count')
         var url = $('.basket-count').attr('href')
         data={}
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
         console.log('---------------cart-item-qty');
         product_basket_id = $(this).data('product_basket_id');
         qty = $(this).val()
         console.log('product_basket_id',product_basket_id)
         var data = {};
         data.product_basket_id= product_basket_id;
         data.qty= qty;
         var url = $('.cart-qty').attr('action')
         console.log('+++++url',url)
         console.log('+++++qty',qty)
         console.log('+++++product_basket_id',product_basket_id)
         console.log('+++++data',data)
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
         console.log('---------------delete_item');
         e.preventDefault()
         product_id = $(this).data('product_id');
         console.log('product_id',product_id)
         console.log('222');
         var data = {};
         data.product_id = product_id;
         console.log('+++++++++deleteItem')
         var url = $(this).attr('href')
         console.log('+++++url',url)
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
        console.log('---------------calculatingBasketAmount')
        var total_order_amount =0;
        $('.total-product-in_basket-amount').each(function(){
        total_order_amount += parseFloat($(this).text());
        })
        $('#total_order_amount').html(total_order_amount.toFixed(2));
     };


     calculatingBasketAmount()


     $(document).on('click' ,".total_amount, .product-in-basket-nmb", function(){
     console.log('total_amount')
     var current_nmb = $(this).val();
     var current_tr = $(this).closest('tr');
     console.log('current_tr',current_tr)
     var current_price = parseFloat(current_tr.find('.product-price').text()).toFixed(2);
     var total_amount = (current_nmb*current_price).toFixed(2);
     current_tr.find('.total-product-in_basket-amount').text(total_amount);
     console.log('total_amount',total_amount)
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