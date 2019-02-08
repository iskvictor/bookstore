$(document).ready(function(){
    var form = $('#form_buying_book');
    console.log(form);

    function basketUpdating(product_id, nmb,is_delete=true){

         var data = {};
             data.product_id = product_id;
             data.nmb = nmb;

             var csrf_token = $('#form_buying_book [name="csrfmiddlewaretoken"]').val();
             data['csrfmiddlewaretoken']=csrf_token;
             data['is_delete']=is_delete;

             var url = form.attr("action");
             $.ajax({
                 url:url,
                 type:'POST',
                 data:data,
                 cache:true,
                 success:function(data){
                    console.log('ok')
                    console.log(data.products)
                    if(data.products_total_nmb || data.products_total_nmb == 0){
                        $('#basket_total_nmb').text('('+data.products_total_nmb+')');
                        $('.basket-items ul').html('');
                        $.each(data.products, function(key,view){
                            $('.basket-items ul').append('<li>'+view.name+', ' + view.number+ 'шт. по '+view.price_per_item+'грн.'+'key'+key+
                             '<a href="" class="delete_item" data-product_id ="'+ view.id+'" >x</a>'+
                              '</li>')
                        });
                    }
                 },


                 error:function(){
                 console.log('error')
                 }
             });


    }

    form.on('submit',function(e){
        e.preventDefault();
        console.log('123');
        var nmb = $('#number').val();
        var submit_btn=$('#submit_btn');
        var product_id = submit_btn.data('product_id');
        var product_name = submit_btn.data('name');
        var product_price = submit_btn.data('price');
        console.log(product_id);
        console.log(product_name);
         console.log(product_price);
         basketUpdating(product_id, nmb,is_delete=false)
        });


    function showingBasket(){
        $('.basket-items').removeClass('hidden');
    }

    $('.basket-container').on('click', function(e){
    e.preventDefault();
    showingBasket();
    })

    $('.basket-container').mouseover( function(){
    showingBasket();
    })

//    $('.basket-container').mouseout( function(){
//    showingBasket();
//    })
     $(document).on('click','.delete_item', function(e){
     e.preventDefault()
     product_id = $(this).data('product_id');
     nmb= 0;
     console.log('222');
     basketUpdating(product_id, nmb,is_delete=true)
     })

     function calculatingBasketAmount(){
        var total_order_amount =0;
        $('.total-product-in_basket-amount').each(function(){
        total_order_amount += parseFloat($(this).text());
        })
        $('#total_order_amount').html(total_order_amount.toFixed(2));


     };
     calculatingBasketAmount()

     $(document).on('change' ,".product-in-basket-nmb", function(){
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

});