$(document).ready(function() {
  $.ajax({
    url: '/unread_messages',
    method: 'GET',
    success: function(data) {

      //Deklarerar count(unread_msg)
      var unread_messages = data['unread_msg'];
      //Skriver över #unreadCount med unread_messages
      $('#unreadCount').html(unread_messages);
    }
  });
});
