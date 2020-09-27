function getCookie(cname)
{
  var name = cname + "=";
  var decodedCookie = decodeURIComponent(document.cookie);
  var ca = decodedCookie.split(';');
  for(var i = 0; i <ca.length; i++)
  {
    var c = ca[i];
    while (c.charAt(0) == ' ')
    {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) { return c.substring(name.length, c.length); }
  }
  return "";
}

function getfilesize(input)
{
    file = input.files[0];

    // get previous file's size
    oldFilesize = getCookie('filesize');
    if(oldFilesize.length > 0) 
        oldFilesize = parseInt(oldFilesize, 10);
    else
        oldFilesize = 0;
    // console.log('old_filesize: ' + oldFilesize);
    // console.log('current_filesize: ' + file.size);

    // replace cookie if current filesize is larger than old one
    if(file.size > oldFilesize) { document.cookie = 'filesize=' + file.size; }
    // console.log(document.cookie);
    return true;
}

function previewimage(input)
{
    //console.log(input.name);
    if (input.files && input.files[0])
    {
        var reader = new FileReader();
        reader.onload = function (e)
        {
            $('#' + input.name + '-img').attr('src', e.target.result);
        }
        reader.readAsDataURL(input.files[0]);
    }
    return true;
}

function storestyle(elem)
{
    console.log(elem);
    localStorage.setItem(elem.name, elem.value);
    return true;
}