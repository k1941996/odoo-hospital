$(document).ready(()=>{
    console.log("ready")
    let ks;
    let json_array=[];
    $('.kshitij').click((e)=>{
        let el = $(e.currentTarget).closest('tr')
        console.log(el)
        ks=el;
        // let name=el.find('#product_name')
        // console.log(name[0].textContent)
        $('#opening_balance').val('')
        $('#seed_purchased').val('')
        $('#tonnes_harvested').val('')
        $('#qty_delivered').val('')
        $('#other').val('')
        $('#qty_retained').val('')

    })
    $('#form_submit_btn').click((e)=>{
        let opening_balance = !isNaN($('#opening_balance').val()) && $('#opening_balance').val()!=''?$('#opening_balance').val():"-"
        let seed_purchased = !isNaN($('#seed_purchased').val()) && $('#seed_purchased').val()!=''?$('#seed_purchased').val():"-"
        let tonnes_harvested = !isNaN($('#tonnes_harvested').val()) && $('#tonnes_harvested').val()!=''?$('#tonnes_harvested').val():"-"
        let qty_delivered = !isNaN($('#qty_delivered').val()) && $('#qty_delivered').val()!=''?$('#qty_delivered').val():"-"
        let other = !isNaN($('#other').val()) && $('#other').val()!=''?$('#other').val():"-"
        let qty_retained = !isNaN($('#qty_retained').val()) && $('#qty_retained').val()!=''?$('#qty_retained').val():"-"
        ks.find('#opening_balance_td').html(opening_balance)
        ks.find('#seed_purchased_td').html(seed_purchased)
        ks.find('#tonnes_harvested_td').html(tonnes_harvested)
        ks.find('#qty_delivered_td').html(qty_delivered)
        ks.find('#other_td').html(other)
        ks.find('#qty_retained_td').html(qty_retained)
    })
})

