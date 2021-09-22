const $ = window.$;
document.onreadystatechange = function () {
  if (document.readyState === 'complete') {
    $('DIV#add_item').click(function () {
      $('UL.my_list').append($('<li>Item</li>'));
    });
    $('DIV#remove_item').click(function () {
      $('UL.my_list').children('LI').last().remove();
    });
    $('DIV#clear_list').click(function () {
      $('UL.my_list li').remove();
    });
  }
};
