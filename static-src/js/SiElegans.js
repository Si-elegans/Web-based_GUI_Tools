//JS to do tooltip for span tags with uuid class
$(document).ready(function(){
            $('.uuid').each(function (index) {
//                console.log(index + ":" + $(this).text());
                $(this).tooltip({"title": $(this).text()});
            });

            //$('[data-toggle="tooltip"]').tooltip();

        });

(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

ga('create', 'UA-78632387-1', 'auto');
ga('send', 'pageview');

function feedback_alert_close() {
    localStorage.setItem("feedback_closed", "1");
}



