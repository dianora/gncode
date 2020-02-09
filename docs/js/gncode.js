$("[data-gncode-lang]").click(function(){
    lang = $(this).attr("data-gncode-lang");
    console.log(lang);

    // var url = window.location.href;
    // url = url.replace("/fr/", "/en/");
    // window.location.href = url;

    console.log(window.location.pathname)
    const regex = new RegExp('^\/..\/')
    window.location.pathname = window.location.pathname.replace(
        regex,
        '/' + lang + '/'
    );
});