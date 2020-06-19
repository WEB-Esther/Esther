#!C:\Users\GRAM\AppData\Local\Programs\Python\Python38-32\python.exe
# -*- coding:utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
print("Content-Type: text/html")
print('''
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <title>ESTHER</title>
    <!-- icon -->
    <link rel="icon" href="img/TheRook.ico" type="image/x-icon">
    <!-- Font -->
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.11.2/css/all.css">
    <!-- Google Fonts Roboto -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap">
    <!-- Bootstrap core CSS -->
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <!-- Material Design Bootstrap -->
    <link rel="stylesheet" href="css/mdb.min.css">

    <link rel="stylesheet" href="stair.css">

  </head>

  <body>

    <!-- Start your project here-->

    <!--Main Navigation-->
    <header>

      <!--Navbar-->
      <nav class="navbar navbar-expand-lg navbar-dark primary-color" style="width:103%">

  <!-- Navbar brand -->
  <a class="navbar-brand" href="#">ESY</a>

  <!-- Collapse button -->
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#basicExampleNav" aria-controls="basicExampleNav"
    aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <!-- Collapsible content -->
  <div class="collapse navbar-collapse" id="basicExampleNav">

    <!-- Links -->
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="index.py">Home
          <span class="sr-only">(current)</span>
        </a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="idea_bank.py">아이디어 뱅크
        <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="empty_room.py">빈 방
        <span class="sr-only">(current)</span></a>
      </li>

      <!-- Dropdown -->
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true"
          aria-expanded="false">개인공간</a>
        <div class="dropdown-menu dropdown-primary" aria-labelledby="navbarDropdownMenuLink">
          <a class="dropdown-item" href="파일 만들고 링크 ㄱ">인빈</a>
          <a class="dropdown-item" href="파일 만들고 링크 ㄱ">준영</a>
          <a class="dropdown-item" href="파일 만들고 링크 ㄱ">희찬</a>
          <a class="dropdown-item" href="seungwoo.py">승우</a>
        </div>
      </li>

    </ul>
    <!-- Links -->

    <form class="form-inline">
      <div class="md-form my-0">
        <input class="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search">
      </div>
    </form>
  </div>
  <!-- Collapsible content -->

</nav>
      <!--/.Navbar-->

    </header>
    <!--Main Navigation-->
<!-- End your project here-->

<!-- jQuery -->
<script type="text/javascript" src="js/jquery.min.js"></script>
<!-- Bootstrap core JavaScript -->
<script type="text/javascript" src="js/bootstrap.min.js"></script>


<script type="text/javascript">
function div_show2() {document.getElementById("stair2").style.visibility = "visible";}
function div_show3() {document.getElementById("stair3").style.visibility = "visible";}
function div_show4() {document.getElementById("stair4").style.visibility = "visible";}
function div_show5() {document.getElementById("stair5").style.visibility = "visible";}
function div_show6() {document.getElementById("stair6").style.visibility = "visible";}
function div_show7() {document.getElementById("stair7").style.visibility = "visible";}
setTimeout("location.reload()",5000)
</script>

<h1 style="padding-top:15px; padding-left:25px"><strong>Stair Code</strong></h1>

<div class="row">
  <h1 style="padding-top:15px; padding-left:30px; width:100%">1st</h1>
    <div class="col-md-3col-sm-3col-xs-6"style="padding:50px"> <a class="btn btn-sm animated-button thar-one"style="font-size:20px;"><strong>1</strong></a> </div>
    <div class="col-md-3col-sm-3col-xs-6"style="padding:50px"> <a class="btn btn-sm animated-button thar-two"style="font-size:20px;"><strong>2</strong></a> </div>
    <div class="col-md-3col-sm-3col-xs-6"style="padding:50px"> <a href="#target1" onclick="div_show2()" class="btn btn-sm animated-button thar-one"style="font-size:20px;"><strong>3</strong></a> </div>
    <div class="col-md-3col-sm-3col-xs-6"style="padding:50px"> <a class="btn btn-sm animated-button thar-two"style="font-size:20px;"><strong>4</strong></a> </div>
</div>
    <div class="row" style="visibility: hidden;" id="stair2">
    <h1 style="padding-top:15px; padding-left:30px; width:100%"><a name="target1">2nd</a></h1>
        <div class="col-md-3col-sm-3col-xs-6"style="padding:50px"> <a class="btn btn-sm animated-button thar-one"style="font-size:20px;"><strong>1</strong></a> </div>
        <div class="col-md-3col-sm-3col-xs-6"style="padding:50px"> <a href="#target" onclick="div_show3()" class="btn btn-sm animated-button thar-two"style="font-size:20px;"><strong>2</strong></a> </div>
        <div class="col-md-3col-sm-3col-xs-6"style="padding:50px"> <a class="btn btn-sm animated-button thar-one"style="font-size:20px;"><strong>3</strong></a> </div>
        <div class="col-md-3col-sm-3col-xs-6"style="padding:50px"> <a class="btn btn-sm animated-button thar-two"style="font-size:20px;"><strong>4</strong></a> </div>
    </div>
    <div class="row"style="visibility: hidden;" id="stair3">
      <h1 style="padding-top:15px; padding-left:30px; width:100%"><a name="target">3rd</a></h1>
        <div class="col-md-3col-sm-3col-xs-6"style="padding:50px"> <a class="btn btn-sm animated-button thar-one"style="font-size:20px;"><strong>1</strong></a> </div>
        <div class="col-md-3col-sm-3col-xs-6"style="padding:50px"> <a class="btn btn-sm animated-button thar-two"style="font-size:20px;"><strong>2</strong></a> </div>
        <div class="col-md-3col-sm-3col-xs-6"style="padding:50px"> <a class="btn btn-sm animated-button thar-one"style="font-size:20px;"><strong>3</strong></a> </div>
        <div class="col-md-3col-sm-3col-xs-6"style="padding:50px"> <a href="#target2" onclick="div_show4()" class="btn btn-sm animated-button thar-two"style="font-size:20px;"><strong>4</strong></a> </div>
    </div>
        <div class="row"style="visibility: hidden;" id="stair4">
      <h1 style="padding-top:15px; padding-left:30px; width:100%"><a name="target2">4th</a></h1>
        <div class="col-md-3col-sm-3col-xs-6"style="padding:50px"> <a href="#target3" onclick="div_show5()" class="btn btn-sm animated-button thar-one"style="font-size:20px;"><strong>1</strong></a> </div>
        <div class="col-md-3col-sm-3col-xs-6"style="padding:50px"> <a class="btn btn-sm animated-button thar-two"style="font-size:20px;"><strong>2</strong></a> </div>
        <div class="col-md-3col-sm-3col-xs-6"style="padding:50px"> <a class="btn btn-sm animated-button thar-one"style="font-size:20px;"><strong>3</strong></a> </div>
        <div class="col-md-3col-sm-3col-xs-6"style="padding:50px"> <a class="btn btn-sm animated-button thar-two"style="font-size:20px;"><strong>4</strong></a> </div>
    </div>

    <div class="row"style="visibility: hidden;" id="stair5">
      <h1 style="padding-top:15px; padding-left:30px; width:100%"><a name="target3">5th</a></h1>
        <div class="col-md-3col-sm-3col-xs-6"style="padding:50px"> <a class="btn btn-sm animated-button thar-one"style="font-size:20px;"><strong>1</strong></a> </div>
        <div class="col-md-3col-sm-3col-xs-6"style="padding:50px"> <a href="#target4"onclick="div_show6()" class="btn btn-sm animated-button thar-two"style="font-size:20px;"><strong>2</strong></a> </div>
        <div class="col-md-3col-sm-3col-xs-6"style="padding:50px"> <a class="btn btn-sm animated-button thar-one"style="font-size:20px;"><strong>3</strong></a> </div>
        <div class="col-md-3col-sm-3col-xs-6"style="padding:50px"> <a class="btn btn-sm animated-button thar-two"style="font-size:20px;"><strong>4</strong></a> </div>
    </div>
    <div class="row"style="visibility: hidden;" id="stair6">
      <h1 style="padding-top:15px; padding-left:30px; width:100%"><a name="target4">6th</a></h1>
        <div class="col-md-3col-sm-3col-xs-6"style="padding:50px"> <a class="btn btn-sm animated-button thar-one"style="font-size:20px;"><strong>1</strong></a> </div>
        <div class="col-md-3col-sm-3col-xs-6"style="padding:50px"> <a href="#target5" onclick="div_show7()" class="btn btn-sm animated-button thar-two"style="font-size:20px;"><strong>2</strong></a> </div>
        <div class="col-md-3col-sm-3col-xs-6"style="padding:50px"> <a class="btn btn-sm animated-button thar-one"style="font-size:20px;"><strong>3</strong></a> </div>
        <div class="col-md-3col-sm-3col-xs-6"style="padding:50px"> <a class="btn btn-sm animated-button thar-two"style="font-size:20px;"><strong>4</strong></a> </div>
    </div>

    <div class="row"style="visibility: hidden;"id="stair7">
      <h1 style="padding-top:15px; padding-left:30px; width:100%"><a name="target5">7th</a></h1>
        <div class="col-md-3col-sm-3col-xs-6"style="padding:50px"> <a class="btn btn-sm animated-button thar-one"style="font-size:20px;"><strong>1</strong></a> </div>
        <div class="col-md-3col-sm-3col-xs-6"style="padding:50px"> <a class="btn btn-sm animated-button thar-two"style="font-size:20px;"><strong>2</strong></a> </div>
        <div class="col-md-3col-sm-3col-xs-6"style="padding:50px"> <a class="btn btn-sm animated-button thar-one"style="font-size:20px;"><strong>3</strong></a> </div>
        <div class="col-md-3col-sm-3col-xs-6"style="padding:50px"> <a href="Seungwoo\Project_Login\Login.html" class="btn btn-sm animated-button thar-two"style="font-size:20px;"><strong>4</strong></a> </div>
    </div>
    <div class="row"style="visibility: hidden;">
      <h1 style="padding-top:15px; padding-left:30px; width:100%"><a name="target5">7th</a></h1>
        <div class="col-md-3col-sm-3col-xs-6"style="padding:50px"> <a class="btn btn-sm animated-button thar-one"style="font-size:20px;"><strong>1</strong></a> </div>
        <div class="col-md-3col-sm-3col-xs-6"style="padding:50px"> <a class="btn btn-sm animated-button thar-two"style="font-size:20px;"><strong>2</strong></a> </div>
        <div class="col-md-3col-sm-3col-xs-6"style="padding:50px"> <a class="btn btn-sm animated-button thar-one"style="font-size:20px;"><strong>3</strong></a> </div>
        <div class="col-md-3col-sm-3col-xs-6"style="padding:50px"> <a href="Seungwoo\Project_Login\Login.html" class="btn btn-sm animated-button thar-two"style="font-size:20px;"><strong>4</strong></a> </div>
    </div>




  </body>
</html>
''')
