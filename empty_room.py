#!C:\Users\GRAM\AppData\Local\Programs\Python\Python38-32\python.exe
# -*- coding:utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
print("Content-Type: text/html")
print()
print('''<!DOCTYPE html>
<html lang="utf-8">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta http-equiv="x-ua-compatible" content="ie=edge">
  <title>ESTHER</title>
  <!-- MDB icon -->
  <link rel="icon" href="img/TheRook.ico" type="image/x-icon">
  <!-- Font Awesome -->
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.11.2/css/all.css">
  <!-- Google Fonts Roboto -->
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap">
  <!-- Bootstrap core CSS -->
  <link rel="stylesheet" href="css/bootstrap.min.css">
  <!-- Material Design Bootstrap -->
  <link rel="stylesheet" href="css/mdb.min.css">

</head>
<body>

        <!-- Start your project here-->
        <!--Main Navigation-->
        <header>

          <!--Navbar-->
          <nav class="navbar navbar-expand-lg navbar-dark primary-color">

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
        <!-- Bootstrap tooltips -->
        <script type="text/javascript" src="js/popper.min.js"></script>
        <!-- Bootstrap core JavaScript -->
        <script type="text/javascript" src="js/bootstrap.min.js"></script>
        <!-- MDB core JavaScript -->
        <script type="text/javascript" src="js/mdb.min.js"></script>

<br>




</body>
</html>
''')
