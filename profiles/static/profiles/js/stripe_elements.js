var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements()
var style = {
  base: {
    color: '#000',
    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif',
    fontSmoothing: 'antialiased',
    fontSize: '16px',
    '::placeholder': {
      color: '#aab7c4'
    },
    ':-webkit-autofill': {
      color: '#32325d',
    },
  },
  invalid: {
    color: '#dc3545',
    iconColor: '#dc3545',
    ':-webkit-autofill': {
      color: '#dc3545',
    },
  }
};

var card = elements.create('card', {style: style});
card.mount('#card-element')

//  handle realtime validation errors on the card element.

card.addEventListener('change', function (event){
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `<span class="icon" role="alert"></span><i class="fas fa-times"></i></span><span>${event.error.message}</span>`;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// handle form submit

var form = document.getElementById('create-profile-form');

form.addEventListener('submit', function(e) {
    e.preventDefault();
    card.update({'disabled': true});
    $('#submit-button').attr('disabled', true);

  var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
  var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        "user": $("#user-id-no").data(),
        "full_name": $.trim(form.full_name.value),
        "town_or_city": $.trim(form.town_or_city.value),
        "country": $.trim(form.country.value),
        "gender": $.trim(form.gender.value),
        'weight': $.trim(form.weight.value),
        "birthdate": $.trim(form.date.value)
  };
var url = '/profile/cache_payment_create_profile/';
  $.post(url, postData).done(function() {
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
        card: card,
        },
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `<span class="icon" role="alert"></span><i class="fas fa-times"></i></span><span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            card.update({'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
    }
  });
}).fail(function () {
    // just reload page to show error message from django
    location.reload();
})
});


// userprofile:{
//                 "user": $("#user-id-no").data(),
//                 "full_name": $("#id_full_name").val(),
//                 "town_or_city": $("#id_town_or_city").val(),
//                 "country": $("#id_country").val(),
//                 "gender": $("#id_gender").val(),
//                 "weight": $("#id_weight").val(),
//                 "birthdate": $("#date").val(),
//                 "image_name": file

// //   $('#create-profile-form').fadeToggle(100);
// //   $('#loading-overlay').fadeToggle(100);
//     stripe.confirmCardPayment(clientSecret, {
//         payment_method: {
//             card: card,
//             billing_details: {
//                 name: $("#id_full_name").val()
//                     },
//             }
//         }
//     }).then(function(result) {
//         if (result.error) {
//             var errorDiv = document.getElementById('card-errors');
//             var html = `
//                 <span class="icon" role="alert">
//                 <i class="fas fa-times"></i>
//                 </span>
//                 <span>${result.error.message}</span>`;
//             $(errorDiv).html(html);
//             card.update({ 'disabled': false});
//             $('#submit-button').attr('disabled', false);
//         } else {
//             if (result.paymentIntent.status === 'succeeded') {
//                 form.submit();
//             }
//         }
//     });